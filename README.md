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
Diecast model car collectors (for example Hot Wheels and MiniGT, in scales such as 1:64 and 1:18) currently track their extensive collections using manual tools like Excel spreadsheets or physical notebooks. These tools are difficult to keep synchronized, cannot show the current market value of a collection, and cannot show how much profit or loss the collector has made since purchase. Furthermore, there is no dedicated, niche social platform where diecast collectors can easily discover missing pieces and make structured trade offers to each other.

### Intended Outcome
A specialized digital portfolio platform that allows diecast collectors to manage their collections with brand, scale, series, and purchase details. The system automatically finds the current new-in-box market price of each model and shows the collector's total collection value and profit or loss over time. The platform also serves as a social network, enabling collectors to view public collections, chat through direct messages (DM), and send formal trade, cash, or mixed offers.

### Stakeholders
- **Primary Users:** Diecast collectors who need digital inventory tracking, automatic valuation, and a predictable way to negotiate trades.
- **Secondary Users:** Visitors who browse public collections before registering.
- **External Dependencies:** A market price data source (for example eBay listings) that provides current new-in-box prices, and a currency exchange rate source that converts USD prices to TRY.

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

#### B. Sprint 1 Stand-up Meeting Logs
Each entry is added after the meeting takes place.

| Date | Attendees | Summary & Key Decisions |
| :--- | :--- | :--- |
| _YYYY-MM-DD_ | _names of people who attended_ | _what was done, what is next, blockers_ |

#### C. Impediment Tracking Log

| ID | Impediment | Impacted Area | Resolution Action | Status |
| :--- | :--- | :--- | :--- | :--- |
| **IMP-01** | Risk of scope creep into payment and shipping workflows | Scope & Architecture | PO and Lead Architect limited the first release to collection management, price tracking, messaging, and offers (see Section 2). | Resolved |
| **IMP-02** | Direct pushes to `main`/`develop` could break the shared branches | GitHub & DevOps | DevOps added a ruleset that requires a pull request, one approval, and a passing `validate-openapi` check. | Resolved |
| **IMP-03** | Squash-only merging caused false conflicts when syncing `main` and `develop` | GitHub & DevOps | Merge commits were enabled; the merge method rule was added to the code review guidelines. | Resolved |
| **IMP-04** | Two team members had not joined the GitHub organization yet | Team & Traceability | All six members joined the organization with write access, so everyone can be assigned issues and reviews. | Resolved |

#### D. Sprint 1 Retrospective Summary
To be completed after the Sprint 1 retrospective meeting (before the 5 November 2026 deadline).
