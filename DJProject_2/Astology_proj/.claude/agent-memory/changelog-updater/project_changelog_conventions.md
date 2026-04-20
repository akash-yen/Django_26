---
name: Project Changelog Conventions
description: CHANGELOG.md format, versioning style, and file location for the Astology_proj Django project
type: project
---

The project uses date-based versioning (YYYY-MM-DD), not semantic versioning (no v1.0.0 style tags).

CHANGELOG.md lives at the project root: `C:\Users\akash\Documents\Django_2026\DJProject_2\Astology_proj\CHANGELOG.md`

Format follows Keep a Changelog conventions with sections: Added, Changed, Fixed, Removed, Deprecated, Security. Only sections with relevant changes are included per entry.

The two git commits in history so far:
- `72d7334` (2026-04-10) — Initial Commit: full project scaffolding
- `babbedd` (2026-04-15) — MySQL migration, ZodiacSign + DailyPrediction models, admin registrations, CLAUDE.md, home.html fix

**Why:** Project has no explicit versioning scheme — date stamps are the natural choice given commit message style.
**How to apply:** Always use YYYY-MM-DD headers for new changelog sections; prepend new entries above older ones below the header block.
