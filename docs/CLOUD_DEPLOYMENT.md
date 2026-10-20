# Supabase + Render

## Supabase

1. Create a free Supabase project.
2. Open **Connect → ORMs → SQLAlchemy** and copy the transaction-pooler connection string.
3. Replace `[YOUR-PASSWORD]` and keep `sslmode=require` if supplied.
4. Store the result only as Render's secret `DATABASE_URL`. Never put it in Git.

The backend automatically converts `postgresql://` to SQLAlchemy's `postgresql+psycopg://` driver.

## Render free deployment

1. Push this folder to a GitHub repository.
2. In Render choose **New → Blueprint** and select the repository. `render.yaml` creates both services.
3. Set the API service `DATABASE_URL` to the Supabase pooler URL.
4. First deploy the API and copy its public URL.
5. Set frontend `VITE_API_URL` to `<API-URL>` without a trailing slash.
6. Set API `CORS_ORIGINS` to the frontend Render URL.
7. Redeploy both services and verify `/health`, `/docs`, login and the catalog.

Free Render services may sleep after inactivity, so the first request can take longer. Supabase and Render limits can change; check their current dashboards before production use.
