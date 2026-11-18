# Software Test Plan — CollecTree

## 1. Document Purpose and Scope
This document defines the overall verification and validation strategy for the **CollecTree** diecast model cataloging and trading platform for **Sprint 2** and subsequent release milestones. It establishes test levels, environments, CI/CD quality gates, entry/exit criteria, risk mitigations, and traceability across functional user stories (`US-01` through `US-09`) and non-functional requirements (`NFR-PERF`, `NFR-REL`, `NFR-SEC`, `NFR-USA`, `NFR-MAIN`, `NFR-PORT`, `NFR-COMP`).

### 1.1 In Scope
* **Authentication & Profile Management (`US-01`, `US-06`):** Registration validation, duplicate credential rejection, password hashing, and JWT-based authentication lifecycle.
* **Collection Management (`US-02`, `US-07`):** Adding diecast models with private purchase metadata, updating item attributes, and removing items from a user's collection.
* **Portfolio & Market Valuation (`US-03`, `US-08`):** Real-time portfolio summary calculations, automated market price retrieval, and TCMB exchange rate fallback behavior.
* **Social Discovery, Messaging & Offers (`US-04`, `US-05`, `US-09`):** Public collection browsing, privacy enforcement on purchase prices, direct messaging threads, and concurrent offer acceptance/cancellation rules.
* **API Contract & Quality Gates:** Compliance with `api/openapi.yaml`, unit test coverage thresholds, and containerized startup verification.

### 1.2 Out of Scope
* Third-party payment gateway settlement (CollecTree coordinates trade and cash offers without in-app financial clearing).
* Native iOS/Android mobile applications (verification targets responsive desktop and mobile web browsers).

---

## 2. Test Levels and Strategy

| Test Level | Target Scope | Tools & Framework | Execution Trigger | Responsibility |
|---|---|---|---|---|
| **Unit Testing** | Domain services, validation rules, JWT utilities, valuation math, TCMB stale-rate fallback (`NFR-REL-02`) | `pytest`, `pytest-cov`, `unittest.mock` | Automated on every Push and Pull Request via GitHub Actions | Implementation & QA Engineers |
| **Integration Testing** | REST API endpoints, database persistence, ownership authorization (`403 Forbidden`), concurrent offer locking (`NFR-REL-03`), expired JWT handling | `pytest`, FastAPI `TestClient` / HTTPX, PostgreSQL test container | Local verification & pre-merge validation (scheduled for CI expansion in Sprint 3) | QA & Test Automation Engineer |
| **API Contract Testing** | Request/response schemas, HTTP status codes, and RFC 9457 `Problem` error payloads against `api/openapi.yaml` (`NFR-COMP-01`) | `validate-openapi`, Schemathesis / OpenAPI schema assertions | Automated in GitHub Actions CI & PR checks | QA & Backend Engineers |
| **System & E2E Testing** | End-to-end user journeys from login to portfolio visualization (`NFR-USA-01`, max 8 clicks) and multi-user offer flows | Manual test scripts, browser DevTools (`NFR-PERF-03`) | Pre-demo and Sprint review staging checks | QA Engineer & Product Owner |
| **Non-Functional & Portability Testing** | Cold/warm Docker startup time (`NFR-PORT-01`), container restart persistence (`NFR-REL-04`), read latency under 1,000 items (`NFR-PERF-01`), cross-browser compatibility (`NFR-COMP-02`) | `docker compose`, load script, Chrome / Firefox / Safari | Before Sprint 2 demo & release freeze | DevOps & QA Engineers |

---

## 3. Test Environment and CI/CD Pipeline

### 3.1 Local & Containerized Test Environment
* **Orchestration:** Docker & Docker Compose (`docker compose up --build`), matching `NFR-PORT-01` targets (initial clean build under 10 minutes; subsequent warm startups under 2 minutes).
* **Database Isolation:** Dedicated PostgreSQL test instance/schema reset per integration test session to prevent cross-test state pollution while verifying volume persistence separately (`NFR-REL-04`).
* **External Provider Stubbing:** eBay pricing sources and TCMB exchange rate endpoints are mocked/stubbed during automated tests to deterministically simulate timeouts, HTTP errors, and weekend/holiday gaps (`NFR-REL-01`, `NFR-REL-02`).

### 3.2 Continuous Integration (GitHub Actions)
* **Trigger:** Every `push` and `pull_request` targeting `develop` or `main`.
* **Execution Time:** Approximately **1 to 1.5 minutes** per workflow run.
* **Automated Quality Gate (`NFR-MAIN-01`):** `pytest` executes the backend unit test suite with `pytest-cov`. The pipeline enforces a **minimum 50% unit test coverage threshold**; any build falling below 50% fails automatically and blocks PR merging.
* **Current Pipeline Boundary:** GitHub Actions currently executes unit tests and OpenAPI contract checks; full database-backed integration suites are executed locally prior to PR approval and are planned for CI pipeline integration in the next iteration.

---

## 4. Entry and Exit Criteria

### 4.1 Entry Criteria
* Feature or bugfix branch is created from `develop` and linked to a tracked GitHub issue.
* API endpoints conform to `api/openapi.yaml` before test execution.
* Local environment builds cleanly with `docker compose up --build` and `.env.example` variables configured.

### 4.2 Exit Criteria (Sprint / Release Gate)
* **100%** of automated unit tests in GitHub Actions pass (`exit code 0`).
* Backend unit test coverage is **at least 50%** (`NFR-MAIN-01`).
* **Zero** open Critical or Blocker defects (including any authentication bypass, cross-user data mutation, or leak of private purchase prices).
* All critical user journeys (`US-01` through `US-09`) verified against acceptance criteria and documented in PR review checks.

---

## 5. Requirements Traceability Matrix (RTM)

| Requirement ID | Feature / Quality Area | Verification Scenario | Planned / Active Test IDs | Verification Method |
|---|---|---|---|---|
| **US-01** | User Registration | Valid registration succeeds; duplicate email/username or weak password (< 8 chars) returns validation error | `US-01.T` (`TC-AUTH-01`..`04`) | Automated API / Unit Test |
| **US-06** | User Login & Session | Valid credentials issue JWT (`JWT_EXPIRE_MINUTES`); invalid credentials return `401`; expired token rejected (`NFR-SEC-02`) | `US-06.T` (`TC-AUTH-05`..`08`) | Automated API / Integration Test |
| **US-02** | Add Collection Item | Authenticated owner adds model with purchase price/date; unauthenticated request returns `401` | `US-02.T` (`TC-COL-01`..`04`) | Automated API Test |
| **US-07** | Remove Collection Item | Owner deletes own item; attempting to delete another user's item returns `403 Forbidden` (`NFR-SEC-03`) | `US-07.T` (`TC-COL-05`..`07`) | Automated API / Integration Test |
| **US-03** | Portfolio Statistics | Total value, item count, and gain/loss metrics match stored collection and market prices; page loads < 2s (`NFR-PERF-03`) | `US-03.T` (`TC-PORT-01`..`03`) | Unit Test + Browser DevTools |
| **US-08** | Market Price Tracking | Daily price job completes < 10 min for 50 models (`NFR-PERF-02`); failed eBay lookup preserves last price (`NFR-REL-01`); holiday TCMB uses stale rate (`NFR-REL-02`) | `US-08.T` (`TC-PRC-01`..`04`) | Unit & Mocked Integration Test |
| **US-04** | Social Discovery | Public profiles/collections are viewable; purchase price and purchase date are stripped from non-owner responses (`NFR-SEC-04`) | `US-04.T` (`TC-SOC-01`..`03`) | Automated API Privacy Test |
| **US-05** | Direct Messaging | Users initiate conversations and exchange messages; unauthorized users cannot read private threads (`NFR-SEC-03`) | `US-05.T` (`TC-MSG-01`..`03`) | Automated API Test |
| **US-09** | Trade / Cash Offers | Offer creation/status updates succeed; accepting one offer concurrently cancels competing offers on the same item (`NFR-REL-03`) | `US-09.T` (`TC-OFR-01`..`04`) | Concurrent Integration Test |

---

## 6. Risk Management and Defect Reporting

### 6.1 Testing Risks and Mitigations
* **External API Instability (eBay / TCMB):** Third-party rate limits or downtime could cause flaky tests. *Mitigation:* Use deterministic HTTP mocks in `pytest` and test stale-data fallback paths explicitly (`NFR-REL-01`, `NFR-REL-02`).
* **Integration Tests Not Yet in CI:** Regressions in database queries or concurrency locks could slip past unit-only CI checks. *Mitigation:* Require local execution of integration tests before PR approval and enforce `CODEOWNERS` review on backend/docs changes.
* **Race Conditions in Offer Acceptance:** Simultaneous `PATCH`/`POST` acceptance requests on a single item. *Mitigation:* Execute parallel async/threaded test requests verifying transactional locking (`NFR-REL-03`).

### 6.2 Defect Severity Classification
* **Critical / Blocker:** Data loss on restart, broken authentication, cross-user modification (`403` bypass), exposure of private purchase prices, or CI pipeline failure. Must be resolved before merge.
* **Major:** Incorrect portfolio calculation, failed offer state transition, or response schema mismatch against `api/openapi.yaml`.
* **Minor:** Non-blocking UI alignment issue or suboptimal error phrasing (`NFR-USA-02`).
