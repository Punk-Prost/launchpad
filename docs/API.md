# API overview

FastAPI exposes interactive documentation at `/api/docs` through Nginx.

| Method | Path | Access |
|---|---|---|
| POST | `/auth/register` | Public |
| POST | `/auth/login` | Public |
| GET | `/startups` | Public |
| GET | `/startups/{slug}` | Public |
| POST | `/startups` | Founder, admin |
| PUT/DELETE | `/startups/{id}` | Owner, admin |
| POST | `/startups/{id}/applications` | Authenticated |
| GET | `/admin/users` | Admin |
