# 🧪 Testing Guide - StudyHub

Complete guide to test and verify your StudyHub installation.

## 📋 Pre-Testing Checklist

Before testing, ensure:
- [ ] Docker and Docker Compose are installed
- [ ] You have valid API keys (YouTube & OpenAI)
- [ ] `.env` file is configured
- [ ] Services are running

---

## 🚀 Step 1: Start the Application

```bash
cd study_hub

# Copy environment file if not done
cp .env.example .env

# Edit .env and add your API keys
nano .env

# Start all services
make up
# OR: docker-compose up -d

# Wait 10-15 seconds for services to start
sleep 15

# Check if all containers are running
docker-compose ps
```

**Expected Output:**
```
NAME                    STATUS
study_hub_backend       Up (healthy)
study_hub_db            Up (healthy)
study_hub_frontend      Up (healthy)
study_hub_redis         Up (healthy)
study_hub_celery        Up
```

---

## 🔍 Step 2: Verify Services

### Check Backend Status

```bash
# View backend logs
docker-compose logs backend

# Should see:
# "Django version X.X.X, using settings 'study_hub.settings'"
# "Starting development server at http://0.0.0.0:8000/"
```

### Check Database Connection

```bash
# Test database
docker-compose exec backend python manage.py check

# Expected: "System check identified no issues (0 silenced)."
```

### Check Frontend Status

```bash
# View frontend logs
docker-compose logs frontend

# Should see Nginx starting successfully
```

---

## 🧪 Step 3: Test Backend API

### Test 1: Health Check

```bash
# Test if backend is responding
curl http://localhost:8000/api/grades/

# Expected: JSON response with grades data
```

**Expected Response:**
```json
{
  "count": 15,
  "results": [
    {
      "id": 1,
      "level": "nursery",
      "description": "Early childhood education"
    }
  ]
}
```

### Test 2: Run Migrations

```bash
# Run database migrations
make migrate
# OR: docker-compose exec backend python manage.py migrate

# Expected: "Operations to perform: 0 already applied"
```

### Test 3: Seed Database

```bash
# Add sample data
make seed
# OR: docker-compose exec backend python manage.py seed_data

# Expected: 
# "✓ Created grade: nursery"
# "✓ Created grade: class_9"
# "Database seeding complete!"
```

### Test 4: API Endpoints

```bash
# Test all major endpoints

# 1. Grades
curl http://localhost:8000/api/grades/

# 2. Subjects (for grade 9)
curl http://localhost:8000/api/subjects/?grade_id=9

# 3. Chapters (for first subject)
curl http://localhost:8000/api/chapters/?subject_id=1

# 4. Materials
curl http://localhost:8000/api/materials/

# 5. Quizzes
curl http://localhost:8000/api/quizzes/
```

---

## 🎨 Step 4: Test Frontend

### Test 1: Frontend Homepage

1. Open browser: http://localhost
2. You should see: **"Choose Your Grade"** page
3. Check for grade cards with emojis

### Test 2: Navigation Flow

```
1. Select "Class 9" card
   → Should navigate to subjects page
   
2. Click on "Science" subject
   → Should show chapters list
   
3. Click on "Chapter 1: Motion"
   → Should show chapter details with AI tools
   
4. Navigate to "AI Tools" in menu
   → Should show Doubt Solver and Concept Explainer
```

### Test 3: Visual Verification

Check these elements:
- [ ] Grade cards display with emojis
- [ ] Navigation bar at top
- [ ] Subject cards with icons
- [ ] Chapter cards with descriptions
- [ ] AI tool buttons visible
- [ ] No console errors (F12 → Console)

---

## 🤖 Step 5: Test AI Features

### Test 1: Fetch Videos (YouTube API)

```bash
# In browser:
1. Go to: http://localhost
2. Navigate: Class 9 → Science → Chapter 1: Motion
3. Click "Fetch Videos" button
4. Wait 3-5 seconds

Expected:
- Button shows "Fetching..."
- Videos appear below with thumbnails
- Each video has title, channel, "Watch Now" button
```

**Verify via API:**
```bash
curl http://localhost:8000/api/chapters/1/fetch_videos/
```

### Test 2: Generate Summary (OpenAI API)

```bash
# In browser:
1. Same chapter page
2. Click "Generate Summary" button
3. Wait 5-10 seconds

Expected:
- Button shows "Generating..."
- AI-generated bullet points appear
- Summary is readable and relevant
```

**Verify via API:**
```bash
curl -X POST http://localhost:8000/api/chapters/1/generate_summary/
```

### Test 3: Generate Flashcards

```bash
# In browser:
1. Same chapter page
2. Click "Generate Flashcards" button
3. Wait 5-10 seconds

Expected:
- Multiple flashcard cards appear
- Each has Question and Answer
- Cards are hoverable
```

**Verify via API:**
```bash
curl -X POST http://localhost:8000/api/chapters/1/generate_flashcards/ \
  -H "Content-Type: application/json" \
  -d '{"num_cards": 5}'
```

### Test 4: Doubt Solver

```bash
# In browser:
1. Go to "AI Tools" page
2. Enter: "What is Newton's first law?"
3. Click "Solve Doubt"

Expected:
- Step-by-step explanation appears
- Solution is clear and educational
```

**Verify via API:**
```bash
curl -X POST http://localhost:8000/api/doubt-solver/ask_doubt/ \
  -H "Content-Type: application/json" \
  -d '{"problem_description": "What is Newton'\''s first law?"}'
```

### Test 5: Concept Explainer

```bash
# In browser:
1. AI Tools page
2. Enter Concept: "Photosynthesis"
3. Enter Grade: "9"
4. Click "Get Explanation"

Expected:
- Simple, grade-appropriate explanation
- Easy to understand
```

**Verify via API:**
```bash
curl -X POST http://localhost:8000/api/explain/explain/ \
  -H "Content-Type: application/json" \
  -d '{"concept": "Photosynthesis", "grade": "9"}'
```

---

## 🔐 Step 6: Test Admin Panel

### Access Admin

```bash
# Create superuser first
make superuser
# OR: docker-compose exec backend python manage.py createsuperuser

# Enter:
# Username: admin
# Email: admin@example.com
# Password: (your secure password)
```

### Test Admin Features

1. Open: http://localhost:8000/admin/
2. Login with superuser credentials
3. Test these actions:

**Grades:**
- [ ] View list of grades
- [ ] Add new grade
- [ ] Edit existing grade
- [ ] Delete grade

**Subjects:**
- [ ] View subjects
- [ ] Add subject to grade
- [ ] Edit subject

**Chapters:**
- [ ] View chapters
- [ ] Add new chapter with content
- [ ] Edit chapter content
- [ ] View materials

**Quizzes:**
- [ ] View quizzes
- [ ] Create new quiz
- [ ] Add questions

---

## 📊 Step 7: Performance Testing

### Test 1: Response Times

```bash
# Test API response time
time curl http://localhost:8000/api/grades/

# Should be: < 200ms for local
```

### Test 2: Concurrent Requests

```bash
# Install Apache Bench (if not installed)
# Ubuntu: apt-get install apache2-utils
# Mac: brew install ab

# Test with 100 requests, 10 concurrent
ab -n 100 -c 10 http://localhost:8000/api/grades/

# Check:
# - Requests per second > 50
# - Failed requests: 0
```

### Test 3: Memory Usage

```bash
# Check container resource usage
docker stats --no-stream

# Verify:
# - Backend < 500MB RAM
# - Database < 200MB RAM
# - Frontend < 50MB RAM
```

---

## 🐛 Step 8: Error Testing

### Test Error Handling

```bash
# 1. Test invalid endpoint
curl http://localhost:8000/api/invalid/
# Expected: 404 Not Found

# 2. Test invalid chapter ID
curl http://localhost:8000/api/chapters/99999/
# Expected: 404 Not Found

# 3. Test missing parameters
curl -X POST http://localhost:8000/api/doubt-solver/ask_doubt/ \
  -H "Content-Type: application/json" \
  -d '{}'
# Expected: 400 Bad Request with error message
```

### Test Frontend Error States

1. Stop backend: `docker-compose stop backend`
2. Refresh frontend
3. Should see: "Failed to load" messages
4. Restart: `docker-compose start backend`

---

## 🔄 Step 9: Test Database Operations

### Test CRUD Operations

```bash
# Enter Django shell
make shell
# OR: docker-compose exec backend python manage.py shell
```

**In Django shell:**
```python
# Test creating a grade
from app.models import Grade
grade = Grade.objects.create(level='test_grade', description='Test')
print(f"Created: {grade}")

# Test reading
grades = Grade.objects.all()
print(f"Total grades: {grades.count()}")

# Test updating
grade.description = "Updated description"
grade.save()
print(f"Updated: {grade}")

# Test deleting
grade.delete()
print("Deleted successfully")

# Exit shell
exit()
```

### Test Database Backup

```bash
# Create backup
make backup-db

# Verify backup file exists
ls -lh backup_*.sql

# Expected: backup_YYYYMMDD_HHMMSS.sql file created
```

---

## 📱 Step 10: Cross-Browser Testing

### Desktop Browsers
Test on:
- [ ] Chrome/Edge (http://localhost)
- [ ] Firefox (http://localhost)
- [ ] Safari (http://localhost)

### Mobile Responsive
Test on:
- [ ] Chrome mobile emulation (F12 → Toggle device toolbar)
- [ ] Different screen sizes (375px, 768px, 1920px)

### Verify:
- [ ] Layout adapts to screen size
- [ ] Navigation menu works
- [ ] Buttons are clickable
- [ ] Text is readable
- [ ] Images scale properly

---

## ✅ Step 11: Comprehensive Test Script

Create and run automated test script:

```bash
# Create test script
cat > study_hub/test_all.sh << 'EOF'
#!/bin/bash

echo "🧪 Running comprehensive tests..."

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

# Test counter
passed=0
failed=0

# Test function
test_endpoint() {
    local name=$1
    local url=$2
    echo -n "Testing $name... "
    
    if curl -s -f "$url" > /dev/null; then
        echo -e "${GREEN}✓ PASSED${NC}"
        ((passed++))
    else
        echo -e "${RED}✗ FAILED${NC}"
        ((failed++))
    fi
}

# Run tests
test_endpoint "Frontend" "http://localhost/"
test_endpoint "Backend API" "http://localhost:8000/api/grades/"
test_endpoint "Subjects" "http://localhost:8000/api/subjects/"
test_endpoint "Chapters" "http://localhost:8000/api/chapters/"
test_endpoint "Materials" "http://localhost:8000/api/materials/"
test_endpoint "Quizzes" "http://localhost:8000/api/quizzes/"
test_endpoint "Flashcards" "http://localhost:8000/api/flashcards/"

# Summary
echo ""
echo "================================"
echo "Test Results:"
echo "  Passed: $passed"
echo "  Failed: $failed"
echo "================================"

if [ $failed -eq 0 ]; then
    echo -e "${GREEN}All tests passed! ✓${NC}"
    exit 0
else
    echo -e "${RED}Some tests failed! ✗${NC}"
    exit 1
fi
EOF

chmod +x study_hub/test_all.sh
./study_hub/test_all.sh
```

---

## 📋 Test Results Checklist

### ✅ Essential Tests (Must Pass)

- [ ] All Docker containers running and healthy
- [ ] Database migrations completed
- [ ] Sample data seeded successfully
- [ ] Frontend loads at http://localhost
- [ ] Backend API responds at http://localhost:8000
- [ ] Can navigate through pages (Grade → Subject → Chapter)
- [ ] Admin panel accessible
- [ ] No critical errors in logs

### ✅ Feature Tests (Should Pass)

- [ ] Fetch Videos works (requires YouTube API key)
- [ ] Generate Summary works (requires OpenAI API key)
- [ ] Generate Flashcards works (requires OpenAI API key)
- [ ] Doubt Solver responds
- [ ] Concept Explainer responds
- [ ] Can create/edit content in admin

### ✅ Performance Tests (Nice to Have)

- [ ] Page load time < 3 seconds
- [ ] API response time < 500ms
- [ ] No memory leaks
- [ ] Handles 100+ concurrent requests

---

## 🐛 Common Issues & Solutions

### Issue 1: "Connection refused"
```bash
# Solution: Check if containers are running
docker-compose ps

# Restart if needed
docker-compose restart
```

### Issue 2: "API key not configured"
```bash
# Solution: Verify .env file
cat .env | grep -E 'YOUTUBE|OPENAI'

# Restart backend
docker-compose restart backend
```

### Issue 3: "No data showing"
```bash
# Solution: Seed database
make seed

# Verify data
docker-compose exec backend python manage.py shell
>>> from app.models import Grade
>>> Grade.objects.count()
```

### Issue 4: Frontend shows errors
```bash
# Solution: Check backend logs
docker-compose logs backend

# Check CORS settings
docker-compose exec backend env | grep CORS
```

---

## 📊 Test Report Template

Use this template to document your testing:

```
StudyHub Test Report
Date: __________
Tester: __________

Environment:
- OS: __________
- Docker Version: __________
- Browser: __________

Test Results:
✅ Services Running: YES / NO
✅ Frontend Loads: YES / NO
✅ Backend API: YES / NO
✅ Database: YES / NO
✅ Fetch Videos: YES / NO
✅ AI Features: YES / NO
✅ Admin Panel: YES / NO

Performance:
- Page Load Time: ____ seconds
- API Response: ____ ms
- Memory Usage: ____ MB

Issues Found:
1. __________
2. __________

Overall Status: PASS / FAIL

Notes:
__________
```

---

## 🎯 Quick Test Commands

```bash
# Quick health check
curl http://localhost:8000/api/grades/ && echo "✓ Backend OK"
curl http://localhost/ && echo "✓ Frontend OK"

# View all logs
make logs

# Check container status
docker-compose ps

# Run Django tests
docker-compose exec backend python manage.py test

# Access database
docker-compose exec db psql -U study_hub_user study_hub
```

---

## 🚀 Automated Testing (CI/CD)

The project includes GitHub Actions for automated testing:

```yaml
# .github/workflows/deploy.yml
# Runs automatically on push to main branch

Tests include:
✓ Backend unit tests
✓ Frontend build
✓ Docker image builds
✓ Integration tests
```

---

## 📞 Need Help?

If tests fail:
1. Check logs: `docker-compose logs -f`
2. Review this guide
3. Check [TROUBLESHOOTING.md](DEPLOYMENT.md#troubleshooting)
4. Create GitHub issue with test results

---

**Pro Tip:** Run the automated test script regularly:
```bash
./study_hub/test_all.sh
```

This ensures everything is working correctly! 🎉
