# ✅ Your StudyHub is READY TO DEPLOY!

All API keys configured and templates ready!

---

## 🔑 API Keys Configured

### ✅ Google Gemini API Key
```
AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
```
**Status:** ✅ Ready to use

### ✅ YouTube Data API v3 Key
```
AIzaSyAU1vqMfV64ZaNRHzHD0qtSMDXuW5XZoMc
```
**Status:** ✅ Ready to use

---

## 🚀 Deploy NOW - 3 Simple Steps

### Step 1: Deploy Backend to Render (10 min)

1. **Go to:** https://render.com
2. **Sign up** with GitHub
3. **New Web Service** → Import `SHASHIYA06/study_hub`
4. **Configure:**
   - Name: `studyhub-backend`
   - Root Directory: `backend`
   - Runtime: `Python 3`
   - Build Command: `./build.sh`
   - Start Command: `gunicorn study_hub.wsgi:application`

5. **Add PostgreSQL:** Click "New +" → "PostgreSQL" → Free tier

6. **Environment Variables** (copy from below):

```env
PYTHON_VERSION=3.11.0
SECRET_KEY=django-insecure-98j2sd9f8j2ksdfjk2sd9fj2k3sdf92k3sdf
DEBUG=False
ALLOWED_HOSTS=.onrender.com,.vercel.app
DISABLE_COLLECTSTATIC=1
YOUTUBE_API_KEY=AIzaSyAU1vqMfV64ZaNRHzHD0qtSMDXuW5XZoMc
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

**Note:** Generate a new SECRET_KEY at https://djecrety.ir/ for better security!

7. **Deploy!** Wait 5-7 minutes

8. **Copy your backend URL:**
   ```
   https://studyhub-backend.onrender.com
   ```

---

### Step 2: Deploy Frontend to Vercel (3 min)

1. **Go to:** https://vercel.com/new
2. **Import:** `SHASHIYA06/study_hub`
3. **Configure:**
   - Framework: Create React App
   - Root Directory: `frontend`
4. **Environment Variable:**
   ```
   REACT_APP_API_URL=https://studyhub-backend.onrender.com
   ```
   (Use YOUR actual backend URL from Step 1!)

5. **Deploy!** Wait 2-3 minutes

6. **Copy your frontend URL:**
   ```
   https://study-hub-shashiya06.vercel.app
   ```

---

### Step 3: Connect Frontend & Backend (2 min)

1. **Go back to Render** Dashboard
2. **Click your backend service**
3. **Environment** → Edit `CORS_ALLOWED_ORIGINS`
4. **Update to:**
   ```
   https://study-hub-shashiya06.vercel.app,http://localhost:3000
   ```
   (Use YOUR actual Vercel URL!)

5. **Save** → Render redeploys automatically

---

## ✅ Test Your Live App

### Test Frontend
Visit: `https://study-hub-shashiya06.vercel.app`
- Should see grade selection page
- Click through grades → subjects → chapters

### Test Backend API
```bash
curl https://studyhub-backend.onrender.com/api/grades/
```
Should return JSON with grades

### Test AI Features
1. Navigate to a chapter
2. Click **"Fetch Videos"** → Should show YouTube videos! ✅
3. Click **"Generate Summary"** → Should show AI summary! ✅
4. Click **"Generate Flashcards"** → Should create flashcards! ✅

### Test Doubt Solver
```bash
curl -X POST https://studyhub-backend.onrender.com/api/doubt-solver/ask_doubt/ \
  -H "Content-Type: application/json" \
  -d '{"problem_description": "What is photosynthesis?"}'
```
Should return detailed AI explanation!

---

## 🎯 Quick Reference

### Backend Environment Variables (Render)
```env
PYTHON_VERSION=3.11.0
DATABASE_URL=[Auto-filled by Render]
SECRET_KEY=[Generate at https://djecrety.ir/]
DEBUG=False
ALLOWED_HOSTS=.onrender.com,.vercel.app
YOUTUBE_API_KEY=AIzaSyAU1vqMfV64ZaNRHzHD0qtSMDXuW5XZoMc
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
CORS_ALLOWED_ORIGINS=https://your-frontend.vercel.app
DISABLE_COLLECTSTATIC=1
```

### Frontend Environment Variables (Vercel)
```env
REACT_APP_API_URL=https://your-backend.onrender.com
```

---

## 📊 What Your Users Will Get

1. **Grade Selection** - Nursery to Class 12
2. **Subject Browser** - Science, Math, English, etc.
3. **Chapter Viewer** - Organized study content
4. **AI Summaries** - Auto-generated bullet points
5. **YouTube Videos** - Curated educational content
6. **Flashcards** - AI-generated study cards
7. **Quizzes** - Auto-generated MCQs
8. **Doubt Solver** - Ask any question, get step-by-step solution
9. **Concept Explainer** - Simple explanations with examples

---

## 🎓 Create Superuser (Access Admin Panel)

After backend deployment:

1. **Render Dashboard** → Your service → **"Shell"**
2. Run:
   ```bash
   python manage.py createsuperuser
   ```
3. Enter:
   - Username: `admin`
   - Email: `admin@studyhub.com`
   - Password: (your choice)

4. **Access admin:**
   ```
   https://studyhub-backend.onrender.com/admin/
   ```

---

## 💰 Cost

**Total Cost: $0/month** (with free tiers!)

- ✅ Render: 750 hours/month FREE
- ✅ Vercel: Unlimited deployments FREE
- ✅ Gemini API: 60 requests/min FREE
- ✅ YouTube API: 10,000 requests/day FREE

---

## 🔧 Troubleshooting

### Issue: Videos not showing
- ✅ API key is configured: `AIzaSyAU1vqMfV64ZaNRHzHD0qtSMDXuW5XZoMc`
- Check if quota exceeded at: https://console.cloud.google.com/apis/dashboard

### Issue: AI features not working
- ✅ Gemini key is configured: `AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM`
- Check logs in Render dashboard

### Issue: CORS error
- Update `CORS_ALLOWED_ORIGINS` in Render with your Vercel URL
- Make sure no trailing slash in URL
- Wait for Render to redeploy (2 min)

---

## 📚 Additional Guides

- **QUICK_DEPLOYMENT.md** - Detailed 15-min guide
- **RENDER_DEPLOYMENT.md** - Full Render instructions
- **SUPABASE_DEPLOYMENT.md** - Alternative with Supabase
- **ENV_SETUP_GUIDE.md** - Environment variables explained

---

## 🎉 You're All Set!

Both API keys are configured and ready:
- ✅ YouTube API for video fetching
- ✅ Gemini API for AI features

**Time to deploy: ~15 minutes**

**Start here:** https://render.com

---

## 🌐 After Deployment

You'll have:
- **Frontend:** `https://study-hub-shashiya06.vercel.app`
- **Backend:** `https://studyhub-backend.onrender.com`
- **Admin:** `https://studyhub-backend.onrender.com/admin/`

**Share with students and start transforming education!** 🎓✨

---

**Questions?** All guides are in your repository: https://github.com/SHASHIYA06/study_hub

**Ready to deploy? Follow Step 1 above!** 🚀
