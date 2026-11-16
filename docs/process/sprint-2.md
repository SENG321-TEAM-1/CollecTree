# Sprint 2 Process Records

## 1 Sprint 1 Retrospective
* **What went well:** GitHub structure and CI/CD pipelines are well established.
* **What did not go well:** Work was concentrated on few members at the start of Sprint 2.
* **Actions for Sprint 2:** Daily written stand-ups and a kick-off meeting to distribute tasks properly (Owner: Feyza).

## 2 Sprint 2 Planning
* **Sprint goal:** Finalize requirements (SRS) and architecture (C4, UML).
* **Dates:** Start 2026-11-14, End 2026-11-24
* **Decisions taken:** 
  - Price source: eBay official API + TCMB currency rates + manually collected seed prices. Auto-scraping from Turkish websites is rejected due to legal risks.
  - Project language is strictly English for all UI and GitHub artifacts.
  - Shared Figma workspace is created by Ata.

## 3 Stand-up Log
| Date | Member | Done | Next | Blockers |
|---|---|---|---|---|
| 2026-11-16 | Feyza | Created Sprint 2 milestone and set up process records | Manage board and daily logs | None |

## 4 Impediment Log
| ID | Date | Impediment | Owner | Action | Status |
|---|---|---|---|---|---|
| IMP-01 | 2026-11-16 | eBay developer account is waiting for approval, spike cannot start. | Berke | The seed price provider is ready as a fallback. | Open |
| IMP-02 | 2026-11-16 | Architecture PRs #93 and #98 are waiting for PO review. | Elif | Review requested in the kick-off meeting. | Open |
| IMP-03 | 2026-11-16 | Sprint 2 work had not started for most members. | Feyza | Kick-off meeting and daily written stand-ups implemented. | Closed |

## 5 Sprint 2 RACI Matrix
| Deliverable | Elif | Feyza | Berke | Kemal | Çağrı | Ata |
|---|---|---|---|---|---|---|
| SRS and refined backlog | A/R | C | C | C | I | C |
| Non-functional requirements | C | I | C | A/R | C | I |
| Figma prototypes and user flows | C | I | C | I | I | A/R |
| C4 and UML architecture document | C | I | A/R | I | C | C |
| Price source spike and ADR-003 | C | I | A/R | I | I | I |
| CI and repository security | I | I | C | C | A/R | I |
| Process records and submission | C | A/R | C | I | I | I |
