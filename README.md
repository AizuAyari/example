# The Blogs

A blog application built with Django. It includes user registration/login, article posting, and incremental search/filtering powered by HTMX, and is deployed to production on Render.com.

- **Live Demo:** [https://the-blogs.onrender.com](https://the-blogs.onrender.com)

## Repository Structure

The app itself lives under `BlogProject/`.

```
BlogProject/
├── BlogProject/   # Project settings (settings.py, urls.py, wsgi.py)
├── blog/          # App code (models, views, forms, templates, tests)
├── openspec/      # Design/spec docs per feature (proposal / design / tasks)
├── manage.py
├── requirements.txt
├── Procfile       # Render startup command
└── render.yaml    # Render service definition
```

`main.py` / `example.py` / `pyproject.toml` at the repository root are leftovers from an unrelated exercise and are not part of this app.

## Tech Stack

- **Django 6** + SQLite (development)
- **HTMX** (vanilla htmx.org, no `django-htmx`; incremental search debounced with `delay:300ms`)
- **django-environ** (`SECRET_KEY` / `DEBUG` / `ALLOWED_HOSTS` as environment variables)
- **WhiteNoise** (static file serving in production)
- **Gunicorn** (production WSGI server)
- **pytest** / **pytest-django** (33 tests)

## Running Locally

```bash
cd BlogProject
python -m venv .venv
.venv\Scripts\activate        # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

copy .env.example .env        # macOS/Linux: cp
# Replace SECRET_KEY in .env with a value generated via:
# python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

python manage.py migrate
python manage.py runserver
```

## Tests

```bash
cd BlogProject
pytest
```

## Specs

Design decisions and acceptance criteria for each feature live under `BlogProject/openspec/specs/` (`article-creation`, `article-search`, `interface-design`, `production-deployment`, `user-auth`).

## Deployment (Render.com)

This project is built for production use and is actually deployed on Render.com.

- **Live Demo URL:** [https://the-blogs.onrender.com](https://the-blogs.onrender.com)

### Environment Variables

Security-related settings are externalized as environment variables via `django-environ`. Set the following in production (e.g. the Render dashboard):

- `DEBUG`: `False` in production (to prevent source code leaks)
- `SECRET_KEY`: A sufficiently random key (never commit this to Git)
- `ALLOWED_HOSTS`: `the-blogs.onrender.com,127.0.0.1` (adjust to your deployed domain)

### Build & Start Commands

- **Root Directory:** `BlogProject`
- **Build Command:**
  ```bash
  pip install -r requirements.txt && python manage.py migrate --noinput && python manage.py seed_articles && python manage.py collectstatic --noinput
  ```
- **Start Command:** (runs Gunicorn as the WSGI server)
  ```bash
  gunicorn BlogProject.wsgi:application
  ```

### Production Constraints & Future Plans

- **Static files:** served directly within the Django process via the WhiteNoise middleware
- **SQLite limitation:** `db.sqlite3` is no longer committed to the repo (it shouldn't be — it's a runtime artifact). Since Render's free instance has an ephemeral filesystem, every deploy starts from an empty database, so the build command runs `migrate` to create the schema and `seed_articles` (idempotent, via `get_or_create`) to repopulate demo articles. Migrating to a persistent external database such as Render PostgreSQL is planned for a permanent production setup.
