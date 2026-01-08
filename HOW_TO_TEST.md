# 🎯 Quick Testing Guide - StudyHub

## The Easiest Way to Test (30 seconds)

### 1️⃣ Run the Quick Test Script

```bash
cd study_hub
./QUICK_TEST.sh
```

This automated script will test:
- ✅ All Docker containers
- ✅ Frontend & Backend connectivity  
- ✅ API endpoints
- ✅ Database connection
- ✅ Data availability

**Expected Result:** "✅ ALL TESTS PASSED!"

---

## 2️⃣ Manual Testing (5 minutes)

### Test the Frontend

1. **Open your browser** → http://localhost

2. **You should see:**
   - Grade selection page with cards (Nursery, UKG, Class 1-12)
   - Each card has an emoji
   - Clean, professional design

3. **Click on "Class 9"**
   - Should navigate to subjects page
   - See subjects: Science, Math, English, etc.

4. **Click on "Science"**
   - Should show chapters list
   - See "Chapter 1: Motion", etc.

5. **Click on a chapter**
   - Should see chapter details
   - Three buttons: Fetch Videos, Generate Summary, Generate Flashcards

6. **Click "AI Tools" in navigation**
   - Should see Doubt Solver and Concept Explainer forms

### Test the Backend API

```bash
# Test 1: Grades endpoint
curl http://localhost:8000/api/grades/

# Should return JSON with grades data

# Test 2: Admin panel
# Open in browser: http://localhost:8000/admin/
# Login with superuser credentials
```

---

## 3️⃣ Test AI Features (requires API keys)

### Before Testing AI Features:
Make sure you have added API keys to `.env`:
```env
YOUTUBE_API_KEY=your_key_here
OPENAI_API_KEY=sk-your_key_here
```

Then restart:
```bash
docker-compose restart backend
```

### Test Each AI Feature:

#### A. Fetch Videos (YouTube API)
1. Go to any chapter page
2. Click "Fetch Videos"
3. Wait 3-5 seconds
4. **Expected:** Video cards appear with thumbnails and "Watch Now" buttons

#### B. Generate Summary (OpenAI)
1. Same chapter page
2. Click "Generate Summary"
3. Wait 5-10 seconds
4. **Expected:** Bullet-point summary appears in blue box

#### C. Generate Flashcards (OpenAI)
1. Same chapter page
2. Click "Generate Flashcards"
3. Wait 5-10 seconds
4. **Expected:** Multiple flashcard cards appear with Q&A

#### D. Doubt Solver
1. Go to "AI Tools" page
2. Enter: "What is Newton's first law?"
3. Click "Solve Doubt"
4. **Expected:** Step-by-step explanation appears

#### E. Concept Explainer
1. Same AI Tools page
2. Enter Concept: "Photosynthesis"
3. Enter Grade: "9"
4. Click "Get Explanation"
5. **Expected:** Simple explanation appears

---

## 4️⃣ Check for Issues

### View Logs
```bash
# All logs
docker-compose logs -f

# Backend only
docker-compose logs -f backend

# Frontend only
docker-compose logs -f frontend
```

### Check Container Status
```bash
docker-compose ps

# All should show "Up" and "healthy"
```

### Common Issues

**Issue:** "Connection refused"
```bash
# Fix: Restart services
docker-compose restart
```

**Issue:** "API key error"
```bash
# Fix: Check .env file and restart
cat .env | grep API
docker-compose restart backend
```

**Issue:** "No data showing"
```bash
# Fix: Seed database
make seed
```

---

## ✅ Success Checklist

- [ ] Frontend loads at http://localhost
- [ ] Backend API works at http://localhost:8000/api/
- [ ] Can navigate: Grade → Subject → Chapter
- [ ] All containers showing "Up (healthy)"
- [ ] No critical errors in logs
- [ ] Admin panel accessible at http://localhost:8000/admin/

### Optional (with API keys):
- [ ] Fetch Videos works
- [ ] Generate Summary works
- [ ] Generate Flashcards works
- [ ] Doubt Solver responds
- [ ] Concept Explainer responds

---

## 📊 Quick Commands Reference

```bash
# Start application
make up

# Run quick test
./QUICK_TEST.sh

# View logs
make logs

# Stop application
make down

# Restart services
docker-compose restart

# Check status
docker-compose ps

# Seed database
make seed

# Create admin user
make superuser
```

---

## 🆘 If Tests Fail

1. **Read detailed guide:** `TESTING_GUIDE.md`
2. **Check logs:** `docker-compose logs -f backend`
3. **Verify .env:** `cat .env`
4. **Restart:** `docker-compose restart`
5. **Clean rebuild:** `docker-compose down -v && make build && make up`

---

## 📞 Need More Help?

- Full testing guide: `TESTING_GUIDE.md`
- Deployment guide: `DEPLOYMENT.md`
- API documentation: `API_DOCUMENTATION.md`
- Getting started: `GET_STARTED.md`

---

**That's it! Your StudyHub should be working now.** 🎉

Access your application:
- **Frontend:** http://localhost
- **Backend:** http://localhost:8000/api/
- **Admin:** http://localhost:8000/admin/
