## Why

The current templates (`home`, `article_list`, `article_detail`, `register`, `login`, `base`) render with no styling at all — plain `<p>` tags and unlabeled default Django form output. Now that registration, login, and logout work end-to-end (Exercise 8), Exercise 9 requires applying semantic HTML, CSS, responsive design, and accessibility (universal design) principles so the app looks and behaves like a real, usable web product rather than a bare functional prototype.

## What Changes

- Restructure templates to use semantic HTML5 elements (`header`, `nav`, `main`, `section`, `footer`, proper heading hierarchy) instead of generic `div`/`p` soup.
- Add a self-authored CSS stylesheet (`blog/static/blog/css/style.css`) providing consistent typography, spacing, color, and component styling (nav, buttons, forms, article list/detail) across all pages.
- Make layout responsive: usable and readable from narrow mobile widths up through desktop, using relative units and media queries (no horizontal scrolling, no overlapping elements).
- Apply accessibility (universal design) improvements: explicit `<label for>`/`id` pairing on all form fields, sufficient color contrast, visible `:focus` states for interactive elements, landmark roles implied by semantic tags, and a logical heading/tab order.
- No changes to URLs, views, or authentication logic — this is a presentation-layer change only.

## Capabilities

### New Capabilities
- `interface-design`: Presentation-layer requirements covering semantic HTML structure, CSS styling, responsive layout, and accessibility across all blog templates.

### Modified Capabilities
_None — `user-auth` and other existing capabilities keep their current behavioral requirements; only markup/styling changes._

## Impact

- Affected files: `blog/templates/blog/base.html`, `home.html`, `article_list.html`, `article_detail.html`, `register.html`, `login.html`.
- New file(s): `blog/static/blog/css/style.css` (and `STATICFILES` already default-configured by Django's `staticfiles` app).
- No changes to `blog/views.py`, `blog/urls.py`, `blog/forms.py`, or `blog/models.py`.
- No new dependencies (no CSS framework/CDN — hand-written CSS per project decision).
