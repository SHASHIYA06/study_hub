# ⚡ Quick Deployment Guide - 15 Minutes to Live!

**Complete deployment in 3 simple steps.**

---

## 🎯 Prerequisites

Before starting, get these ready:

1. ✅ **YouTube API Key**
   - Go to: https://console.cloud.google.com/apis/credentials
   - Create project → Enable "YouTube Data API v3" → Create API Key
   - Copy the key

2. ✅ **GitHub Account** (you have: SHASHIYA06/study_hub)

3. ✅ **Gemini API Key** (already configured! ✅)
   - `AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM`

---

## 🚀 Step 1: Deploy Backend to Render (10 min)

### A. Create Account
1. Go to: https://render.com
2. Click **"Get Started for Free"**
3. Sign up with GitHub
4. Authorize Render

### B. Create PostgreSQL Database
1. Click **"New +"** → **"PostgreSQL"**
2. Name: `studyhub-db`
3. Plan: **Free**
4. Click **"Create Database"**
5. Wait 1 minute

### C. Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Click **"Build and deploy from a Git repository"**
3. Find: **SHASHIYA06/study_hub**
4. Click **"Connect"**

### D. Configure Service
Fill in:
- **Name:** `studyhub-backend`
- **Region:** Same as database
- **Branch:** `main`
- **Root Directory:** `backend`
- **Runtime:** `Python 3`
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn study_hub.wsgi:application`
- **Plan:** `Free`

### E. Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Copy from `RENDER_ENV_TEMPLATE.txt` or add these:

```env
PYTHON_VERSION=3.11.0
SECRET_KEY=[Generate at https://djecrety.ir/]
DEBUG=False
ALLOWED_HOSTS=.onrender.com,.vercel.app
YOUTUBE_API_KEY=[Your YouTube API key]
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
CORS_ALLOWED_ORIGINS=http://localhost:3000
DISABLE_COLLECTSTATIC=1
```

**Note:** Leave `DATABASE_URL` empty - Render fills it automatically!

### F. Deploy!
1. Click **"Create Web Service"**
2. Wait 5-7 minutes
3. Watch logs for "Build complete!"

### G. Copy Backend URL
After deployment, you'll see:
```
https://studyhub-backend.onrender.com
```
**Copy this URL!** You need it for Step 2.

---

## 🎨 Step 2: Deploy Frontend to Vercel (3 min)

### A. Go to Vercel
1. Visit: https://vercel.com/new
2. Click **"Import Git Repository"**
3. Sign in with GitHub if needed

### B. Select Repository
1. Find: **SHASHIYA06/study_hub**
2. Click **"Import"**

### C. Configure Project
- **Framework Preset:** Create React App
- **Root Directory:** `frontend`
- **Build Command:** `npm run build`
- **Output Directory:** `build`

### D. Add Environment Variable

Click **"Environment Variables"**

Add:
```
Name: REACT_APP_API_URL
Value: https://studyhub-backend.onrender.com
```
*(Use YOUR actual backend URL from Step 1!)*

### E. Deploy!
1. Click **"Deploy"**
2. Wait 2-3 minutes
3. Vercel will show: **"Congratulations!"**

### F. Copy Frontend URL
You'll get a URL like:
```
https://study-hub-shashiya06.vercel.app
```
**Copy this URL!** You need it for Step 3.

---

## 🔗 Step 3: Connect Frontend & Backend (2 min)

### A. Update Backend CORS

1. Go back to **Render Dashboard**
2. Click your **studyhub-backend** service
3. Click **"Environment"** in sidebar
4. Find **`CORS_ALLOWED_ORIGINS`**
5. Click **"Edit"**
6. Update to:
   ```
   https://study-hub-shashiya06.vercel.app,http://localhost:3000
   ```
   *(Use YOUR actual Vercel URL!)*
7. Click **"Save Changes"**
8. Render will automatically redeploy (takes 2 min)

---

## ✅ Step 4: Test Your Live App!

### Test Frontend
Visit your Vercel URL:
```
https://study-hub-shashiya06.vercel.app
```

You should see:
- ✅ Grade selection page
- ✅ Can click on grades
- ✅ Can browse subjects

### Test Backend API
```bash
curl https://studyhub-backend.onrender.com/api/grades/
```

Should return JSON with grades!

### Test AI Features
1. Navigate to a chapter
2. Click **"Generate Summary"** - Should work with Gemini!
3. Click **"Fetch Videos"** - Should work with YouTube API!

---

## 🎉 Success!

Your StudyHub is now LIVE! 🌐

**Your URLs:**
- **Frontend:** https://study-hub-shashiya06.vercel.app
- **Backend:** https://studyhub-backend.onrender.com/api/
- **Admin:** https://studyhub-backend.onrender.com/admin/

---

## 🔧 Post-Deployment

### Create Superuser (for Admin Panel)

1. In Render Dashboard → Your service
2. Click **"Shell"** tab
3. Run:
```bash
python manage.py createsuperuser
```
4. Enter username, email, password
5. Now you can access admin panel!

### Add More Content

1. Login to admin: `https://studyhub-backend.onrender.com/admin/`
2. Add more:
   - Grades
   - Subjects
   - Chapters
   - Study materials

---

## 📊 What You Built

✅ **Full-stack educational platform**
✅ **AI-powered learning tools** (Gemini)
✅ **Video integration** (YouTube)
✅ **Grade-wise content** (Nursery to Class 12)
✅ **Deployed on internet** (Free!)
✅ **Scalable architecture**

---

## 💰 Cost

**Monthly Cost: $0** (using free tiers!)

- Render: 750 hours/month (free)
- Vercel: Unlimited (free)
- Gemini API: 60 req/min (free)
- YouTube API: 10,000 req/day (free)

---

## 🐛 Troubleshooting

### Frontend shows blank page
- Check browser console for errors
- Verify `REACT_APP_API_URL` in Vercel
- Make sure backend is running

### "CORS error" in browser
- Verify backend `CORS_ALLOWED_ORIGINS` includes Vercel URL
- No trailing slash in URL
- Wait for backend redeploy after CORS update

### Videos not loading
- Check `YOUTUBE_API_KEY` in Render
- Verify API key is enabled in Google Cloud Console
- Check API quota: https://console.cloud.google.com/apis/dashboard

### AI features not working
- Check `GOOGLE_GEMINI_API_KEY` in Render
- Test: `curl https://studyhub-backend.onrender.com/api/doubt-solver/ask_doubt/`

---

## 📚 Next Steps

1. ✅ Test all features
2. ✅ Add more content via admin panel
3. ✅ Share with students!
4. ✅ Get feedback
5. ✅ Iterate and improve

---

## 🎓 Share Your App

- Share URL with students
- Add to your portfolio
- Post on social media
- Get user feedback
- Build your EdTech platform!

---

**Congratulations! Your educational platform is LIVE!** 🎉

**Questions?** Check the detailed guides:
- RENDER_DEPLOYMENT.md
- ENV_SETUP_GUIDE.md
- DEPLOYMENT_COMPARISON.md
