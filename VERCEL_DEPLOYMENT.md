# 🚀 Vercel Deployment Guide - StudyHub

Complete guide to deploy StudyHub on Vercel (Free tier available).

## 🎯 Overview

Vercel is great for:
- ✅ Frontend (React) - Perfect fit
- ⚠️ Backend (Django) - Limited (serverless functions)
- 💡 Recommended: Deploy frontend on Vercel, backend elsewhere

## 📋 Option 1: Frontend Only on Vercel (Recommended)

### Step 1: Prepare Frontend for Vercel

1. **Update API URL in frontend**

Create `frontend/.env.production`:
```env
REACT_APP_API_URL=https://your-backend-url.com
```

2. **Create `vercel.json` in frontend folder**

```json
{
  "version": 2,
  "name": "studyhub-frontend",
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "build"
      }
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
```

### Step 2: Deploy Frontend to Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy frontend
cd frontend
vercel --prod
```

Or use Vercel Dashboard:
1. Go to https://vercel.com/new
2. Import your GitHub repository
3. Select `frontend` as root directory
4. Click Deploy

### Step 3: Deploy Backend Separately

**Recommended platforms for Django backend:**
- **Railway** (easiest): https://railway.app
- **Render**: https://render.com
- **Heroku**: https://heroku.com
- **AWS EC2**: Full control

## 📋 Option 2: Full Stack on Vercel (Advanced)

⚠️ Note: Vercel serverless functions have limitations for Django.

### Configuration Files Created:

1. **Root `vercel.json`** - Already created
2. **`backend/vercel_build.sh`** - Build script

### Deploy Full Stack:

```bash
# From project root
vercel --prod
```

### Set Environment Variables:

In Vercel Dashboard → Settings → Environment Variables:

| Variable | Value |
|----------|-------|
| `YOUTUBE_API_KEY` | Your YouTube API key |
| `GOOGLE_GEMINI_API_KEY` | AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM |
| `SECRET_KEY` | Your Django secret key |
| `DATABASE_URL` | PostgreSQL connection string |
| `DEBUG` | False |
| `ALLOWED_HOSTS` | .vercel.app |

## 🎯 Recommended: Hybrid Deployment

### Best Architecture:

1. **Frontend on Vercel** (Free, fast, CDN)
2. **Backend on Railway** (Free tier, easy Django hosting)
3. **Database on Railway** (PostgreSQL included)

### Setup:

#### 1. Deploy Backend to Railway:

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize
cd backend
railway init

# Deploy
railway up
```

Add environment variables in Railway dashboard.

#### 2. Deploy Frontend to Vercel:

```bash
# Update .env.production with Railway backend URL
echo "REACT_APP_API_URL=https://your-backend.railway.app" > frontend/.env.production

# Deploy to Vercel
cd frontend
vercel --prod
```

## 📝 Vercel-Specific Files

### Frontend `package.json` update:

```json
{
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "vercel-build": "npm run build"
  }
}
```

### Root `.vercelignore`:

```
node_modules
.git
.env
.env.local
__pycache__
*.pyc
db.sqlite3
```

## 🔧 Configuration for Vercel

### Update CORS in Django:

```python
# backend/study_hub/settings.py

CORS_ALLOWED_ORIGINS = [
    'https://your-frontend.vercel.app',
    'http://localhost:3000',  # For development
]

ALLOWED_HOSTS = [
    'your-backend.railway.app',
    '.vercel.app',
    'localhost',
]
```

## 📊 Architecture Diagram

```
┌─────────────────┐
│   Vercel CDN    │  ← Frontend (React)
│   (Global)      │     Fast, Free, Scalable
└────────┬────────┘
         │ API Calls
         ↓
┌─────────────────┐
│   Railway       │  ← Backend (Django + PostgreSQL)
│   (US/EU)       │     Free tier, Easy setup
└─────────────────┘
```

## 💰 Cost Comparison

| Platform | Frontend | Backend | Database | Cost/Month |
|----------|----------|---------|----------|------------|
| **Vercel + Railway** | ✅ Free | ✅ Free | ✅ Free | $0 |
| **Vercel Only** | ✅ Free | ⚠️ Limited | ❌ No DB | $0 |
| **All Railway** | ✅ Free | ✅ Free | ✅ Free | $0 |

## 🚀 Quick Deploy Commands

### Deploy Frontend to Vercel:
```bash
cd frontend
vercel --prod
```

### Deploy Backend to Railway:
```bash
cd backend
railway up
```

## 🔐 Environment Variables Setup

### Vercel (Frontend):
```env
REACT_APP_API_URL=https://your-backend.railway.app
```

### Railway (Backend):
```env
YOUTUBE_API_KEY=your_key
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
SECRET_KEY=your_secret
DEBUG=False
ALLOWED_HOSTS=.railway.app
DATABASE_URL=postgresql://... (auto-provided by Railway)
```

## ✅ Deployment Checklist

- [ ] GitHub repository updated
- [ ] Frontend builds successfully
- [ ] Backend tested locally
- [ ] Environment variables configured
- [ ] CORS settings updated
- [ ] API URL updated in frontend
- [ ] Database migrations ready
- [ ] Static files collected
- [ ] Domain configured (optional)

## 🐛 Troubleshooting

### Frontend can't reach backend:
```bash
# Check CORS settings in Django
# Verify REACT_APP_API_URL is correct
# Check network tab in browser DevTools
```

### Build fails on Vercel:
```bash
# Check build logs
# Verify package.json scripts
# Check Node.js version compatibility
```

### Backend issues on Vercel:
```bash
# Django on Vercel has limitations
# Consider using Railway instead
# Or use Vercel only for frontend
```

## 📚 Resources

- **Vercel Docs**: https://vercel.com/docs
- **Railway Docs**: https://docs.railway.app
- **GitHub Repo**: https://github.com/SHASHIYA06/study_hub

## 🎯 Recommended Approach

**Best setup for StudyHub:**

1. ✅ **Push to GitHub** (we'll do this first)
2. ✅ **Deploy frontend to Vercel** (fast, free)
3. ✅ **Deploy backend to Railway** (easy Django hosting)
4. ✅ **Connect them** (update API URL)

This gives you:
- Fast global CDN (Vercel)
- Full Django support (Railway)
- PostgreSQL database (Railway)
- Free tier for both
- Easy to scale

---

**Next Step:** Let's push to GitHub first, then deploy! 🚀
