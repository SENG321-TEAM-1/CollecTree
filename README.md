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
 elifarat-patch-1
1. Project Proposal and Problem Definition   

Problem: Diecast and hobby collectors currently track their extensive collections using manual tools like Excel spreadsheets or physical notebooks. These primitive methods lack visual tracking (photos), are difficult to keep synchronized, and fail to provide real-time portfolio valuation. Furthermore, there is a lack of a dedicated, niche social platform where collectors can easily discover missing pieces and directly communicate to negotiate trades.

Proposed Solution: A specialized digital inventory platform that allows users to seamlessly manage their collections with photos and financial details. The platform will also serve as a social network, enabling collectors to view public inventories and use direct messaging (DM) to negotiate trades.

Open-Source License: MIT License.

2. System Vision and System Boundary Specification   

System Vision: To simplify and digitalize collection management while building a dedicated social network focused on trading hobby items.

In Scope (System Boundaries): User authentication and profile creation, adding/removing collection items (including photos, brand, purchase cost, and current market value), automated calculation of total portfolio value, viewing other users' public collections, and a Direct Messaging (DM) system for trade negotiations.

Out of Scope (System Boundaries): The system will strictly NOT process any financial transactions. Payment gateways, digital wallets, shopping carts, checkout processes, and shipping tracking are completely outside the system boundaries. All trade agreements and payments must be handled externally by the users. develop
