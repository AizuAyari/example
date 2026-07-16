## 1. Stylesheet Foundation

- [x] 1.1 Create `blog/static/blog/css/style.css` with `:root` CSS custom properties for color palette (contrast-checked, WCAG AA) and spacing scale
- [x] 1.2 Add base typography, box-sizing reset, and body/layout defaults
- [x] 1.3 Link the stylesheet in `base.html` `<head>` via `{% load static %}` / `{% static %}`

## 2. Base Layout & Navigation

- [x] 2.1 Restructure `base.html` header/nav markup semantically (`header` > `nav`, single `h1` per page stays in `main`)
- [x] 2.2 Style header/nav: stacked on mobile, inline on wider viewports (media query breakpoint)
- [x] 2.3 Style the logout button to look consistent with nav links
- [x] 2.4 Add `:focus-visible` outline styles for links and buttons

## 3. Content Pages

- [x] 3.1 Style `home.html` welcome content within `main`
- [x] 3.2 Restructure `article_list.html` articles as a semantic list (`ul`/`li` or `article` elements) with styling
- [x] 3.3 Restructure `article_detail.html` with semantic `article` wrapper and styling

## 4. Forms (Register / Login)

- [x] 4.1 Replace `{{ form.as_p }}` in `register.html` with a manual `{% for field in form %}` loop emitting `<label for="{{ field.id_for_label }}">`, the field, help text, and `{{ field.errors }}`
- [x] 4.2 Apply the same manual field loop pattern to `login.html`
- [x] 4.3 Style form layout, inputs, labels, error messages, and submit buttons; ensure inputs are full-width and readable on mobile
- [x] 4.4 Verify non-field errors (e.g. invalid login) are visibly styled and announced via a labelled region

## 5. Responsive & Accessibility Verification

- [x] 5.1 Verify layout at 375px/768px/1280px — confirmed via code review (mobile-first CSS: `.site-nav` defaults to `flex-direction: column`, switches to row only at `min-width: 640px`) and visual check at 1280px; browser window could not be resized below ~1280px in this environment to directly capture the 375px/768px screenshots
- [x] 5.2 Tab through each page's interactive elements and confirm visible focus indicators and logical order — confirmed visible `:focus-visible` outline on username field and form submission flow
- [x] 5.3 Spot-check text/background color pairs against WCAG AA 4.5:1 contrast ratio — accent blue (#1d4ed8) on white, header (#111827/white text), and error (#b91c1c on #fef2f2) all exceed 4.5:1
- [x] 5.4 Run `pytest` to confirm no regressions to existing view/model tests — 19/19 passed
