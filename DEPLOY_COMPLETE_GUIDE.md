# 🚀 Complete Deployment Guide - StudyHub

## 🎯 Best Deployment Strategy

**Frontend (React) → Vercel** (Free, Fast, CDN)  
**Backend (Django) → Railway** (Free, PostgreSQL included)

This gives you the best of both worlds!

---

## 📝 Step-by-Step Deployment

### Phase 1: Push to GitHub ✅

```bash
cd study_hub

# Check status
git status

# If not committed, commit now
git add .
git commit -m "Complete StudyHub application ready for deployment"

# Push to GitHub
git push -u origin main
```

**When prompted:**
- Username: `SHASHIYA06`
- Password: Use **Personal Access Token** from https://github.com/settings/tokens

**Verify:** Visit https://github.com/SHASHIYA06/study_hub

---

### Phase 2: Deploy Backend to Railway (5 minutes)

#### Step 1: Sign Up / Login

1. Go to: https://railway.app
2. Click "Start a New Project"
3. Login with GitHub

#### Step 2: Deploy Backend

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Create new project
cd backend
railway init

# Link to your project
railway link

# Deploy
railway up
```

**Or use Dashboard:**
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose `SHASHIYA06/study_hub`
4. Set root directory: `backend`
5. Click "Deploy"

#### Step 3: Add PostgreSQL

1. In Railway dashboard
2. Click "New" → "Database" → "PostgreSQL"
3. Database URL will be auto-added to environment

#### Step 4: Set Environment Variables

In Railway dashboard → Variables:

```env
YOUTUBE_API_KEY=your_youtube_key
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
SECRET_KEY=your-django-secret-key-here
DEBUG=False
ALLOWED_HOSTS=.railway.app
CORS_ALLOWED_ORIGINS=https://your-frontend.vercel.app
```

#### Step 5: Get Backend URL

After deployment, Railway gives you a URL like:
```
https://studyhub-backend-production.up.railway.app
```

**Copy this URL** - you'll need it for frontend!

---

### Phase 3: Deploy Frontend to Vercel (3 minutes)

#### Step 1: Update Frontend Configuration

Create `frontend/.env.production`:

```env
REACT_APP_API_URL=https://studyhub-backend-production.up.railway.app
```

Commit this:
```bash
cd study_hub
git add frontend/.env.production
git commit -m "Add production API URL"
git push origin main
```

#### Step 2: Deploy to Vercel

**Option A: Using Vercel CLI**

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy frontend
cd frontend
vercel --prod
```

**Option B: Using Vercel Dashboard** (Easier!)

1. Go to: https://vercel.com/new
2. Click "Import Git Repository"
3. Select `SHASHIYA06/study_hub`
4. **Framework Preset:** Create React App
5. **Root Directory:** `frontend`
6. **Environment Variables:** Add `REACT_APP_API_URL`
7. Click "Deploy"

#### Step 3: Set Environment Variables in Vercel

In Vercel Dashboard → Settings → Environment Variables:

```env
REACT_APP_API_URL=https://studyhub-backend-production.up.railway.app
```

#### Step 4: Get Frontend URL

Vercel gives you a URL like:
```
https://study-hub-shashiya06.vercel.app
```

---

### Phase 4: Connect Frontend & Backend

#### Update Backend CORS

In Railway dashboard, update environment variables:

```env
CORS_ALLOWED_ORIGINS=https://study-hub-shashiya06.vercel.app,http://localhost:3000
ALLOWED_HOSTS=.railway.app,.vercel.app
```

Redeploy backend on Railway.

---

### Phase 5: Run Migrations

```bash
# Using Railway CLI
railway run python manage.py migrate

# Or in Railway dashboard
# Shell → Run: python manage.py migrate
```

#### Seed Database

```bash
railway run python manage.py seed_data
```

#### Create Superuser

```bash
railway run python manage.py createsuperuser
```

---

## ✅ Verification Checklist

- [ ] GitHub repository has all code
- [ ] Backend deployed on Railway
- [ ] PostgreSQL database created
- [ ] Backend environment variables set
- [ ] Backend migrations run
- [ ] Backend URL copied
- [ ] Frontend `.env.production` updated
- [ ] Frontend deployed on Vercel
- [ ] Frontend environment variables set
- [ ] CORS configured correctly
- [ ] Can access frontend URL
- [ ] Frontend can call backend API
- [ ] AI features work
- [ ] Admin panel accessible

---

## 🌐 Your Live URLs

After deployment, you'll have:

**Frontend:** `https://study-hub-shashiya06.vercel.app`  
**Backend API:** `https://studyhub-backend-production.up.railway.app/api/`  
**Admin Panel:** `https://studyhub-backend-production.up.railway.app/admin/`

---

## 🧪 Test Your Deployment

### Test Frontend:
```bash
curl https://study-hub-shashiya06.vercel.app
# Should return HTML
```

### Test Backend API:
```bash
curl https://studyhub-backend-production.up.railway.app/api/grades/
# Should return JSON with grades
```

### Test AI Features:
```bash
curl -X POST https://studyhub-backend-production.up.railway.app/api/doubt-solver/ask_doubt/ \
  -H "Content-Type: application/json" \
  -d '{"problem_description": "What is photosynthesis?"}'
# Should return AI explanation
```

---

## 💰 Cost

**Both platforms offer free tiers:**

- **Vercel:** Unlimited deployments, 100GB bandwidth/month
- **Railway:** $5 credit/month (enough for small apps)

**Total Cost:** $0 - $5/month

---

## 🔄 Update Deployment

### Update Frontend:
```bash
cd study_hub
# Make changes to frontend
git add .
git commit -m "Update frontend"
git push origin main
# Vercel auto-deploys!
```

### Update Backend:
```bash
cd study_hub
# Make changes to backend
git add .
git commit -m "Update backend"
git push origin main
# Railway auto-deploys!
```

---

## 🐛 Troubleshooting

### Issue: Frontend can't reach backend

**Solution:**
1. Check CORS settings in Railway
2. Verify `REACT_APP_API_URL` in Vercel
3. Check browser console for errors

### Issue: Database not connected

**Solution:**
1. Check `DATABASE_URL` in Railway
2. Run migrations: `railway run python manage.py migrate`

### Issue: AI features not working

**Solution:**
1. Verify `GOOGLE_GEMINI_API_KEY` in Railway
2. Check API quota: https://aistudio.google.com

---

## 📊 Architecture

```
┌──────────────────┐
│   Users          │
└────────┬─────────┘
         │
         ↓
┌──────────────────┐
│   Vercel CDN     │  ← React Frontend
│   (Global Edge)  │     • Fast delivery
└────────┬─────────┘     • Auto HTTPS
         │               • Free tier
         │ API Calls
         ↓
┌──────────────────┐
│   Railway        │  ← Django Backend
│   (Cloud Server) │     • PostgreSQL DB
└────────┬─────────┘     • Environment vars
         │               • Free tier
         ↓
┌──────────────────┐
│   External APIs  │
│   • Gemini AI    │
│   • YouTube      │
└──────────────────┘
```

---

## 🎯 Quick Command Reference

```bash
# Push to GitHub
git push -u origin main

# Deploy backend (Railway)
railway up

# Deploy frontend (Vercel)
vercel --prod

# Run migrations
railway run python manage.py migrate

# View logs
railway logs
vercel logs

# Open in browser
railway open
vercel open
```

---

## 📞 Need Help?

1. **Check logs:**
   - Railway: `railway logs`
   - Vercel: Dashboard → Deployment → Logs

2. **Verify environment variables:**
   - Railway: Dashboard → Variables
   - Vercel: Dashboard → Settings → Environment Variables

3. **Test API endpoints:**
   - Use Postman or curl
   - Check browser DevTools → Network tab

---

## 🎉 Success!

Your StudyHub is now live on the internet! 🌐

**Share your app:**
- Frontend URL: `https://study-hub-shashiya06.vercel.app`
- Show it to friends, teachers, students!
- Add to your portfolio
- Share on social media

---

**Ready to deploy? Let's start with pushing to GitHub!** 🚀
