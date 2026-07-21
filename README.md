# 【blog】

## Overview
【このプロジェクトの一言説明】

## Environment
- Python 3.13
- uv (package manager)

## Tools
- **ruff**: formatting and linting
- **pytest**: testing
- **pytest-cov**: coverage measurement

## Setup
```bash
uv sync
```

## Usage
```bash
uv run main.py
```

## Deployment

This project is prepared for a production-ready environment and is successfully deployed on **Render.com**.

- **Live Demo URL:** [https://the-blogs.onrender.com](https://the-blogs.onrender.com)

### Environment Variables

The application relies on `django-environ` for security configuration. The following environment variables must be configured in the production environment (e.g., Render Dashboard):

- `DEBUG`: Set to `False` in production to prevent source code leaks.
- `SECRET_KEY`: A secure, randomly generated key for cryptographic signing (do not commit this key to Git).
- `ALLOWED_HOSTS`: Set to `the-blogs.onrender.com,127.0.0.1` (or your corresponding host domains).

### Production Build & Launch

- **Root Directory:** `BlogProject`
- **Build Command:**
  ```bash
  uv pip install -r pyproject.toml && python manage.py migrate && python manage.py collectstatic --noinput
  ```
- **Start Command:** Runs Gunicorn as the WSGI application server:
  ```bash
  gunicorn BlogProject.wsgi:application --bind 0.0.0.0:$PORT
  ```

### Production Constraints & Future Database Planning

- **Static Files:** Served efficiently using WhiteNoise middleware directly through the Django process.
- **SQLite Database Limitation:** This service currently uses SQLite (`db.sqlite3`). Because Render's free instance has an ephemeral file system, data will reset on every redeployment. For a permanent production environment, migrating to an external database like Render PostgreSQL is planned for future phases.