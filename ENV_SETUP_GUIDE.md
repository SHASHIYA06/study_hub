# 🔐 Environment Variables Setup Guide

Complete guide for setting up environment variables for deployment.

---

## 📋 Backend Environment Variables

### For Render Deployment

In Render Dashboard → Your Service → Environment:

```env
# Python Version
PYTHON_VERSION=3.11.0

# Database (Render provides this automatically when you add PostgreSQL)
DATABASE_URL=postgresql://user:password@host/database

# Django Settings
SECRET_KEY=your-generated-secret-key-here
DEBUG=False
ALLOWED_HOSTS=.onrender.com,.vercel.app
DISABLE_COLLECTSTATIC=1

# API Keys
YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY_HERE
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM

# CORS (Update after deploying frontend)
CORS_ALLOWED_ORIGINS=https://your-frontend-name.vercel.app,http://localhost:3000
```

---

### For Supabase + Render Deployment

**Step 1: Get Supabase Database URL**

1. Go to Supabase Dashboard → Settings → Database
2. Copy the Connection String (URI format)
3. It looks like: `postgresql://postgres:[PASSWORD]@db.xxx.supabase.co:5432/postgres`
4. Replace `[PASSWORD]` with your actual database password

**Step 2: Set in Render**

```env
# Python Version
PYTHON_VERSION=3.11.0

# Supabase Database URL
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@db.xxx.supabase.co:5432/postgres

# Django Settings
SECRET_KEY=your-generated-secret-key-here
DEBUG=False
ALLOWED_HOSTS=.onrender.com,.vercel.app
DISABLE_COLLECTSTATIC=1

# API Keys
YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY_HERE
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM

# CORS (Update after deploying frontend)
CORS_ALLOWED_ORIGINS=https://your-frontend-name.vercel.app,http://localhost:3000
```

---

## 🎯 How to Get YouTube API Key

### Step 1: Create Google Cloud Project

1. Go to: https://console.cloud.google.com/
2. Click **"Select a project"** → **"New Project"**
3. Name: **"StudyHub"**
4. Click **"Create"**

### Step 2: Enable YouTube Data API v3

1. In Google Cloud Console, click **"☰ Menu"**
2. Go to **"APIs & Services"** → **"Library"**
3. Search: **"YouTube Data API v3"**
4. Click on it
5. Click **"Enable"**

### Step 3: Create API Key

1. Go to **"APIs & Services"** → **"Credentials"**
2. Click **"+ Create Credentials"** → **"API Key"**
3. Your API key will be generated
4. **Copy it immediately!**
5. (Optional) Click **"Restrict Key"** for security:
   - API restrictions → Select **"YouTube Data API v3"**
   - Application restrictions → Select **"HTTP referrers"** or **"None"**

### Step 4: Use the API Key

Copy your API key and use it as `YOUTUBE_API_KEY` in your environment variables.

**Example:**
```env
YOUTUBE_API_KEY=AIzaSyDxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🔑 Generate Django SECRET_KEY

### Method 1: Using Python

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and use it as `SECRET_KEY`.

### Method 2: Using Online Generator

Visit: https://djecrety.ir/

Click "Generate" and copy the key.

---

## 🌐 Frontend Environment Variables

### For Vercel Deployment

In Vercel Dashboard → Your Project → Settings → Environment Variables:

```env
REACT_APP_API_URL=https://your-backend-name.onrender.com
```

**Important:** Replace `your-backend-name` with your actual Render service URL!

---

## 📝 Step-by-Step Environment Setup

### For Render Backend:

1. **Deploy backend to Render first** (follow RENDER_DEPLOYMENT.md)
2. **Add PostgreSQL database** in Render
3. **Set these environment variables:**
   ```env
   PYTHON_VERSION=3.11.0
   DATABASE_URL=[Auto-filled by Render]
   SECRET_KEY=[Generate new one]
   DEBUG=False
   ALLOWED_HOSTS=.onrender.com,.vercel.app
   YOUTUBE_API_KEY=[Your YouTube API key]
   GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
   CORS_ALLOWED_ORIGINS=http://localhost:3000
   ```
4. **Deploy!**
5. **Copy your backend URL:** `https://studyhub-backend.onrender.com`

### For Vercel Frontend:

1. **Go to Vercel** (https://vercel.com/new)
2. **Import your GitHub repo**
3. **Set root directory:** `frontend`
4. **Add environment variable:**
   ```env
   REACT_APP_API_URL=https://studyhub-backend.onrender.com
   ```
5. **Deploy!**
6. **Copy your frontend URL:** `https://studyhub.vercel.app`

### Update Backend CORS:

1. **Go back to Render**
2. **Update `CORS_ALLOWED_ORIGINS`:**
   ```env
   CORS_ALLOWED_ORIGINS=https://studyhub.vercel.app,http://localhost:3000
   ```
3. **Redeploy backend**

---

## ✅ Complete Environment Checklist

### Backend (Render):
- [ ] `PYTHON_VERSION` = 3.11.0
- [ ] `DATABASE_URL` = Set (auto or Supabase)
- [ ] `SECRET_KEY` = Generated
- [ ] `DEBUG` = False
- [ ] `ALLOWED_HOSTS` = .onrender.com,.vercel.app
- [ ] `YOUTUBE_API_KEY` = Your key
- [ ] `GOOGLE_GEMINI_API_KEY` = AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
- [ ] `CORS_ALLOWED_ORIGINS` = Your Vercel URL

### Frontend (Vercel):
- [ ] `REACT_APP_API_URL` = Your Render backend URL

---

## 🔒 Security Best Practices

1. **Never commit `.env` files** (already in .gitignore ✅)
2. **Use different SECRET_KEY** for production
3. **Set DEBUG=False** in production
4. **Restrict API keys** to specific domains
5. **Use HTTPS** (automatic on Render & Vercel ✅)
6. **Rotate keys** if compromised

---

## 🐛 Troubleshooting

### Issue: "YOUTUBE_API_KEY not configured"

**Solution:**
1. Verify key is set in Render environment variables
2. Check spelling: `YOUTUBE_API_KEY` (all caps, underscore)
3. Restart Render service after adding
4. Check logs: `render logs`

### Issue: "CORS error" in browser

**Solution:**
1. Verify `CORS_ALLOWED_ORIGINS` includes your Vercel URL
2. Make sure URL has `https://` (not `http://`)
3. No trailing slash: `https://app.vercel.app` ✅
4. With trailing slash: `https://app.vercel.app/` ❌

### Issue: Frontend can't reach backend

**Solution:**
1. Check `REACT_APP_API_URL` in Vercel
2. Verify backend is deployed and running
3. Test backend: `curl https://your-backend.onrender.com/api/grades/`
4. Check browser console for errors

---

## 📊 Example Production Setup

### Backend on Render:
```env
PYTHON_VERSION=3.11.0
DATABASE_URL=postgresql://user:pass@host/db
SECRET_KEY=django-insecure-a1b2c3d4e5f6g7h8i9j0
DEBUG=False
ALLOWED_HOSTS=.onrender.com,.vercel.app
YOUTUBE_API_KEY=AIzaSyDxxxxxxxxxxxxxxxxxxxxxxx
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
CORS_ALLOWED_ORIGINS=https://studyhub-frontend.vercel.app
```

### Frontend on Vercel:
```env
REACT_APP_API_URL=https://studyhub-backend.onrender.com
```

---

## 🎯 Quick Reference

| Variable | Where | Value |
|----------|-------|-------|
| `YOUTUBE_API_KEY` | Render | Get from Google Cloud Console |
| `GOOGLE_GEMINI_API_KEY` | Render | AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM |
| `SECRET_KEY` | Render | Generate new random key |
| `DATABASE_URL` | Render | Auto-filled or Supabase URL |
| `CORS_ALLOWED_ORIGINS` | Render | Your Vercel frontend URL |
| `REACT_APP_API_URL` | Vercel | Your Render backend URL |

---

## 🚀 Deployment Order

1. ✅ Get YouTube API key
2. ✅ Deploy backend to Render (with env vars)
3. ✅ Copy backend URL
4. ✅ Deploy frontend to Vercel (with backend URL)
5. ✅ Copy frontend URL
6. ✅ Update backend CORS with frontend URL
7. ✅ Test your live app! 🎉

---

## 📞 Need Help?

- **YouTube API:** https://console.cloud.google.com/apis/credentials
- **Generate SECRET_KEY:** https://djecrety.ir/
- **Render Docs:** https://render.com/docs
- **Vercel Docs:** https://vercel.com/docs

---

**Ready to deploy? Follow the deployment guide and use these environment variables!** 🚀
