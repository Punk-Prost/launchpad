# VPS deployment runbook

## Prerequisites

Ubuntu 24.04 VPS, a domain pointed to it, Docker Engine with Compose, and ports 80/443 open.

## Deploy

1. Clone into `/opt/launchpad`.
2. Copy `.env.example` to `.env`; replace the password and `JWT_SECRET`.
3. Run `docker compose up -d --build`.
4. Check `docker compose ps` and `curl http://127.0.0.1/api/health`.
5. Add HTTPS with `sudo certbot --nginx -d launchpad.example.com`.

## Operations

```bash
docker compose logs -f api
docker compose exec api alembic upgrade head
docker compose up -d --build
docker compose exec db pg_dump -U launchpad launchpad > backup.sql
```

To roll back, check out the previous release tag and rebuild. Database downgrade scripts must be tested before production rollback.
