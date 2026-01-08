# 📚 StudyHub - Comprehensive Learning Platform

A full-stack educational platform providing study materials, AI-powered learning tools, and interactive content for students from Nursery to Class 12.

## 🌟 Features

### Core Features
- **Grade-based Learning**: Organized content from Nursery to Class 12
- **Subject-wise Chapters**: Structured curriculum for all major subjects
- **Study Materials**: Videos, notes, quizzes, and formula sheets
- **Progress Tracking**: Monitor learning progress per chapter

### AI-Powered Features
- **Video Fetching**: Automatically curate educational YouTube videos
- **AI Summary Generator**: Generate bullet-point summaries of chapters
- **Auto Quiz Generator**: Create MCQ quizzes from chapter content
- **Doubt Solver**: Get step-by-step solutions to problems
- **Concept Explainer**: Simple explanations of complex topics
- **Flashcard Generator**: Auto-create flashcards for memorization

## 🛠️ Tech Stack

### Backend
- **Django 4.2**: Web framework
- **Django REST Framework**: API development
- **PostgreSQL**: Database
- **Redis**: Caching and Celery broker
- **Celery**: Async task processing
- **Gunicorn**: WSGI server

### Frontend
- **React 18**: UI framework
- **React Router**: Navigation
- **Axios**: HTTP client
- **CSS3**: Styling

### External APIs
- **YouTube Data API v3**: Video fetching
- **OpenAI GPT-3.5**: AI features

### Infrastructure
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **Nginx**: Reverse proxy and static file serving

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- YouTube API Key ([Get it here](https://console.cloud.google.com/apis/credentials))
- OpenAI API Key ([Get it here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/study-hub.git
   cd study_hub
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

3. **Build and start services**
   ```bash
   make build
   make up
   ```

4. **Run migrations and seed data**
   ```bash
   make migrate
   make seed
   ```

5. **Create a superuser (optional)**
   ```bash
   make superuser
   ```

6. **Access the application**
   - Frontend: http://localhost
   - Backend API: http://localhost:8000/api/
   - Admin Panel: http://localhost:8000/admin/

## 📖 Usage

### Using Makefile Commands

```bash
# Start all services
make up

# View logs
make logs

# Run migrations
make migrate

# Seed database
make seed

# Create superuser
make superuser

# Stop all services
make down

# Clean up (removes volumes)
make clean

# Development mode
make dev-up
```

### Manual Docker Compose Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f backend

# Execute commands in backend
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py seed_data
```

## 📂 Project Structure

```
study_hub/
├── backend/                 # Django backend
│   ├── app/                # Main application
│   │   ├── models.py       # Database models
│   │   ├── views.py        # API views
│   │   ├── serializers.py  # DRF serializers
│   │   ├── ai_utils.py     # AI utilities
│   │   └── youtube_utils.py # YouTube API utilities
│   ├── study_hub/          # Project settings
│   ├── manage.py
│   └── requirements.txt
├── frontend/               # React frontend
│   ├── src/
│   │   ├── pages/         # Page components
│   │   ├── App.js
│   │   └── api.js         # API client
│   ├── public/
│   └── package.json
├── docker-compose.yml     # Production compose file
├── docker-compose.dev.yml # Development compose file
├── Makefile              # Convenience commands
└── README.md
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Database
POSTGRES_DB=study_hub
POSTGRES_USER=study_hub_user
POSTGRES_PASSWORD=your_secure_password

# Django
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# API Keys
YOUTUBE_API_KEY=your_youtube_api_key
OPENAI_API_KEY=your_openai_api_key

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
```

## 🌐 API Documentation

### Endpoints

#### Grades
- `GET /api/grades/` - List all grades
- `GET /api/grades/{id}/` - Get specific grade

#### Subjects
- `GET /api/subjects/` - List all subjects
- `GET /api/subjects/?grade_id={id}` - Filter by grade

#### Chapters
- `GET /api/chapters/` - List all chapters
- `GET /api/chapters/?subject_id={id}` - Filter by subject
- `GET /api/chapters/{id}/fetch_videos/` - Fetch YouTube videos
- `POST /api/chapters/{id}/generate_summary/` - Generate AI summary
- `POST /api/chapters/{id}/generate_quiz/` - Generate quiz
- `POST /api/chapters/{id}/generate_flashcards/` - Generate flashcards

#### AI Features
- `POST /api/doubt-solver/ask_doubt/` - Solve student doubts
- `POST /api/explain/explain/` - Explain concepts

## 🧪 Testing

Run tests:
```bash
make test
```

Or manually:
```bash
docker-compose exec backend python manage.py test
```

## 📊 Database Management

### Backup Database
```bash
make backup-db
```

### Restore Database
```bash
make restore-db BACKUP_FILE=backup_20240101_120000.sql
```

## 🚀 Deployment

### Deployment Options

1. **Docker-based deployment** (Recommended)
2. **AWS EC2** with Docker
3. **Railway** (PaaS)
4. **Render** (PaaS)
5. **Heroku** (PaaS)

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed deployment instructions.

## 📝 Development

### Development Mode

```bash
# Start development environment
make dev-up

# Frontend will be available at http://localhost:3000
# Backend will be available at http://localhost:8000
```

### Adding New Features

1. Backend: Add models in `backend/app/models.py`
2. Create serializers in `backend/app/serializers.py`
3. Add views in `backend/app/views.py`
4. Frontend: Create pages in `frontend/src/pages/`
5. Add API calls in `frontend/src/api.js`

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- YouTube Data API for video content
- OpenAI for AI-powered features
- All open-source contributors

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Email: support@studyhub.com

## 🔮 Future Enhancements

- [ ] User authentication and profiles
- [ ] Real-time progress tracking
- [ ] Gamification (badges, leaderboards)
- [ ] Mobile app (React Native)
- [ ] Live classes integration
- [ ] Parent dashboard
- [ ] Offline mode
- [ ] Multi-language support

---

Made with ❤️ for students everywhere
