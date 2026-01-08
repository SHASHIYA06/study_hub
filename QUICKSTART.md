# 🚀 Quick Start Guide - StudyHub

Get StudyHub running in 5 minutes!

## Prerequisites

- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Docker Compose installed
- YouTube API Key ([Get it here](https://console.cloud.google.com/apis/credentials))
- OpenAI API Key ([Get it here](https://platform.openai.com/api-keys))

## 5-Minute Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/study-hub.git
cd study_hub
```

### 2. Configure Environment

```bash
cp .env.example .env
nano .env  # or use your favorite editor
```

Add your API keys:
```env
YOUTUBE_API_KEY=your_youtube_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Run Setup Script

```bash
./scripts/setup.sh
```

Or manually:

```bash
# Build images
docker-compose build

# Start services
docker-compose up -d

# Run migrations
docker-compose exec backend python manage.py migrate

# Seed database
docker-compose exec backend python manage.py seed_data

# Create admin user
docker-compose exec backend python manage.py createsuperuser
```

### 4. Access Application

- **Frontend**: http://localhost
- **Backend API**: http://localhost:8000/api/
- **Admin Panel**: http://localhost:8000/admin/

## Using the Application

### 1. Browse Grades
- Visit http://localhost
- Select a grade (Nursery to Class 12)

### 2. Explore Subjects
- Click on a subject to see chapters
- Each subject has organized chapters

### 3. Study Materials
- Click on a chapter to view:
  - Fetch educational videos
  - Generate AI summaries
  - Create flashcards
  - Take quizzes

### 4. AI Features
- Navigate to "AI Tools" in the menu
- **Doubt Solver**: Ask any question
- **Concept Explainer**: Get simple explanations

## Common Commands

```bash
# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Restart services
docker-compose restart

# Access backend shell
docker-compose exec backend python manage.py shell

# Create superuser
docker-compose exec backend python manage.py createsuperuser
```

## Troubleshooting

### Port Already in Use

```bash
# Change ports in docker-compose.yml
# Frontend: Change "80:80" to "3000:80"
# Backend: Change "8000:8000" to "8001:8000"
```

### Database Connection Error

```bash
# Reset database
docker-compose down -v
docker-compose up -d
docker-compose exec backend python manage.py migrate
```

### API Keys Not Working

1. Check if keys are correct in `.env`
2. Restart services: `docker-compose restart`
3. Check logs: `docker-compose logs backend`

## Next Steps

- Read the [full README](README.md)
- Check [deployment guide](DEPLOYMENT.md)
- Explore the API documentation
- Customize for your needs

## Need Help?

- Check logs: `docker-compose logs -f backend`
- Create an issue on GitHub
- Read the documentation

---

Happy Learning! 📚
