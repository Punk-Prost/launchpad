# Architecture

```text
Browser → Nginx :80 ─┬→ React static app
                     └→ /api/* → FastAPI :8000 → SQLAlchemy → PostgreSQL :5432
```

The frontend owns interactions. The backend is the source of truth for users, startups and applications. Repository classes isolate database queries; Pydantic schemas define contracts; Alembic owns schema evolution.

## Security review

- Passwords are stored only as bcrypt hashes.
- JWTs expire and contain only user ID and role.
- Ownership checks protect updates and deletes.
- Role dependencies protect founder/admin operations.
- Secrets stay in `.env`, ignored by Git.
- Production must use a strong random secret, strict CORS and rate limiting on auth endpoints.
