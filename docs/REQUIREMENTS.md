# Requirement traceability

| # | Milestone | Implementation |
|---|---|---|
| 1 | Semantic HTML5 | `legacy/index.html`, `about.html`, `contact.html`; landmarks, labels, accessible navigation |
| 2 | Responsive CSS and tokens | CSS tokens; breakpoints at 620/900px plus desktop; light/dark themes |
| 3 | JavaScript catalog | Search, industry/stage filters; theme and session in `localStorage` |
| 4 | External REST API | Typed API layer; loading, ready, empty and fallback states; `AbortController` cancellation |
| 5 | React, Vite, TypeScript | Typed component tree in `frontend/src`; Vite build |
| 6 | Router, forms, validation | Five routes, forms and Zod login validation |
| 7 | FastAPI CRUD | Startup CRUD, applications, auth and generated OpenAPI docs |
| 8 | PostgreSQL, SQLAlchemy, migrations | Relational schema, repository layer and Alembic migration |
| 9 | JWT auth and authorization | JWT, password hashing, four roles and protected endpoints |
| 10 | Full-stack and testing | API client, 12 backend tests + 2 frontend tests, `.env.example` |
| 11 | Containers | Multi-stage Dockerfiles, Compose and database healthcheck |
| 12 | VPS and Nginx | Reverse proxy and deployment runbook |

## Component tree

```text
App
├── Header / theme switcher
├── Home → StartupCard[]
├── Catalog → Filters + StartupCard[]
├── Details → Roadmap + ApplicationForm
├── Auth
├── Dashboard
└── Footer
```

The catalog models loading, ready, empty and error-safe fallback behavior. The API layer cancels the previous in-flight request through `AbortController`.
