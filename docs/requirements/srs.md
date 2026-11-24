# Software Requirements Specification

| Field | Value |
|---|---|
| Project | CollecTree |
| Course | BM 321 / SENG 321 Software Engineering — Sprint 2 |
| Version | 0.2.0 |
| Owner (Accountable) | Elif Zahide Arat — Product Owner and Requirements Engineer |
| Consulted | Berke Akman (Architect), Kemal Yusuf Ateşer (QA), Ata Eren Atlı (Implementation) |
| Informed | Feyza Sayar (Scrum Master), Çağrı Baynal (DevOps) |

## 1 Introduction

### 1.1 Purpose
This document specifies the software requirements for the CollecTree platform. It is intended for developers, quality assurance engineers, the product owner, and project stakeholders (evaluators/jury) to understand the system's expected functional and non-functional behavior during Sprint 2.

### 1.2 Scope
CollecTree is a web platform for diecast model collectors. The first release covers personal inventory tracking, daily market valuation in TRY, portfolio profit and loss, public profile discovery, direct messaging, and formal item, cash, or mixed trade offers. Payments, delivery, and checkout are out of scope.

### 1.3 Definitions
* **Collector:** A registered user of the system who maintains an inventory.
* **Visitor:** A user who is not logged in. A visitor can search the catalogue, view public profiles and collections (without purchase prices), view price histories, and register or log in.
* **Model:** A definitive catalog entry of a collectible.
* **Item:** A specific physical instance of a model owned by a collector.
* **Portfolio:** The financial summary of a collector's items.
* **Offer:** A formal trade proposal between collectors involving items, cash, or both.
* **Market Price:** The daily median price of new, fixed-price eBay listings for a model, converted from USD to TRY (ADR-003).
* **Seed Price:** A reference price collected manually by the team, used for demos and when the external price source is not available.

### 1.4 References
* `README.md`
* `docs/architecture/README.md`
* `docs/architecture/domain-model.md`
* ADR-003 (Pricing Source)
* `api/openapi.yaml`
* `docs/requirements/product-backlog.md`

## 2 Overall Description

### 2.1 Product perspective
The system is designed as a standalone platform. Its high-level context and container boundaries are detailed in the C4 Level 1 diagram located in `docs/architecture/c4-model.md`. 

### 2.2 User classes
* **Visitor:** A user who is not logged in. A visitor can search the catalogue, view public profiles and collections (without purchase prices), view price histories, and register or log in.
* **Collector:** A registered user who can add items, manage collections, view statistics, search other collectors, and negotiate trades.

### 2.3 Operating environment
The system is accessed via current modern web browsers. The backend infrastructure runs using Docker Compose. The system and user interface are entirely in English.

### 2.4 Constraints
System boundaries and constraints are defined in `docs/architecture/system-boundary.md` (Section Constraints). A major constraint is that no financial transactions or checkouts are processed on the platform (BR-10). Payments and deliveries are handled outside the system by the users. Prices derived from eBay are used only inside CollecTree: they are not exported, downloaded in bulk, or offered as a data feed (ADR-003, decision 6).

### 2.5 Assumptions
Refer to `docs/architecture/system-boundary.md` for assumptions AS-1 to AS-4.

## 3 Functional Requirements

### 3.1 F-01 Account Access
| ID | Requirement | User story | API operation | Business rules |
|---|---|---|---|---|
| FR-01 | The system shall let a visitor create an account with a unique username and email address. | US-01 | `register` | BR-01 |
| FR-02 | The system shall let a registered user log in with email and password and receive an access token. | US-06 | `login` | - |
| FR-03 | The system shall return the profile details of the currently logged-in user. | US-06 | `getMe` | - |

### 3.2 F-02 Collection Management
| ID | Requirement | User story | API operation | Business rules |
|---|---|---|---|---|
| FR-05 | The system shall let a user search the catalogue for models to add to their collection. Results are returned in pages of at most 50 models. | US-02 | `searchModels` | - |
| FR-06 | The system shall let a user add an item to their collection based on an existing catalogue model. | US-02 | `addItem` | - |
| FR-07 | The system shall let a user update the purchase price, purchase date, and trade status of their own items. | US-10 | `updateItem` | BR-03, BR-18, BR-19 |
| FR-08 | The system shall let a user remove an item from their collection, applying a soft delete. | US-07 | `deleteItem` | BR-03, BR-04, BR-05 |
| FR-09 | The system shall list and filter the items present in a user's collection. Results are returned in pages of at most 50 items. | US-02, US-04 | `listUserItems` | BR-04 |

### 3.3 F-03 Market Price Tracking
| ID | Requirement | User story | API operation | Business rules |
|---|---|---|---|---|
| FR-11 | The system shall automatically update the market prices of models daily via a background job. A price is saved only if at least 5 matching listings remain and their prices are consistent (p75/p25 ≤ 2.0); otherwise the last known price is kept (ADR-003). | US-08 | `(background job)` | BR-13, BR-15 |
| FR-12 | The system shall automatically update the USD to TRY exchange rate daily via a background job. | US-08 | `(background job)` | - |
| FR-13 | The system shall return the historical market price data of a specific model. | US-08 | `getPriceHistory` | - |

### 3.4 F-04 Portfolio Valuation
| ID | Requirement | User story | API operation | Business rules |
|---|---|---|---|---|
| FR-14 | The system shall calculate and return the total purchase cost, current market value, and profit/loss of a collector's portfolio. | US-03 | `getMyPortfolio` | BR-14 |
| FR-15 | The system shall return historical chart data points for the portfolio valuation within a specified date range. | US-03 | `getMyPortfolioHistory` | - |

### 3.5 F-05 Collector Discovery
| ID | Requirement | User story | API operation | Business rules |
|---|---|---|---|---|
| FR-04 | The system shall return the public profile information of a specified collector. | US-04 | `getUserProfile` | - |
| FR-10 | The system shall omit purchase prices when listing collection items to a user other than the owner. | US-04 | `listUserItems` | BR-02 |
| FR-16 | The system shall let a user view the visible collection items of other collectors. | US-04 | `listUserItems` | - |

### 3.6 F-06 Trade Negotiation
| ID | Requirement | User story | API operation | Business rules |
|---|---|---|---|---|
| FR-17 | The system shall let a user start a new direct message conversation with another collector. | US-05 | `startConversation`, `listConversations` | BR-12 |
| FR-18 | The system shall let a user send text messages and retrieve the message history of a conversation. | US-05 | `sendMessage`, `listMessages` | BR-11 |
| FR-19 | The system shall let a user submit a formal trade offer including items, cash, or both. | US-09 | `createOffer` | BR-06, BR-07, BR-08 |
| FR-20 | The system shall let the receiver accept or reject an offer, and the sender withdraw it. | US-09 | `updateOfferStatus` | BR-09, BR-10 |
| FR-21 | The system shall, when an offer is accepted, cancel every other pending offer that contains any of its items and close all of its items for trade. | US-09 | `updateOfferStatus` | BR-16, BR-17 |
| FR-22 | The system shall list all offers sent and received by the current user. | US-09 | `listMyOffers` | - |

## 4 External Interface Requirements
### 4.1 User interface
The user interface specifications and screens map to the functional requirements defined above.
- **Figma prototype (12 desktop screens):** [CollecTree – Sprint 2 Prototype](https://www.figma.com/design/kpeIcUYw4x5FKOvrRbYFaM/CollecTree-Sprint-2-Prototype?node-id=24-2)
- **Clickable main journey:** [Login → My Collection → Add Item → Portfolio → Public Profile → Make Offer → My Offers → Conversations](https://www.figma.com/proto/kpeIcUYw4x5FKOvrRbYFaM/CollecTree-Sprint-2-Prototype?page-id=24%3A2&node-id=24-4&starting-point-node-id=24%3A4)
- **User flows:** [`docs/design/user-flows.md`](../design/user-flows.md) has 7 flow diagrams, the on-screen messages shared by the screens and the API tests, and a table that maps every screen to its API operations.
- Every market price is labelled "International listing price (eBay), converted to TRY", and the offer screens show the notice "Payment and delivery are handled by the users outside the platform." (BR-10).

### 4.2 API
The backend interface is strictly defined by the OpenAPI specification contract located at `api/openapi.yaml`.

### 4.3 External systems
The system integrates with the eBay Browse API for international listing prices and the TCMB (Central Bank of the Republic of Türkiye) for currency conversion to TRY (ADR-003).

## 5 Data Requirements
Refer to the domain concepts in `docs/architecture/domain-model.md` (Section 2).

## 6 Non-functional Requirements
The non-functional requirements are in [`non-functional-requirements.md`](non-functional-requirements.md): 20 requirements grouped by the quality characteristics of ISO/IEC 25010 (performance efficiency, reliability, security, usability, maintainability, portability, and compatibility). Each requirement has a measurable target and a verification method. The test plan in [`docs/testing/test-plan.md`](../testing/test-plan.md) describes how each one is verified.

## 7 Traceability Matrix

| User story | Functional requirements | API operations | Business rules |
|---|---|---|---|
| US-01 | FR-01 | `register` | BR-01 |
| US-02 | FR-05, FR-06, FR-09 | `searchModels`, `addItem`, `listUserItems` | BR-04 |
| US-03 | FR-14, FR-15 | `getMyPortfolio`, `getMyPortfolioHistory` | BR-14 |
| US-04 | FR-04, FR-09, FR-10, FR-16 | `getUserProfile`, `listUserItems` | BR-02, BR-04 |
| US-05 | FR-17, FR-18 | `startConversation`, `listConversations`, `sendMessage`, `listMessages` | BR-11, BR-12 |
| US-06 | FR-02, FR-03 | `login`, `getMe` | - |
| US-07 | FR-08 | `deleteItem` | BR-03, BR-04, BR-05 |
| US-08 | FR-11, FR-12, FR-13 | `(background job)`, `getPriceHistory` | BR-13, BR-15 |
| US-09 | FR-19, FR-20, FR-21, FR-22 | `createOffer`, `updateOfferStatus`, `listMyOffers` | BR-06, BR-07, BR-08, BR-09, BR-10, BR-16, BR-17 |
| US-10 | FR-07 | `updateItem` | BR-03, BR-18, BR-19 |
