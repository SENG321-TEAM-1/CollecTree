# ADR-002: Open-Source License

| Field | Value |
|---|---|
| Status | Proposed (to be accepted by the team in Sprint 1 review) |
| Date | 2026-10-27 |
| Proposed by | Berke Akman — Lead Software Architect |
| Final approval | Product Owner, with the team |

## Context

The course requires an open-source license for the project. The questions from the course material:

| Question | Our answer |
|---|---|
| May others use the code commercially? | Yes, we do not need to restrict this. |
| Must derived work use the same license? | No, we do not need copyleft. |
| Do we need an explicit patent grant? | No, the project has no patentable technology. |
| Are dependency licenses compatible? | Yes, see the table below. |

## Decision

**MIT License.** The full text is in `LICENSE` at the repository root, with the copyright line:
`Copyright (c) 2026 SENG321-TEAM 1`.

## Dependency license check

| Dependency | License | Compatible with MIT |
|---|---|---|
| FastAPI | MIT | Yes |
| SQLAlchemy | MIT | Yes |
| Pydantic | MIT | Yes |
| APScheduler | MIT | Yes |
| PostgreSQL | PostgreSQL License (permissive) | Yes |
| React | MIT | Yes |
| Vite | MIT | Yes |
| Recharts | MIT | Yes |
| pytest | MIT | Yes |

All main dependencies are permissive. New dependencies are checked during code review.

## Alternatives considered

| License | Why not chosen |
|---|---|
| Apache 2.0 | Also a good choice; adds a patent grant and NOTICE file rules we do not need. Longer text. |
| GPL-3.0 | Forces everyone who distributes a modified version to publish it under GPL; stricter than we need. |

## Consequences

- Anyone can use, copy, and modify the code if they keep the copyright notice.
- The project gives no warranty.
- External price data is **not** covered by this license; its use follows the data source's own terms.
