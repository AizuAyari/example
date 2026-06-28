## Why

The project's agentic setup (CLAUDE.md, openspec/) exists but lacks the context and foundational specs needed for AI agents to make well-informed decisions. Without documented capabilities and project context, agents must infer conventions from code alone, increasing the risk of drift and inconsistency across the Django apps.

## What Changes

- Populate `openspec/config.yaml` with project context (tech stack, domain, conventions)
- Create foundational capability specs for the four core apps:
  - `order-management` — order lifecycle, status transitions, business rules
  - `user-accounts` — users, roles, and permissions
  - `rest-api` — DRF endpoints, response shapes, versioning conventions
  - `staff-ui` — server-rendered staff-facing views and form patterns
- Align CLAUDE.md with the new specs (no duplication; CLAUDE.md points to specs as the canonical source)

## Capabilities

### New Capabilities

- `order-management`: Covers order lifecycle states, valid transitions, and business rules enforced in `apps/orders/services.py`
- `user-accounts`: Covers user model, role definitions, permission rules, and authentication enforced in `apps/accounts`
- `rest-api`: Covers DRF endpoint conventions, response shapes, URL naming, versioning, and authentication in `apps/api`
- `staff-ui`: Covers server-rendered view patterns, form conventions, and template structure in `apps/web`

### Modified Capabilities

<!-- No existing specs — nothing to modify -->

## Impact

- `openspec/config.yaml` — context section populated
- `openspec/specs/<capability>/spec.md` — four new spec files created
- `CLAUDE.md` — minor update to confirm specs are the canonical source (already partially stated; to be verified and tightened)
- No code changes; documentation only
