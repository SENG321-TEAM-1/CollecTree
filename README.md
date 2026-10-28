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
Diecast and hobby collectors currently track their extensive collections using manual tools like Excel spreadsheets or physical notebooks. These primitive methods lack visual tracking (photos), are difficult to keep synchronized, and fail to provide real-time portfolio valuation. Furthermore, there is a lack of a dedicated, niche social platform where collectors can easily discover missing pieces and directly communicate to negotiate trades.

### Intended Outcome
A specialized digital inventory platform that allows users to seamlessly manage their collections with photos and financial details. The platform will also serve as a social network, enabling collectors to view public inventories and use direct messaging (DM) to negotiate trades.

### Stakeholders
- **Primary Users:** Hobby and diecast collectors who need digital inventory tracking and a predictable trade communication system.
- **External Dependencies:** Identity/Email providers for user registration.

### Initial Success Measure
A collector successfully creates a profile, adds a new collection item with its photo and market value, and views it in their inventory in less than two minutes.

---

# 2. System Vision and Boundary

### System Vision
To simplify and digitalize collection management while building a dedicated social network focused on trading hobby items.

### First Release Scope (In Scope)
- User authentication and profile creation
- Adding/removing collection items (including photos, brand, purchase cost, and current market value)
- Automated calculation of total portfolio value
- Viewing other users' public collections
- Direct Messaging (DM) system for trade negotiations

### Exclusions (Out of Scope)
The system will strictly NOT process any financial transactions. Payment gateways, digital wallets, shopping carts, checkout processes, and shipping tracking are completely outside the system boundaries. All trade agreements and payments must be handled externally by the users.

---

# 3. Assumptions and Risks

| Type | Statement | Validation or response |
|---|---|---|
| Assumption | Intended users have valid email addresses for registration. | Confirm during the sign-up process |
| Risk | Users may enter fake market values for their items. | The system is for personal tracking; values will not be verified but can be flagged if reported during DM trades|
| Risk | Concurrent message requests may create duplicate DMs. | Treat as an architecture driver and integration-test it |

---

# 4. Open-Source License Decision Record

**Decision:** MIT License for original project code

**Rationale:**
- Provides a short, permissive license.
- Permits use, modification, and redistribution
- Fits the team's intended permissive reuse model
