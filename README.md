# PulseDesk

PulseDesk is an academic prototype for logging and managing IT support tickets across branches. It includes role-aware demo login, basic statistics, explainable incident pattern detection, update correlation, alerts, and CSV reports. It uses restrained red/white/black styling without official bank logos or assets.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py app.py
```

Open http://127.0.0.1:5000. The SQLite database (`support.db`) and starter users/branches are created on first run.

Demo password: `demo123` for all three accounts.

- IT Support Officer: `officer@pulsedesk.test`
- IT Supervisor: `supervisor@pulsedesk.test`
- Administrator: `admin@pulsedesk.test`

## Project shape

- `app.py`: Flask routes, SQLAlchemy models, auth, seed data, and pattern detection
- `templates/`: Bootstrap server-rendered pages
- `static/style.css`: small visual layer over Bootstrap
- `support.db`: created automatically and intentionally ignored by Git

## Generate realistic demo activity

Sign in as the Administrator and click **Generate demo activity** on the dashboard. Choose the date range, ticket volume, systems, and categories in the form. The application then creates normal SQLite records with varied branches, assignments, priorities, statuses, descriptions, deployments, and explainable alerts. A 60-ticket range over two months is a good presentation-sized starting point.
