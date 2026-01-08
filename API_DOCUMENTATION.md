# 📖 API Documentation - StudyHub

Complete REST API documentation for StudyHub backend.

## Base URL

```
http://localhost:8000/api/
```

## Authentication

Currently, most endpoints are public. Authentication is required for:
- Student Progress endpoints

## Endpoints

### Grades

#### List All Grades

```http
GET /api/grades/
```

**Response:**
```json
{
  "count": 15,
  "results": [
    {
      "id": 1,
      "level": "nursery",
      "description": "Early childhood education"
    },
    {
      "id": 9,
      "level": "class_9",
      "description": "Secondary School - Grade 9"
    }
  ]
}
```

#### Get Single Grade

```http
GET /api/grades/{id}/
```

**Response:**
```json
{
  "id": 9,
  "level": "class_9",
  "description": "Secondary School - Grade 9"
}
```

---

### Subjects

#### List All Subjects

```http
GET /api/subjects/
```

**Query Parameters:**
- `grade_id` (optional): Filter subjects by grade

**Example:**
```http
GET /api/subjects/?grade_id=9
```

**Response:**
```json
{
  "count": 4,
  "results": [
    {
      "id": 1,
      "name": "science",
      "description": "Physics, Chemistry, Biology",
      "grade": 9
    },
    {
      "id": 2,
      "name": "mathematics",
      "description": "Algebra, Geometry, Trigonometry",
      "grade": 9
    }
  ]
}
```

---

### Chapters

#### List All Chapters

```http
GET /api/chapters/
```

**Query Parameters:**
- `subject_id` (optional): Filter chapters by subject

**Example:**
```http
GET /api/chapters/?subject_id=1
```

**Response:**
```json
{
  "count": 3,
  "results": [
    {
      "id": 1,
      "title": "Motion",
      "description": "Understanding motion, speed, velocity",
      "chapter_number": 1,
      "content": "Motion is the change in position...",
      "materials": [],
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### Get Single Chapter

```http
GET /api/chapters/{id}/
```

#### Fetch Videos for Chapter

```http
GET /api/chapters/{id}/fetch_videos/
```

**Description:** Fetches educational videos from YouTube for the chapter.

**Response:**
```json
{
  "videos": [
    {
      "title": "Class 9 Motion - Complete Chapter",
      "video_id": "abc123xyz",
      "thumbnail": "https://i.ytimg.com/vi/abc123xyz/hqdefault.jpg",
      "channel": "Physics Wallah",
      "description": "Complete explanation of motion...",
      "quality_score": 80
    }
  ]
}
```

#### Generate Chapter Summary

```http
POST /api/chapters/{id}/generate_summary/
```

**Description:** Generates AI-powered bullet-point summary of chapter content.

**Response:**
```json
{
  "summary": "• Motion is change of position\n• Speed = Distance/Time\n• Velocity = Displacement/Time",
  "chapter_id": 1
}
```

#### Generate Quiz

```http
POST /api/chapters/{id}/generate_quiz/
```

**Request Body:**
```json
{
  "num_questions": 10
}
```

**Description:** Generates MCQ quiz from chapter content.

**Response:**
```json
{
  "id": 1,
  "title": "AI Generated Quiz - Motion",
  "questions": [
    {
      "id": 1,
      "question_text": "What is motion?",
      "question_type": "mcq",
      "difficulty": 1,
      "choices": [
        {
          "id": 1,
          "choice_text": "Change in position",
          "is_correct": true,
          "order": 0
        }
      ]
    }
  ],
  "created_at": "2024-01-01T00:00:00Z"
}
```

#### Generate Flashcards

```http
POST /api/chapters/{id}/generate_flashcards/
```

**Request Body:**
```json
{
  "num_cards": 10
}
```

**Response:**
```json
[
  {
    "id": 1,
    "question": "What is motion?",
    "answer": "Motion is the change in position of an object with respect to time",
    "created_at": "2024-01-01T00:00:00Z"
  }
]
```

---

### Study Materials

#### List Materials

```http
GET /api/materials/
```

**Query Parameters:**
- `chapter_id` (optional): Filter by chapter

**Response:**
```json
{
  "count": 5,
  "results": [
    {
      "id": 1,
      "title": "Motion - Khan Academy",
      "material_type": "video",
      "content": null,
      "video_url": "https://youtube.com/watch?v=xyz",
      "video_id": "xyz",
      "source": "YouTube",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

---

### Quizzes

#### List Quizzes

```http
GET /api/quizzes/
```

**Query Parameters:**
- `chapter_id` (optional): Filter by chapter

**Response:**
```json
{
  "count": 2,
  "results": [
    {
      "id": 1,
      "title": "Motion Quiz",
      "questions": [...],
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

---

### Flashcards

#### List Flashcards

```http
GET /api/flashcards/
```

**Query Parameters:**
- `chapter_id` (optional): Filter by chapter

**Response:**
```json
{
  "count": 10,
  "results": [
    {
      "id": 1,
      "question": "What is velocity?",
      "answer": "Rate of change of displacement",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

---

### AI Features

#### Solve Doubt

```http
POST /api/doubt-solver/ask_doubt/
```

**Request Body:**
```json
{
  "problem_description": "I don't understand how to solve quadratic equations"
}
```

**Response:**
```json
{
  "solution": "Step 1: Identify coefficients a, b, c\nStep 2: Use quadratic formula...",
  "problem": "I don't understand how to solve quadratic equations"
}
```

#### Explain Concept

```http
POST /api/explain/explain/
```

**Request Body:**
```json
{
  "concept": "Photosynthesis",
  "grade": "9"
}
```

**Response:**
```json
{
  "concept": "Photosynthesis",
  "explanation": "Photosynthesis is the process by which plants make food using sunlight..."
}
```

---

### Student Progress (Authentication Required)

#### List Student Progress

```http
GET /api/progress/
```

**Headers:**
```
Authorization: Bearer {token}
```

**Response:**
```json
{
  "count": 5,
  "results": [
    {
      "id": 1,
      "chapter": 1,
      "status": "in_progress",
      "progress_percentage": 60,
      "last_studied": "2024-01-01T12:00:00Z"
    }
  ]
}
```

#### Update Progress

```http
POST /api/progress/update_progress/
```

**Headers:**
```
Authorization: Bearer {token}
```

**Request Body:**
```json
{
  "chapter_id": 1,
  "status": "mastered",
  "progress_percentage": 100
}
```

**Response:**
```json
{
  "id": 1,
  "chapter": 1,
  "status": "mastered",
  "progress_percentage": 100,
  "last_studied": "2024-01-01T12:00:00Z"
}
```

---

## Status Codes

| Code | Description |
|------|-------------|
| 200  | Success |
| 201  | Created |
| 400  | Bad Request |
| 401  | Unauthorized |
| 404  | Not Found |
| 500  | Internal Server Error |

## Error Response Format

```json
{
  "error": "Error message description"
}
```

## Rate Limiting

Currently no rate limiting is implemented. In production, consider:
- 100 requests per minute for authenticated users
- 30 requests per minute for anonymous users

## Pagination

All list endpoints support pagination:

**Query Parameters:**
- `page`: Page number (default: 1)
- `page_size`: Items per page (default: 20)

**Example:**
```http
GET /api/chapters/?page=2&page_size=10
```

## Testing with cURL

### Fetch Grades
```bash
curl http://localhost:8000/api/grades/
```

### Fetch Videos for Chapter
```bash
curl http://localhost:8000/api/chapters/1/fetch_videos/
```

### Generate Summary
```bash
curl -X POST http://localhost:8000/api/chapters/1/generate_summary/
```

### Solve Doubt
```bash
curl -X POST http://localhost:8000/api/doubt-solver/ask_doubt/ \
  -H "Content-Type: application/json" \
  -d '{"problem_description": "What is Newton'\''s first law?"}'
```

## API Client Libraries

### Python
```python
import requests

response = requests.get('http://localhost:8000/api/grades/')
grades = response.json()
```

### JavaScript
```javascript
fetch('http://localhost:8000/api/grades/')
  .then(response => response.json())
  .then(data => console.log(data));
```

### Using Axios (React)
```javascript
import axios from 'axios';

const fetchGrades = async () => {
  const response = await axios.get('http://localhost:8000/api/grades/');
  return response.data;
};
```

---

## WebSocket Support (Future)

Real-time features (planned):
- Live doubt solving
- Real-time progress updates
- Collaborative study sessions

---

**Need more help?** Check the [main README](README.md) or create an issue on GitHub.
