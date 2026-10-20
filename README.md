# LaunchPad

LaunchPad is a portfolio-ready full-stack platform where founders publish startups, build teams, accept applications, and track milestones.

## Stack

- `legacy/`: three semantic HTML5 pages for the W2 milestone.
- `frontend/`: React, Vite, TypeScript, React Router, Zod, responsive CSS tokens, light/dark themes.
- `backend/`: FastAPI, SQLAlchemy, Alembic, PostgreSQL, JWT authentication and role checks.
- `nginx/`: reverse proxy configuration for production.
- `docker-compose.yml`: one-command local/production-like launch.
- `docs/`: architecture, API integration, deployment runbook and requirement checklist.

## Quick start with Docker

```bash
cp .env.example .env
docker compose up --build
```

Open <http://localhost>. API documentation is at <http://localhost/api/docs>.

Demo accounts are created by the seed script:

- `founder@launchpad.dev` / `Founder123!`
- `mentor@launchpad.dev` / `Mentor123!`
- `admin@launchpad.dev` / `Admin123!`

## Local development

Backend:

```bash
cd backend
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
alembic upgrade head
python -m app.seed
uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

## Tests

```bash
cd backend && pytest
cd frontend && npm test -- --run
```

See [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md) for traceability against all 12 milestones.
