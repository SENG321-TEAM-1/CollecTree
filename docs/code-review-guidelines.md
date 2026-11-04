# Code Review Guidelines

| Field | Value |
|---|---|
| Owner (Accountable) | Berke Akman — Lead Software Architect and Technical Lead |
| Applied in repository settings by | Çağrı Baynal — DevOps and CI/CD Infrastructure Engineer |
| Version | 0.1.0 |

## 1 Rules

1. Every change goes through a pull request (PR). Nobody pushes directly to `main` or `develop`.
2. Every PR links an issue (`Closes #12`).
3. Every PR needs **at least one approval** from a teammate who did not write the code.
4. Changes to `api/openapi.yaml` or `docs/architecture/` also need approval from the architect (enforced by `CODEOWNERS`).
5. CI checks (tests, lint) must pass before merge.
6. The PR author merges after approval and the branch is deleted. Choose the merge method on the merge button:

   | Pull request | Merge method | Why |
   |---|---|---|
   | `feature/*`, `fix/*`, `docs/*` → `develop` | **Squash and merge** | One clean commit per story in `develop` |
   | `develop` → `main` (sprint release) | **Create a merge commit** | Keeps shared history; avoids false conflicts |
   | `main` → `develop` (sync) | **Create a merge commit** | Same reason |
7. Reviewers answer within **two working days**. If a review is blocked, the Scrum Master is told in the stand-up.

## 2 Branch and commit naming

| Type | Pattern | Example |
|---|---|---|
| Feature | `feature/<issue>-<short-name>` | `feature/13-openapi-draft` |
| Bug fix | `fix/<issue>-<short-name>` | `fix/41-wrong-profit-sign` |
| Docs | `docs/<issue>-<short-name>` or `docs/<short-name>` | `docs/19-architecture-docs` |

Commit messages are short and in the imperative: `Add offer status endpoint`, `Fix portfolio total when no price exists`.

## 3 Reviewer checklist

**Correctness**
- [ ] The code does what the linked issue and its acceptance criteria say.
- [ ] Error cases return the status codes written in `api/openapi.yaml` (400, 401, 403, 404, 409).

**API contract**
- [ ] New or changed endpoints match `api/openapi.yaml`. If the contract changed, the YAML is updated in the same PR.

**Tests**
- [ ] New logic has unit tests; the happy path and at least one error case are covered.
- [ ] Coverage does not drop below 50 percent.

**Readability**
- [ ] Names explain what things are; no unused code or commented-out blocks.
- [ ] The module boundaries in ADR-001 are respected (for example, `offers` does not query `messaging` tables directly).

**Security**
- [ ] No passwords, tokens, or `.env` files are committed.
- [ ] Endpoints that change data check that the user owns that data.

## 4 How to write review comments

- Comment on the code, not the person.
- Mark optional ideas with `nit:` so the author knows they do not block the merge.
- Explain *why*: "This returns 500 when the item is missing; the contract says 404."
