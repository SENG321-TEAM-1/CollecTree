# Price Source Spike: eBay Browse API and TCMB

| Field | Value |
|---|---|
| Project | CollecTree |
| Course | BM 321 / SENG 321 Software Engineering — Sprint 2 |
| Issue | [#96](https://github.com/SENG321-TEAM-1/CollecTree/issues/96) |
| Date | 2026-11-17 |
| Owner (Accountable) | Berke Akman — Lead Software Architect |
| Decision it informs | [ADR-003](../../adr/ADR-003-market-price-and-exchange-rate-source.md) |
| Code | [`spikes/price-source/`](../../../spikes/price-source/) (throwaway spike code, not the production provider) |

## 1 Summary

The eBay Browse API can supply consistent daily market prices for diecast models, **but only if every catalogue model is one specific release and its search keyword identifies that release**. With generic keywords such as "mini gt porsche 911 gt3 rs", the results mix several releases, chase cars, and lots, and only 5 of 10 test models had a plausible median. With release-specific keywords, a title match rule, and a consistency check, **all 10 test models gave a consistent and plausible median**.

All four acceptance conditions of ADR-003 are met. The licence check adds one usage constraint: prices derived from eBay are used only inside CollecTree and are never exported, downloaded in bulk, or offered as a data feed (section 5.4).

## 2 Set-up

| Item | Value |
|---|---|
| Environment | eBay **Production**, marketplace `EBAY_US` |
| Authentication | Application token (OAuth client credentials, scope `https://api.ebay.com/oauth/api_scope`) |
| Endpoint | `GET /buy/browse/v1/item_summary/search` |
| Category | `222` Toys & Hobbies > Diecast & Toy Vehicles |
| Filters | `conditionIds:{1000}` (new), `buyingOptions:{FIXED_PRICE}` (no auctions) |
| Listings read per model | 100 (one request) |
| Exchange rate | TCMB `today.xml`, USD `ForexSelling`: 1 USD = 50.4199 TRY on 2026-11-17 |
| Keys | Stored only in the architect's local `.env` file, which is ignored by Git |

## 3 Run 1: generic keywords

The first run used one generic keyword per model, the title filter for lots and bundles from the first draft of ADR-003, and the median.

| Model | Keyword | Listings found | Median $ | Plausible? |
|---|---|---:|---:|---|
| Hot Wheels Nissan Skyline GT-R (BNR34) | hot wheels skyline r34 | 2,569 | 26.99 | Mixed: mainline, premium, RLC, and decal sheets |
| Hot Wheels '55 Chevy Bel Air Gasser | hot wheels 55 chevy bel air gasser | 4,507 | 28.00 | Mixed |
| Hot Wheels Datsun 510 Wagon | hot wheels datsun 510 wagon | 5,233 | 35.99 | Mixed: $1.65 to $109.99 |
| Hot Wheels Volkswagen T1 Panel Bus | hot wheels volkswagen t1 panel bus | 1,029 | 18.59 | Yes |
| MiniGT Nissan Skyline GT-R R34 V-Spec II | mini gt skyline r34 v-spec | 205 | 18.99 | Yes |
| MiniGT Porsche 911 GT3 RS (992) | mini gt porsche 911 gt3 rs 992 | 98 | 69.99 | **No**: the regular release sells for $16 to $24; chase and older releases pull the median up |
| MiniGT Lamborghini Huracan EVO | mini gt lamborghini huracan evo | 187 | 58.49 | **No**: ten different releases |
| Matchbox Land Rover Defender 110 | matchbox land rover defender 110 | 381 | 9.99 | Yes |
| Tarmac Works Toyota GR Supra | tarmac works toyota supra | 204 | 29.99 | Yes |
| Inno64 Honda Civic Type R FK8 | inno64 honda civic type r fk8 | 238 | 34.90 | Yes |

**Result: 5 of 10 plausible.** The cause is visible in the listing titles: one casting (for example the MiniGT Porsche 911 GT3 RS) exists as several releases with their own catalogue numbers (#853, #1060, #706, #630) and rare "chase" versions at $100 to $200. A keyword that matches all of them produces a median of a mixture, not the price of the model a collector owns.

## 4 Run 2: release-specific keywords and the matching rule

### 4.1 The matching rule

1. **A catalogue model is one specific release**: brand, casting, series or catalogue number, and colour. For example "MiniGT Porsche 911 (992) GT3 RS Weissach Package White (MGT00853)", not "MiniGT Porsche 911".
2. **The search keyword identifies that release.** It uses a small syntax:

   | Part | Meaning | Example |
   |---|---|---|
   | `word` | The listing title must contain the word | `huracan` |
   | `(a,b)` | The title must contain at least one of the words | `(853,mgt00853)` |
   | `-word` | The title must not contain the word; it is not sent to eBay | `-premium` |

   Words are compared after normalisation: lower case, hyphens and apostrophes inside words removed ("GT-R" becomes "gtr", "T64-011-JV" becomes "t64011jv"), other punctuation treated as a space.
3. **Excluded title words.** Listings whose title contains a word that points to several models, a used or modified model, a part, or a special edition are dropped: *lot, lots, bundle, set of, x2, x3, loose, damaged, open box, custom, repaint, wheel swap, swap, decal, sticker, replica, chase, treasure hunt, sth, rlc, convention, error, sample, prototype*. A word is not excluded if the model's own keyword requires it, so a catalogue entry for a chase car still works.
4. **Consistency check.** The median is accepted only if **at least 5 listings** remain **and** the middle half of their prices is consistent: **75th percentile / 25th percentile ≤ 2.0**. Otherwise the last known price is kept, exactly as when eBay does not answer.

### 4.2 Results

| Model (one release) | Search keyword | Found | Kept | Median $ | Median TRY | p25 $ | p75 $ | p75/p25 | Result |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| MiniGT Nissan Skyline GT-R (R34) V-Spec Lightning Yellow (MGT00762) | `mini gt skyline r34 (762,mgt00762)` | 43 | 17 | 13.25 | 668.06 | 12.72 | 18.49 | 1.45 | Accepted |
| MiniGT Porsche 911 (992) GT3 RS Weissach Package White (MGT00853) | `mini gt porsche gt3 rs (853,mgt00853)` | 39 | 19 | 18.95 | 955.46 | 16.99 | 23.60 | 1.39 | Accepted |
| MiniGT Lamborghini Huracan GT3 EVO2 Presentation Green (MGT00687) | `mini gt huracan (687,mgt00687)` | 12 | 5 | 25.00 | 1,260.50 | 24.97 | 29.37 | 1.18 | Accepted |
| Tarmac Works Toyota Supra Designed by Joshua Vides (T64-011-JV) | `tarmac works supra (t64-011-jv)` | 138 | 8 | 27.99 | 1,411.51 | 26.94 | 32.44 | 1.20 | Accepted |
| Inno64 Honda Civic Type R (FK8) Championship White (IN64-FK8-WHI) | `inno64 civic fk8 white` | 188 | 12 | 29.99 | 1,512.34 | 26.49 | 34.29 | 1.29 | Accepted |
| Matchbox Land Rover Defender 110 (mainline) | `matchbox land rover defender 110` | 381 | 81 | 10.98 | 553.61 | 7.13 | 13.82 | 1.94 | Accepted (close to the limit) |
| Hot Wheels '71 Datsun Bluebird 510 Wagon (Car Culture Japan Historics) | `hot wheels japan historics datsun 510 wagon` | 119 | 33 | 69.99 | 3,528.89 | 55.49 | 93.70 | 1.69 | Accepted |
| Hot Wheels '55 Chevy Bel Air Gasser (Boulevard) | `hot wheels boulevard 55 gasser` | 72 | 49 | 25.00 | 1,260.50 | 21.38 | 30.99 | 1.45 | Accepted |
| Hot Wheels Volkswagen T1 Panel Bus (Car Culture) | `hot wheels car culture volkswagen t1 panel bus` | 254 | 42 | 19.99 | 1,007.89 | 15.99 | 28.24 | 1.77 | Accepted |
| Hot Wheels Nissan Skyline GT-R (BNR34) (Fast & Furious) | `hot wheels fast furious skyline r34` | 428 | 64 | 46.94 | 2,366.71 | 39.99 | 73.30 | 1.83 | Accepted |

**Result: 10 of 10 accepted, and every accepted median is in the price range a collector would expect for that release.** The medians of the MiniGT models are now close to their shop prices (for example $18.95 instead of $69.99 for the Porsche).

### 4.3 What the consistency check catches

The Matchbox entry is a generic mainline casting, not one release. Its p75/p25 ratio was 2.00 in an earlier run on the same day and 1.94 in the final run, so it moves around the limit. When it is above the limit, the job keeps the last price instead of saving a mixed one. In the same way, generic keywords from run 1 such as `hot wheels datsun 510 wagon` (p75/p25 above 6) and `hot wheels skyline bnr34` (above 3) are rejected. The check turns a wrong price into a missing price, which the system already handles.

## 5 Answers to the questions of #96

### 5.1 Production keyset

**Yes.** A Production keyset is active. eBay requires every Production application either to receive marketplace account deletion notifications or to declare an exemption. The application was registered on 2026-11-17 as **exempted ("not persisting eBay data")**, which is true for CollecTree because it stores no eBay user or listing data (section 6).

### 5.2 Daily call limit

The Developer Analytics API reports **5,000 Browse API calls per 24 hours** for the application. The price job needs one call per catalogue model per day, so a catalogue of up to about 4,000 models fits with room for retries.

### 5.3 Category

**`222` (Diecast & Toy Vehicles).** The leaf category `180506` (Cars, Trucks & Vans > Contemporary Manufacture) gave almost the same medians but misses some listings, so the parent category is used.

### 5.4 Licence

The architect read the storage and data clauses of the current eBay API License Agreement in the developer portal on 2026-11-17 (the page is not readable without signing in).

| Clause | What it says | Effect on CollecTree |
|---|---|---|
| Definition of eBay Content | All information, data, content, and images stored by and retrieved from eBay | The listing prices read by the price job are eBay Content. CollecTree keeps only a median calculated from them, never the listings. |
| User IDs and passwords | Never collect, store, or share eBay user IDs or passwords | Not affected: CollecTree uses an application token and has no eBay user sign-in. |
| Prohibited aggregated data | Aggregated seller or buyer data, seller performance data, and aggregated data about transactions through third-party affiliates | Not affected: the median is a price of a model, not data about sellers, buyers, or transactions. |
| Displaying aggregated content | No framing or mirroring of pages served by eBay | Not affected: no eBay page is shown. |
| Restricted APIs | APIs that provide information about market trends, pricing strategies, sales volumes, or user behaviour. Their data, raw or aggregated, may not be distributed electronically through an API or downloaded in bulk | The Browse API returns active listings, but a price derived from it could be read as pricing information. CollecTree therefore follows this rule in any case (constraint below). |

**Result: no clause forbids storing a daily median calculated by the application.** To stay clearly inside the agreement, ADR-003 adds one constraint:

> **Prices derived from eBay are used only inside CollecTree.** They are shown to users in the CollecTree web app. They are not exported, not offered for bulk download, not sold or passed to third parties as a data feed, and not used to train AI models. The CollecTree REST API serves its own web app and returns prices only one model or one collection at a time.

The price history endpoint already returns the history of one model per request, and the API has no export or bulk endpoint, so the current API contract meets this constraint.

## 6 Data stored from eBay

Unchanged from the domain model: one median price per model per day and the number of listings it came from (`sample_size`). No listing IDs, titles, URLs, sellers, or user data are stored. The spike script prints the result and writes nothing to disk.

## 7 Recommendation

1. **Accept ADR-003** with the matching rule of section 4.1 and the usage constraint of section 5.4.
2. **Update the documents** so that they describe the same rule:
   - ADR-003: the rule, the consistency check, the usage constraint, and the validation results.
   - System boundary: the usage constraint in the list of constraints.
   - Domain model: a catalogue model is one specific release; the syntax of `search_keyword`.
   - C4 model and the price job sequence diagram: "at least 5 listings **and** p75/p25 ≤ 2.0".
   - System boundary and architecture overview: the mitigation of risk R-2.
3. **Seed catalogue (Sprint 3):** every model gets a release-specific keyword, checked with the spike script before it is added. Entries for generic mainline castings are avoided, or they are kept with seed prices only.
4. **Tests (Sprint 3):** unit tests for the keyword parser, the title match, and the consistency check, with recorded listing titles instead of live calls.

## 8 How to repeat the spike

```bash
cp .env.example .env            # then set EBAY_ENVIRONMENT=production, EBAY_CLIENT_ID, EBAY_CLIENT_SECRET
python3 spikes/price-source/ebay_spike.py token
python3 spikes/price-source/ebay_spike.py limits
python3 spikes/price-source/ebay_spike.py categories "diecast cars"
python3 spikes/price-source/ebay_spike.py prices
```

Prices change every day, so a new run gives slightly different numbers. The method and the acceptance rule stay the same.
