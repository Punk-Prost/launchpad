# LaunchPad: guide to every project file

## Root

- `.env.example` — template for database, JWT, CORS and frontend API variables. Copy to `.env`; never commit real secrets.
- `.gitignore` — excludes secrets, dependencies, builds, virtual environments and caches.
- `README.md` — overview, commands, demo credentials and entry point for contributors.
- `docker-compose.yml` — starts PostgreSQL, FastAPI, the built React app and Nginx together.
- `render.yaml` — free Render Blueprint for the public API and static frontend.
- `start-backend.cmd` — Windows shortcut: selects SQLite, seeds it and starts FastAPI on port 8000.
- `start-frontend.cmd` — Windows shortcut: installs missing packages and starts Vite on port 5173.
- `START-HERE.txt` — minimal local launch instructions.

## `frontend/`

- `package.json` — npm dependencies and the `dev`, `build`, `test`, `lint` scripts.
- `package-lock.json` — exact installed JavaScript versions for repeatable builds.
- `index.html` — the single HTML shell where React mounts into `#root`.
- `vite.config.ts` — Vite, React, Vitest and local `/api` proxy configuration.
- `tsconfig.json` — TypeScript project entry and reference to app settings.
- `tsconfig.app.json` — strict browser/React TypeScript compiler rules.
- `Dockerfile` — builds React with Node, then serves `dist` through Nginx.
- `nginx.conf` — SPA fallback so direct routes open `index.html`.

### `frontend/src/`

- `main.tsx` — browser entry: mounts `App` inside `BrowserRouter`.
- `App.tsx` — global layout, navigation, theme switcher and route table.
- `api.ts` — typed HTTP client, JWT header and cancellation of previous requests.
- `types.ts` — shared `Startup`, `User` and `Stage` TypeScript contracts.
- `data.ts` — fallback demo startups shown when the API is unavailable.
- `styles.css` — design tokens, layout, components, two themes and responsive breakpoints.
- `vite-env.d.ts` — Vite types for `import.meta.env`.

### Components and pages

- `components/StartupCard.tsx` — reusable startup preview card.
- `components/StartupCard.test.tsx` — component content and link tests.
- `pages/Home.tsx` — hero, metrics, featured projects and positioning section.
- `pages/Catalog.tsx` — API loading and client-side search/industry/stage filters.
- `pages/Details.tsx` — startup profile, roles, roadmap and application form.
- `pages/Auth.tsx` — Zod-validated login and token persistence.
- `pages/Dashboard.tsx` — founder workspace UI; its metrics are currently demo content.

## `backend/`

- `requirements.txt` — pinned FastAPI, SQLAlchemy, PostgreSQL, JWT and test libraries.
- `Dockerfile` — Python API container.
- `alembic.ini` — Alembic command and logging configuration.
- `launchpad.db` — local SQLite data file; only present after local setup.

### `backend/app/`

- `__init__.py` — marks the folder as a Python package.
- `config.py` — environment settings and Supabase PostgreSQL URL normalization.
- `database.py` — SQLAlchemy engine, sessions and declarative base.
- `models.py` — database tables, enums, relationships and constraints.
- `schemas.py` — validated API request/response DTOs.
- `security.py` — bcrypt hashing, JWT creation, current-user and role dependencies.
- `repositories.py` — isolated startup listing and creation database queries.
- `main.py` — FastAPI app, CORS and all REST endpoints.
- `seed.py` — idempotently creates demo accounts and startups in an empty database.

### Database migration and tests

- `alembic/env.py` — connects Alembic to the configured database and model metadata.
- `alembic/script.py.mako` — template for future migration files.
- `alembic/versions/0001_initial.py` — creates users, startups, applications, enums and indexes.
- `tests/conftest.py` — isolated SQLite test database and reusable fixtures.
- `tests/test_api.py` — 12 auth, permissions, CRUD and application API tests.

## Other folders

- `legacy/index.html` — semantic project catalog page for the HTML milestone.
- `legacy/about.html` — semantic platform explanation page.
- `legacy/contact.html` — accessible contact form page.
- `legacy/styles.css` — responsive styles shared by the legacy pages.
- `nginx/default.conf` — production reverse proxy: `/api` to FastAPI, everything else to React.
- `docs/API.md` — endpoint and access-level summary.
- `docs/ARCHITECTURE.md` — system flow and security review.
- `docs/DEPLOYMENT.md` — Docker/VPS operations runbook.
- `docs/CLOUD_DEPLOYMENT.md` — Supabase and Render deployment instructions.
- `docs/REQUIREMENTS.md` — traceability from all 12 coursework requirements to files.
- `docs/FILE_GUIDE.md` — this file-by-file explanation.
