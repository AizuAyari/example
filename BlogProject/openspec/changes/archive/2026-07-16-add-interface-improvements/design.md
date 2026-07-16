## Context

All six templates (`base.html`, `home.html`, `article_list.html`, `article_detail.html`, `register.html`, `login.html`) currently render unstyled default HTML: bare `<p>` tags, Django's default `form.as_p` output with no `<label for>` association styling, and no stylesheet at all. Django's `staticfiles` app is already installed (default `settings.py`), so a static CSS file just needs to be added and referenced — no new package or build tooling.

## Goals / Non-Goals

**Goals:**
- Semantic HTML structure across all templates (proper landmarks, heading hierarchy, labelled form fields).
- One consolidated, hand-written stylesheet applied via `base.html` so every page shares consistent look and feel.
- Responsive layout from ~320px mobile width up through desktop, no horizontal scroll, no overlap.
- Baseline accessibility: label/input association, visible focus states, sufficient color contrast (WCAG AA, 4.5:1 for body text), logical tab order.

**Non-Goals:**
- No CSS framework/CDN (Bootstrap, Tailwind) — hand-written CSS only, per project decision.
- No JavaScript-driven interactivity (mobile nav toggle, animations) — out of scope for this exercise.
- No visual redesign of content/copy, no new pages, no change to views/URLs/models.
- No dark mode / theming system.

## Decisions

- **Single global stylesheet** at `blog/static/blog/css/style.css`, linked once in `base.html` `<head>`, rather than per-template stylesheets. Rationale: the app is small (5 pages), a single file keeps styles consistent and avoids duplication; per-page stylesheets would be premature for this scale.
- **Hand-authored form field rendering** instead of `{{ form.as_p }}`: iterate `{% for field in form %}` in `register.html`/`login.html` to emit explicit `<label for="{{ field.id_for_label }}">` and wrap each field/errors in a `<div class="form-field">`. Rationale: `as_p` provides no hook for accessible label association or per-field styling; manual iteration is the standard Django pattern for this and keeps forms.py unchanged.
- **Mobile-first CSS with a single breakpoint** (e.g. `min-width: 640px`) widening the nav from stacked to inline and constraining content to a max-width centered column on larger screens. Rationale: the content is simple enough that one breakpoint covers phone vs. tablet/desktop without added complexity.
- **CSS custom properties (`:root` variables)** for color palette and spacing scale, so contrast-checked colors are defined once and reused. Rationale: keeps contrast/consistency easy to audit and adjust.
- **Focus visibility via `:focus-visible`** on links, buttons, and inputs (outline, not just color change) rather than removing the default outline. Rationale: required for keyboard accessibility; relying on color alone fails WCAG.

## Risks / Trade-offs

- [Risk] Hand-written CSS takes longer than a framework and may miss edge cases a framework would handle → Mitigation: keep scope to the 5 existing pages/components only, verify visually at 375px/768px/1280px widths after implementation.
- [Risk] Manual form field loop in templates could drift from Django's built-in error rendering conventions → Mitigation: still use `{{ field.errors }}` and `{{ field }}` as provided by Django's form field rendering, only add the surrounding label/wrapper markup.
- [Risk] Contrast/focus requirements are subjective without automated tooling → Mitigation: pick colors from a pre-checked palette (compute contrast ratio manually for text/background pairs used) and manually tab through each page during verification.

## Migration Plan

Not applicable — purely additive presentation-layer change (new CSS file, template edits). No data migration, no deployment sequencing beyond the normal `collectstatic`-free `DEBUG=True` dev server static serving already in place.
