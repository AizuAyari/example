## 1. Project Context

- [ ] 1.1 Populate `openspec/config.yaml` context section with tech stack, domain, and key conventions (Django, DRF, Celery, PostgreSQL; customer order management domain)
- [ ] 1.2 Verify `CLAUDE.md` references `openspec/specs/` as the canonical source for capability behavior (already partially stated — confirm wording is unambiguous)

## 2. Capability Specs

- [ ] 2.1 Promote `changes/refine-agentic-setup/specs/order-management/spec.md` to `openspec/specs/order-management/spec.md`
- [ ] 2.2 Promote `changes/refine-agentic-setup/specs/user-accounts/spec.md` to `openspec/specs/user-accounts/spec.md`
- [ ] 2.3 Promote `changes/refine-agentic-setup/specs/rest-api/spec.md` to `openspec/specs/rest-api/spec.md`
- [ ] 2.4 Promote `changes/refine-agentic-setup/specs/staff-ui/spec.md` to `openspec/specs/staff-ui/spec.md`

## 3. Validation

- [ ] 3.1 Run `openspec status` and confirm no blocking issues
- [ ] 3.2 Spot-check each spec for spec format compliance (MUST use `####` for scenarios, `SHALL/MUST` for normative requirements)
- [ ] 3.3 Confirm `openspec/config.yaml` context is loaded correctly by running `openspec instructions proposal --change refine-agentic-setup --json` and checking the `context` field
