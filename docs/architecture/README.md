# CollecTree Architecture

| Field | Value |
|---|---|
| Project | CollecTree |
| Course | BM 321 / SENG 321 Software Engineering — Sprint 2 deliverable "C4 model and UML architecture document" |
| Version | 0.2.0 |
| Owner (Accountable) | Berke Akman — Lead Software Architect |
| Reviewed by | Elif Zahide Arat (Product Owner), Çağrı Baynal (DevOps), Ata Eren Atlı (Implementation), Kemal Yusuf Ateşer (QA) |

**In one sentence:** CollecTree is an API-first **modular monolith**: a React web app, one FastAPI backend split into seven modules with strict boundaries, and a PostgreSQL database, started together with one `docker compose up`, with market prices fetched once a day from the eBay Browse API and converted to TRY with the TCMB rate.

This page is the entry point to the architecture. Each view is kept in its own file so that it can be reviewed and changed on its own; this page explains how they fit together and why.

---

## 1 Architecture drivers

The architecture is shaped by these requirements and constraints.

| Driver | Source | Effect on the architecture |
|---|---|---|
| Daily market value and profit or loss in TRY | Core value; US-03, US-08 | A scheduled price job, a price provider interface, and stored daily prices and rates |
| Formal offers that stay consistent when users act at the same time | US-09, BR-16, BR-17 | Offer life cycle with a final `CANCELLED` state, transactions, row locks in a fixed order |
| Purchase prices are private | BR-02 | Owner-only fields filtered in the `collection` service |
| Whole system starts with one command | Course requirement | Three Docker Compose services, configuration only through `.env` |
| At least 50% unit-test coverage, SonarQube analysis | Course requirement | Modules with a router, service, and data layer that can be tested separately; external systems replaced in tests |
| API-first development | Course topic (Week 3) | `api/openapi.yaml` is written and validated in CI before the code |
| Six students without project experience, ten weeks | Team constraint | One language on the backend, one deployable backend, well-known open-source tools |
| Respect the terms of use of external sources; no payments | System boundary | eBay's official API instead of scraping; cash amounts in offers are information only |

---

## 2 Main decisions

| Decision | Reason | Record |
|---|---|---|
| Modular monolith with seven modules, not microservices | Clear boundaries without the network, deployment, and data consistency cost of microservices | [ADR-001](../adr/ADR-001-architecture-style-and-technology-stack.md) |
| FastAPI, PostgreSQL, React with Vite, Docker Compose | Simple, documented, open source, familiar to the team | [ADR-001](../adr/ADR-001-architecture-style-and-technology-stack.md) |
| MIT License | Permissive; compatible with every dependency | [ADR-002](../adr/ADR-002-open-source-license.md) |
| eBay Browse API for prices, TCMB for rates, seed prices as fallback | Legal, structured access; scraping Turkish sites is forbidden by their terms | [ADR-003](../adr/ADR-003-market-price-and-exchange-rate-source.md) |
| Modules use each other only through services, in a fixed order without cycles | Each module can be built and tested by a different member | [C4 model](c4-model.md), section 3.2 |
| Collection items are soft deleted | The portfolio history and offer history must not change | [Domain model](domain-model.md), section 2.2 |
| Portfolio values are calculated, not stored | They can never get out of sync with items and prices | [Domain model](domain-model.md), section 2.2 |
| Accepting an offer locks items first, then offers | Prevents double acceptance and deadlocks | [UML diagrams](uml-diagrams.md), section 4 |
| Only an aggregated median is stored from eBay | Minimal data; truthful exemption from eBay's deletion notifications | [ADR-003](../adr/ADR-003-market-price-and-exchange-rate-source.md) |
| Prices derived from eBay are used only inside CollecTree; list endpoints return at most 50 entries per page | Stays inside the eBay API License Agreement: no export, bulk download, or data feed | [ADR-003](../adr/ADR-003-market-price-and-exchange-rate-source.md), decision 6 |

---

## 3 Architecture views

Read the views in this order. Each one zooms in on the previous one.

| # | View | What it shows | File |
|---|---|---|---|
| 1 | System context | Users, CollecTree, eBay, TCMB; assumptions, constraints, risks | [system-boundary.md](system-boundary.md) |
| 2 | C4 Level 1: System Context | The same context in C4 notation with protocols | [c4-model.md](c4-model.md#1-level-1-system-context) |
| 3 | C4 Level 2: Containers | Web app, REST API with the price job, database | [c4-model.md](c4-model.md#2-level-2-containers) |
| 4 | C4 Level 3: Components | The seven backend modules, their tables, endpoints, and dependency rules | [c4-model.md](c4-model.md#3-level-3-components-of-the-rest-api) |
| 5 | UML class diagram (domain model) | Business objects and their relationships | [domain-model.md](domain-model.md#1-domain-model) |
| 6 | Database schema (ER diagram) | Tables, keys, constraints, and indexes | [domain-model.md](domain-model.md#2-database-schema-er-diagram) |
| 7 | Business rules | BR-01 to BR-19, where each is enforced, and the API result | [domain-model.md](domain-model.md#3-business-rules) |
| 8 | UML state diagram | The life cycle of an offer | [domain-model.md](domain-model.md#31-offer-life-cycle) |
| 9 | UML sequence diagrams | Login, adding an item, the daily price job, accepting an offer | [uml-diagrams.md](uml-diagrams.md) |
| 10 | UML deployment diagram | Docker Compose services, ports, volume; operating and recovery guide | [deployment.md](deployment.md) |
| 11 | API contract | Every endpoint, request, response, and error | [`api/openapi.yaml`](../../api/openapi.yaml) |

Requirements that the architecture implements: [product backlog](../requirements/product-backlog.md), the SRS, and the non-functional requirements in `docs/requirements/`.

---

## 4 How the quality attributes are achieved

Each quality attribute from the non-functional requirements is reached through a concrete architectural tactic.

| Quality attribute | Tactic | Where |
|---|---|---|
| **Reliability:** an external source fails | Last known price and rate are kept; one failing model does not stop the job; the seed provider can replace eBay | [Sequence diagram 3](uml-diagrams.md#3-daily-price-job), [ADR-003](../adr/ADR-003-market-price-and-exchange-rate-source.md) |
| **Reliability:** two users act at the same time | One transaction per request; items locked before offers; status checked again after locking; database constraints for unique pairs and daily prices | [Sequence diagram 4](uml-diagrams.md#4-accept-an-offer), [domain model 2.1](domain-model.md#21-constraints-and-indexes) |
| **Reliability:** data survives restarts | Data in the `pgdata` volume; backup and restore commands | [Deployment, sections 4 and 5](deployment.md#4-operating-the-system) |
| **Security:** authentication | bcrypt password hashes, signed JWT with expiry, one shared `get_current_user` check | [Sequence diagram 1](uml-diagrams.md#1-log-in-and-call-a-protected-endpoint) |
| **Security:** authorization and privacy | Ownership checked in services (BR-03); purchase prices left out for others (BR-02) | [Business rules](domain-model.md#3-business-rules) |
| **Security:** secrets and attack surface | Secrets only in `.env`; only the web port is published; the database is internal | [Deployment, section 1](deployment.md#1-uml-deployment-diagram) |
| **Maintainability:** change one module without breaking others | Each module owns its tables; services depend only on lower modules; no cycles | [C4 model, section 3.2](c4-model.md#32-dependency-rules) |
| **Testability:** 50% coverage without external systems | Business rules in services, not in routers; `PriceProvider` interface replaced by the seed provider in tests | [C4 model, section 3.1](c4-model.md#31-components) |
| **Interoperability:** the web app and the API agree | API-first contract validated in CI; one error format (`Problem`); validation errors mapped to `400` | [UML diagrams, section 0](uml-diagrams.md#0-conventions-for-every-request) |
| **Portability:** runs on any team member's machine | Docker images, one command, configuration only through environment variables | [Deployment](deployment.md) |
| **Performance:** pages stay fast as data grows | Indexes on owner, model, and conversation; one price request per model, not per item | [Domain model 2.1](domain-model.md#21-constraints-and-indexes) |

---

## 5 Risks and technical debt

| ID | Risk or debt | Impact | Response | Status |
|---|---|---|---|---|
| R-1 | eBay production access is not granted or is limited | No real daily prices | Seed provider is the official source; eBay stays behind the interface | Mitigated: the Production keyset is active with 5,000 calls per day (#96) |
| R-2 | Search keywords match the wrong model | Wrong prices | One catalogue model per release with a release-specific keyword; titles must match the keyword; a price is saved only if at least 5 listings remain and p75/p25 ≤ 2.0 | Mitigated: 10 of 10 test models consistent in the spike (#96) |
| TD-1 | The price job runs inside the API process | A long or failing job uses API resources | The job is light; it can move to its own container without code changes | Accepted for the first release |
| TD-2 | Messages and offers are refreshed by polling | Updates arrive with a delay | WebSocket is a later improvement (ADR-001) | Accepted for the first release |
| TD-3 | Prices are US asking prices, not Turkish sale prices | Values can differ from the Turkish market | Clear label in the interface; a better source can be added behind the interface | Accepted, documented in ADR-003 |
| TD-4 | Dependency rules are checked only in code review | A wrong import can break module boundaries | Add an automated import check in CI in Sprint 3 | Planned |

---

## 6 Change process

- A change to the architecture is made in a pull request that updates the affected views in the same PR.
- A change to a decision is recorded as a new ADR or as an update to an existing one; old decisions are marked *Superseded*, never deleted.
- Changes to `docs/architecture/`, `docs/adr/`, and `api/openapi.yaml` need the approval of the architect and the Product Owner (`CODEOWNERS`).
- The CI checks that the API contract is valid. All diagrams are rendered and reviewed before merge.
