# System Boundary Specification

| Field | Value |
|---|---|
| Project | CollecTree |
| Course | BM 321 / SENG 321 Software Engineering — Sprint 1, updated in Sprint 2 |
| Version | 0.2.0 (draft) |
| Owner (Accountable) | Berke Akman — Lead Software Architect |
| Consulted | Elif Zahide Arat (Product Owner), Ata Eren Atlı (Implementation), Kemal Yusuf Ateşer (QA) |
| Informed | Feyza Sayar (Scrum Master), Çağrı Baynal (DevOps) |

The system vision and the in-scope / out-of-scope list are owned by the Product Owner and are in [README Section 2](../../README.md#2-system-vision-and-boundary). This document describes where the software boundary lies, which external systems it talks to, and what we assume and risk.

---

## 1 System Context Diagram

The same context in C4 notation, with protocols, is in the [C4 model](c4-model.md), Level 1.

```mermaid
flowchart TB
    visitor([Visitor])
    collector([Collector])

    app["<b>CollecTree</b><br/>Web App, REST API and Price Job"]

    pricesrc[(eBay Browse API)]
    fxsrc[(TCMB exchange rates)]

    visitor -->|"browses public profiles and collections (read only)"| app
    collector <-->|"sends: collection items, purchase prices, messages, offers<br/>receives: value, profit and loss charts, offer status, messages"| app
    app -->|"daily search per model; returns active listing prices in USD"| pricesrc
    app -->|"daily rate request; returns the USD to TRY rate"| fxsrc
```

### 1.1 Relationship descriptions

| From | To | Information | Purpose | Trust assumption |
|---|---|---|---|---|
| Visitor | Platform | Public profile and collection requests | Discover collectors before signing up | Unauthenticated; read-only access to public data only |
| Collector | Platform | Account data, collection items, purchase prices, messages, offers | Manage portfolio and trade | Authenticated by JWT; users may modify only their own data |
| Platform | Collector | Valuation, charts, conversations, offer status | Show portfolio value and trade progress | Purchase prices are private to the owner and never shown to other users |
| Platform | eBay Browse API | Search keyword of a model, once a day | Find the current market price (median of new, fixed-price listings) | External data may be missing or wrong; the platform stores only the median, the sample size, the source, and the date, never listing or seller data (ADR-003) |
| Platform | TCMB | Request for today's rates | Convert USD prices to TRY | On weekends, holidays, or errors, the last known rate is used and marked as stale |

## 2 Assumptions

| ID | Assumption | Validation action |
|---|---|---|
| AS-1 | A public source for diecast market prices is reachable. Proposed source: the eBay Browse API (ADR-003). | Price source spike in Sprint 2 (#96); the result accepts or changes ADR-003. |
| AS-2 | Daily price updates are sufficient; collectors do not need minute-by-minute prices. | Product Owner confirms with 3–5 collectors. |
| AS-3 | A pre-filled catalogue of popular models can be prepared by the team for the demo. | Implementation engineer prepares a seed file. |
| AS-4 | TRY is the display currency for all users in the first release. | Product Owner confirms. |

## 3 Constraints

| Type | Constraint |
|---|---|
| Schedule | Ten-week course; MVP by Week 8; live demo in Week 10. |
| Deployment | The whole system must start with one `docker compose up` command. |
| Quality | At least 50 percent unit-test coverage, enforced in GitHub Actions; SonarQube analysis in the final submission. |
| Team | Six third-year students without prior project experience; technology choices favor simplicity (see `docs/adr/`). |
| Legal | The platform must respect the terms of use of external price sources and must not store payment data. |
| Privacy | Personal data is limited to username, email, and password hash. |

## 4 Risks

| ID | Risk | Response |
|---|---|---|
| R-1 | The market price source blocks, limits, or changes its API, or production access is not granted. | Price access sits behind the `PriceProvider` interface; the seed price provider keeps tests and the demo working (ADR-003). |
| R-2 | Model names do not match listings exactly, producing wrong prices. | Use the median of at least 5 listings, drop lots and bundles by title, store the sample size with each price, and let the team correct the search keyword per model in the seed data. No listing data is stored (ADR-003). |
| R-3 | Users treat the platform as responsible for failed off-platform payments. | Clear notice in the offer screen; payments are explicitly out of scope. |
| R-4 | Scope grows beyond what the team can deliver. | Product Owner protects the boundary in this document; new ideas go to the deferred list. |


