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
| Post a written stand-up every evening in the team chat | Everyone | Partly done: see section 5 |
| Open a draft pull request early so that reviews can start before the deadline | Everyone | Done |
| Record the stand-ups of every member in the process records, using the GitHub history when a written stand-up is missing | Feyza | Done |

## 2 Sprint 2 Planning

**Sprint goal:** Specify and design CollecTree before implementation: a detailed SRS and refined backlog, measurable non-functional requirements, Figma prototypes with user flows, and a C4 and UML architecture document.

| Deliverable | Owner | Issue / PR |
|---|---|---|
| SRS and refined backlog | Elif | #107, #108/#109, #110/#111 |
| Non-functional requirements and quality measures | Kemal | #123/#124 |
| Test plan (draft for Sprint 3) | Kemal | #125/#126, #134/#135 |
| Figma prototypes and user flows | Ata | #119/#120 |
| Seed catalogue | Ata | #121/#122 |
| C4 and UML architecture document | Berke | #92/#93, #97/#98, #99/#100, #101/#102, #103/#104, #105/#106 |
| Price source spike and ADR-003 | Berke | #96/#117, #127/#128 |
| CI, deployment decisions, and repository security | Çağrı | #94/#95, #114, #115/#116 |
| Process records | Feyza; last update by Berke | #113/#118, #129/#130, #136 (this update) |
| Sprint 2 submission | Berke | – |
| Individual contributions | Berke | #131/#132 |
| Sprint 2 release | Çağrı opened the pull request; Berke merges and publishes | #133 |

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
| 2026-11-19 | Çağrı | Merged the CI check pull request #116, so `render-mermaid` runs on every pull request (closes #115); reviewed and approved the deployment diagram #104 | – | None |
| 2026-11-20 | Berke | Approved #124 and #130; reviewed the updated test plan #126 and asked for four small changes | Re-test the seed catalogue when #122 is updated | Waiting for the Product Owner review of #104, #106, #117, and #128 (IMP-05) |
| 2026-11-20 | Kemal | Updated the non-functional requirements #124 and the test plan #126 after the review; reviewed and approved #117 and #128 | Make the last changes in #126 | None |
| 2026-11-21 | Feyza | Approved the non-functional requirements #124 as code owner | Merge #130 | None |
| 2026-11-21 | Kemal | Added the paging and self-conversation test cases to #126; reviewed and approved the architecture overview #106 | Merge #124 and #126 | None |
| 2026-11-21 | Ata | Merged the user flows #120; updated the seed catalogue #122 with checked catalogue numbers and manual prices; approved #128 | Merge #122 after the review | None |
| 2026-11-22 | Elif | Completed the SRS with the Figma, user flow, and NFR links and the price and paging rules; merged #109 and #111; approved #104, #106, #117, and #128 as code owner | Check my documents in the submission | None |
| 2026-11-22 | Feyza | Approved the SRS #111 as code owner; merged the stand-up update #130 | Update the process records with the review and retrospective | None |
| 2026-11-22 | Berke | Re-tested the 40 seed catalogue keywords (18 accepted) and approved #122; approved #126 and #111; merged #104, #106, #117, and #128; moved US-10 (#107) out of the Sprint 2 milestone; opened #131 for the contributions | Write the Sprint 2 contributions and the submission document | None |
| 2026-11-22 | Çağrı | Made `render-mermaid` a required check next to `validate-openapi`; took the secret scanning and push protection screenshot for the submission; re-reviewed and approved the non-functional requirements #124 | Open the release pull request and publish `v0.2.0-sprint2` | None |
| 2026-11-22 | Kemal | Merged the non-functional requirements #124 and the test plan #126 | – | None |
| 2026-11-23 | Ata | Merged the seed catalogue #122 | – | None |
| 2026-11-23 | Berke | Checked the merged pull requests #122, #124, and #126 and found that the test plan had no links to its source documents; checked that the Figma design file and the prototype open without logging in; opened the contributions pull request #132 | Review the last Sprint 2 pull requests; complete CONTRIBUTIONS.md and the submission document | None |
| 2026-11-23 | Çağrı | Opened the Sprint 2 release pull request #133 (`develop` → `main`) | – | None |
| 2026-11-24 | Kemal | Added links from the test plan to the requirement and architecture documents (#134, pull request #135) | – | None |
| 2026-11-24 | Berke | Opened #136 and completed the process records with the stand-ups of 20–24 November and the Sprint 2 review and retrospective | Publish the release and submit the Sprint 2 submission | None |

## 4 Impediment Log
| ID | Date | Impediment | Owner | Action | Status |
|---|---|---|---|---|---|
| IMP-01 | 2026-11-16 | The eBay developer account is waiting for approval, so the price source spike cannot start. | Berke | The seed price provider was ready as a fallback. Resolved on 2026-11-17: the account was approved and the spike was completed (#96, PR #117). | Closed |
| IMP-02 | 2026-11-16 | Four architecture pull requests (#93, #98, #100, #102) needed the Product Owner review required by CODEOWNERS, while the Product Owner also writes the SRS. | Elif | Review order agreed in the kick-off. Resolved on 2026-11-16: Elif approved all four. | Closed |
| IMP-03 | 2026-11-16 | Sprint 2 work had not started for most members two days after the sprint start. | Feyza | Kick-off meeting, a personal task list for every member, and daily written stand-ups. Resolved on 2026-11-18: Kemal and Ata opened their pull requests (#120, #122, #124, #126), so every member is working. | Closed |
| IMP-04 | 2026-11-19 | Most catalogue numbers in the seed catalogue (#122) do not appear in eBay listings, so the price job finds no price for most of the new models. | Ata | Check every catalogue number on the manufacturer's website or the box, remove the rows that cannot be checked, and test the keywords with the spike script before merging. Resolved on 2026-11-22: the catalogue numbers were checked and 18 of 40 keywords are accepted; the other models keep their manual seed price, as ADR-003 describes. | Closed |
| IMP-05 | 2026-11-19 | Four architecture pull requests (#104, #106, #117, #128) need the code owner approval of the Product Owner, while the Product Owner also finishes the SRS. | Elif | Review order agreed in the team chat: #128 first, then #117, #106, and #104. Resolved on 2026-11-22: Elif approved all four and they were merged. | Closed |

## 5 Sprint 2 Review and Retrospective
Prepared by Berke on 2026-11-24 and reviewed in the pull request of this update. The instructor confirmed that there is no presentation at the end of each sprint; the sprint work is submitted, and there is one presentation at the end of the course.

### Delivered
| Course deliverable | Result | Owner |
|---|---|---|
| Detailed SRS and refined backlog | Done: 22 functional requirements with their user stories, API operations, and business rules; US-10 added to the backlog (48 story points in the first release) | Elif |
| Non-functional requirements and quality measures | Done: 20 requirements grouped by ISO/IEC 25010, each with a measurable target and a verification method; test plan draft for Sprint 3 | Kemal |
| Figma prototypes with user-flow diagrams | Done: 12 screens, a clickable main journey, and 7 user flows | Ata |
| C4 model and UML architecture document | Done: C4 context, container, and component diagrams, 4 sequence diagrams, the deployment diagram, the domain model, ADR-003, and the price source spike | Berke |
| Release | Release pull request #133, published as `v0.2.0-sprint2` after this update is merged, with `validate-openapi` and `render-mermaid` as required checks | Çağrı (release pull request, checks), Berke (merge and publication) |

### Not delivered
- US-10 (Edit Collection Item) is specified in the SRS and the API contract; its implementation is planned for a later sprint, so it was moved out of the Sprint 2 milestone.
- 22 of the 40 seed catalogue models do not get an eBay price yet; they keep their manual seed price. Better search keywords are a Sprint 3 task.

### What went well
- Every Sprint 2 change went through an issue and a reviewed pull request, and the documents were compared with the API contract and with each other on `develop` before the release.
- The price source risk (R-1) was closed early with a spike on real eBay data, so ADR-003 is based on measured results.
- The new `render-mermaid` check renders every diagram on every pull request, so a broken diagram cannot reach `develop`.
- Draft pull requests were opened early, so most reviews started several days before the deadline.

### What did not go well
- Written stand-ups were still missing on many days; the log was completed from the GitHub history.
- Several pull requests waited for a single code owner approval (IMP-02, IMP-05).
- Some pull requests needed more than one review round because the first version did not follow the agreed rules (for example the seed catalogue numbers, IMP-04).

### Actions for Sprint 3
| Action | Owner |
|---|---|
| Post the stand-up in the team chat before 21:00; Feyza reminds the members who have not posted by 20:00 | Feyza, everyone |
| Review the pull requests that need your code owner approval within one day; tell the team when you cannot | Elif, Berke |
| Check a pull request against its issue and the review checklist before asking for a review | Everyone |
| Split the implementation into small pull requests per user story, so that reviews stay short | Ata, Berke |

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
| Process records | C | A/R | C | I | I | I |
| Sprint 2 submission | C | C | A/R | C | C | C |

