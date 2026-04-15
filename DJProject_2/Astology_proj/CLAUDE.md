# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the development server
python manage.py runserver

# Apply migrations
python manage.py migrate

# Run tests
python manage.py test human_ast_app
```

## URL Structure

All app routes are prefixed with `/astology/` via the root `urls.py`:

| URL | View | Template |
|-----|------|----------|
| `/astology/home/` | `views.home` | `home.html` |
| `/astology/luck/` | `views.another` | `navi.html` |

When linking between pages inside templates, always use the full `/astology/<path>/` prefix, not relative paths like `../home` or bare filenames like `navi.html`.

## Architecture

- **`Astology_proj/`** — project config package (`settings.py`, root `urls.py`)
- **`human_ast_app/`** — the sole Django app; contains `views.py`, `urls.py`, `models.py`
- **`templates/human_ast_app/`** — all HTML templates; resolved via `TEMPLATE_DIR = BASE_DIR / 'templates'` in settings
- **`static/images/`** — static assets; served via `STATICFILES_DIRS = [BASE_DIR / 'static']`

All prediction logic lives entirely in `human_ast_app/views.py` — there are no models or database tables in use. `get_daily_prediction()` builds a random prediction dict that is passed as `{{ prediction }}` context to `home.html`.

Templates use Tailwind CSS (CDN) and Google Fonts (Cinzel + Quicksand). The background image is loaded via `{% static %}` in `home.html`.
