# 🤖 Google Gemini API Setup Guide

Your StudyHub has been configured to use **Google Gemini AI** instead of OpenAI!

## ✅ Your Gemini API Key

Your key has been added: `AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM`

## 🚀 Quick Setup

### Step 1: Add API Key to Environment

```bash
cd study_hub

# Copy the environment file
cp .env.example .env

# The key is already configured in .env.production
# Or manually edit .env and add:
echo "GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM" >> .env
```

### Step 2: Rebuild Backend

```bash
# Rebuild backend with new dependencies
docker-compose build backend

# Restart services
docker-compose up -d

# Wait for services to start
sleep 10
```

### Step 3: Test AI Features

```bash
# Test the Gemini integration
curl -X POST http://localhost:8000/api/doubt-solver/ask_doubt/ \
  -H "Content-Type: application/json" \
  -d '{"problem_description": "What is photosynthesis?"}'
```

## 🎯 What Changed?

### Updated Files:
1. **backend/requirements.txt** - Added `google-generativeai` package
2. **backend/app/ai_utils.py** - Switched from OpenAI to Gemini API
3. **backend/study_hub/settings.py** - Updated API key variable
4. **.env.example** - Changed to GOOGLE_GEMINI_API_KEY

### AI Features Using Gemini:
- ✅ Summary Generation
- ✅ Quiz Generation
- ✅ Flashcard Creation
- ✅ Doubt Solver
- ✅ Concept Explainer

## 📊 Gemini API Capabilities

**Model Used:** `gemini-pro`

**Features:**
- Natural language understanding
- Educational content generation
- Step-by-step explanations
- Multi-turn conversations
- JSON structured outputs

**Advantages over OpenAI:**
- Free tier available
- Fast response times
- Good educational content quality
- Multilingual support

## 🧪 Testing Gemini Integration

### Test 1: Generate Summary

```bash
# Navigate to a chapter in browser
http://localhost/chapter/1

# Click "Generate Summary" button
# Should see AI-generated summary using Gemini
```

### Test 2: Doubt Solver

```bash
# Go to AI Tools page
http://localhost/ai-features

# Ask a question in Doubt Solver
# Example: "Explain Newton's laws of motion"

# Should get detailed step-by-step explanation
```

### Test 3: API Test

```bash
# Test concept explainer
curl -X POST http://localhost:8000/api/explain/explain/ \
  -H "Content-Type: application/json" \
  -d '{"concept": "Photosynthesis", "grade": "9"}'

# Expected: Detailed explanation in JSON
```

## 🔧 Configuration Details

### Environment Variable

```env
GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM
```

### Python Code (ai_utils.py)

```python
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(prompt)
```

## 📈 API Quotas

**Free Tier Limits:**
- 60 requests per minute
- 1,500 requests per day
- Rate limits apply

**Monitor Usage:**
- Check: https://aistudio.google.com/app/apikey
- View quota usage
- Upgrade if needed

## 🐛 Troubleshooting

### Issue: "API key not configured"

**Solution:**
```bash
# Verify .env file
cat .env | grep GEMINI

# Should show: GOOGLE_GEMINI_API_KEY=AIzaSy...

# Restart backend
docker-compose restart backend
```

### Issue: "Invalid API key"

**Solution:**
1. Verify key at: https://aistudio.google.com/app/apikey
2. Check if key is enabled
3. Verify API is activated

### Issue: "Quota exceeded"

**Solution:**
- Wait for quota to reset (daily limit)
- Upgrade to paid tier
- Implement caching to reduce calls

### Issue: JSON parsing errors

**Solution:**
The code now handles markdown code blocks in responses:
```python
# Strips ```json and ``` from responses
if response_text.startswith('```json'):
    response_text = response_text[7:]
```

## 🎯 Next Steps

1. **Test all AI features** in the browser
2. **Monitor API usage** in Google AI Studio
3. **Implement caching** for repeated queries (optional)
4. **Add error handling** for quota limits (optional)

## 📚 Documentation

- **Gemini API Docs:** https://ai.google.dev/docs
- **Python SDK:** https://github.com/google/generative-ai-python
- **API Key Management:** https://aistudio.google.com/app/apikey

## ⚡ Quick Commands

```bash
# Rebuild and restart with Gemini
cd study_hub
docker-compose build backend
docker-compose up -d

# Test AI features
curl -X POST http://localhost:8000/api/doubt-solver/ask_doubt/ \
  -H "Content-Type: application/json" \
  -d '{"problem_description": "Test question"}'

# View logs
docker-compose logs backend | grep -i gemini
```

## ✅ Success Checklist

- [ ] Gemini API key added to .env
- [ ] Backend rebuilt with new dependencies
- [ ] Services restarted
- [ ] Summary generation works
- [ ] Doubt solver responds
- [ ] Concept explainer works
- [ ] No API errors in logs

## 🎉 You're All Set!

Your StudyHub now uses Google Gemini AI for all intelligent features!

**Test it now:**
```bash
cd study_hub
./QUICK_TEST.sh
```

Then visit: http://localhost and try the AI features!

---

**Questions?** Check the main documentation or logs:
```bash
docker-compose logs backend
```
