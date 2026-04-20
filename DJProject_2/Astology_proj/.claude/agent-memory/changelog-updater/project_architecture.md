---
name: Project Architecture Overview
description: Key structural facts about the Astology_proj Django project relevant to changelog writing
type: project
---

- Single Django app: `human_ast_app` — all prediction logic in `views.py` via `get_daily_prediction()`
- Database: MySQL (`astrology_db`, localhost:3306) — switched from SQLite in commit `babbedd`
- Models introduced in `babbedd`: `ZodiacSign` and `DailyPrediction` (with initial migration `0001_initial.py`)
- Templates in `templates/human_ast_app/` — `home.html` (predictions) and `navi.html` (luck page)
- Static assets in `static/images/` — background image `ast_back_ground_pic.png`
- URL prefix: `/astology/` for all app routes
- Companion project `DJProject_1` (firstproject) also lives in the same git repo under `DJProject_1/`

**Why:** Understanding the architecture helps accurately categorize changes (model vs. view vs. template vs. config) in future changelog entries.
**How to apply:** Check `views.py` for prediction logic changes, `models.py` + `migrations/` for data layer changes, `templates/` for UI changes, `settings.py` for config changes.
