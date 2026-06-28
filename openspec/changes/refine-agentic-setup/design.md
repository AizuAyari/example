## Context

The project ships a Django application with four apps (`orders`, `accounts`, `api`, `web`). A `CLAUDE.md` and `openspec/` directory exist but `openspec/config.yaml` has no project context, and `openspec/specs/` is entirely empty. AI agents operating on this codebase have no machine-readable capability contracts — they infer rules solely from code and `CLAUDE.md` prose, which increases the chance of inconsistent or incorrect changes.

This is a documentation-only change; no application code is modified.

## Goals / Non-Goals

**Goals:**
- Give AI agents a stable, queryable source of truth for each core capability
- Populate `openspec/config.yaml` so agents understand the tech stack and domain without reading CLAUDE.md first
- Establish lightweight specs that define normative requirements and testable scenarios for the four Django apps
- Confirm CLAUDE.md stays as the convention/command reference and defers to specs for capability behavior

**Non-Goals:**
- Designing new features or changing existing business logic
- Writing tests or migrations
- Fully exhaustive specs — initial specs capture the most critical requirements; detail grows incrementally

## Decisions

**One spec file per Django app**
Each of the four apps (`orders`, `accounts`, `api`, `web`) maps to one capability spec. This keeps boundaries clear and avoids cross-cutting monoliths. Agents needing to work on `apps/orders` read `openspec/specs/order-management/spec.md`.

*Alternative considered*: A single `system.md` spec. Rejected — too coarse; agents can't selectively load relevant context.

**`openspec/config.yaml` holds tech context; `CLAUDE.md` holds dev conventions**
`config.yaml` is loaded automatically by OpenSpec tooling. Putting stack/domain info there means agents get it for free during any `openspec instructions` call. `CLAUDE.md` stays focused on conventions, commands, and coupling rules.

*Alternative considered*: Duplicate context in both files. Rejected — duplication drifts.

**Specs describe normative behavior at the service boundary, not implementation**
Requirements use SHALL/MUST and describe observable behavior (inputs, outcomes, errors). Implementation details (SQL queries, class names) are excluded — those live in code.

## Risks / Trade-offs

- **Specs drift from code** → Mitigate by adding a spec-maintenance note to CLAUDE.md's "Change coupling" section (already partially present)
- **Initial specs are incomplete** → Acceptable; they are a foundation, not a freeze. Agents should propose spec additions when they discover undocumented behavior.
- **Four files to maintain** → Low overhead for a four-app project; revisit if app count grows significantly
