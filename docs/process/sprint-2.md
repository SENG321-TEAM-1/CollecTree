
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
| Record the stand-ups of every member in the process records, using the GitHub history when a written stand-up is missing | Feyza | In progress |

## 2 Sprint 2 Planning

**Sprint goal:** Specify and design CollecTree before implementation: a detailed SRS and refined backlog, measurable non-functional requirements, Figma prototypes with user flows, and a C4 and UML architecture document.

| Deliverable | Owner | Issue / PR |
|---|---|---|
| SRS and refined backlog | Elif | #107, #108/#109, #110/#111 |
| Non-functional requirements and quality measures | Kemal | #123/#124 |
| Test plan (draft for Sprint 3) | Kemal | #125/#126 |
| Figma prototypes and user flows | Ata | #119/#120 |
| Seed catalogue | Ata | #121/#122 |
| C4 and UML architecture document | Berke | #92/#93, #97/#98, #99/#100, #101/#102, #103/#104, #105/#106 |
| Price source spike and ADR-003 | Berke | #96/#117, #127/#128 |
| CI, deployment decisions, and repository security | Çağrı | #94/#95, #114, #115/#116 |
| Process records and submission | Feyza | #113/#118, #129 |

**Decisions taken during planning**
- Market prices come from the eBay Browse API, exchange rates from TCMB, with hand-collected seed prices as the fallback. Automated collection from Turkish listing sites was rejected because their terms of use forbid it (ADR-003).
- When an offer is accepted, the other pending offers with the same items are cancelled and the items are closed for trade (BR-16, BR-17).
- A new endpoint `PATCH /items/{itemId}` lets owners edit their items (US-10).
- The Docker Compose setup was agreed in #114: PostgreSQL 16, a FastAPI backend, and an nginx frontend that forwards `/api` to the backend.
- All repository content and the user interface are in English.
- Ata creates the shared Figma file for the prototypes.

## 3 Stand-up Log

Every member posts a written stand-up in the team chat by 21:00. The Scrum Master copies them here. When a member did not post one, the row is completed from that member's GitHub activity on that day (issues, pull requests, reviews, and commits), so that every working day of every member is visible.

| Date | Member | Done | Next | Blockers |
|---|---|---|---|---|
| 2026-11-14 | Berke | Opened the domain model and database schema issue #92 and pull request #93 | Write the C4 model, the sequence diagrams, and ADR-003 | None |
| 2026-11-16 | Berke | Opened the C4 model (#98), sequence diagrams (#100), ADR-003 (#102), deployment (#104), and architecture overview (#106) pull requests, and the `.gitignore` pull request #95 | Run the price source spike when the eBay account is approved | The eBay developer account is waiting for approval (IMP-01) |
| 2026-11-16 | Elif | Reviewed and approved #93, #98, #100, and #102; added US-10 (#107); opened the backlog update #109 and the SRS draft #111 | Complete the SRS sections | SRS sections 4.1 and 6 wait for the Figma and NFR links |
| 2026-11-16 | Feyza | Created the Sprint 2 milestone and the process records | Manage the board and the daily log | None |
| 2026-11-17 | Berke | Completed the price source spike with the approved eBay account (#96, pull request #117); merged #95; reviewed #116 and #118 | Merge the architecture pull requests and align the documents with the spike | None |
| 2026-11-17 | Çağrı | Reviewed #95 and #98, opened the deployment decisions issue #114, opened the CI check pull request #116 (render-mermaid is green), checked secret scanning and push protection | Merge #116 after Berke's review, review Kemal's NFR pull request when it is opened | None |
| 2026-11-17 | Feyza | Opened the process issue #113 and pull request #118, renamed the board column to "To Do", approved #109, merged #118 | Add the stand-ups every evening | None |
| 2026-11-18 | Kemal | Reviewed #93 for testability and asked four questions; opened the NFR pull request #124 and the test plan pull request #126 | Address the review comments | Waiting for the answers on #93 |
| 2026-11-18 | Ata | Reviewed #98 and #100; opened the user flows pull request #120 (7 flows, 12 screens, Figma prototype) and the seed catalogue pull request #122 | Address the review comments | None |
| 2026-11-19 | Berke | Merged #93, #98, #100, and #102; answered Kemal's questions on #93; opened #128 (ADR-003 accepted); marked #104 ready for review; reviewed #120, #122, #124, and #126 | Re-test the seed catalogue keywords on eBay; review the updated #124 and #126 | None |
| 2026-11-19 | Feyza | Updated the stand-up log and the impediment log (#129) | Collect the stand-ups every evening; prepare the submission document with Berke | None |

## 4 Impediment Log
| ID | Date | Impediment | Owner | Action | Status |
|---|---|---|---|---|---|
| IMP-01 | 2026-11-16 | The eBay developer account is waiting for approval, so the price source spike cannot start. | Berke | The seed price provider was ready as a fallback. Resolved on 2026-11-17: the account was approved and the spike was completed (#96, PR #117). | Closed |
| IMP-02 | 2026-11-16 | Four architecture pull requests (#93, #98, #100, #102) needed the Product Owner review required by CODEOWNERS, while the Product Owner also writes the SRS. | Elif | Review order agreed in the kick-off. Resolved on 2026-11-16: Elif approved all four. | Closed |
| IMP-03 | 2026-11-16 | Sprint 2 work had not started for most members two days after the sprint start. | Feyza | Kick-off meeting, a personal task list for every member, and daily written stand-ups. Resolved on 2026-11-18: Kemal and Ata opened their pull requests (#120, #122, #124, #126), so every member is working. | Closed |
| IMP-04 | 2026-11-19 | Most catalogue numbers in the seed catalogue (#122) do not appear in eBay listings, so the price job finds no price for most of the new models. | Ata | Check every catalogue number on the manufacturer's website or the box, remove the rows that cannot be checked, and test the keywords with the spike script before merging. | Open |
| IMP-05 | 2026-11-19 | Four architecture pull requests (#104, #106, #117, #128) need the code owner approval of the Product Owner, while the Product Owner also finishes the SRS. | Elif | Review order agreed in the team chat: #128 first, then #117, #106, and #104. | Open |

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

