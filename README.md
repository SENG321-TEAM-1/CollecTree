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
