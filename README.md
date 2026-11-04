# CollecTree
## Git-Flow & Branching Rules
As part of our CI/CD and DevOps infrastructure, we have established the following Git-Flow rules:
* **`main` branch:** Protected branch. Direct commits are blocked. This branch is strictly for tested, working releases.
* **`develop` branch:** The primary integration branch for ongoing development.
* **Pull Requests:** All changes must be pushed to a feature branch and merged into `develop` or `main` via a Pull Request. At least 1 code review approval is required before merging.

## Team Members and Roles
* [Çağrı Baynal] - DevOps and CI/CD Infrastructure Engineer
* [Elif Zahide Arat] - Product Owner and Requirements Engineer
* [Feyza Sayar] - Scrum Master and Agile Process Coach
* [Berke Akman] - Lead Software Architect and Technical Lead
* [Kemal Yusuf Ateşer] - Quality Assurance and Test Automation Engineer
* [Ata Eren Atlı] - Implementation and Integration Engineer
  
# 1. Project Proposal

### Problem Definition
Diecast model car collectors (for example Hot Wheels and MiniGT, in scales such as 1:64 and 1:18) currently track their collections with phone notes and photos, spreadsheets, or notebooks, and many do not track them at all. These methods are difficult to keep synchronized, cannot show the current market value of a collection, and cannot show how much profit or loss the collector has made since purchase. Collector apps exist (see Supporting Evidence), but they focus on cataloguing and valuation, keep some valuation features behind paid plans, and support trading only through marketplace listings or a "for trade" mark. Collectors still have no structured way to offer items, cash, or both for another collector's model and track the answer.

### Supporting Evidence

#### Competitor Analysis
We reviewed existing collector platforms on 30 October 2026, based on their public websites and app store descriptions.

| Platform | What it offers | What is missing for our users |
|---|---|---|
| [hobbyDB](https://help.hobbydb.com) | Large collectibles catalogue, collection management, and a marketplace | Estimated collection value requires a Premium plan; trading works as marketplace selling, not structured offers |
| [Hunt64](https://apps.apple.com/app/id6757083316) | Hot Wheels catalogue, price paid vs. estimated value, swapping with nearby collectors | Focused on Hot Wheels; no item-plus-cash offers with accept, reject, and withdraw |
| [Carlect](https://apps.apple.com/us/app/id6759272451) | Collection value, value growth over time, brand and series breakdown | No trading between collectors |
| [DiecastDB](https://apps.apple.com/app/id1644711318) | Diecast catalogue; models can be marked "For Trade" or "For Sale" | The trade itself is not supported; users must agree elsewhere |
| [Diecast Hub](https://apps.apple.com/us/app/id6751733514) | Value guide based on market trends, wishlist, community features | No structured trade or cash offers |

**Our difference:** CollecTree combines automatic daily valuation in Turkish lira, profit and loss over time, and formal item, cash, or mixed offers in one free platform for diecast collectors.

#### Collector Survey
We ran an anonymous online survey with diecast collectors in Turkey between 30 October and 1 November 2026 and received **27 responses** ([raw responses in Turkish](docs/requirements/collector-survey-responses.csv)).

| Topic | Result |
|---|---|
| Collection size | 15 (56%) own 1–20 models, 8 (30%) own 21–100, and 4 (15%) own more than 100 |
| How they track their collection | 14 (52%) do not track it at all; 7 (26%) use phone notes or photos, 3 (11%) spreadsheets, 2 (7%) notebooks, and only 2 (7%) an app |
| Knowledge of current market value | Only 3 (11%) follow it regularly; 13 (48%) know it roughly and 11 (41%) do not know it |
| Where they check prices | 16 (59%) check Turkish listing sites and 5 (19%) check eBay |
| Trading in the last year | 19 (70%) did not trade; those who traded agreed mostly on listing sites (5) or face to face (3) |
| Problems mentioned in trades | Lack of trust, missing information about the item, condition problems after the trade, and prices above market value |

**Importance of the planned features** (average score from 1 to 5):

| Feature | All (27) | More than 20 models (12) | 1–20 models (15) |
|---|---|---|---|
| Keeping the collection in one place | 3.63 | 4.42 | 3.00 |
| Seeing the current market value automatically (TRY) | 3.41 | 4.25 | 2.73 |
| Seeing the total profit or loss | 3.11 | 4.25 | 2.20 |
| Viewing other collectors' collections | 3.30 | 3.92 | 2.80 |
| Sending item, cash, or mixed offers | 3.37 | 4.25 | 2.67 |

**What we learned:**
- Collectors with more than 20 models rated every feature between 3.9 and 4.4, while collectors with small collections rated them between 2.2 and 3.0. The primary users of CollecTree are therefore collectors with larger collections.
- 89% of the respondents do not follow the value of their collection regularly, and almost no one uses an app to track it. This supports automatic valuation as the core feature.
- Most collectors check prices on Turkish listing sites rather than eBay. This supports showing values in TRY, and the choice of the price source will be reviewed in the Sprint 2 price source spike (assumption AS-1).
- Trust and price disagreements were the main trade problems. Showing the market value next to an offer can help both sides agree on a fair price.

### Stakeholders
- **Primary Users:** Diecast collectors with larger collections (more than about 20 models) who need digital inventory tracking, automatic valuation, and a predictable way to negotiate trades.
- **Secondary Users:** Visitors and collectors with small collections who browse public collections before registering.
- **External Dependencies:** A market price data source (for example eBay listings) that provides current new-in-box prices, and a currency exchange rate source that converts USD prices to TRY.

### Stakeholder Analysis

| Stakeholder | Interest | Influence | Main expectations | How we involve them |
|---|---|---|---|---|
| Diecast collectors (primary users) | High | High | Easy item entry, correct market values, private purchase prices, simple trade offers | Collector survey in Sprint 1; feedback on Figma prototypes in Sprint 2 |
| Visitors | Medium | Low | Browse public collections without an account | Public pages need no login |
| Course instructor and jury | High | High | Working product, traceable process, clear architecture decisions | Sprint submissions, release tags, and the final architectural defense |
| Development team | High | High | Realistic scope and a stack the team can learn quickly | Sprint planning, RACI matrix, and ADRs |
| Market price source (for example eBay) | Low | High | Use of the data within its terms and request limits | One request per model per day; a mock provider if access is not possible |
| Exchange rate source | Low | Medium | Use within its terms | Daily rate; the last known rate is used if it is unavailable |

### Feasibility Assessment

| Area | Assessment | Result |
|---|---|---|
| **Technical** | The stack (FastAPI, PostgreSQL, React, Docker Compose) is open source, well documented, and suited to a team without project experience (ADR-001). The main technical uncertainty is access to a real market price source (assumption AS-1). | Feasible. A Sprint 2 spike tests the price source; a mock price provider keeps development, tests, and the demo working if access fails. |
| **Schedule** | The course gives 10 weeks: requirements and design until Week 5, the MVP in Week 8, and the final product in Week 10. The first release has 9 user stories (45 story points) shared by six members. Photo upload and payments are left out of scope to keep the release realistic. | Feasible, provided the MVP starts with the high-priority stories (accounts and collection). |
| **Team** | Six members with named roles (see Section 5). No member has previous project experience, so the team chose the simplest suitable stack and a modular monolith instead of microservices. | Feasible with peer reviews and the code review guidelines. |
| **Cost** | All tools are free: GitHub, GitHub Actions for public repositories, Docker, and open-source libraries. External data sources are used only within free access; otherwise the mock provider is used. | No budget is needed. |
| **Legal and ethical** | The platform does not process payments, so no payment regulation applies. Personal data is limited to username, email, and a password hash, in line with the Turkish data protection law (KVKK). External price data is used within the source's terms. Brand and model names are used only to identify items. | Feasible. Purchase prices stay private to the owner. |

**Conclusion:** The project is feasible within the course time frame. The highest risk, the external price source, has a fallback that protects the MVP and the demo.

### Intended Outcome
A specialized digital portfolio platform that allows diecast collectors to manage their collections with brand, scale, series, and purchase details. The system automatically finds the current new-in-box market price of each model and shows the collector's total collection value and profit or loss over time. The platform also serves as a social network, enabling collectors to view public collections, chat through direct messages (DM), and send formal trade, cash, or mixed offers.

### Initial Success Measure
A collector successfully creates a profile, adds a new collection item with its purchase price, and sees its current market value and profit or loss in their portfolio in less than two minutes.



---

# 2. System Vision and Boundary

### System Vision
To simplify and digitalize diecast collection management, show collectors the real market value of their collections, and build a dedicated social network for trading diecast models.

### First Release Scope (In Scope)
- User authentication and profile creation
- Adding/removing collection items (brand, scale, series, purchase price, and purchase date)
- Filtering collections by brand, scale, and series
- Automatic daily market price tracking for each model through an external price source
- Automated calculation of total portfolio value and profit or loss, with history charts
- Viewing other users' public collections (purchase prices stay private)
- Direct Messaging (DM) system for trade negotiations
- Formal offers on collection items: item-for-item, item plus cash, or cash only, which the receiver can accept or reject

### Exclusions (Out of Scope)
- **Financial transactions:** The system will strictly NOT process any payments. Payment gateways, digital wallets, shopping carts, checkout processes, and shipping tracking are completely outside the system boundaries. Cash amounts in offers are only information; all trade agreements and payments are handled externally by the users (in person or by IBAN).
- **Other collectible types:** Lego, vinyl records, stamps, and other non-diecast collectibles are not supported.
- **Condition-based pricing:** The system always uses the new-in-box market value. There is no automatic price reduction for unboxed or damaged items; users negotiate condition themselves.
- **Deferred to a later release:** Item photo upload (items show the catalogue image in the first release).

---

# 3. Assumptions and Risks

| Type | Statement | Validation or response |
|---|---|---|
| Assumption | Intended users have valid email addresses for registration. | Confirm during the sign-up process |
| Assumption | A public source for diecast market prices is reachable. | Architect tests the price source in Sprint 2 |
| Risk | The external price source may be unavailable, limited, or return wrong prices for a model. | Prices are fetched by a background job behind an adapter; the last known price is shown and a mock price source keeps tests and the demo working |
| Risk | Users may enter wrong purchase prices for their items. | Purchase prices are private and only affect the user's own profit or loss; they are never shown to other users |
| Risk | Concurrent message requests may create duplicate DMs. | Treat as an architecture driver and integration-test it |

---

# 4. Open-Source License Decision Record

**Decision:** MIT License for original project code

**Rationale:**
- Provides a short, permissive license.
- Permits use, modification, and redistribution
- Fits the team's intended permissive reuse model

---

# 5. Team Roles, RACI Matrix, and Agile Process Management

### 5.1 Team Member Roles and Responsibilities

| Team Member | Role Title | Domain | Primary Responsibilities & Sprint 1 Outputs |
| :--- | :--- | :--- | :--- |
| **Elif Zahide Arat** | Product Owner and Requirements Engineer | Product | Writes the project proposal (problem statement, target users, expected outcomes, feasibility, risks), the system vision, and the open-source license decision. Creates and prioritizes the initial user stories with effort estimates in the Product Backlog. |
| **Feyza Sayar** | Scrum Master and Agile Process Coach | Process | Prepares the team roles documentation and the Sprint 1 RACI matrix. Administers the GitHub Projects board, keeps stand-up and retrospective records, tracks impediments, and watches delivery dates. |
| **Berke Akman** | Lead Software Architect and Technical Lead | Architecture | Defines the system boundary (Mermaid context diagram, assumptions, constraints, risks) and the architecture decisions (ADRs). Designs the `openapi.yaml` contract for collection management, price tracking, messaging, and offers. Leads technical peer reviews. |
| **Kemal Yusuf Ateşer** | Quality Assurance and Test Automation Engineer | Quality | Defines testable acceptance criteria for the backlog user stories. Checks the error responses in the OpenAPI contract (`400`, `401`, `403`, `404`, `409`), plans the test strategy, and reviews pull requests for quality. |
| **Çağrı Baynal** | DevOps and CI/CD Infrastructure Engineer | DevOps | Sets up the GitHub organization and repository. Configures the branch protection ruleset on `main` and `develop` and the CI status check, and documents the Git-Flow workflow and merge policy. |
| **Ata Eren Atlı** | Implementation and Integration Engineer | Implementation | Works on issue-based feature branches following the Git-Flow rules, checks that frontend and backend plans match the OpenAPI contract, and takes part in peer reviews. |

---

### 5.2 Sprint 1 RACI Responsibility Matrix

* **R (Responsible):** The team member(s) who do the work.
* **A (Accountable):** The single team member who owns and approves the deliverable.
* **C (Consulted):** Team members who give input before the work is finished.
* **I (Informed):** Team members who are kept up to date.

| Sprint 1 Deliverable / Task | Elif (PO) | Feyza (SM) | Berke (Arch) | Kemal (QA) | Çağrı (DevOps) | Ata (Impl) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1.1 Project Proposal, Problem Statement & Stakeholders** | **A / R** | I | C | I | I | I |
| **1.2 Feasibility, Risks & Open-Source License Selection** | **A / R** | I | C | I | C | I |
| **2.1 System Vision & First Release Scope** | **A / R** | I | C | C | I | C |
| **2.2 System Boundary & Mermaid Context Diagram** | C | I | **A / R** | I | I | C |
| **2.3 Architecture Decision Records (ADRs)** | C | I | **A / R** | I | C | C |
| **3.1 OpenAPI Draft (`openapi.yaml` Endpoints & Schemas)** | C | I | **A / R** | C | I | C |
| **3.2 OpenAPI Error Scenarios (`400`, `401`, `403`, `404`, `409`)** | I | I | **A** | **R** | I | C |
| **4.1 Team Roles & RACI Matrix Documentation** | C | **A / R** | I | I | I | I |
| **4.2 GitHub Projects Board Administration & Tracking** | C | **A / R** | I | I | I | I |
| **4.3 Stand-up, Retrospective & Impediment Records** | C | **A / R** | C | C | C | C |
| **5.1 GitHub Repository Setup & Branch Protection Rules** | I | C | C | I | **A / R** | I |
| **5.2 Git-Flow Policy Documentation** | I | C | C | I | **A / R** | C |
| **5.3 Pull Request Peer Reviews & Contract Verification** | I | I | **A / R** | **R** | I | **R** |
| **6.1 Initial Product Backlog (Epics, User Stories & Estimates)** | **A / R** | C | C | C | I | C |
| **6.2 User Story Acceptance Criteria** | **A** | I | C | **R** | I | C |

---

### 5.3 Agile Process Management, Stand-up, and Retrospective Records

#### A. Board Administration (GitHub Projects)
Our board has five columns, so every requirement can be traced to its delivery:
1. **Backlog:** Prioritized user stories and epics created by the Product Owner.
2. **To Do (Sprint 1):** Tasks committed for Sprint 1 with owners, labels, and effort estimates.
3. **In Progress:** Tasks being worked on in their own branches.
4. **In Review:** Tasks with an open pull request waiting for peer review.
5. **Done:** Tasks merged into `develop` after review.

**Board link:** [CollecTree Sprint Board](https://github.com/orgs/SENG321-TEAM-1/projects/1)

#### B. Sprint 1 Stand-up Meeting Logs
Each entry is added after the meeting takes place.

| Date | Attendees | Summary & Key Decisions |
| :--- | :--- | :--- |
| 2026-10-20 | All members (Elif, Feyza, Berke, Kemal, Çağrı, Ata) | Kick-off meeting. Chose the project topic (CollecTree, a portfolio and trading platform for diecast collectors) and agreed on each member's Sprint 1 role and tasks. |
| 2026-10-21 | All members (Elif, Feyza, Berke, Kemal, Çağrı, Ata) | Created the GitHub organization and invited the team members. Reviewed the problem definition and the in-scope / out-of-scope items prepared by the Product Owner. Reviewed the first draft of the OpenAPI contract (`openapi.yaml`). |
| 2026-10-28 | All members (Elif, Feyza, Berke, Kemal, Çağrı, Ata) | Started the pull request workflow and began uploading the Sprint 1 documents to GitHub. Made the needed repository adjustments on GitHub (branch protection, merge settings, reviews). |
| 2026-11-04 | All members (Elif, Feyza, Berke, Kemal, Çağrı, Ata) | Final Sprint 1 stand-up and retrospective. Reviewed the work since 28 October: the QA review of all user stories (#31) and the Product Owner's updates, the accepted ADRs (#35), the project board link (#36), the consistency fixes (#40), and the Sprint 1 release `v0.1.0-sprint1` (#39). Confirmed the Sprint 1 submission document. No open impediments. |

#### C. Impediment Tracking Log

| ID | Impediment | Impacted Area | Resolution Action | Status |
| :--- | :--- | :--- | :--- | :--- |
| **IMP-01** | Risk of scope creep into payment and shipping workflows | Scope & Architecture | PO and Lead Architect limited the first release to collection management, price tracking, messaging, and offers (see Section 2). | Resolved |
| **IMP-02** | Direct pushes to `main`/`develop` could break the shared branches | GitHub & DevOps | DevOps added a ruleset that requires a pull request, one approval, and a passing `validate-openapi` check. | Resolved |
| **IMP-03** | Squash-only merging caused false conflicts when syncing `main` and `develop` | GitHub & DevOps | Merge commits were enabled; the merge method rule was added to the code review guidelines. | Resolved |
| **IMP-04** | Two team members had not joined the GitHub organization yet | Team & Traceability | All six members joined the organization with write access, so everyone can be assigned issues and reviews. | Resolved |
| **IMP-05** | A false README conflict blocked the `develop` → `main` release pull request | GitHub & DevOps | The Lead Architect merged `main` into `develop` with a merge commit (#38), which removed the conflict without changing any file. | Resolved |

#### D. Sprint 1 Retrospective Summary
**Date:** 2026-11-04 · **Attendees:** all six members (Elif, Feyza, Berke, Kemal, Çağrı, Ata)

**What went well**
- After the ruleset was set up (from #9 on), every change went through a reviewed pull request. Reviews found real problems, such as stories that did not match the API and contradictions in the system boundary (#40).
- The collector survey (27 responses) and the competitor review gave the proposal real evidence and showed that collectors with larger collections are the primary users.
- The QA review (#31) made every acceptance criterion testable and linked it to the status codes in `api/openapi.yaml`.
- Every deliverable had one accountable owner in the RACI matrix, so everyone knew who decides.

**What did not go well**
- The first pull requests (#2, #9, #10) had no linked issue and used default branch names, because the rules were written after them.
- Squash merges between `main` and `develop` caused false conflicts twice (IMP-03 and IMP-05).
- Two members joined the GitHub organization late (IMP-04), so their first contributions started late.
- Most reviews and fixes happened in the last week of the sprint.
- The first user stories did not match the README scope and the API, and some acceptance criteria could not be tested.
- Long texts pasted into GitHub were cut off (the release notes had to be fixed after publishing).

**Action items for Sprint 2**

| Action | Owner |
| :--- | :--- |
| Every task starts with an issue and a branch named after it; checked in each stand-up | Feyza |
| `develop` → `main` and `main` → `develop` always use **Create a merge commit** | Çağrı |
| New user stories go to QA review as soon as they are written | Elif, Kemal |
| Reviews are done within two working days, as the code review guidelines say | All members |
| Sprint 2 work is planned so that it starts in the first week | Feyza |
| The price source spike (assumption AS-1) is done at the start of Sprint 2 | Berke |
| Every member opens at least one pull request in Sprint 2 | All members |
| Pasted text is checked in the preview before it is published | All members |

**Sprint 1 rating (team vote):** 5 / 5

**Next meeting:** 2026-11-13, 18:00
