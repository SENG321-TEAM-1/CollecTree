# Initial Product Backlog

This document summarizes the CollecTree Product Backlog for the first release. The backlog itself lives in GitHub Issues and on the [CollecTree Sprint Board](https://github.com/orgs/SENG321-TEAM-1/projects/1); this page shows all items in one place with their priorities, estimates, dependencies, and owners. The Product Owner (Elif) is accountable for the backlog (RACI row 6.1).

## 1 Backlog hierarchy

The backlog has four levels, linked to each other as GitHub sub-issues:

| Level | Meaning | Example |
| :--- | :--- | :--- |
| **Epic** | A large business goal of the product | EPIC-2: Collection |
| **Feature** | A capability that delivers part of an epic | F-02: Collection Management |
| **User story** | A user need that fits into one sprint, with acceptance criteria | US-02: Add Collection Item |
| **Task** | A technical step that implements or tests a story | US-02.1: Implement the catalogue search and add item endpoints |

Every item has a label (`epic`, `feature`, `user-story`, or `task`), and features and tasks also use the GitHub Feature and Task issue types.

## 2 Epics and features

| Epic | Feature | Priority | Estimate (SP) | User stories | Owner |
| :--- | :--- | :---: | :---: | :--- | :--- |
| [#25](https://github.com/SENG321-TEAM-1/CollecTree/issues/25) EPIC-1: Accounts | [#56](https://github.com/SENG321-TEAM-1/CollecTree/issues/56) F-01: Account Access | High | 6 | [#4](https://github.com/SENG321-TEAM-1/CollecTree/issues/4) US-01, [#21](https://github.com/SENG321-TEAM-1/CollecTree/issues/21) US-06 | Elif |
| [#26](https://github.com/SENG321-TEAM-1/CollecTree/issues/26) EPIC-2: Collection | [#58](https://github.com/SENG321-TEAM-1/CollecTree/issues/58) F-02: Collection Management | High | 7 | [#5](https://github.com/SENG321-TEAM-1/CollecTree/issues/5) US-02, [#22](https://github.com/SENG321-TEAM-1/CollecTree/issues/22) US-07 | Elif |
| [#27](https://github.com/SENG321-TEAM-1/CollecTree/issues/27) EPIC-3: Pricing and Portfolio | [#61](https://github.com/SENG321-TEAM-1/CollecTree/issues/61) F-03: Market Price Tracking | Medium | 8 | [#23](https://github.com/SENG321-TEAM-1/CollecTree/issues/23) US-08 | Elif |
| [#27](https://github.com/SENG321-TEAM-1/CollecTree/issues/27) EPIC-3: Pricing and Portfolio | [#66](https://github.com/SENG321-TEAM-1/CollecTree/issues/66) F-04: Portfolio Valuation | Medium | 3 | [#6](https://github.com/SENG321-TEAM-1/CollecTree/issues/6) US-03 | Elif |
| [#28](https://github.com/SENG321-TEAM-1/CollecTree/issues/28) EPIC-4: Social and Trading | [#65](https://github.com/SENG321-TEAM-1/CollecTree/issues/65) F-05: Collector Discovery | Medium | 5 | [#7](https://github.com/SENG321-TEAM-1/CollecTree/issues/7) US-04 | Elif |
| [#28](https://github.com/SENG321-TEAM-1/CollecTree/issues/28) EPIC-4: Social and Trading | [#69](https://github.com/SENG321-TEAM-1/CollecTree/issues/69) F-06: Trade Negotiation | Low | 16 | [#8](https://github.com/SENG321-TEAM-1/CollecTree/issues/8) US-05, [#24](https://github.com/SENG321-TEAM-1/CollecTree/issues/24) US-09 | Elif |

The first release is estimated at **45 story points** in total.

## 3 User stories

Priority 1 is the highest. Stories are estimated in story points (SP) on the Fibonacci scale (1, 2, 3, 5, 8). The acceptance criteria of every story are in its issue and were reviewed by QA in [#31](https://github.com/SENG321-TEAM-1/CollecTree/issues/31).

| Priority | ID | User story | Feature | Estimate (SP) | Dependencies | Owner |
| :---: | :--- | :--- | :--- | :---: | :--- | :--- |
| 1 | US-01 | [#4](https://github.com/SENG321-TEAM-1/CollecTree/issues/4) User Registration | F-01 | 3 | None | Berke |
| 1 | US-06 | [#21](https://github.com/SENG321-TEAM-1/CollecTree/issues/21) User Login | F-01 | 3 | Requires US-01 to be completed first. | Çağrı |
| 2 | US-02 | [#5](https://github.com/SENG321-TEAM-1/CollecTree/issues/5) Add Collection Item | F-02 | 5 | Requires US-01 to be completed first. | Ata |
| 2 | US-07 | [#22](https://github.com/SENG321-TEAM-1/CollecTree/issues/22) Remove Collection Item | F-02 | 2 | Requires US-02 (so there are items to remove). The pending-offer rule depends on US-09 (Offers). | Feyza |
| 3 | US-08 | [#23](https://github.com/SENG321-TEAM-1/CollecTree/issues/23) Automatic Market Price Tracking | F-03 | 8 | Requires the model catalogue (seed data). Access to a real price source will be tested in a Sprint 2 spike (assumption AS-1); until then a mock price provider is used. | Berke |
| 3 | US-03 | [#6](https://github.com/SENG321-TEAM-1/CollecTree/issues/6) Portfolio Statistics | F-04 | 3 | Requires US-02 (so there is data to calculate) and US-08 (so market prices are available). | Elif |
| 4 | US-04 | [#7](https://github.com/SENG321-TEAM-1/CollecTree/issues/7) Social Discovery | F-05 | 5 | Requires US-02 (so there are items to show). | Çağrı |
| 5 | US-05 | [#8](https://github.com/SENG321-TEAM-1/CollecTree/issues/8) Direct Messaging for Trades | F-06 | 8 | Requires US-01 (for user accounts) and US-04 (to discover profiles to message). | Kemal |
| 5 | US-09 | [#24](https://github.com/SENG321-TEAM-1/CollecTree/issues/24) Trade and Cash Offers | F-06 | 8 | Requires US-02 (items must exist) and US-04 (to find items of other collectors). | Ata |

## 4 Tasks

Tasks are estimated in hours. Each story has implementation tasks owned by the story owner and one API test task owned by the QA engineer (Kemal). "Mock first" means that the frontend task can start against a mock of the OpenAPI contract before its backend task is finished.

| Story | Task | Estimate (h) | Dependencies | Owner |
| :--- | :--- | :---: | :--- | :--- |
| US-01 | [#52](https://github.com/SENG321-TEAM-1/CollecTree/issues/52) US-01.1: Implement the registration endpoint | 6 | None | Berke |
| US-01 | [#53](https://github.com/SENG321-TEAM-1/CollecTree/issues/53) US-01.2: Build the registration page | 4 | US-01.1 (mock first) | Berke |
| US-01 | [#77](https://github.com/SENG321-TEAM-1/CollecTree/issues/77) US-01.T: Write the API tests for the US-01 acceptance criteria | 3 | US-01.1 | Kemal |
| US-06 | [#57](https://github.com/SENG321-TEAM-1/CollecTree/issues/57) US-06.1: Implement the login and current user endpoints | 5 | US-01.1 | Çağrı |
| US-06 | [#59](https://github.com/SENG321-TEAM-1/CollecTree/issues/59) US-06.2: Build the login page and keep the session | 4 | US-06.1 (mock first) | Çağrı |
| US-06 | [#79](https://github.com/SENG321-TEAM-1/CollecTree/issues/79) US-06.T: Write the API tests for the US-06 acceptance criteria | 3 | US-06.1 | Kemal |
| US-02 | [#74](https://github.com/SENG321-TEAM-1/CollecTree/issues/74) US-02.1: Implement the catalogue search and add item endpoints | 6 | US-06.1 | Ata |
| US-02 | [#75](https://github.com/SENG321-TEAM-1/CollecTree/issues/75) US-02.2: Build the add item form with catalogue search | 5 | US-02.1 (mock first) | Ata |
| US-02 | [#80](https://github.com/SENG321-TEAM-1/CollecTree/issues/80) US-02.T: Write the API tests for the US-02 acceptance criteria | 3 | US-02.1 | Kemal |
| US-07 | [#60](https://github.com/SENG321-TEAM-1/CollecTree/issues/60) US-07.1: Implement the delete item endpoint | 3 | US-02.1 | Feyza |
| US-07 | [#67](https://github.com/SENG321-TEAM-1/CollecTree/issues/67) US-07.2: Add the remove action to the collection page | 2 | US-07.1 (mock first) | Feyza |
| US-07 | [#81](https://github.com/SENG321-TEAM-1/CollecTree/issues/81) US-07.T: Write the API tests for the US-07 acceptance criteria | 3 | US-07.1 | Kemal |
| US-08 | [#54](https://github.com/SENG321-TEAM-1/CollecTree/issues/54) US-08.1: Build the price provider adapter with a mock provider | 6 | Model catalogue seed data | Berke |
| US-08 | [#55](https://github.com/SENG321-TEAM-1/CollecTree/issues/55) US-08.2: Implement the daily price job and the price history endpoint | 5 | US-08.1 | Berke |
| US-08 | [#82](https://github.com/SENG321-TEAM-1/CollecTree/issues/82) US-08.T: Write the API tests for the US-08 acceptance criteria | 3 | US-08.2 | Kemal |
| US-03 | [#70](https://github.com/SENG321-TEAM-1/CollecTree/issues/70) US-03.1: Implement the portfolio endpoints | 5 | US-02.1, US-08.2 | Elif |
| US-03 | [#71](https://github.com/SENG321-TEAM-1/CollecTree/issues/71) US-03.2: Build the portfolio dashboard | 6 | US-03.1 (mock first) | Elif |
| US-03 | [#83](https://github.com/SENG321-TEAM-1/CollecTree/issues/83) US-03.T: Write the API tests for the US-03 acceptance criteria | 3 | US-03.1 | Kemal |
| US-04 | [#62](https://github.com/SENG321-TEAM-1/CollecTree/issues/62) US-04.1: Implement the public profile and collection endpoints | 4 | US-02.1 | Çağrı |
| US-04 | [#63](https://github.com/SENG321-TEAM-1/CollecTree/issues/63) US-04.2: Build the public profile and collection page | 4 | US-04.1 | Çağrı |
| US-04 | [#84](https://github.com/SENG321-TEAM-1/CollecTree/issues/84) US-04.T: Write the API tests for the US-04 acceptance criteria | 3 | US-04.1 | Kemal |
| US-05 | [#72](https://github.com/SENG321-TEAM-1/CollecTree/issues/72) US-05.1: Implement the conversation and message endpoints | 6 | US-01.1, US-04.1 | Kemal |
| US-05 | [#73](https://github.com/SENG321-TEAM-1/CollecTree/issues/73) US-05.2: Build the inbox and conversation pages | 6 | US-05.1 (mock first) | Kemal |
| US-05 | [#85](https://github.com/SENG321-TEAM-1/CollecTree/issues/85) US-05.T: Write the API tests for the US-05 acceptance criteria | 3 | US-05.1 | Kemal |
| US-09 | [#76](https://github.com/SENG321-TEAM-1/CollecTree/issues/76) US-09.1: Implement the offer endpoints and status transitions | 8 | US-02.1, US-04.1 | Ata |
| US-09 | [#78](https://github.com/SENG321-TEAM-1/CollecTree/issues/78) US-09.2: Build the make offer form and the offers list | 6 | US-09.1 (mock first) | Ata |
| US-09 | [#86](https://github.com/SENG321-TEAM-1/CollecTree/issues/86) US-09.T: Write the API tests for the US-09 acceptance criteria | 3 | US-09.1 | Kemal |

## 5 Prioritization

Priorities follow the dependencies between stories and the value shown in the collector survey (`README.md`, Supporting Evidence):

1. Accounts come first, because every other story needs a logged-in user.
2. The collection comes next, because pricing, portfolio, and trading all need collection items.
3. Automatic pricing and portfolio statistics are the core value of the product.
4. Social discovery, messaging, and offers build on the earlier stories and come last.

## 6 Definition of Ready

A backlog item can enter a sprint only when:

- the user, the capability, and the value are explicit;
- the acceptance criteria are testable and cover the main behavior and the error cases;
- the dependencies and the API impact (`api/openapi.yaml` operations) are understood;
- the item has an estimate and an owner;
- the item is small enough to finish within one sprint;
- every open question has an owner.

## 7 Definition of Done

A backlog item is done when:

- the change is merged into `develop` through a reviewed pull request;
- the `validate-openapi` check and the tests pass;
- every acceptance criterion is covered by a test;
- the implementation matches `api/openapi.yaml`;
- the issue is closed and its card is in the Done column.
