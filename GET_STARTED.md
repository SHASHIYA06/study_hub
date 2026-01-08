# 🎯 Get Started with StudyHub - Complete Guide

Welcome to StudyHub! This guide will get you up and running in minutes.

## 📋 What You Need

### Required
1. **Docker Desktop** - [Download here](https://www.docker.com/products/docker-desktop/)
2. **Git** - [Download here](https://git-scm.com/downloads)
3. **YouTube API Key** - [Get it here](https://console.cloud.google.com/apis/credentials)
4. **OpenAI API Key** - [Get it here](https://platform.openai.com/api-keys)

### System Requirements
- 4GB RAM (8GB recommended)
- 10GB free disk space
- macOS, Windows, or Linux

## 🚀 Installation (3 Steps)

### Step 1: Get the Code

```bash
# Clone the repository
git clone https://github.com/yourusername/study-hub.git

# Navigate to the project
cd study_hub
```

### Step 2: Configure API Keys

```bash
# Copy the environment template
cp .env.example .env

# Edit the .env file and add your API keys
nano .env
# or use your favorite editor: code .env, vim .env, etc.
```

Add these two lines with your actual keys:
```env
YOUTUBE_API_KEY=your_youtube_api_key_here
OPENAI_API_KEY=sk-your_openai_key_here
```

### Step 3: Run Setup

```bash
# Make scripts executable (Unix/Linux/Mac)
chmod +x scripts/*.sh

# Run the setup script
./scripts/setup.sh

# Or manually:
make build
make up
make migrate
make seed
```

## ✅ Verify Installation

### Check Services
```bash
# View running containers
docker-compose ps

# All should show "Up" and "healthy"
```

### Test the Application

1. **Frontend**: Open http://localhost in your browser
   - You should see the grade selection page
   
2. **Backend API**: Visit http://localhost:8000/api/grades/
   - You should see JSON data with grades
   
3. **Admin Panel**: Go to http://localhost:8000/admin/
   - Login with the superuser you created

## 📱 Using StudyHub

### For Students

1. **Select Your Grade**
   - Choose from Nursery to Class 12
   
2. **Pick a Subject**
   - Science, Math, English, etc.
   
3. **Choose a Chapter**
   - View chapter description and materials
   
4. **Access Learning Tools**
   - Click "Fetch Videos" for educational videos
   - Click "Generate Summary" for AI summaries
   - Click "Generate Flashcards" for study cards
   
5. **Use AI Features**
   - Navigate to "AI Tools" in the menu
   - Ask doubts or get concept explanations

### For Teachers/Admins

1. **Access Admin Panel**
   - Go to http://localhost:8000/admin/
   - Login with superuser credentials
   
2. **Add Content**
   - Add new grades, subjects, chapters
   - Upload study materials
   - Create quizzes
   
3. **Manage Users**
   - Create student accounts
   - Track progress
   - Generate reports

## 🎓 Sample Workflow

### Example: Learning Physics Chapter

1. Visit http://localhost
2. Select "Class 9"
3. Click on "Science"
4. Select "Chapter 1: Motion"
5. Click "Fetch Videos" → Get top educational videos
6. Click "Generate Summary" → Get AI-powered summary
7. Click "Generate Flashcards" → Get study flashcards
8. Navigate to "AI Tools" → Ask doubts

## 🛠️ Common Commands

```bash
# Start application
make up

# Stop application
make down

# View logs
make logs

# Access Django shell
make shell

# Run migrations
make migrate

# Seed database
make seed

# Create admin user
make superuser

# Backup database
make backup-db
```

## 🐛 Troubleshooting

### Issue: Port Already in Use

**Solution**:
```bash
# Stop conflicting services or change ports in docker-compose.yml
# Change "80:80" to "3000:80" for frontend
# Change "8000:8000" to "8001:8000" for backend
```

### Issue: API Keys Not Working

**Solution**:
```bash
# 1. Verify keys in .env file
cat .env | grep -E 'YOUTUBE|OPENAI'

# 2. Restart services
docker-compose restart

# 3. Check logs
docker-compose logs backend
```

### Issue: Database Connection Failed

**Solution**:
```bash
# Reset database
docker-compose down -v
docker-compose up -d
make migrate
make seed
```

### Issue: Frontend Shows Errors

**Solution**:
```bash
# Check if backend is running
curl http://localhost:8000/api/grades/

# Check CORS settings in backend/.env
# Ensure CORS_ALLOWED_ORIGINS includes http://localhost:3000
```

## 📚 Learning Resources

### Documentation
- [README.md](README.md) - Overview and features
- [QUICKSTART.md](QUICKSTART.md) - 5-minute guide
- [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - API reference
- [DEPLOYMENT.md](DEPLOYMENT.md) - Production deployment
- [STARTUP_COMMANDS.md](STARTUP_COMMANDS.md) - Command reference

### Video Tutorials (Coming Soon)
- Installation walkthrough
- Creating your first content
- Using AI features
- Deployment guide

## 🎯 Next Steps

### For Development
1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Set up development environment
3. Explore the codebase
4. Make your first contribution

### For Production
1. Read [DEPLOYMENT.md](DEPLOYMENT.md)
2. Choose deployment platform (AWS, Railway, etc.)
3. Configure domain and SSL
4. Deploy your instance

### For Customization
1. Add more subjects in admin panel
2. Customize frontend theme
3. Add custom features
4. Integrate with your systems

## 💡 Pro Tips

1. **Use Makefile commands** - They're shortcuts for common tasks
   ```bash
   make help  # See all available commands
   ```

2. **Monitor logs** - Keep an eye on what's happening
   ```bash
   make logs  # Or docker-compose logs -f
   ```

3. **Regular backups** - Save your data
   ```bash
   make backup-db  # Creates timestamped backup
   ```

4. **Keep containers updated**
   ```bash
   docker-compose pull
   docker-compose up -d
   ```

## 🆘 Getting Help

### Self-Help
1. Check logs: `docker-compose logs -f backend`
2. Review documentation in this folder
3. Search GitHub issues

### Community Support
- **GitHub Issues**: Report bugs
- **GitHub Discussions**: Ask questions
- **Email**: support@studyhub.com

### Professional Support
- Custom development
- Deployment assistance
- Training and consulting

## ✨ What's Next?

After getting comfortable with StudyHub:

1. **Customize Content**
   - Add subjects relevant to your curriculum
   - Upload custom study materials
   - Create your own quizzes

2. **Extend Features**
   - Add user authentication
   - Implement progress tracking
   - Create mobile app

3. **Deploy to Production**
   - Choose hosting platform
   - Set up domain
   - Configure SSL

4. **Scale Your Platform**
   - Add more servers
   - Implement caching
   - Use CDN for media

## 🎊 Success Checklist

- [ ] Docker and Git installed
- [ ] Repository cloned
- [ ] API keys configured in .env
- [ ] Services started with `make up`
- [ ] Migrations completed
- [ ] Database seeded
- [ ] Frontend accessible at http://localhost
- [ ] Backend API works at http://localhost:8000
- [ ] Admin panel accessible
- [ ] Can fetch videos for a chapter
- [ ] AI features working
- [ ] Ready to add content!

## 🌟 Quick Reference Card

| What | Command | URL |
|------|---------|-----|
| Start | `make up` | - |
| Stop | `make down` | - |
| Frontend | Browser | http://localhost |
| Backend | Browser | http://localhost:8000/api/ |
| Admin | Browser | http://localhost:8000/admin/ |
| Logs | `make logs` | - |
| Shell | `make shell` | - |
| Migrate | `make migrate` | - |

## 🎓 Congratulations!

You're now ready to use StudyHub! 

**Remember**: This is a powerful platform with AI capabilities. The more content you add, the more valuable it becomes for students.

Happy Learning! 📚✨

---

**Questions?** Check [README.md](README.md) or create an issue on GitHub.

**Version**: 1.0.0  
**Last Updated**: January 2024
