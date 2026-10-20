@echo off
cd /d "%~dp0backend"
set DATABASE_URL=sqlite:///./launchpad.db
set JWT_SECRET=local-launchpad-secret-change-before-publishing
call .venv\Scripts\python.exe -m app.seed
call .venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8000
