# Non-Functional Requirements and Quality Measures

| Field | Value |
|---|---|
| Project | CollecTree |
| Course | BM 321 / SENG 321 Software Engineering — Sprint 2 |
| Version | 0.2.0 |
| Owner (Accountable) | Kemal Yusuf Ateşer — Quality Assurance and Test Automation Engineer |
| Consulted | Berke Akman (Architect), Çağrı Baynal (DevOps), Elif Zahide Arat (Product Owner) |

This document defines the non-functional requirements (NFRs) and measurable quality specifications for the **CollecTree** platform. All requirements are categorized according to the **ISO/IEC 25010** software product quality model. Each specification establishes a concrete, verifiable target alongside its corresponding verification method and architectural or requirement source. The functional requirements are in the SRS; the architectural tactics that meet these requirements are in `docs/architecture/README.md`, section 4. The test plan in `docs/testing/test-plan.md` describes how each requirement is verified.

| ID | Quality characteristic | Requirement | Measure and target | Verification | Source |
|---|---|---|---|---|---|
| NFR-PERF-01 | Performance efficiency | Read endpoints respond quickly. | 95% of `GET` requests finish in under 500 ms with 1,000 collection items in the database. | Load test script run before the demo | Survey: users with large collections |
| NFR-PERF-02 | Performance efficiency | The daily price job finishes in time. | The job finishes in under 10 minutes for 50 catalogue models. | Job duration in the backend log | C4 model, section 3.3 |
| NFR-PERF-03 | Performance efficiency | The portfolio page opens quickly. | The portfolio page is usable in under 2 seconds on a home internet connection. | Browser developer tools, measured manually | US-03 |
| NFR-REL-01 | Reliability | A failing price source does not stop the price job. | If eBay does not answer for a model, its last known price is kept and the job continues with the next model. | Integration test with a failing price provider | US-08, risk R-1 |
| NFR-REL-02 | Reliability | A missing exchange rate does not stop the price job. | On weekends and holidays the last known TCMB rate is used and marked as stale. | Unit test | US-08 |
| NFR-REL-03 | Reliability | Concurrent offer acceptance is safe. | When two offers for the same item are accepted at the same time, exactly one is accepted and the other becomes cancelled. | Integration test with two parallel requests | BR-16, C4 model section 3.2 |
| NFR-REL-04 | Reliability | Data survives a restart. | No data is lost when the database container is stopped and started again. | Manual test with `docker compose restart` | Docker volume |
| NFR-SEC-01 | Security | Passwords are stored safely. | Passwords are hashed with bcrypt; no password is stored or logged in plain text. | Unit test and code review | ADR-001 |
| NFR-SEC-02 | Security | Login tokens expire. | A JWT expires after `JWT_EXPIRE_MINUTES` (default 60 minutes). | Integration test with an expired token | ADR-001 |
| NFR-SEC-03 | Security | Users change only their own data. | Every change to another user's data returns `403 Forbidden`. | Integration test for every changing endpoint | BR-03 |
| NFR-SEC-04 | Security | Purchase prices stay private. | No API response to another user contains a purchase price or purchase date. | Integration test | BR-02 |
| NFR-SEC-05 | Security | No secrets are in the repository. | No password, key, or `.env` file is committed. | `.gitignore` and GitHub push protection | #94 |
| NFR-USA-01 | Usability | The main journey is short. | A new user can log in, add an item, and see the portfolio in at most 8 clicks (including form inputs; 5 action clicks). | Count clicks in the Figma prototype | User flows |
| NFR-USA-02 | Usability | Error messages are helpful. | Every error message says what went wrong and what the user can do next. | Review of the Figma screens and the `Problem` responses | OpenAPI |
| NFR-MAIN-01 | Maintainability | The code is tested. | Unit test coverage is at least 50%; CI fails below 50%. | pytest-cov in GitHub Actions | Course requirement |
| NFR-MAIN-02 | Maintainability | The code has no serious quality issues. | SonarQube reports no blocker or critical issues. | SonarQube report | Course requirement |
| NFR-MAIN-03 | Maintainability | Modules stay independent. | A module reads and writes only its own tables and calls other modules only through their services. | Code review checklist | C4 model, section 3.2 |
| NFR-PORT-01 | Portability | The system starts with one command. | On a clean computer with Docker, the initial `docker compose up --build` starts the whole system in under 10 minutes, and subsequent restarts complete in under 2 minutes. | Manual test on a team member's computer | Course requirement |
| NFR-COMP-01 | Compatibility | The API follows its contract. | Every response matches `api/openapi.yaml`; the contract passes validation in CI. | `validate-openapi` check and integration tests | API-first (ADR-001) |
| NFR-COMP-02 | Compatibility | The web app works in common browsers. | The main journey works in the current versions of Chrome, Firefox, and Safari. | Manual test before the demo | Survey users |
