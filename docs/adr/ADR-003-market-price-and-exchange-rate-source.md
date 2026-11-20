# ADR-003: Market Price and Exchange Rate Source

| Field | Value |
|---|---|
| Status | Accepted on 2026-11-19, after the price source spike ([#96](https://github.com/SENG321-TEAM-1/CollecTree/issues/96), [spike report](../architecture/spikes/price-source-spike.md)) |
| Date | 2026-11-16 |
| Decision owner | Berke Akman — Lead Software Architect |
| Final approval | Elif Zahide Arat — Product Owner |
| Consulted | Whole team |
| eBay developer account owner | Berke Akman |

## Context

- Automatic daily valuation in TRY is the core value of CollecTree (README, Collector Survey). It needs an external source of market prices for new-in-box diecast models (US-08) and a USD to TRY exchange rate.
- Assumption AS-1 says a public price source is reachable. It has not been tested yet.
- In the collector survey, 16 of 27 respondents (59%) check prices on Turkish listing sites and 5 (19%) check eBay.
- The system boundary sets two constraints: the platform must respect the terms of use of external sources, and it must start and be demonstrated with one `docker compose up`, even when an external source fails (risk R-1).
- The team has ten weeks, no budget for paid data, and no contract with any marketplace.

## Decision

**1. Daily market price: eBay Browse API.**
- Endpoint `GET /buy/browse/v1/item_summary/search` on the `EBAY_US` marketplace, with an application access token (OAuth client credentials, scope `https://api.ebay.com/oauth/api_scope`).
- One request per catalogue model per day, using the model's `search_keyword`, category `222` (Diecast & Toy Vehicles), and the filters `conditionIds:{1000}` (new) and `buyingOptions:{FIXED_PRICE}` (no auctions). The first 100 listings are read.
- **A catalogue model is one specific release** (brand, casting, series or catalogue number, and colour), and its search keyword identifies that release. A keyword for a whole casting mixes several releases and chase cars into one price.
- **Matching rule.** A listing counts only if its title contains every word of the keyword. `(a,b)` means at least one of the words, for example `(853,mgt00853)`; `-word` means the title must not contain the word. Titles and keywords are compared in lower case, with hyphens and apostrophes inside words removed.
- **Excluded title words.** Listings for several models, used or modified models, parts, or special editions are dropped: lot, lots, bundle, set of, x2, x3, loose, damaged, open box, custom, repaint, wheel swap, swap, decal, sticker, replica, chase, treasure hunt, sth, rlc, convention, error, sample, prototype. A word is not excluded if the model's own keyword requires it.
- **Consistency check.** The price is the **median** of the remaining USD prices, without shipping. It is saved only if **at least 5 listings** remain **and** the 75th percentile is at most **2.0 times** the 25th percentile. Otherwise the last known price is kept, as when eBay does not answer.

**2. Exchange rate: TCMB (Central Bank of the Republic of Turkey).**
- `https://www.tcmb.gov.tr/kurlar/today.xml`, USD `ForexSelling`.
- On weekends and holidays, or when TCMB is not reachable, the last known rate is reused and marked as stale.

**3. Fallback: seed prices.**
- The team collects TRY prices for the seed catalogue **by hand**, by viewing Turkish listing sites in a normal browser, and records the source and date of each price.
- Prices derived from eBay are never copied into the seed file; the seed file holds only prices that the team collected by hand.
- `SeedPriceProvider` serves these prices. It is used in all tests, in the demo if eBay is not available, and whenever `PRICE_PROVIDER=seed`.

**4. Data kept from eBay.** Only one median price per model per day and the number of listings it came from (`sample_size`). No listing, seller, or user data is stored. This lets the team truthfully opt out of eBay's marketplace account deletion notifications ("Not persisting eBay data").

**5. Presentation.** The user interface labels the price as "International listing price (eBay), converted to TRY", so that it is not mistaken for a Turkish sale price.

**6. Usage constraint.** Prices derived from eBay are used only inside CollecTree. They are shown to users in the CollecTree web app. They are not exported, not offered for bulk download, not sold or passed to third parties as a data feed, and not used to train AI models. The REST API serves its own web app: it has no export or bulk endpoint, the price history endpoint returns one model per request, and the list endpoints that include prices (`searchModels`, `listUserItems`) return at most 50 entries per page.

All price access goes through the `PriceProvider` interface in the `pricing` module ([C4 model](../architecture/c4-model.md), section 3), so the source can change without changes in other modules.

## Alternatives considered

| Alternative | Why not chosen |
|---|---|
| Automated collection from Turkish listing sites (sahibinden.com, Trendyol, Hepsiburada, Dolap) | The terms of use of sahibinden.com explicitly forbid robots, crawlers, scraping, and data mining, and state that the site's database is protected under Law No. 5846 (FSEK). Trendyol's `robots.txt` disallows its search pages for all user agents. sahibinden.com and Hepsiburada answered even a request for `robots.txt` from a script with `403` and a bot challenge (checked on 2026-11-16). Automated collection would break our own boundary constraint, carries legal risk (FSEK database protection, Turkish Penal Code articles 243–244 when access controls are bypassed, unfair competition), and could be blocked during the live demo. |
| eBay Marketplace Insights API (sold prices) | Real sale prices would be better data, but the API is a restricted, limited-release API that needs eBay's approval. It is not realistic within the course schedule. |
| Prices entered by the community (average purchase price of users) | No external dependency and in TRY, but there is almost no data while the platform has few users, and the values are easy to manipulate. Changes the product scope. |
| Paid scraping or price data services | No budget; adds a vendor dependency and terms of use of its own. |
| Seed prices only | Always works, but does not meet US-08 ("updated automatically every day"). Kept as the fallback. |

## Consequences

- **Positive:** Legal and documented access with structured JSON; no HTML parsing that breaks when a site changes.
- **Positive:** The demo and all tests work without eBay, because the seed provider implements the same interface.
- **Positive:** Very small data footprint: one number and one count per model per day.
- **Negative:** The price is an **asking price of active listings**, not a sale price, and it reflects the US marketplace, not the Turkish market. The interface label makes this clear to users.
- **Negative:** Production access to the Buy APIs is restricted by eBay. If access is not granted, the seed provider becomes the official source and eBay stays behind the interface for a later release.
- **Negative:** The eBay keyset is tied to one team member's developer account (the owner above). It must be handed over or replaced if that member leaves the project.
- **Negative:** Search keywords can match the wrong model (risk R-2). Release-specific catalogue entries, the matching rule, and the consistency check reduce the effect: a mixed result is rejected and the last price is kept. Every keyword is checked with the spike script before it is added to the seed catalogue.
- **Negative:** The seed catalogue needs more care: every entry must be one release with a verified catalogue number or series.

## Validation

The price source spike (#96) had to confirm four conditions. All four are met ([spike report](../architecture/spikes/price-source-spike.md)):

- [x] an active Production keyset, and the daily call limit of the application: active since 2026-11-17, **5,000 Browse API calls per 24 hours**;
- [x] the category ID for diecast cars: **`222`** (Diecast & Toy Vehicles);
- [x] plausible medians for at least 8 of 10 test models: **10 of 10** with release-specific keywords and the consistency check (5 of 10 with generic keywords);
- [x] no clause in the eBay API License Agreement that forbids storing an aggregated daily median: none found; decision 6 keeps the use of the prices inside CollecTree.

## References

- [eBay Browse API overview](https://developer.ebay.com/api-docs/buy/browse/static/overview.html) and [Buy API field filters](https://developer.ebay.com/api-docs/buy/static/ref-buy-browse-filters.html)
- [eBay API License Agreement](https://developer.ebay.com/products/license)
- [eBay marketplace account deletion notifications](https://developer.ebay.com/marketplace-account-deletion)
- [TCMB daily exchange rates](https://www.tcmb.gov.tr/kurlar/today.xml)
- [sahibinden.com terms of use (Ek-1)](https://www.sahibinden.com/sozlesmeler/ek-1-kullanim-kosullari-37)
- [Trendyol robots.txt](https://www.trendyol.com/robots.txt)
