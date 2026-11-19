# ADR-003: Market Price and Exchange Rate Source

| Field | Value |
|---|---|
| Status | Proposed (to be accepted after the price source spike, #96) |
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
- One request per catalogue model per day, using the model's `search_keyword`, the diecast leaf category, and the filters `conditionIds:{1000}` (new) and `buyingOptions:{FIXED_PRICE}` (no auctions).
- Listings whose titles show several models or modified models (lot, bundle, loose, custom, repaint) are dropped.
- The price is the **median** of the remaining USD prices, without shipping. If fewer than 5 listings remain, the last known price is kept.

**2. Exchange rate: TCMB (Central Bank of the Republic of Turkey).**
- `https://www.tcmb.gov.tr/kurlar/today.xml`, USD `ForexSelling`.
- On weekends and holidays, or when TCMB is not reachable, the last known rate is reused and marked as stale.

**3. Fallback: seed prices.**
- The team collects TRY prices for the seed catalogue **by hand**, by viewing Turkish listing sites in a normal browser, and records the source and date of each price.
- `SeedPriceProvider` serves these prices. It is used in all tests, in the demo if eBay is not available, and whenever `PRICE_PROVIDER=seed`.

**4. Data kept from eBay.** Only one median price per model per day and the number of listings it came from (`sample_size`). No listing, seller, or user data is stored. This lets the team truthfully opt out of eBay's marketplace account deletion notifications ("Not persisting eBay data").

**5. Presentation.** The user interface labels the price as "International listing price (eBay), converted to TRY", so that it is not mistaken for a Turkish sale price.

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
- **Negative:** Search keywords can match the wrong model (risk R-2). The median, the title filter, and the minimum of 5 listings reduce the effect; the team corrects keywords in the seed data.

## Validation

The price source spike (#96) confirms or rejects this decision. This ADR becomes **Accepted** when the spike shows:

- [ ] an active Production keyset, and the daily call limit of the application;
- [ ] the leaf category ID for diecast cars;
- [ ] plausible medians for at least 8 of 10 test models;
- [ ] no clause in the eBay API License Agreement that forbids storing an aggregated daily median.

If the spike fails, this ADR is updated with decision 3 (seed prices) as the official source.

## References

- [eBay Browse API overview](https://developer.ebay.com/api-docs/buy/browse/static/overview.html) and [Buy API field filters](https://developer.ebay.com/api-docs/buy/static/ref-buy-browse-filters.html)
- [eBay API License Agreement](https://developer.ebay.com/products/license)
- [eBay marketplace account deletion notifications](https://developer.ebay.com/marketplace-account-deletion)
- [TCMB daily exchange rates](https://www.tcmb.gov.tr/kurlar/today.xml)
- [sahibinden.com terms of use (Ek-1)](https://www.sahibinden.com/sozlesmeler/ek-1-kullanim-kosullari-37)
- [Trendyol robots.txt](https://www.trendyol.com/robots.txt)
