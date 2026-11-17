# Sprint 2 Process Records

| Field | Value |
|---|---|
| Sprint | 2 — Requirements & Architecture |
| Dates | 2026-11-14 to 2026-11-24 |
| Owner (Accountable) | Feyza Sayar — Scrum Master and Agile Process Coach |

## 1 Sprint 1 Retrospective

### What went well
- Every change went through an issue and a reviewed pull request, and the branch rules and CODEOWNERS were followed.
- The OpenAPI contract is checked automatically on every pull request.
- The Sprint 1 release was tagged and submitted on time.

### What did not go well
- Most of the work was done in the last days of the sprint.
- Only a few written stand-ups were recorded.
- The work was not shared evenly between the members.

### Actions for Sprint 2
| Action | Owner | Status |
|---|---|---|
| Hold a kick-off meeting and give every member a written task list | Feyza | Done |
| Post a written stand-up every evening in the team chat | Everyone | In progress |
| Open a draft pull request early so that reviews can start before the deadline | Everyone | In progress |

## 2 Sprint 2 Planning

**Sprint goal:** Specify and design CollecTree before implementation: a detailed SRS and refined backlog, measurable non-functional requirements, Figma prototypes with user flows, and a C4 and UML architecture document.

| Deliverable | Owner | Issue / PR |
|---|---|---|
| SRS and refined backlog | Elif | #107, #108/#109, #110/#111 |
| Non-functional requirements and quality measures | Kemal | To be added |
| Figma prototypes and user flows | Ata | To be added |
| C4 and UML architecture document | Berke | #92/#93, #97/#98, #99/#100, #101/#102, #103/#104, #105/#106 |
| Price source spike | Berke | #96 |
| CI and repository security | Çağrı | #94/#95 |
| Process records and submission | Feyza | #113 |

**Decisions taken during planning**
- Market prices come from the eBay Browse API, exchange rates from TCMB, with hand-collected seed prices as the fallback. Automated collection from Turkish listing sites was rejected because their terms of use forbid it (ADR-003).
- When an offer is accepted, the other pending offers with the same items are cancelled and the items are closed for trade (BR-16, BR-17).
- A new endpoint `PATCH /items/{itemId}` lets owners edit their items (US-10).
- All repository content and the user interface are in English.
- Ata creates the shared Figma file for the prototypes.

## 3 Stand-up Log
| Date | Member | Done | Next | Blockers |
|---|---|---|---|---|
| 2026-11-16 | Feyza | Created the Sprint 2 milestone and the process records | Manage the board and the daily log | None |
| 2026-11-17 | Feyza | Opened the process issue and fixed the README link | Add the stand-ups every evening | None |

## 4 Impediment Log
| ID | Date | Impediment | Owner | Action | Status |
|---|---|---|---|---|---|
| IMP-01 | 2026-11-16 | The eBay developer account is waiting for approval, so the price source spike cannot start. | Berke | The seed price provider is ready as a fallback; the spike starts when the account is approved. | Open |
| IMP-02 | 2026-11-16 | Four architecture pull requests (#93, #98, #100, #102) needed the Product Owner review required by CODEOWNERS, while the Product Owner also writes the SRS. | Elif | Review order agreed in the kick-off. Resolved on 2026-11-16: Elif approved all four. | Closed |
| IMP-03 | 2026-11-16 | Sprint 2 work had not started for most members two days after the sprint start. | Feyza | Kick-off meeting, a personal task list for every member, and daily written stand-ups. | Open |

## 5 Sprint 2 Review and Retrospective
To be filled on 2026-11-23: what was delivered, what was not, what went well, and what to improve in Sprint 3, with owners.

## 6 Sprint 2 RACI
R = Responsible, A = Accountable, C = Consulted, I = Informed.

| Deliverable | Elif | Feyza | Berke | Kemal | Çağrı | Ata |
|---|---|---|---|---|---|---|
| SRS and refined backlog | A/R | C | C | C | I | C |
| Non-functional requirements | C | I | C | A/R | C | I |
| Figma prototypes and user flows | C | I | C | I | I | A/R |
| C4 and UML architecture document | C | I | A/R | I | C | C |
| Price source spike and ADR-003 | C | I | A/R | I | I | I |
| CI and repository security | I | I | C | C | A/R | I |
| Process records and submission | C | A/R | C | I | I | I |
