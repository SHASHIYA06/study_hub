# 🔧 Render Deployment Fix

## ❌ Error: "no such file or directory: Dockerfile"

This error happens because Render is set to "Docker" mode, but we need "Native Environment" mode.

---

## ✅ Solution: Configure Render Correctly

### Step 1: Delete Current Service (if created)

1. Go to Render Dashboard
2. Click your service (if exists)
3. Settings → Scroll down → "Delete Web Service"

### Step 2: Create Service with Correct Settings

1. **Click:** "New +" → "Web Service"
2. **Select:** "Build and deploy from a Git repository"
3. **Connect:** `SHASHIYA06/study_hub`
4. **Configure EXACTLY as below:**

| Setting | Value |
|---------|-------|
| **Name** | `studyhub-backend` |
| **Region** | Oregon (US West) or closest |
| **Branch** | `main` |
| **Root Directory** | `backend` |
| **Environment** | `Python 3` ⚠️ (NOT Docker!) |
| **Build Command** | `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate` |
| **Start Command** | `gunicorn study_hub.wsgi:application` |
| **Plan** | `Free` |

⚠️ **IMPORTANT:** Make sure "Environment" is set to **"Python 3"** NOT "Docker"!

---

### Step 3: Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Add these ONE BY ONE:

```env
PYTHON_VERSION=3.11.0
```

```env
SECRET_KEY=django-insecure-change-this-to-random-key
```
(Generate at https://djecrety.ir/)

```env
DEBUG=False
```

```env
ALLOWED_HOSTS=.onrender.com,.vercel.app
```

```env
DISABLE_COLLECTSTATIC=1
```

```env
YOUTUBE_API_KEY=AIzaSyAU1vqMfV64ZaNRHzHD0qtSMDXuW5XZoMc
```

```env
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
```

```env
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

---

### Step 4: Add PostgreSQL Database

1. In Render Dashboard, click **"New +"**
2. Select **"PostgreSQL"**
3. **Name:** `studyhub-db`
4. **Plan:** `Free`
5. Click **"Create Database"**
6. Wait 1 minute for provisioning
7. **Copy Internal Database URL** (looks like `postgresql://user:pass@dpg-xxx-internal/database`)

---

### Step 5: Add DATABASE_URL to Web Service

1. Go back to your **Web Service**
2. Click **"Environment"** in sidebar
3. Click **"Add Environment Variable"**
4. Add:
   ```
   Name: DATABASE_URL
   Value: [paste your Internal Database URL]
   ```

---

### Step 6: Deploy

1. Click **"Manual Deploy"** → **"Deploy latest commit"**
2. Watch logs for progress
3. Wait 5-7 minutes
4. Look for: **"Build successful"** and **"Your service is live"**

---

## ✅ Alternative: Simpler Build Command

If the above build command is too long, use this instead:

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
gunicorn study_hub.wsgi:application --bind 0.0.0.0:$PORT
```

Then add this environment variable:
```env
PORT=10000
```

---

## 🐛 Still Getting Errors?

### Error: "Module 'study_hub' not found"

**Solution:** Check that Root Directory is set to `backend`

### Error: "requirements.txt not found"

**Solution:** 
1. Root Directory must be `backend`
2. Make sure `requirements.txt` exists in backend folder

### Error: "collectstatic failed"

**Solution:** Add this environment variable:
```env
DISABLE_COLLECTSTATIC=1
```

### Error: Database connection failed

**Solution:**
1. Make sure you added PostgreSQL database
2. Use **Internal Database URL** (not External)
3. Format should be: `postgresql://user:pass@dpg-xxx-internal/db`

---

## 📊 Correct Configuration Summary

```
Environment: Python 3 (NOT Docker!)
Root Directory: backend
Build Command: pip install -r requirements.txt
Start Command: gunicorn study_hub.wsgi:application
```

**Environment Variables:**
- PYTHON_VERSION=3.11.0
- DATABASE_URL=[Internal DB URL]
- SECRET_KEY=[generated]
- DEBUG=False
- ALLOWED_HOSTS=.onrender.com,.vercel.app
- YOUTUBE_API_KEY=AIzaSyAU1vqMfV64ZaNRHzHD0qtSMDXuW5XZoMc
- GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
- CORS_ALLOWED_ORIGINS=http://localhost:3000
- DISABLE_COLLECTSTATIC=1

---

## ✅ After Successful Deployment

You'll see your backend URL:
```
https://studyhub-backend.onrender.com
```

Test it:
```bash
curl https://studyhub-backend.onrender.com/api/grades/
```

Should return JSON!

---

## 🎯 Quick Checklist

- [ ] Service deleted (if error occurred)
- [ ] New service created
- [ ] Environment set to "Python 3" (NOT Docker)
- [ ] Root Directory = `backend`
- [ ] Build command set correctly
- [ ] Start command set correctly
- [ ] All environment variables added
- [ ] PostgreSQL database created
- [ ] DATABASE_URL added
- [ ] Deployed successfully
- [ ] API responding

---

**Follow these steps exactly and it will work!** 🚀

Need more help? Share the exact error message from Render logs!
