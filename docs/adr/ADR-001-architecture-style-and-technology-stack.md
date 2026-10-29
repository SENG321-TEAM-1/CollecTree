# ADR-001: Architecture Style and Technology Stack

| Field | Value |
|---|---|
| Status | Proposed (to be accepted by the team in Sprint 1 review) |
| Date | 2026-10-26 |
| Decision owner | Berke Akman — Lead Software Architect |
| Consulted | Whole team |

## Context

- The team has six third-year students without prior project experience.
- The course requires API-first development, at least 50 percent unit-test coverage in GitHub Actions, SonarQube analysis, and a system that starts with one Docker Compose command.
- The product needs a REST API, a web user interface, a relational data model (users, items, offers, messages, price history), and a scheduled background job for market prices.

## Decision

### Architecture style: modular monolith, API-first

One backend application, split into clearly separated modules with their own routers, services, and data access:

| Module | Responsibility |
|---|---|
| `auth` | Registration, login, JWT issue and validation |
| `users` | Public profiles |
| `catalog` | Brands, scales, series, catalogue models |
| `collection` | Collection items owned by users |
| `pricing` | Price provider adapter, scheduled price job, price history, valuation |
| `messaging` | Conversations and messages |
| `offers` | Trade and cash offers and their lifecycle |

The OpenAPI contract in `api/openapi.yaml` is written first and reviewed before implementation.

### Technology stack

| Layer | Choice |
|---|---|
| Backend | Python 3.12, FastAPI, SQLAlchemy 2, Alembic (migrations), Pydantic |
| Database | PostgreSQL 16 |
| Background job | APScheduler running inside the backend process |
| Frontend | React 18 with Vite (JavaScript), React Router, Recharts for charts |
| Authentication | Local accounts, bcrypt password hashing, JWT bearer tokens |
| Testing | pytest, pytest-cov, FastAPI TestClient (unit and integration); Playwright (end-to-end) |
| Infrastructure | Docker, Docker Compose, GitHub Actions, SonarQube (SonarCloud for CI) |

## Alternatives considered

| Alternative | Why not chosen |
|---|---|
| Microservices | Adds network calls, service discovery, and multiple deployments. Too much operational weight for a ten-week, inexperienced team. Module boundaries keep a later split possible. |
| Spring Boot (Java) | Strong option, but more setup and boilerplate; slower learning curve for the team. |
| Node.js / NestJS | Viable, but splitting attention between TypeScript types and decorators adds learning cost; Python is more familiar to the team. |
| WebSocket real-time chat | More complex to build and test; periodic polling satisfies first-release needs. |
| External identity provider (OAuth) | Adds external setup and accounts; local JWT authentication is enough for the course. |

## Consequences

- **Positive:** One language on the backend, automatic interactive API documentation (`/docs`), simple testing, a small Docker Compose file (`db`, `backend`, `frontend`).
- **Positive:** The price source is hidden behind a `PriceProvider` interface, so a mock provider can be used in tests and demos.
- **Negative:** All modules scale together; acceptable for the expected load.
- **Negative:** Polling chat is less instant than WebSocket; recorded as a deferred improvement.
