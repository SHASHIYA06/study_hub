# 🚀 Supabase + Render Deployment Guide

Using Supabase for PostgreSQL database and Render for Django hosting.

## 🎯 Why This Combination?

**Supabase (Database):**
- ✅ **Free PostgreSQL database** (500MB)
- ✅ **Auto backups**
- ✅ **Built-in auth** (optional)
- ✅ **Real-time subscriptions** (optional)
- ✅ **Great dashboard**

**Render (Django Backend):**
- ✅ **Free hosting** (750 hours/month)
- ✅ **Easy Django deployment**
- ✅ **Auto deploys from GitHub**
- ✅ **Free SSL**

**Best of both worlds!** 🌟

---

## 📋 Part 1: Setup Supabase Database

### Step 1: Create Supabase Account

1. Go to: **https://supabase.com**
2. Click **"Start your project"**
3. Sign up with GitHub (recommended)
4. Authorize Supabase

### Step 2: Create New Project

1. Click **"New project"**
2. Fill in:
   - **Name:** `StudyHub`
   - **Database Password:** Create strong password (save it!)
   - **Region:** Choose closest to you
   - **Plan:** Free
3. Click **"Create new project"**

**Wait 1-2 minutes** for database provisioning.

### Step 3: Get Database Connection String

1. In Supabase Dashboard → **Settings** (gear icon)
2. Click **"Database"** in left sidebar
3. Scroll to **"Connection string"**
4. Select **"URI"** tab
5. Copy the connection string:

```
postgresql://postgres:[YOUR-PASSWORD]@db.xxx.supabase.co:5432/postgres
```

**Replace `[YOUR-PASSWORD]` with your actual database password!**

### Step 4: Test Connection (Optional)

```bash
# Using psql
psql "postgresql://postgres:your-password@db.xxx.supabase.co:5432/postgres"

# Or using Python
python -c "import psycopg2; conn = psycopg2.connect('your-connection-string'); print('✅ Connected!')"
```

---

## 📋 Part 2: Deploy Django to Render

### Step 1: Create Build Script

Create `backend/build.sh`:

```bash
#!/usr/bin/env bash
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate

echo "Seeding database..."
python manage.py seed_data || echo "Seeding failed or already seeded"

echo "Build complete!"
```

Make it executable:
```bash
chmod +x backend/build.sh
git add backend/build.sh
git commit -m "Add Render build script"
git push origin main
```

### Step 2: Sign Up on Render

1. Go to: **https://render.com**
2. Sign up with GitHub
3. Authorize Render

### Step 3: Create Web Service

1. Dashboard → **"New +"** → **"Web Service"**
2. Connect repository: **SHASHIYA06/study_hub**
3. Configure:

| Setting | Value |
|---------|-------|
| **Name** | `studyhub-backend` |
| **Region** | Same as Supabase |
| **Branch** | `main` |
| **Root Directory** | `backend` |
| **Runtime** | `Python 3` |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn study_hub.wsgi:application` |
| **Plan** | `Free` |

### Step 4: Add Environment Variables

Click **"Advanced"** → Add these:

```env
# Supabase Database URL
DATABASE_URL=postgresql://postgres:YOUR-PASSWORD@db.xxx.supabase.co:5432/postgres

# Python
PYTHON_VERSION=3.11.0

# Django
SECRET_KEY=your-django-secret-key-generate-new-one
DEBUG=False
ALLOWED_HOSTS=.onrender.com,.vercel.app
DISABLE_COLLECTSTATIC=1

# API Keys
YOUTUBE_API_KEY=your_youtube_api_key
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM

# CORS
CORS_ALLOWED_ORIGINS=https://your-frontend.vercel.app,http://localhost:3000

# Redis (optional, for caching)
REDIS_URL=redis://red-xxx.oregon-postgres.render.com:6379
```

### Step 5: Deploy

1. Click **"Create Web Service"**
2. Wait 5-7 minutes for deployment
3. Watch logs for any errors

---

## 🔧 Configuration

### Update Django Settings for Supabase

Your `settings.py` already has:
```python
DATABASES = {
    'default': dj_database_url.parse(
        os.getenv('DATABASE_URL'),
        conn_max_age=600
    )
}
```

This works with Supabase! ✅

### SSL Configuration (if needed)

If you get SSL errors, update `settings.py`:

```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}
```

---

## 🧪 Testing

### Test Backend API

```bash
# Get your Render URL
https://studyhub-backend.onrender.com

# Test endpoints
curl https://studyhub-backend.onrender.com/api/grades/
curl https://studyhub-backend.onrender.com/api/subjects/
curl https://studyhub-backend.onrender.com/api/chapters/
```

### Test Database Connection

In Render Shell:
```bash
python manage.py dbshell
```

Should connect to Supabase!

---

## 📊 Supabase Dashboard Features

### View Tables

1. Supabase Dashboard → **"Table Editor"**
2. See all your Django tables:
   - app_grade
   - app_subject
   - app_chapter
   - etc.

### Run SQL Queries

1. Click **"SQL Editor"**
2. Run queries:

```sql
-- Count grades
SELECT COUNT(*) FROM app_grade;

-- View all subjects
SELECT * FROM app_subject;

-- Check chapters
SELECT id, title, chapter_number FROM app_chapter;
```

### Database Backups

1. Dashboard → **"Database"** → **"Backups"**
2. Daily backups (automatic on free tier)
3. Point-in-time recovery (paid tiers)

---

## 🔄 Auto-Deploy Workflow

```bash
# Make changes locally
cd study_hub

# Edit files
vim backend/app/models.py

# Commit and push
git add .
git commit -m "Update models"
git push origin main

# Render auto-deploys!
# Check Render dashboard for logs
```

---

## 🎯 Create Superuser

### Option 1: Using Render Shell

1. Render Dashboard → Your service
2. Click **"Shell"** tab
3. Run:
```bash
python manage.py createsuperuser
```

### Option 2: Using Django Admin Setup

Create a management command `backend/app/management/commands/create_superuser_if_none.py`:

```python
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                'admin',
                'admin@studyhub.com',
                'ChangeThisPassword123!'
            )
            self.stdout.write('✅ Superuser created!')
        else:
            self.stdout.write('Superuser already exists')
```

Add to `build.sh`:
```bash
python manage.py create_superuser_if_none
```

---

## 💰 Pricing

### Supabase:
- **Free:** 500MB database, 2GB bandwidth
- **Pro:** $25/month, 8GB database

### Render:
- **Free:** 750 hours/month
- **Starter:** $7/month

**Total Free:** $0/month! 🎉

---

## 🔒 Security

### Supabase Security

1. **Row Level Security (RLS):**
   ```sql
   ALTER TABLE app_grade ENABLE ROW LEVEL SECURITY;
   ```

2. **API Keys:**
   - Keep anon/public keys separate
   - Use service role key only server-side

3. **Connection pooling:**
   - Supabase handles this automatically

### Django Security

1. **Strong SECRET_KEY:**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **Environment variables** for all secrets

3. **HTTPS only** (Render provides this)

---

## 📈 Monitoring

### Supabase Monitoring

1. Dashboard → **"Database"** → **"Usage"**
2. See:
   - Database size
   - Active connections
   - API requests

### Render Monitoring

1. Dashboard → Your service → **"Metrics"**
2. See:
   - CPU usage
   - Memory usage
   - Response times

---

## 🐛 Troubleshooting

### Issue: "peer authentication failed"

**Solution:**
Use connection string with password, not peer auth:
```
postgresql://postgres:PASSWORD@db.xxx.supabase.co:5432/postgres
```

### Issue: SSL required

**Solution:**
Add `?sslmode=require` to connection string:
```
postgresql://postgres:PASSWORD@db.xxx.supabase.co:5432/postgres?sslmode=require
```

Or in `settings.py`:
```python
DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}
```

### Issue: Too many connections

**Solution:**
Use connection pooling:
```python
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,  # Keep connections alive
        pool=True
    )
}
```

### Issue: Migrations fail

**Solution:**
```bash
# In Render Shell
python manage.py migrate --fake-initial
python manage.py migrate
```

---

## 🔄 Database Management

### Backup Database

```bash
# From Supabase Dashboard
Dashboard → Database → Backups → Create backup
```

### Restore Database

```bash
# Download backup from Supabase
# Restore using psql
psql "your-supabase-url" < backup.sql
```

### Reset Database (if needed)

```bash
# In Render Shell
python manage.py flush --no-input
python manage.py migrate
python manage.py seed_data
```

---

## 🌐 Connect Frontend

### Update Frontend Environment

Create `frontend/.env.production`:
```env
REACT_APP_API_URL=https://studyhub-backend.onrender.com
```

### Deploy Frontend to Vercel

```bash
cd frontend
vercel --prod
```

Or use Vercel Dashboard:
1. Import repository
2. Set root: `frontend`
3. Add env var: `REACT_APP_API_URL`
4. Deploy!

### Update Backend CORS

In Render, update `CORS_ALLOWED_ORIGINS`:
```
https://study-hub-shashiya06.vercel.app
```

---

## ✅ Complete Checklist

- [ ] Supabase project created
- [ ] Database password saved
- [ ] Connection string copied
- [ ] Render web service created
- [ ] Environment variables set
- [ ] build.sh created and pushed
- [ ] Deployment successful
- [ ] Migrations run
- [ ] Database seeded
- [ ] Superuser created
- [ ] API endpoints tested
- [ ] Frontend connected
- [ ] CORS configured
- [ ] SSL working

---

## 🎉 Success!

Your app is now running on:

**Database:** Supabase (PostgreSQL)
**Backend:** Render (Django)
**Frontend:** Vercel (React)

**Backend URL:** `https://studyhub-backend.onrender.com`
**API Docs:** `https://studyhub-backend.onrender.com/api/`
**Admin:** `https://studyhub-backend.onrender.com/admin/`

---

## 📚 Resources

- **Supabase Docs:** https://supabase.com/docs
- **Render Django Guide:** https://render.com/docs/deploy-django
- **Your Repo:** https://github.com/SHASHIYA06/study_hub

---

## 🚀 Quick Start Commands

```bash
# Test locally with Supabase
export DATABASE_URL="postgresql://postgres:password@db.xxx.supabase.co:5432/postgres"
python manage.py migrate
python manage.py runserver

# Deploy to Render
git push origin main
# Auto-deploys!

# Create superuser
# Render Dashboard → Shell
python manage.py createsuperuser
```

---

**Your StudyHub is now LIVE with Supabase + Render!** 🎓✨
