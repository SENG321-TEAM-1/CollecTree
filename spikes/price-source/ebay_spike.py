"""Price source spike (issue #96): eBay Browse API + TCMB exchange rate.

Throwaway spike code. It answers the questions in #96; it is not the
production price provider. Only the Python standard library is used.

Usage (from the repository root):
    python3 spikes/price-source/ebay_spike.py token
    python3 spikes/price-source/ebay_spike.py categories "hot wheels skyline"
    python3 spikes/price-source/ebay_spike.py prices [--category 222] [--limit 100]
    python3 spikes/price-source/ebay_spike.py limits
    python3 spikes/price-source/ebay_spike.py rate

Keys are read from .env in the repository root (see .env.example):
    EBAY_ENVIRONMENT=sandbox|production
    EBAY_CLIENT_ID=...
    EBAY_CLIENT_SECRET=...

Search keyword syntax (one keyword per catalogue model, see models.csv):
    word      the listing title must contain this word
    (a,b,c)   the listing title must contain at least one of these words
    -word     the listing title must not contain this word (not sent to eBay)
Words are compared after normalisation: lower case, hyphens and apostrophes
removed inside words ("GT-R" -> "gtr", "T64-011-JV" -> "t64011jv"), other
punctuation treated as a space.

A price is accepted only if at least MIN_SAMPLE_SIZE listings remain and the
middle half of their prices is consistent (75th percentile / 25th percentile
at most MAX_SPREAD). Otherwise the last known price is kept.

Nothing returned by eBay is written to disk. Only the median price and the
number of listings are printed, matching the domain model (no listing data
is stored).
"""

import argparse
import base64
import csv
import json
import re
import statistics
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODELS_FILE = Path(__file__).with_name("models.csv")

HOSTS = {
    "sandbox": "https://api.sandbox.ebay.com",
    "production": "https://api.ebay.com",
}
SCOPE = "https://api.ebay.com/oauth/api_scope"
MARKETPLACE = "EBAY_US"
NEW_CONDITION_ID = "1000"
# Title words that point to several models, used or modified models, parts, or
# special editions. A word is skipped if the model's own keyword requires it
# (for example a catalogue entry for a chase car).
EXCLUDED_WORDS = (
    "lot", "lots", "bundle", "set of", "x2", "x3",
    "loose", "damaged", "open box",
    "custom", "repaint", "wheel swap", "swap", "decal", "sticker", "replica",
    "chase", "treasure hunt", "sth", "rlc", "convention", "error", "sample", "prototype",
)
MIN_SAMPLE_SIZE = 5
MAX_SPREAD = 2.0
TCMB_URL = "https://www.tcmb.gov.tr/kurlar/today.xml"


def load_env():
    env_file = REPO_ROOT / ".env"
    values = {}
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                values[key.strip()] = value.strip()
    missing = [k for k in ("EBAY_CLIENT_ID", "EBAY_CLIENT_SECRET") if not values.get(k)]
    if missing:
        sys.exit(f"Missing in {env_file}: {', '.join(missing)}. Copy .env.example to .env and fill them in.")
    environment = values.get("EBAY_ENVIRONMENT", "sandbox")
    if environment not in HOSTS:
        sys.exit(f"EBAY_ENVIRONMENT must be one of {list(HOSTS)}, not {environment!r}")
    return environment, values["EBAY_CLIENT_ID"], values["EBAY_CLIENT_SECRET"]


def http(request):
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as error:
        body = error.read().decode(errors="replace")
        sys.exit(f"HTTP {error.code} from {request.full_url}\n{body}")


def get_token(environment, client_id, client_secret):
    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    request = urllib.request.Request(
        f"{HOSTS[environment]}/identity/v1/oauth2/token",
        data=urllib.parse.urlencode({"grant_type": "client_credentials", "scope": SCOPE}).encode(),
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {credentials}",
        },
        method="POST",
    )
    return http(request)


def api_get(environment, token, path, params):
    url = f"{HOSTS[environment]}{path}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "X-EBAY-C-MARKETPLACE-ID": MARKETPLACE},
    )
    return http(request)


def usd_to_try():
    with urllib.request.urlopen(TCMB_URL, timeout=30) as response:
        root = ET.fromstring(response.read())
    usd = root.find("./Currency[@Kod='USD']")
    return root.get("Date"), float(usd.findtext("ForexSelling"))


def cmd_token(args):
    environment, client_id, client_secret = load_env()
    token = get_token(environment, client_id, client_secret)
    print(f"OK: {environment} token received, expires in {token.get('expires_in')} seconds")


def cmd_categories(args):
    environment, client_id, client_secret = load_env()
    token = get_token(environment, client_id, client_secret)["access_token"]
    tree = api_get(environment, token, "/commerce/taxonomy/v1/get_default_category_tree_id",
                   {"marketplace_id": MARKETPLACE})
    tree_id = tree["categoryTreeId"]
    result = api_get(environment, token,
                     f"/commerce/taxonomy/v1/category_tree/{tree_id}/get_category_suggestions",
                     {"q": args.query})
    for suggestion in result.get("categorySuggestions", []):
        category = suggestion["category"]
        path = " > ".join(a["categoryName"] for a in reversed(suggestion.get("categoryTreeNodeAncestors", [])))
        print(f"{category['categoryId']:>8}  {path} > {category['categoryName']}")


def normalise(text):
    """Lower case; drop hyphens and apostrophes inside words; other punctuation becomes a space."""
    text = re.sub(r"(?<=\w)['\u2018\u2019-](?=\w)", "", text.lower())
    return re.sub(r"[^a-z0-9]+", " ", text).split()


def parse_keyword(keyword):
    """Return (query sent to eBay, required word groups, forbidden words)."""
    required, forbidden, query = [], [], []
    for match in re.finditer(r"\(([^)]*)\)|(\S+)", keyword):
        group, word = match.group(1), match.group(2)
        if word and word.startswith("-"):
            forbidden.append(" ".join(normalise(word[1:])))
            continue
        alternatives = group.split(",") if group else [word]
        required.append({" ".join(normalise(a)) for a in alternatives if normalise(a)})
        query.append(f"({','.join(a.strip() for a in alternatives)})" if group else word)
    return " ".join(query), required, forbidden


def title_matches(title, required, forbidden):
    words = " " + " ".join(normalise(title)) + " "
    keyword_words = {w for group in required for w in group}
    excluded = [w for w in EXCLUDED_WORDS if w not in keyword_words] + forbidden
    if any(f" {w} " in words for w in excluded):
        return False
    return all(any(f" {w} " in words for w in group) for group in required)


def cmd_prices(args):
    environment, client_id, client_secret = load_env()
    token = get_token(environment, client_id, client_secret)["access_token"]
    rate_date, rate = usd_to_try()
    print(f"Environment: {environment}   Category: {args.category}   USD/TRY {rate} (TCMB {rate_date})")
    print(f"Accepted if at least {MIN_SAMPLE_SIZE} listings and p75/p25 <= {MAX_SPREAD}\n")
    print(f"{'Model':<52} {'found':>6} {'kept':>5} {'median $':>9} {'median TL':>10}"
          f" {'p25 $':>7} {'p75 $':>7} {'spread':>6}  result")

    with MODELS_FILE.open() as f:
        models = list(csv.DictReader(f))
    accepted = 0
    for model in models:
        query, required, forbidden = parse_keyword(model["search_keyword"])
        filters = f"conditionIds:{{{NEW_CONDITION_ID}}},buyingOptions:{{FIXED_PRICE}}"
        result = api_get(environment, token, "/buy/browse/v1/item_summary/search", {
            "q": query,
            "category_ids": args.category,
            "filter": filters,
            "limit": args.limit,
        })
        prices = sorted(
            float(item["price"]["value"])
            for item in result.get("itemSummaries", [])
            if item.get("price", {}).get("currency") == "USD"
            and title_matches(item.get("title", ""), required, forbidden)
        )
        label = f"{model['brand']} {model['name']}"[:52]
        if len(prices) < MIN_SAMPLE_SIZE:
            print(f"{label:<52} {result.get('total', 0):>6} {len(prices):>5}"
                  f"   too few listings: keep the last price")
            continue
        median = statistics.median(prices)
        p25, _, p75 = statistics.quantiles(prices, n=4)
        spread = p75 / p25
        ok = spread <= MAX_SPREAD
        accepted += ok
        print(f"{label:<52} {result.get('total', 0):>6} {len(prices):>5} {median:>9.2f} {median * rate:>10.2f}"
              f" {p25:>7.2f} {p75:>7.2f} {spread:>6.2f}  {'accepted' if ok else 'inconsistent: keep the last price'}")
    print(f"\nAccepted: {accepted} of {len(models)} models")


def cmd_limits(args):
    environment, client_id, client_secret = load_env()
    token = get_token(environment, client_id, client_secret)["access_token"]
    result = api_get(environment, token, "/developer/analytics/v1_beta/rate_limit/", {"api_name": "browse"})
    for api in result.get("rateLimits", []):
        for resource in api.get("resources", []):
            for rate in resource.get("rates", []):
                print(f"{resource['name']}: {rate['limit']} calls per {rate['timeWindow'] // 3600} hours"
                      f" ({rate['remaining']} remaining, resets {rate['reset']})")


def cmd_rate(args):
    rate_date, rate = usd_to_try()
    print(f"TCMB {rate_date}: 1 USD = {rate} TRY (ForexSelling)")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("token", help="check that the keys work").set_defaults(run=cmd_token)
    categories = commands.add_parser("categories", help="find the leaf category ID for a search")
    categories.add_argument("query")
    categories.set_defaults(run=cmd_categories)
    prices = commands.add_parser("prices", help="median price of every model in models.csv")
    prices.add_argument("--category", default="222", help="eBay category ID (default 222, Diecast & Toy Vehicles)")
    prices.add_argument("--limit", type=int, default=100, help="listings per model, at most 200")
    prices.set_defaults(run=cmd_prices)
    commands.add_parser("limits", help="daily call limit of the Browse API").set_defaults(run=cmd_limits)
    commands.add_parser("rate", help="today's USD to TRY rate from TCMB").set_defaults(run=cmd_rate)
    args = parser.parse_args()
    args.run(args)


if __name__ == "__main__":
    main()
