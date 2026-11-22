# Individual Contributions

This file lists what each team member did in each sprint and links to the GitHub records that show it. Every member worked from their own GitHub account, so the work can also be checked directly:

- Commits by author: `https://github.com/SENG321-TEAM-1/CollecTree/commits/develop?author=<github-username>`
- Pull requests by author: `https://github.com/SENG321-TEAM-1/CollecTree/pulls?q=is:pr+author:<github-username>`
- Issues by assignee: `https://github.com/SENG321-TEAM-1/CollecTree/issues?q=is:issue+assignee:<github-username>`

Changes reach `develop` through squash-merged pull requests, so each merged pull request is one commit on `develop` with the pull request author as the commit author.

## Sprint 2: Requirements and Architecture

Sprint 2 ran from 14 November to 24 November 2026. The counts below cover the work from the start of Sprint 2 to the `v0.2.0-sprint2` release. All Sprint 2 issues and pull requests are in the [Sprint 2 milestone](https://github.com/SENG321-TEAM-1/CollecTree/milestone/1?closed=1).

### Summary

| Name | GitHub | Role | Issues opened | Commits on `develop` / `main` | Pull requests merged | Pull request approvals given |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| Elif Zahide Arat | [@elifarat](https://github.com/elifarat) | Product Owner and Requirements Engineer | 3 | 2 | 2 | 8 |
| Feyza Sayar | [@feyzasayar001](https://github.com/feyzasayar001) | Scrum Master and Agile Process Coach | 1 | @@FEYZA_N@@ | @@FEYZA_N@@ | 3 |
| Berke Akman | [@berkeakman0](https://github.com/berkeakman0) | Lead Software Architect and Technical Lead | 11 | 10 | 10 | 8 |
| Kemal Yusuf Ateşer | [@kemalyusufateser](https://github.com/kemalyusufateser) | Quality Assurance and Test Automation Engineer | 2 | 2 | 2 | 3 |
| Çağrı Baynal | [@CagriBaynal](https://github.com/CagriBaynal) | DevOps and CI/CD Infrastructure Engineer | 2 | @@CAGRI_C@@ | @@CAGRI_P@@ | 4 |
| Ata Eren Atlı | [@atalirr](https://github.com/atalirr) | Implementation and Integration Engineer | 2 | 2 | 2 | 3 |

Berke's issue count includes #129, which he opened for Feyza's stand-up update. Çağrı's commit count includes the release merge commit on `main`.

---

### Elif Zahide Arat

- **Responsibilities:** Software Requirements Specification, refined product backlog, and code owner reviews of the architecture and API (RACI row "SRS and refined backlog": Accountable).

**Work done**

- Wrote the Software Requirements Specification (`docs/requirements/srs.md`): purpose, scope, user classes, constraints, 22 functional requirements in 6 feature groups, each linked to its user story, API operation, and business rules, the external interfaces (Figma prototype, user flows, API, eBay and TCMB), and a traceability matrix from US-01 to US-10.
- Added US-10 (Edit Collection Item) to the backlog and updated the product backlog document with the Sprint 2 decisions (first release total: 48 story points).
- Reviewed and approved the architecture pull requests as code owner of `docs/architecture/`, `docs/adr/`, and `api/`: the domain model, the C4 model, the sequence diagrams, ADR-003, the deployment diagram, the architecture overview, the price source spike, and the ADR-003 alignment.

**Issues:** created and assigned [#107](https://github.com/SENG321-TEAM-1/CollecTree/issues/107) (US-10), [#108](https://github.com/SENG321-TEAM-1/CollecTree/issues/108), [#110](https://github.com/SENG321-TEAM-1/CollecTree/issues/110).

**Pull requests:** [#109](https://github.com/SENG321-TEAM-1/CollecTree/pull/109) Update the product backlog with the Sprint 2 decisions, [#111](https://github.com/SENG321-TEAM-1/CollecTree/pull/111) Add the SRS.

**Commits:** [`f10a13c`](https://github.com/SENG321-TEAM-1/CollecTree/commit/f10a13c90e3154d0d098116d43f786826776a39e), [`53999bc`](https://github.com/SENG321-TEAM-1/CollecTree/commit/53999bc96699e31efa48d7ea5bd1f8c25602276d).

**Reviews (approved):** [#93](https://github.com/SENG321-TEAM-1/CollecTree/pull/93), [#98](https://github.com/SENG321-TEAM-1/CollecTree/pull/98), [#100](https://github.com/SENG321-TEAM-1/CollecTree/pull/100), [#102](https://github.com/SENG321-TEAM-1/CollecTree/pull/102), [#104](https://github.com/SENG321-TEAM-1/CollecTree/pull/104), [#106](https://github.com/SENG321-TEAM-1/CollecTree/pull/106), [#117](https://github.com/SENG321-TEAM-1/CollecTree/pull/117), [#128](https://github.com/SENG321-TEAM-1/CollecTree/pull/128).

---

### Feyza Sayar

- **Responsibilities:** Sprint 2 milestone and board, process records (planning, stand-ups, impediments, review and retrospective, RACI), and the Sprint 2 submission document (RACI row "Process records and submission": Accountable).

**Work done**

- Created the Sprint 2 milestone and the "Sprint 2" board view, and renamed the board column to "To Do".
- Wrote the Sprint 2 process records (`docs/process/sprint-2.md`): the Sprint 1 retrospective actions, the Sprint 2 planning, the stand-up log, the impediment log, the review and retrospective, and the Sprint 2 RACI, and linked them from the README.
- Kept the daily stand-up log and the impediment log (IMP-01 to IMP-05).
- Prepared the Sprint 2 submission document.
- Reviewed and approved the backlog update, the SRS, and the non-functional requirements as code owner of the requirements documents.

**Issues:** created and assigned [#113](https://github.com/SENG321-TEAM-1/CollecTree/issues/113); assigned to [#129](https://github.com/SENG321-TEAM-1/CollecTree/issues/129)@@FEYZA_ISSUE@@.

**Pull requests:** [#118](https://github.com/SENG321-TEAM-1/CollecTree/pull/118) Add the Sprint 2 process records (replaces [#112](https://github.com/SENG321-TEAM-1/CollecTree/pull/112), closed after the branch rename), [#130](https://github.com/SENG321-TEAM-1/CollecTree/pull/130) Add the stand-ups and impediments of 14–19 November@@FEYZA_PR@@.

**Commits:** [`bb389dd`](https://github.com/SENG321-TEAM-1/CollecTree/commit/bb389dd6b6f889fbd2a00c2545af6c762268e933), [`544a7c0`](https://github.com/SENG321-TEAM-1/CollecTree/commit/544a7c0d3fde304eaa2014d8a4a6a5c23e7d8468)@@FEYZA_SHA@@.

**Reviews (approved):** [#109](https://github.com/SENG321-TEAM-1/CollecTree/pull/109), [#111](https://github.com/SENG321-TEAM-1/CollecTree/pull/111), [#124](https://github.com/SENG321-TEAM-1/CollecTree/pull/124).

---

### Berke Akman

- **Responsibilities:** C4 model and UML architecture document, domain model, architecture decisions, the price source spike, the API contract, and technical reviews (RACI rows "C4 and UML architecture document" and "Price source spike and ADR-003": Accountable).

**Work done**

- Wrote the domain model and the database schema (`docs/architecture/domain-model.md`): entities, ER diagram, and business rules BR-01 to BR-19, and answered the testability questions from the QA review.
- Wrote the C4 model (context, container, and component diagrams, and the module dependency rules) and four UML sequence diagrams (log in, add an item, daily price job, accept an offer).
- Wrote the UML deployment diagram and the operating guide, based on the deployment decisions agreed with Çağrı in #114, and added the health endpoint to the API contract.
- Wrote ADR-003 (market price and exchange rate source), set up the eBay Production keyset, and ran the price source spike with the eBay Browse API and the TCMB exchange rate; then accepted ADR-003 with the matching rule (at least 5 listings and p75/p25 ≤ 2.0) and aligned the architecture documents and the API with it (paging of `searchModels` and `listUserItems`).
- Wrote the architecture overview (`docs/architecture/README.md`): views, key decisions, quality tactics, and risks.
- Added `.gitignore` and `.env.example` before any API key was used.
- Re-tested all 40 seed catalogue keywords with the spike script during the review of #122.
- Wrote this Sprint 2 section of `CONTRIBUTIONS.md` from the GitHub records.

**Issues:** created and assigned [#92](https://github.com/SENG321-TEAM-1/CollecTree/issues/92), [#94](https://github.com/SENG321-TEAM-1/CollecTree/issues/94), [#96](https://github.com/SENG321-TEAM-1/CollecTree/issues/96), [#97](https://github.com/SENG321-TEAM-1/CollecTree/issues/97), [#99](https://github.com/SENG321-TEAM-1/CollecTree/issues/99), [#101](https://github.com/SENG321-TEAM-1/CollecTree/issues/101), [#103](https://github.com/SENG321-TEAM-1/CollecTree/issues/103), [#105](https://github.com/SENG321-TEAM-1/CollecTree/issues/105), [#127](https://github.com/SENG321-TEAM-1/CollecTree/issues/127), [#131](https://github.com/SENG321-TEAM-1/CollecTree/issues/131); created [#129](https://github.com/SENG321-TEAM-1/CollecTree/issues/129) for Feyza.

**Pull requests:** [#93](https://github.com/SENG321-TEAM-1/CollecTree/pull/93) Add the domain model and database schema, [#95](https://github.com/SENG321-TEAM-1/CollecTree/pull/95) Add .gitignore and .env.example, [#98](https://github.com/SENG321-TEAM-1/CollecTree/pull/98) Add the C4 model, [#100](https://github.com/SENG321-TEAM-1/CollecTree/pull/100) Add the UML sequence diagrams, [#102](https://github.com/SENG321-TEAM-1/CollecTree/pull/102) Add ADR-003 and align the system boundary with it, [#104](https://github.com/SENG321-TEAM-1/CollecTree/pull/104) Add the UML deployment diagram and operating guide, [#106](https://github.com/SENG321-TEAM-1/CollecTree/pull/106) Add the architecture overview document, [#117](https://github.com/SENG321-TEAM-1/CollecTree/pull/117) Add the price source spike results, [#128](https://github.com/SENG321-TEAM-1/CollecTree/pull/128) Accept ADR-003 and align the architecture documents and the API with it, @@BERKE_PR@@ Add the Sprint 2 contributions to CONTRIBUTIONS.md.

**Commits:** [`d20069b`](https://github.com/SENG321-TEAM-1/CollecTree/commit/d20069b34bca7a1c49bf227a98056f7a6a74373b), [`adac26e`](https://github.com/SENG321-TEAM-1/CollecTree/commit/adac26e5e9da924c796bdfcb65d0088fcc743f2e), [`8e6c9f1`](https://github.com/SENG321-TEAM-1/CollecTree/commit/8e6c9f1f92d86e74c9bbd7f55a0e82a19fabfb64), [`8d91bf9`](https://github.com/SENG321-TEAM-1/CollecTree/commit/8d91bf9f5a32b2fe438234ef8e37cfae5ee392aa), [`0e4bd8b`](https://github.com/SENG321-TEAM-1/CollecTree/commit/0e4bd8b27607d2b4db54703fdd73a71f95467354), [`5d175fc`](https://github.com/SENG321-TEAM-1/CollecTree/commit/5d175fc2df0266fcd606b42685b75086a694a8c5), [`661f284`](https://github.com/SENG321-TEAM-1/CollecTree/commit/661f2844e0de6aa9759f53c606faf67730aa1a5b), [`5f65843`](https://github.com/SENG321-TEAM-1/CollecTree/commit/5f658435d67aab990fbec0a357259897bb0e2b75), [`d66f688`](https://github.com/SENG321-TEAM-1/CollecTree/commit/d66f68882cbec1e65e97b3f873775f4a4ef5300f)@@BERKE_SHA@@.

**Reviews (approved):** [#111](https://github.com/SENG321-TEAM-1/CollecTree/pull/111), [#116](https://github.com/SENG321-TEAM-1/CollecTree/pull/116), [#118](https://github.com/SENG321-TEAM-1/CollecTree/pull/118), [#120](https://github.com/SENG321-TEAM-1/CollecTree/pull/120), [#122](https://github.com/SENG321-TEAM-1/CollecTree/pull/122) (after requesting changes first), [#124](https://github.com/SENG321-TEAM-1/CollecTree/pull/124), [#126](https://github.com/SENG321-TEAM-1/CollecTree/pull/126) (after requesting changes first), [#130](https://github.com/SENG321-TEAM-1/CollecTree/pull/130).

---

### Kemal Yusuf Ateşer

- **Responsibilities:** Non-functional requirements and quality measures, the test plan, and testability reviews (RACI row "Non-functional requirements": Accountable).

**Work done**

- Wrote the non-functional requirements and quality measures (`docs/requirements/non-functional-requirements.md`): 20 requirements grouped by the ISO/IEC 25010 quality characteristics, each with a measurable target and a verification method.
- Wrote the test plan for Sprint 3 (`docs/testing/test-plan.md`): test levels, test environment, entry and exit criteria, the CI quality gate, and one test case for every business rule (BR-01 to BR-19) and for the ADR-003 price rule.
- Reviewed the domain model for testability and asked four questions on the business rules, which were answered and added to the domain model (BR-12, BR-14, BR-19).
- Reviewed the architecture overview against the non-functional requirements, and reviewed the price source spike and the ADR-003 alignment.

**Issues:** created and assigned [#123](https://github.com/SENG321-TEAM-1/CollecTree/issues/123), [#125](https://github.com/SENG321-TEAM-1/CollecTree/issues/125).

**Pull requests:** [#124](https://github.com/SENG321-TEAM-1/CollecTree/pull/124) Add the non-functional requirements and quality measures, [#126](https://github.com/SENG321-TEAM-1/CollecTree/pull/126) Add the Sprint 2 test plan.

**Commits:** [`42a50ec`](https://github.com/SENG321-TEAM-1/CollecTree/commit/42a50ec5e4955938eb6dac8273f08555fd9f5ce7), [`8ee0cea`](https://github.com/SENG321-TEAM-1/CollecTree/commit/8ee0cea47f4d927a1780bc04869815cdbccd4818).

**Reviews:** [#93](https://github.com/SENG321-TEAM-1/CollecTree/pull/93) (testability questions); approved [#106](https://github.com/SENG321-TEAM-1/CollecTree/pull/106), [#117](https://github.com/SENG321-TEAM-1/CollecTree/pull/117), [#128](https://github.com/SENG321-TEAM-1/CollecTree/pull/128).

---

### Çağrı Baynal

- **Responsibilities:** Docker Compose deployment decisions, the CI checks, repository security, and the Sprint 2 release (RACI row "CI and repository security": Accountable).

**Work done**

- Agreed the Docker Compose deployment decisions in #114: images and versions, ports, volumes, health checks, the startup order, and the nginx reverse proxy for `/api`.
- Added the `render-mermaid` CI check (`.github/workflows/check-docs.yml`), which renders every Mermaid diagram on every pull request, and made it a required check next to `validate-openapi`.
- Checked that secret scanning and push protection are enabled before the eBay keys were used.
- Re-reviewed the non-functional requirements after the update and checked them against the deployment decisions and the CI checks.
- Opened and merged the release pull request from `develop` to `main` and published the [`v0.2.0-sprint2` release](https://github.com/SENG321-TEAM-1/CollecTree/releases/tag/v0.2.0-sprint2).
- Reviewed the `.gitignore`, the C4 model, the deployment diagram, and the non-functional requirements.

**Issues:** created and assigned [#114](https://github.com/SENG321-TEAM-1/CollecTree/issues/114), [#115](https://github.com/SENG321-TEAM-1/CollecTree/issues/115).

**Pull requests:** [#116](https://github.com/SENG321-TEAM-1/CollecTree/pull/116) Add a CI check that renders all Mermaid diagrams@@CAGRI_PR@@.

**Commits:** [`38f9f67`](https://github.com/SENG321-TEAM-1/CollecTree/commit/38f9f67a13095d2668455c507d9caed040f38849)@@CAGRI_SHA@@.

**Reviews (approved):** [#95](https://github.com/SENG321-TEAM-1/CollecTree/pull/95), [#98](https://github.com/SENG321-TEAM-1/CollecTree/pull/98), [#104](https://github.com/SENG321-TEAM-1/CollecTree/pull/104), [#124](https://github.com/SENG321-TEAM-1/CollecTree/pull/124) (approved again after the update).

---

### Ata Eren Atlı

- **Responsibilities:** Figma prototype, user flows, the seed catalogue, and implementation reviews of the architecture (RACI row "Figma prototypes and user flows": Accountable).

**Work done**

- Designed the Figma prototype: 12 desktop screens and a clickable main journey (log in, collection, add an item, portfolio, public profile, offers, conversations).
- Wrote the user flows (`docs/design/user-flows.md`): 7 Mermaid flow diagrams, the on-screen messages shared by the screens and the API tests, and a table that maps every screen to its API operations.
- Added the seed catalogue (`data/seed/catalog.csv`): 40 release-specific models from five brands with checked catalogue numbers, eBay search keywords, and manually collected prices.
- Reviewed the C4 model, the sequence diagrams, and the ADR-003 alignment against the planned implementation.

**Issues:** created and assigned [#119](https://github.com/SENG321-TEAM-1/CollecTree/issues/119), [#121](https://github.com/SENG321-TEAM-1/CollecTree/issues/121).

**Pull requests:** [#120](https://github.com/SENG321-TEAM-1/CollecTree/pull/120) Add user flow diagrams and prototype screens, [#122](https://github.com/SENG321-TEAM-1/CollecTree/pull/122) Add the initial seed catalogue.

**Commits:** [`7afdae3`](https://github.com/SENG321-TEAM-1/CollecTree/commit/7afdae323d708a591dfca55bb5daf901f2751305), [`2af504e`](https://github.com/SENG321-TEAM-1/CollecTree/commit/2af504e83417b4fd2049c5f70c7875b8d8a5b867).

**Reviews (approved):** [#98](https://github.com/SENG321-TEAM-1/CollecTree/pull/98), [#100](https://github.com/SENG321-TEAM-1/CollecTree/pull/100), [#128](https://github.com/SENG321-TEAM-1/CollecTree/pull/128).

---

## Sprint 1: Project Foundation

### Summary

| Name | Student number | GitHub | Role | Issues opened | Commits on `develop` / `main` | Pull requests merged | Pull request approvals given |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| Elif Zahide Arat | 230201017 | [@elifarat](https://github.com/elifarat) | Product Owner and Requirements Engineer | 23 | 3 | 3 | 4 |
| Feyza Sayar | 230201044 | [@feyzasayar001](https://github.com/feyzasayar001) | Scrum Master and Agile Process Coach | 8 | 3 | 3 | 4 |
| Berke Akman | 230204038 | [@berkeakman0](https://github.com/berkeakman0) | Lead Software Architect and Technical Lead | 12 | 10 | 9 | 9 |
| Kemal Yusuf Ateşer | 220205056 | [@kemalyusufateser](https://github.com/kemalyusufateser) | Quality Assurance and Test Automation Engineer | 12 | 1 | 1 | 1 |
| Çağrı Baynal | 260201303 | [@CagriBaynal](https://github.com/CagriBaynal) | DevOps and CI/CD Infrastructure Engineer | 5 | 6 | 4 | 5 |
| Ata Eren Atlı | 220205046 | [@atalirr](https://github.com/atalirr) | Implementation and Integration Engineer | 5 | 1 | 1 | 2 |

The counts cover the work up to the final Sprint 1 release. Issues closed as duplicates are not counted. The backlog hierarchy (epics, features, user stories, and tasks) is described in [`docs/requirements/product-backlog.md`](docs/requirements/product-backlog.md). Çağrı's count includes the two release merge commits on `main`, and Berke's count includes the merge commit of the history sync in #38 and the commit of this update (#90).

---

### Elif Zahide Arat

- **Student number:** 230201017
- **GitHub:** [@elifarat](https://github.com/elifarat)
- **Role:** Product Owner and Requirements Engineer
- **Responsibilities:** Project proposal, system vision and first release scope, open-source license decision, and the initial Product Backlog (RACI rows 1.1, 1.2, 2.1, 6.1, 6.2: Accountable).

**Work done**

- Wrote the project proposal in `README.md`: problem definition, stakeholders, system vision, first release scope, exclusions, assumptions and risks, and the license decision.
- Added the supporting evidence (competitor analysis and a collector survey with 27 responses), the stakeholder analysis, and the feasibility assessment.
- Created the Product Backlog: 4 epics and 9 user stories with priorities, acceptance criteria, estimates, and dependencies, and linked each story to its epic as a sub-issue.
- Added the feature level to the backlog: created the 6 features and updated the epic descriptions.
- Wrote the product backlog document with the Definition of Ready and the Definition of Done.
- Created the tasks of US-03.
- Reviewed the OpenAPI contract, the architecture documents, the ADR acceptance, and the system boundary fixes.

**Issues:** created [#4](https://github.com/SENG321-TEAM-1/CollecTree/issues/4), [#5](https://github.com/SENG321-TEAM-1/CollecTree/issues/5), [#6](https://github.com/SENG321-TEAM-1/CollecTree/issues/6), [#7](https://github.com/SENG321-TEAM-1/CollecTree/issues/7), [#8](https://github.com/SENG321-TEAM-1/CollecTree/issues/8), [#21](https://github.com/SENG321-TEAM-1/CollecTree/issues/21) to [#28](https://github.com/SENG321-TEAM-1/CollecTree/issues/28) (user stories and epics), [#29](https://github.com/SENG321-TEAM-1/CollecTree/issues/29) (supporting evidence), [#87](https://github.com/SENG321-TEAM-1/CollecTree/issues/87) (backlog document); created and assigned the features [#56](https://github.com/SENG321-TEAM-1/CollecTree/issues/56), [#58](https://github.com/SENG321-TEAM-1/CollecTree/issues/58), [#61](https://github.com/SENG321-TEAM-1/CollecTree/issues/61), [#66](https://github.com/SENG321-TEAM-1/CollecTree/issues/66), [#65](https://github.com/SENG321-TEAM-1/CollecTree/issues/65), [#69](https://github.com/SENG321-TEAM-1/CollecTree/issues/69) and the tasks [#70](https://github.com/SENG321-TEAM-1/CollecTree/issues/70), [#71](https://github.com/SENG321-TEAM-1/CollecTree/issues/71); assigned to the epics [#25](https://github.com/SENG321-TEAM-1/CollecTree/issues/25)–[#28](https://github.com/SENG321-TEAM-1/CollecTree/issues/28), [#6](https://github.com/SENG321-TEAM-1/CollecTree/issues/6), and [#29](https://github.com/SENG321-TEAM-1/CollecTree/issues/29).

**Pull requests:** [#10](https://github.com/SENG321-TEAM-1/CollecTree/pull/10) Enhance README with project details and license, [#30](https://github.com/SENG321-TEAM-1/CollecTree/pull/30) Add supporting evidence, stakeholder analysis, and feasibility to the proposal, [#88](https://github.com/SENG321-TEAM-1/CollecTree/pull/88) Add the product backlog document with the Definition of Ready.

**Commits:** [`e949ad4`](https://github.com/SENG321-TEAM-1/CollecTree/commit/e949ad4761b68717ef6e5223c846367672863857), [`e69cf14`](https://github.com/SENG321-TEAM-1/CollecTree/commit/e69cf14880d300bb25223250d129d23309ff33b0), [`bb38c23`](https://github.com/SENG321-TEAM-1/CollecTree/commit/bb38c231e33827ce6570ed5434e495366c4c5765).

**Reviews (approved):** [#14](https://github.com/SENG321-TEAM-1/CollecTree/pull/14), [#20](https://github.com/SENG321-TEAM-1/CollecTree/pull/20), [#35](https://github.com/SENG321-TEAM-1/CollecTree/pull/35), [#41](https://github.com/SENG321-TEAM-1/CollecTree/pull/41).

---

### Feyza Sayar

- **Student number:** 230201044
- **GitHub:** [@feyzasayar001](https://github.com/feyzasayar001)
- **Role:** Scrum Master and Agile Process Coach
- **Responsibilities:** Team roles and RACI matrix, GitHub Projects board, stand-up, impediment, and retrospective records, and the Sprint 1 submission (RACI rows 4.1, 4.2, 4.3: Accountable).

**Work done**

- Wrote the team roles and responsibilities table and the Sprint 1 RACI matrix in `README.md`.
- Set up and administered the [CollecTree Sprint Board](https://github.com/orgs/SENG321-TEAM-1/projects/1) and added its link to the README.
- Kept the stand-up logs, the impediment log, and the Sprint 1 retrospective summary.
- Created the process issues for the Sprint 1 review, release, and submission.
- Created the tasks of US-07.
- Reviewed `CONTRIBUTIONS.md` and the product backlog document as code owner of the requirements documents.

**Issues:** created and assigned [#18](https://github.com/SENG321-TEAM-1/CollecTree/issues/18), [#33](https://github.com/SENG321-TEAM-1/CollecTree/issues/33), [#36](https://github.com/SENG321-TEAM-1/CollecTree/issues/36), [#42](https://github.com/SENG321-TEAM-1/CollecTree/issues/42); created [#31](https://github.com/SENG321-TEAM-1/CollecTree/issues/31) and [#32](https://github.com/SENG321-TEAM-1/CollecTree/issues/32); created and assigned the tasks [#60](https://github.com/SENG321-TEAM-1/CollecTree/issues/60), [#67](https://github.com/SENG321-TEAM-1/CollecTree/issues/67); assigned to [#22](https://github.com/SENG321-TEAM-1/CollecTree/issues/22) (US-07).

**Pull requests:** [#15](https://github.com/SENG321-TEAM-1/CollecTree/pull/15) Document team roles and Sprint 1 RACI matrix, [#37](https://github.com/SENG321-TEAM-1/CollecTree/pull/37) Add the project board link to the README, [#43](https://github.com/SENG321-TEAM-1/CollecTree/pull/43) Add the final Sprint 1 stand-up and the retrospective summary.

**Commits:** [`a816e8a`](https://github.com/SENG321-TEAM-1/CollecTree/commit/a816e8a1dd33198d28963005e24bfe3d3ce5d0f7), [`eb42a9a`](https://github.com/SENG321-TEAM-1/CollecTree/commit/eb42a9ac90337a56a6d94bc8a5ec06f0fe1ed7f7), [`8289156`](https://github.com/SENG321-TEAM-1/CollecTree/commit/82891560c54f5d2e8607662c29252dcfb1bed08b).

**Reviews (approved):** [#30](https://github.com/SENG321-TEAM-1/CollecTree/pull/30), [#35](https://github.com/SENG321-TEAM-1/CollecTree/pull/35), [#51](https://github.com/SENG321-TEAM-1/CollecTree/pull/51), [#88](https://github.com/SENG321-TEAM-1/CollecTree/pull/88).

---

### Berke Akman

- **Student number:** 230204038
- **GitHub:** [@berkeakman0](https://github.com/berkeakman0)
- **Role:** Lead Software Architect and Technical Lead
- **Responsibilities:** System boundary and context diagram, architecture decision records, the OpenAPI contract, and technical peer reviews (RACI rows 2.2, 2.3, 3.1, 3.2, 5.3: Accountable).

**Work done**

- Wrote the system boundary specification with the Mermaid context diagram, assumptions, constraints, and risks (`docs/architecture/system-boundary.md`).
- Wrote ADR-001 (modular monolith, FastAPI, PostgreSQL, React + Vite) and ADR-002 (MIT license), and recorded their acceptance in the team review.
- Designed the draft OpenAPI 3 contract (`api/openapi.yaml`) and added the `validate-openapi` CI check.
- Added `CODEOWNERS`, the pull request template, and the code review guidelines.
- Fixed the contradictions between the system boundary, README, and OpenAPI, and synced `main` into `develop` before the release.
- Wrote this `CONTRIBUTIONS.md` file from the GitHub records.
- Created the tasks of US-01 and US-08, and linked all features, user stories, and tasks into the backlog hierarchy.
- Reviewed most of the team's pull requests as the technical lead.

**Issues:** created and assigned [#11](https://github.com/SENG321-TEAM-1/CollecTree/issues/11), [#13](https://github.com/SENG321-TEAM-1/CollecTree/issues/13), [#16](https://github.com/SENG321-TEAM-1/CollecTree/issues/16), [#19](https://github.com/SENG321-TEAM-1/CollecTree/issues/19), [#34](https://github.com/SENG321-TEAM-1/CollecTree/issues/34), [#40](https://github.com/SENG321-TEAM-1/CollecTree/issues/40), [#50](https://github.com/SENG321-TEAM-1/CollecTree/issues/50), [#89](https://github.com/SENG321-TEAM-1/CollecTree/issues/89); created and assigned the tasks [#52](https://github.com/SENG321-TEAM-1/CollecTree/issues/52), [#53](https://github.com/SENG321-TEAM-1/CollecTree/issues/53), [#54](https://github.com/SENG321-TEAM-1/CollecTree/issues/54), [#55](https://github.com/SENG321-TEAM-1/CollecTree/issues/55); assigned to [#4](https://github.com/SENG321-TEAM-1/CollecTree/issues/4) (US-01), [#23](https://github.com/SENG321-TEAM-1/CollecTree/issues/23) (US-08), and [#32](https://github.com/SENG321-TEAM-1/CollecTree/issues/32) (release, with Çağrı).

**Pull requests:** [#12](https://github.com/SENG321-TEAM-1/CollecTree/pull/12) Add CODEOWNERS, PR template, and OpenAPI validation check, [#14](https://github.com/SENG321-TEAM-1/CollecTree/pull/14) Add draft OpenAPI contract for the first release, [#17](https://github.com/SENG321-TEAM-1/CollecTree/pull/17) Add QA and implementation owners to CODEOWNERS, [#20](https://github.com/SENG321-TEAM-1/CollecTree/pull/20) Add architecture documents, [#35](https://github.com/SENG321-TEAM-1/CollecTree/pull/35) Accept ADR-001 and ADR-002, [#38](https://github.com/SENG321-TEAM-1/CollecTree/pull/38) Sync main into develop, [#41](https://github.com/SENG321-TEAM-1/CollecTree/pull/41) Fix purchase price and personal data contradictions, [#51](https://github.com/SENG321-TEAM-1/CollecTree/pull/51) Add CONTRIBUTIONS.md, [#90](https://github.com/SENG321-TEAM-1/CollecTree/pull/90) Update CONTRIBUTIONS.md.

**Commits:** [`92a5eb3`](https://github.com/SENG321-TEAM-1/CollecTree/commit/92a5eb323d4589e2fbbb41dd587de4f043fea1d7), [`c364165`](https://github.com/SENG321-TEAM-1/CollecTree/commit/c3641659a184c1bf09e22b541e9f171a2cb80733), [`d5a7447`](https://github.com/SENG321-TEAM-1/CollecTree/commit/d5a7447777b8530ad7f75e5a4552e1ba94a97e88), [`a626733`](https://github.com/SENG321-TEAM-1/CollecTree/commit/a626733b4e87d10f1b77518a66e049003df172f4), [`db3d76c`](https://github.com/SENG321-TEAM-1/CollecTree/commit/db3d76cbff0619458f53f3ac7bd0592f6fb20b55), [`3bed87f`](https://github.com/SENG321-TEAM-1/CollecTree/commit/3bed87f52396b5431137c58fa727bd94d13924c4), [`b5063d8`](https://github.com/SENG321-TEAM-1/CollecTree/commit/b5063d81279bdee2119455227cf333ade16f049a), [`5bb0886`](https://github.com/SENG321-TEAM-1/CollecTree/commit/5bb0886cad08acf9798077f3572ba1bd9a4e0c72), [`f9d6b8a`](https://github.com/SENG321-TEAM-1/CollecTree/commit/f9d6b8a7871aa87f9c47d4f3e4336c83bdaba8df).

**Reviews (approved):** [#9](https://github.com/SENG321-TEAM-1/CollecTree/pull/9), [#15](https://github.com/SENG321-TEAM-1/CollecTree/pull/15) (after requesting changes first), [#30](https://github.com/SENG321-TEAM-1/CollecTree/pull/30), [#37](https://github.com/SENG321-TEAM-1/CollecTree/pull/37), [#39](https://github.com/SENG321-TEAM-1/CollecTree/pull/39), [#43](https://github.com/SENG321-TEAM-1/CollecTree/pull/43), [#45](https://github.com/SENG321-TEAM-1/CollecTree/pull/45), [#48](https://github.com/SENG321-TEAM-1/CollecTree/pull/48), [#49](https://github.com/SENG321-TEAM-1/CollecTree/pull/49).

---

### Kemal Yusuf Ateşer

- **Student number:** 220205056
- **GitHub:** [@kemalyusufateser](https://github.com/kemalyusufateser)
- **Role:** Quality Assurance and Test Automation Engineer
- **Responsibilities:** Testable acceptance criteria, OpenAPI error scenarios, and quality reviews of pull requests (RACI rows 3.2, 5.3, 6.2: Responsible).

**Work done**

- Reviewed the acceptance criteria of all 9 user stories against the OpenAPI contract and its error responses, and gave the QA sign-off after the Product Owner's update ([first review](https://github.com/SENG321-TEAM-1/CollecTree/issues/31#issuecomment-6618784788), [sign-off](https://github.com/SENG321-TEAM-1/CollecTree/issues/31#issuecomment-6626510610)).
- Created one API test task for each of the 9 user stories, so that every acceptance criterion gets an automated test.
- Created the tasks of US-05.
- Added the release tag rule and the chore branch type to the code review guidelines.
- Reviewed the architecture documents pull request.

**Issues:** assigned and closed [#31](https://github.com/SENG321-TEAM-1/CollecTree/issues/31) (acceptance criteria review); created and assigned [#46](https://github.com/SENG321-TEAM-1/CollecTree/issues/46); created and assigned the test tasks [#77](https://github.com/SENG321-TEAM-1/CollecTree/issues/77), [#79](https://github.com/SENG321-TEAM-1/CollecTree/issues/79), [#80](https://github.com/SENG321-TEAM-1/CollecTree/issues/80), [#81](https://github.com/SENG321-TEAM-1/CollecTree/issues/81), [#82](https://github.com/SENG321-TEAM-1/CollecTree/issues/82), [#83](https://github.com/SENG321-TEAM-1/CollecTree/issues/83), [#84](https://github.com/SENG321-TEAM-1/CollecTree/issues/84), [#85](https://github.com/SENG321-TEAM-1/CollecTree/issues/85), [#86](https://github.com/SENG321-TEAM-1/CollecTree/issues/86) and the tasks [#72](https://github.com/SENG321-TEAM-1/CollecTree/issues/72), [#73](https://github.com/SENG321-TEAM-1/CollecTree/issues/73); assigned to [#8](https://github.com/SENG321-TEAM-1/CollecTree/issues/8) (US-05).

**Pull requests:** [#48](https://github.com/SENG321-TEAM-1/CollecTree/pull/48) Add the release tag rule and the chore branch type to the code review guidelines.

**Commits:** [`5d4c8b5`](https://github.com/SENG321-TEAM-1/CollecTree/commit/5d4c8b516a7c1d41a1bd6123748181cb48d96472).

**Reviews (approved):** [#20](https://github.com/SENG321-TEAM-1/CollecTree/pull/20).

---

### Çağrı Baynal

- **Student number:** 260201303
- **GitHub:** [@CagriBaynal](https://github.com/CagriBaynal)
- **Role:** DevOps and CI/CD Infrastructure Engineer
- **Responsibilities:** GitHub organization and repository, branch protection, Git-Flow policy, and the Sprint 1 release (RACI rows 5.1, 5.2: Accountable).

**Work done**

- Created the GitHub organization and the repository, and set up the `main` and `develop` branches.
- Configured the branch protection ruleset on `main` and `develop` (pull request with 1 approval, code owner review, required `validate-openapi` check, no force push or deletion).
- Wrote the Git-Flow and branching rules in `README.md`.
- Opened and merged the release pull requests from `develop` to `main`, and published the [`v0.1.0-sprint1` release](https://github.com/SENG321-TEAM-1/CollecTree/releases/tag/v0.1.0-sprint1).
- Filled in the repository description and topics.
- Gave the course assistants and the instructor read access to the repository.
- Created the tasks of US-06 and US-04.

**Issues:** created, assigned, and closed [#1](https://github.com/SENG321-TEAM-1/CollecTree/issues/1) (repository and Git-Flow setup); assigned and closed [#32](https://github.com/SENG321-TEAM-1/CollecTree/issues/32) (release); created and assigned the tasks [#57](https://github.com/SENG321-TEAM-1/CollecTree/issues/57), [#59](https://github.com/SENG321-TEAM-1/CollecTree/issues/59), [#62](https://github.com/SENG321-TEAM-1/CollecTree/issues/62), [#63](https://github.com/SENG321-TEAM-1/CollecTree/issues/63); assigned to [#7](https://github.com/SENG321-TEAM-1/CollecTree/issues/7) (US-04) and [#21](https://github.com/SENG321-TEAM-1/CollecTree/issues/21) (US-06).

**Pull requests:** [#2](https://github.com/SENG321-TEAM-1/CollecTree/pull/2) Add Git-Flow rules and team roles, [#9](https://github.com/SENG321-TEAM-1/CollecTree/pull/9) Sync develop with main, [#39](https://github.com/SENG321-TEAM-1/CollecTree/pull/39) Sprint 1 release, [#49](https://github.com/SENG321-TEAM-1/CollecTree/pull/49) Sprint 1 release update.

**Commits:** [`97de2c6`](https://github.com/SENG321-TEAM-1/CollecTree/commit/97de2c60270c68479c119fc908536ee4eff098e6) (initial commit), [`0cf8545`](https://github.com/SENG321-TEAM-1/CollecTree/commit/0cf8545535657cc5bbccdb823287320d28441fe2), [`f90dbd2`](https://github.com/SENG321-TEAM-1/CollecTree/commit/f90dbd2768d8a6775ede9b1fffb57269d4c605eb), [`ca17ec6`](https://github.com/SENG321-TEAM-1/CollecTree/commit/ca17ec6b85aa97aacf871b871f866bc94937f6f9), [`3b7bc6a`](https://github.com/SENG321-TEAM-1/CollecTree/commit/3b7bc6a3fab45e939b68452e2ee1d88b073680de) and [`ff6c940`](https://github.com/SENG321-TEAM-1/CollecTree/commit/ff6c9407283fc533a3da5b882ada94d98360116d) (release merges on `main`).

**Reviews (approved):** [#10](https://github.com/SENG321-TEAM-1/CollecTree/pull/10), [#12](https://github.com/SENG321-TEAM-1/CollecTree/pull/12), [#17](https://github.com/SENG321-TEAM-1/CollecTree/pull/17), [#35](https://github.com/SENG321-TEAM-1/CollecTree/pull/35), [#38](https://github.com/SENG321-TEAM-1/CollecTree/pull/38).

---

### Ata Eren Atlı

- **Student number:** 220205046
- **GitHub:** [@atalirr](https://github.com/atalirr)
- **Role:** Implementation and Integration Engineer
- **Responsibilities:** Issue-based feature branches, checking that the frontend and backend plans match the OpenAPI contract, and peer reviews (RACI row 5.3: Responsible).

**Work done**

- Fixed the branch name rule in the pull request template so that it matches the code review guidelines.
- Created the tasks of US-02 and US-09.
- Reviewed the architecture documents and the ADR acceptance against the planned implementation.

**Issues:** created and assigned [#44](https://github.com/SENG321-TEAM-1/CollecTree/issues/44); created and assigned the tasks [#74](https://github.com/SENG321-TEAM-1/CollecTree/issues/74), [#75](https://github.com/SENG321-TEAM-1/CollecTree/issues/75), [#76](https://github.com/SENG321-TEAM-1/CollecTree/issues/76), [#78](https://github.com/SENG321-TEAM-1/CollecTree/issues/78); assigned to [#5](https://github.com/SENG321-TEAM-1/CollecTree/issues/5) (US-02) and [#24](https://github.com/SENG321-TEAM-1/CollecTree/issues/24) (US-09).

**Pull requests:** [#45](https://github.com/SENG321-TEAM-1/CollecTree/pull/45) Fix the branch name rule in the pull request template.

**Commits:** [`c8af0f2`](https://github.com/SENG321-TEAM-1/CollecTree/commit/c8af0f27a1d052aa1714426717b40abb2dfac819).

**Reviews (approved):** [#20](https://github.com/SENG321-TEAM-1/CollecTree/pull/20), [#35](https://github.com/SENG321-TEAM-1/CollecTree/pull/35).
