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
## 4. Team Roles, RACI Matrix, and Agile Process Management

### 4.1 Team Member Roles and Responsibilities

| Team Member | Role Title | Domain | Primary Responsibilities & Sprint 1 Outputs |
| :--- | :--- | :--- | :--- |
| **Elif Zahide Arat** | Product Owner and Requirements Engineer[cite: 7] | Product | Defines the project proposal (problem statement, target users, expected outcomes, feasibility, risks) and selects the open-source license. Creates and prioritizes initial user stories with effort estimates in the Product Backlog[cite: 2, 3, 5]. |
| **Feyza Sayar** | Scrum Master and Agile Process Coach[cite: 6, 7] | Process | Prepares the Team Roles documentation and Sprint 1 RACI responsibility matrix[cite: 3, 5, 6]. Administers the GitHub Projects / Jira board, maintains stand-up and retrospective records, tracks impediments, and ensures timely delivery[cite: 5]. |
| **Berke Akman** | Lead Software Architect and Technical Lead[cite: 7] | Architecture | Defines system vision and scope boundaries (in-scope: digital inventory, valuation stats, discovery, DM trading; out-of-scope: payment processing, cart, shipping). Draws the Mermaid system context diagram, designs the `openapi.yaml` contract, and leads technical Peer Reviews[cite: 2, 3, 5]. |
| **Kemal Yusuf Ateşer** | Quality Assurance and Test Automation Engineer[cite: 7] | Quality | Defines testable Acceptance Criteria for all backlog user stories[cite: 3, 5]. Validates the OpenAPI contract for error scenarios (`400`, `401`, `409`), plans test strategies, and reviews Pull Requests for quality compliance. |
| **Çağrı Baynal** | DevOps and CI/CD Infrastructure Engineer[cite: 7] | DevOps | Sets up and organizes the GitHub repository[cite: 3, 5]. Configures branch protection rules on `main` and `develop`, and documents the Lightweight Git-Flow workflow and Pull Request merge policies. |
| **Ata Eren Atlı** | Implementation and Integration Engineer[cite: 7] | Implementation | Executes issue-based feature branching in accordance with Git-Flow rules, coordinates Frontend and Backend alignment with the OpenAPI contract, and conducts technical Peer Reviews on Pull Requests[cite: 3, 5]. |

---

### 4.2 Sprint 1 RACI Responsibility Matrix

* **R (Responsible):** The team member(s) who directly execute and complete the task[cite: 3, 6].
* **A (Accountable):** The single team member with final ownership and approval authority for the deliverable[cite: 3, 6].
* **C (Consulted):** Team members who provide domain, architectural, or quality input prior to completion[cite: 3, 6].
* **I (Informed):** Team members kept updated on task progress and final outcomes[cite: 3, 6].

| Sprint 1 Deliverable / Task | Elif Zahide Arat (PO)[cite: 7] | Feyza Sayar (SM)[cite: 6, 7] | Berke Akman (Arch)[cite: 7] | Kemal Yusuf Ateşer (QA)[cite: 7] | Çağrı Baynal (DevOps)[cite: 7] | Ata Eren Atlı (Impl)[cite: 7] |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1.1 Project Proposal, Problem Statement & Stakeholders**[cite: 2] | **A / R** | I | C | I | I | I |
| **1.2 Feasibility, Risks Table & Open-Source License Selection**[cite: 2] | **A / R** | I | C | I | C | I |
| **2.1 System Vision & Scope Boundaries (In-Scope / Out-of-Scope)**[cite: 2] | **A** | I | **R** | C | I | C |
| **2.2 System Context & Mermaid Flow Diagram**[cite: 2] | C | I | **A / R** | I | I | C |
| **3.1 OpenAPI Draft (`openapi.yaml` Endpoints & Schemas)**[cite: 2, 3] | C | I | **A / R** | C | I | C |
| **3.2 OpenAPI Error Scenarios (`400`, `401`, `409`) & Validation**[cite: 3] | I | I | **A** | **R** | I | C |
| **4.1 Team Roles & RACI Matrix Documentation**[cite: 3, 6] | C | **A / R** | I | I | I | I |
| **4.2 GitHub Projects / Jira Board Administration & Tracking**[cite: 5, 6] | C | **A / R** | I | I | I | I |
| **4.3 Stand-up, Retrospective & Impediment Tracking Records**[cite: 5] | C | **A / R** | C | C | C | C |
| **5.1 GitHub Repository Setup & Branch Protection Rules**[cite: 3] | I | C | C | I | **A / R** | I |
| **5.2 Lightweight Git-Flow Policy Documentation**[cite: 3] | I | C | C | I | **A / R** | C |
| **5.3 Pull Request Peer Reviews & Contract Verification**[cite: 3, 5] | I | I | **A / R** | **R** | I | **R** |
| **6.1 Initial Product Backlog (Epics, User Stories & Estimates)**[cite: 3, 5] | **A / R** | C | C | C | I | C |
| **6.2 User Story Acceptance Criteria Definition**[cite: 3, 5] | **A** | I | C | **R** | I | C |

---

### 4.3 Agile Process Management, Stand-up, and Retrospective Records

#### A. Board Administration (GitHub Projects / Jira)
Our agile board is structured into five columns to ensure full traceability from requirement to delivery[cite: 5, 6]:
1. **Backlog:** Prioritized user stories and epics created by the Product Owner[cite: 3, 5, 6].
2. **To Do (Sprint 1):** Tasks committed for Sprint 1 with assigned owners, labels, and effort estimates[cite: 3, 5, 6].
3. **In Progress:** Active tasks currently being developed or documented on dedicated branches[cite: 3, 5, 6].
4. **In Review:** Tasks with open Pull Requests awaiting peer review from the Lead Architect, QA, or Implementation Engineer[cite: 3, 5, 6].
5. **Done:** Verified tasks merged into `develop` / `main` after passing peer review[cite: 3, 5, 6].

#### B. Sprint 1 Stand-up Meeting Logs[cite: 5]

| Session | Attendees | Summary & Key Decisions |
| :--- | :--- | :--- |
| **Stand-up #1 (Kick-off)** | All Team Members (6/6) | Finalized project topic ("Digital Inventory & Social Trading Platform for Diecast Collectors"). Agreed to exclude financial transactions and shipping from system scope. Assigned Sprint 1 roles and initialized the GitHub repository[cite: 3, 5]. |
| **Stand-up #2 (Mid-Sprint Sync)** | All Team Members (6/6) | Çağrı configured branch protection rules. Elif drafted the project proposal and initial user stories. Berke started the `openapi.yaml` contract and Mermaid context diagram. Feyza completed the RACI matrix and updated the project board[cite: 2, 3, 5, 6]. |
| **Stand-up #3 (Pre-Release Review)** | All Team Members (6/6) | Kemal Yusuf finalized acceptance criteria and API error code checks (`400`, `401`, `409`). Berke, Kemal Yusuf, and Ata Eren completed PR peer reviews. Verified that all team members have traceable issues, commits, and PRs[cite: 1, 3, 4, 5]. |

#### C. Impediment Tracking Log[cite: 5]

| ID | Identified Impediment | Impacted Area | Resolution Action | Status |
| :--- | :--- | :--- | :--- | :--- |
| **IMP-01** | Risk of scope creep into complex e-commerce payment/shipping workflows | Scope & Architecture | Coordinated between PO and Lead Architect to strictly limit scope to digital inventory, valuation tracking, and DM communication. | Resolved |
| **IMP-02** | Risk of direct pushes to `main`/`develop` breaking repository integrity | GitHub & DevOps | DevOps configured branch protection rules requiring Pull Requests and at least one peer review approval before merging. | Resolved |
| **IMP-03** | Potential mismatch between backlog user stories and initial API endpoints | OpenAPI & Backlog | Established a joint review checkpoint among the Lead Architect, QA, and Implementation Engineer prior to PR approval. | Resolved |

#### D. Sprint 1 Retrospective Summary[cite: 5]
* **What Went Well:** Clear role definitions and the RACI matrix prevented task overlap; scope boundaries were established early.
* **What Could Be Improved:** Pull Requests should be opened earlier in the sprint cycle to allow more time for asynchronous peer reviews.
* **Action Items for Sprint 2:** Break down Sprint 2 deliverables (Detailed SRS, Figma UI/UX prototypes, and C4/UML diagrams) into granular GitHub Issues on Day 1 of Sprint 2[cite: 4, 5].

