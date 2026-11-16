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
CollecTree is a digital inventory and social trading platform for Diecast and hobby collectors. The first release scope covers personal inventory tracking, portfolio valuation based on external market data, public profile discovery, and direct messaging for trade negotiations. The system explicitly excludes checkouts and financial transactions.

### 1.3 Definitions
* **Collector:** A registered user of the system who maintains an inventory.
* **Visitor:** An unregistered or not logged-in user with read-only access to public sections.
* **Model:** A definitive catalog entry of a collectible.
* **Item:** A specific physical instance of a model owned by a collector.
* **Portfolio:** The financial summary of a collector's items.
* **Offer:** A formal trade proposal between collectors involving items, cash, or both.
* **Market Price:** The current estimated value of a model, sourced from external platforms.
* **Seed Price:** The fallback initial value if the market price is not yet available.

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
* **Visitor:** Has read-only access and can only register or log in.
* **Collector:** A registered user who can add items, manage collections, view statistics, search other collectors, and negotiate trades.

### 2.3 Operating environment
The system is accessed via current modern web browsers. The backend infrastructure runs using Docker Compose. The system and user interface are entirely in English.

### 2.4 Constraints
System boundaries and constraints are defined in `docs/architecture/system-boundary.md` (Section Constraints). A major constraint is that no financial transactions or checkouts are processed on the platform (ADR-003). Payments and deliveries are handled outside the system by the users.

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
| FR-05 | The system shall let a user search the catalogue for models to add to their collection. | US-02 | `searchModels` | - |
| FR-06 | The system shall let a user add an item to their collection based on an existing catalogue model. | US-02 | `addItem` | BR-19 |
| FR-07 | The system shall let a user update the purchase price, purchase date, and trade status of their own items. | US-10 | `updateItem` | BR-18, BR-19 |
| FR-08 | The system shall let a user remove an item from their collection, applying a soft delete. | US-07 | `deleteItem` | BR-05 |
| FR-09 | The system shall list and filter the items present in a user's collection. | US-02, US-04 | `listUserItems` | - |

### 3.3 F-03 Market Price Tracking
| ID | Requirement | User story | API operation | Business rules |
|---|---|---|---|---|
| FR-11 | The system shall automatically update the market prices of models daily via a background job. | US-08 | `(background job)` | - |
| FR-12 | The system shall automatically update the USD to TRY exchange rate daily via a background job. | US-08 | `(background job)` | - |
| FR-13 | The system shall return the historical market price data of a specific model. | US-08 | `getPriceHistory` | - |

### 3.4 F-04 Portfolio Valuation
| ID | Requirement | User story | API operation | Business rules |
|---|---|---|---|---|
| FR-14 | The system shall calculate and return the total purchase cost, current market value, and profit/loss of a collector's portfolio. | US-03 | `getMyPortfolio` | - |
| FR-15 | The system shall return historical chart data points for the portfolio valuation within a specified date range. | US-03 | `getMyPortfolioHistory` | - |

### 3.5 F-05 Collector Discovery
| ID | Requirement | User story | API operation | Business rules |
|---|---|---|---|---|
| FR-04 | The system shall return the public profile information of a specified collector. | US-04 | `getUserProfile` | - |
| FR-10 | The system shall omit purchase prices when listing collection items to a user other than the owner. | US-04 | `listUserItems` | - |
| FR-16 | The system shall let a user view the visible collection items of other collectors. | US-04 | `listUserItems` | - |

### 3.6 F-06 Trade Negotiation
| ID | Requirement | User story | API operation | Business rules |
|---|---|---|---|---|
| FR-17 | The system shall let a user start a new direct message conversation with another collector. | US-05 | `startConversation`, `listConversations` | - |
| FR-18 | The system shall let a user send text messages and retrieve the message history of a conversation. | US-05 | `sendMessage`, `listMessages` | - |
| FR-19 | The system shall let a user submit a formal trade offer including items, cash, or both. | US-09 | `createOffer` | - |
| FR-20 | The system shall let the receiver accept or reject an offer, and the sender withdraw it. | US-09 | `updateOfferStatus` | - |
| FR-21 | The system shall automatically cancel all other pending offers involving an item when a related offer is accepted. | US-09 | `updateOfferStatus` | BR-16, BR-17 |
| FR-22 | The system shall list all offers sent and received by the current user. | US-09 | `listMyOffers` | - |

## 4 External Interface Requirements
### 4.1 User interface
The user interface specifications and screens map to the functional requirements defined above.
*(Link to the Figma prototype and `docs/design/user-flows.md` from Ata will be added here).*

### 4.2 API
The backend interface is strictly defined by the OpenAPI specification contract located at `api/openapi.yaml`.

### 4.3 External systems
The system integrates with the eBay Browse API for international listing prices and the TCMB (Central Bank of the Republic of Türkiye) for currency conversion to TRY (ADR-003).

## 5 Data Requirements
Refer to the domain concepts in `docs/architecture/domain-model.md` (Section 2).

## 6 Non-functional Requirements
*(Link to `docs/requirements/non-functional-requirements.md` from Kemal will be added here).*

## 7 Traceability Matrix

| User story | Functional requirements | API operations | Business rules |
|---|---|---|---|
| US-01 | FR-01 | `register` | BR-01 |
| US-02 | FR-05, FR-06, FR-09 | `searchModels`, `addItem`, `listUserItems` | BR-19 |
| US-03 | FR-14, FR-15 | `getMyPortfolio`, `getMyPortfolioHistory` | - |
| US-04 | FR-04, FR-09, FR-10, FR-16 | `getUserProfile`, `listUserItems` | - |
| US-05 | FR-17, FR-18 | `startConversation`, `listConversations`, `sendMessage`, `listMessages` | - |
| US-06 | FR-02, FR-03 | `login`, `getMe` | - |
| US-07 | FR-08 | `deleteItem` | BR-05 |
| US-08 | FR-11, FR-12, FR-13 | `(background job)`, `getPriceHistory` | - |
| US-09 | FR-19, FR-20, FR-21, FR-22 | `createOffer`, `updateOfferStatus`, `listMyOffers` | BR-16, BR-17 |
| US-10 | FR-07 | `updateItem` | BR-18, BR-19 |
