# Changelog

All notable changes to this project will be documented in this file.
This project adheres to [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2026-04-15]

### Added
- `ZodiacSign` model with fields for name, symbol, element (Fire/Earth/Air/Water), ruling planet, date range, and optional description
- `DailyPrediction` model linked to `ZodiacSign` via foreign key, storing per-sign daily predictions across love, career, health, and overall categories, plus lucky number and lucky color
- Initial database migration (`0001_initial.py`) creating both new tables with a unique-together constraint on `(zodiac_sign, date)`
- Django admin registration for `ZodiacSign` with list display, element filter, and name/planet search
- Django admin registration for `DailyPrediction` with list display, sign/date filters, search by sign name, and descending date ordering
- `CLAUDE.md` project guidance file documenting commands, URL structure, and architecture for AI-assisted development

### Changed
- Database backend switched from SQLite to MySQL (`astrology_db` on localhost:3306)
- Moved `{% load static %}` tag to the top of `home.html`, above the `<!DOCTYPE html>` declaration, to follow Django template best practices

---

## [2026-04-10]

### Added
- Initial project setup for `DJProject_2` Django astrology application
- `human_ast_app` Django app with `views.py` containing `get_daily_prediction()` for random prediction generation
- URL routing under the `/astology/` prefix with `home/` and `luck/` endpoints
- `home.html` template rendering daily predictions with Tailwind CSS and Google Fonts (Cinzel + Quicksand)
- `navi.html` template for the luck/navigation page
- Background image static asset (`ast_back_ground_pic.png`)
- Companion `DJProject_1` Django project (`firstproject`) with `testapp` and `secondapp` apps included in the same repository
