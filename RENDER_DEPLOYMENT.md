# 🚀 Render Deployment Guide - StudyHub Backend

Complete guide to deploy your Django backend on Render.

## 🎯 Why Render?

- ✅ **Free tier available** (750 hours/month)
- ✅ **PostgreSQL database included** (free tier)
- ✅ **Easy Django deployment**
- ✅ **Auto deploys from GitHub**
- ✅ **Free SSL certificates**
- ✅ **No credit card required for free tier**

---

## 📋 Step-by-Step Deployment

### Step 1: Prepare Your Repository

Your code is already on GitHub: https://github.com/SHASHIYA06/study_hub

We need to create a `build.sh` file for Render.

#### Create `backend/build.sh`:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py seed_data
```

#### Update `backend/requirements.txt`:

Add these if not present:
```txt
gunicorn==21.2.0
whitenoise==6.6.0
dj-database-url==2.1.0
psycopg2-binary==2.9.9
```

---

### Step 2: Sign Up on Render

1. Go to: **https://render.com**
2. Click **"Get Started for Free"**
3. Sign up with GitHub (recommended)
4. Authorize Render to access your repositories

---

### Step 3: Create PostgreSQL Database

1. In Render Dashboard, click **"New +"**
2. Select **"PostgreSQL"**
3. Fill in:
   - **Name:** `studyhub-db`
   - **Database:** `studyhub`
   - **User:** `studyhub_user`
   - **Region:** Choose closest to you
   - **Plan:** Free
4. Click **"Create Database"**
5. **Copy the Internal Database URL** (we'll use this later)

It looks like:
```
postgresql://studyhub_user:password@dpg-xxx-internal/studyhub
```

---

### Step 4: Create Web Service

1. Click **"New +"** → **"Web Service"**
2. Select **"Build and deploy from a Git repository"**
3. Click **"Connect account"** if needed
4. Find and select: **SHASHIYA06/study_hub**
5. Click **"Connect"**

---

### Step 5: Configure Web Service

Fill in these settings:

| Setting | Value |
|---------|-------|
| **Name** | `studyhub-backend` |
| **Region** | Same as database |
| **Branch** | `main` |
| **Root Directory** | `backend` |
| **Runtime** | `Python 3` |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn study_hub.wsgi:application` |
| **Plan** | `Free` |

---

### Step 6: Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Add these variables:

```env
# Database (use Internal Database URL from Step 3)
DATABASE_URL=postgresql://studyhub_user:password@dpg-xxx-internal/studyhub

# Python version
PYTHON_VERSION=3.11.0

# Django settings
SECRET_KEY=your-super-secret-key-change-this
DEBUG=False
ALLOWED_HOSTS=.onrender.com
DISABLE_COLLECTSTATIC=1

# API Keys
YOUTUBE_API_KEY=your_youtube_api_key
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM

# CORS (we'll update this after deploying frontend)
CORS_ALLOWED_ORIGINS=https://study-hub-frontend.vercel.app,http://localhost:3000
```

---

### Step 7: Deploy!

1. Click **"Create Web Service"**
2. Render will:
   - Clone your repository
   - Install dependencies
   - Run migrations
   - Seed database
   - Start your app

**Deployment takes 5-7 minutes.**

Watch the logs to see progress.

---

### Step 8: Get Your Backend URL

After deployment succeeds, you'll get a URL like:
```
https://studyhub-backend.onrender.com
```

**Test it:**
```bash
curl https://studyhub-backend.onrender.com/api/grades/
```

Should return JSON with grades!

---

## 🔧 Post-Deployment Configuration

### Create Superuser

1. In Render Dashboard → your service
2. Click **"Shell"** tab
3. Run:
```bash
python manage.py createsuperuser
```

Follow prompts to create admin user.

### Run Additional Commands

In the Shell:
```bash
# Check migrations
python manage.py showmigrations

# Create more data
python manage.py seed_data

# Check database
python manage.py dbshell
```

---

## 🔄 Auto-Deploy from GitHub

Render automatically deploys when you push to GitHub:

```bash
cd study_hub
# Make changes
git add .
git commit -m "Update backend"
git push origin main
# Render auto-deploys!
```

---

## 📊 Monitoring

### View Logs

In Render Dashboard:
- Click your service
- Go to **"Logs"** tab
- See real-time logs

### Metrics

In Render Dashboard:
- **"Metrics"** tab shows:
  - CPU usage
  - Memory usage
  - Request count

---

## 🐛 Troubleshooting

### Issue: Build fails

**Solution:**
```bash
# Check build.sh has execute permissions
chmod +x backend/build.sh
git add backend/build.sh
git commit -m "Make build.sh executable"
git push origin main
```

### Issue: Database connection fails

**Solution:**
- Use **Internal Database URL** (not External)
- Format: `postgresql://user:pass@dpg-xxx-internal/db`

### Issue: Static files not loading

**Solution:**
Add to `settings.py`:
```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Issue: CORS errors

**Solution:**
Update `CORS_ALLOWED_ORIGINS` in environment variables:
```
https://your-frontend.vercel.app,http://localhost:3000
```

---

## 💰 Render Pricing

### Free Tier:
- **Web Services:** 750 hours/month (one always-on service)
- **PostgreSQL:** 90 days free, then $7/month
- **Storage:** 1GB
- **Bandwidth:** 100GB/month

### Paid Tiers:
- **Starter:** $7/month (PostgreSQL)
- **Standard:** $25/month (better performance)

**Recommendation:** Start with free tier, upgrade if needed.

---

## 🔒 Security Best Practices

1. **Change SECRET_KEY:**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **Set DEBUG=False** in production

3. **Use environment variables** for all secrets

4. **Enable HTTPS** (automatic on Render)

5. **Regular backups:**
   - Render auto-backs up PostgreSQL
   - Manual backup: Dashboard → Database → Backups

---

## 📈 Scaling

### Horizontal Scaling:
```
# In Render Dashboard
Service → Settings → Instances
Increase instance count
```

### Vertical Scaling:
```
# Upgrade plan
Service → Settings → Plan
Choose higher tier
```

---

## 🔄 Database Backups

### Manual Backup:
1. Dashboard → Database
2. Click **"Backups"** tab
3. Click **"Create Backup"**

### Restore Backup:
1. Go to Backups tab
2. Click backup
3. Click **"Restore"**

---

## 🎯 Complete Deployment Checklist

- [ ] GitHub repository ready
- [ ] PostgreSQL database created on Render
- [ ] Web service configured
- [ ] Environment variables set
- [ ] Build.sh created and executable
- [ ] Deployment successful
- [ ] API endpoints working
- [ ] Superuser created
- [ ] Database seeded
- [ ] Backend URL copied for frontend
- [ ] CORS configured

---

## 🌐 Connect Frontend

After backend is deployed:

1. **Copy backend URL:** `https://studyhub-backend.onrender.com`

2. **Update frontend `.env.production`:**
   ```env
   REACT_APP_API_URL=https://studyhub-backend.onrender.com
   ```

3. **Deploy frontend to Vercel**

4. **Update CORS in Render:**
   ```
   CORS_ALLOWED_ORIGINS=https://your-frontend.vercel.app
   ```

---

## 📚 Resources

- **Render Docs:** https://render.com/docs
- **Django on Render:** https://render.com/docs/deploy-django
- **PostgreSQL Guide:** https://render.com/docs/databases
- **Your Repository:** https://github.com/SHASHIYA06/study_hub

---

## 🎉 Success!

Your Django backend is now:
- ✅ Deployed on Render
- ✅ Connected to PostgreSQL
- ✅ Auto-deploying from GitHub
- ✅ Secured with HTTPS
- ✅ Ready for production!

**Backend URL:** `https://studyhub-backend.onrender.com`

**Next:** Deploy frontend to Vercel and connect them!

---

## ⚡ Quick Commands

```bash
# Local testing
cd backend
python manage.py runserver

# Push updates
git push origin main
# Render auto-deploys!

# View logs
# Go to Render Dashboard → Logs

# Run commands
# Dashboard → Shell → Enter command
```

---

**Need help?** Check Render logs or documentation!
