# ✅ Installation Checklist - StudyHub

Use this checklist to ensure successful installation and deployment of StudyHub.

## Pre-Installation

### System Requirements
- [ ] Docker installed (version 20.10+)
- [ ] Docker Compose installed (version 2.0+)
- [ ] Git installed
- [ ] 4GB RAM minimum (8GB recommended)
- [ ] 10GB free disk space
- [ ] Internet connection

### API Keys Required
- [ ] YouTube Data API v3 key obtained
  - Visit: https://console.cloud.google.com/apis/credentials
  - Enable YouTube Data API v3
  - Create credentials (API key)
  
- [ ] OpenAI API key obtained
  - Visit: https://platform.openai.com/api-keys
  - Create new secret key
  - Note: Requires credits/billing setup

### Optional
- [ ] Domain name (for production)
- [ ] SSL certificate (for HTTPS)
- [ ] SMTP credentials (for email)

## Installation Steps

### 1. Clone Repository
- [ ] Repository cloned successfully
  ```bash
  git clone https://github.com/yourusername/study-hub.git
  cd study_hub
  ```

### 2. Environment Configuration
- [ ] `.env` file created from template
  ```bash
  cp .env.example .env
  ```

- [ ] Required environment variables set:
  - [ ] `YOUTUBE_API_KEY`
  - [ ] `OPENAI_API_KEY`
  - [ ] `SECRET_KEY` (generate new for production)
  - [ ] `POSTGRES_PASSWORD` (change from default)
  - [ ] `DEBUG` (set to False for production)
  - [ ] `ALLOWED_HOSTS` (add your domain)
  - [ ] `CORS_ALLOWED_ORIGINS` (add your frontend URL)

### 3. Build Docker Images
- [ ] Backend image built successfully
  ```bash
  docker-compose build backend
  ```

- [ ] Frontend image built successfully
  ```bash
  docker-compose build frontend
  ```

- [ ] All images built
  ```bash
  make build
  ```

### 4. Start Services
- [ ] All containers started
  ```bash
  make up
  ```

- [ ] Database container healthy
  ```bash
  docker-compose ps db
  ```

- [ ] Redis container healthy
  ```bash
  docker-compose ps redis
  ```

- [ ] Backend container running
  ```bash
  docker-compose ps backend
  ```

- [ ] Frontend container running
  ```bash
  docker-compose ps frontend
  ```

### 5. Database Setup
- [ ] Migrations completed
  ```bash
  make migrate
  ```

- [ ] Sample data seeded
  ```bash
  make seed
  ```

- [ ] Superuser created
  ```bash
  make superuser
  ```
  - Username: ___________
  - Email: ___________
  - Password: ___________

### 6. Verification

#### Backend Verification
- [ ] Backend API accessible at http://localhost:8000/api/
- [ ] Admin panel accessible at http://localhost:8000/admin/
- [ ] Can login to admin panel
- [ ] Grades endpoint returns data:
  ```bash
  curl http://localhost:8000/api/grades/
  ```

#### Frontend Verification
- [ ] Frontend accessible at http://localhost
- [ ] Grade selection page loads
- [ ] Can navigate to subjects
- [ ] Can view chapters
- [ ] AI features page accessible

#### Feature Testing
- [ ] Can fetch videos for a chapter
- [ ] Can generate summary (requires chapter with content)
- [ ] Can generate flashcards (requires chapter with content)
- [ ] Doubt solver works
- [ ] Concept explainer works

### 7. Logs Check
- [ ] No critical errors in backend logs
  ```bash
  docker-compose logs backend
  ```

- [ ] No errors in frontend logs
  ```bash
  docker-compose logs frontend
  ```

- [ ] Database logs show successful connections
  ```bash
  docker-compose logs db
  ```

## Post-Installation

### Security
- [ ] Changed default admin password
- [ ] Changed SECRET_KEY from default
- [ ] Changed database password from default
- [ ] Set DEBUG=False in production
- [ ] Configured ALLOWED_HOSTS properly
- [ ] Configured CORS_ALLOWED_ORIGINS properly

### Performance
- [ ] Static files collected
  ```bash
  docker-compose exec backend python manage.py collectstatic
  ```

- [ ] Database queries optimized
- [ ] Redis cache working

### Monitoring
- [ ] Health checks passing
- [ ] Logs rotating properly
- [ ] Disk space monitored
- [ ] Backup strategy in place

### Documentation
- [ ] Read README.md
- [ ] Reviewed QUICKSTART.md
- [ ] Understood API_DOCUMENTATION.md
- [ ] Reviewed DEPLOYMENT.md

## Production Deployment

### Pre-Production
- [ ] All tests passing
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] Backup taken

### Domain & SSL
- [ ] Domain configured
- [ ] DNS records set
- [ ] SSL certificate obtained (Let's Encrypt)
- [ ] HTTPS configured
- [ ] HTTP to HTTPS redirect enabled

### Server Setup
- [ ] Firewall configured
- [ ] Ports opened (80, 443)
- [ ] SSH keys configured
- [ ] Regular backups scheduled

### Final Checks
- [ ] Application accessible via domain
- [ ] HTTPS working
- [ ] All features functional
- [ ] Performance acceptable
- [ ] Monitoring configured

## Troubleshooting

### Common Issues

#### Port Already in Use
- [ ] Checked for conflicting services
- [ ] Changed ports in docker-compose.yml if needed

#### Database Connection Failed
- [ ] Verified DATABASE_URL format
- [ ] Checked database container status
- [ ] Reviewed database logs

#### API Keys Not Working
- [ ] Verified keys are correct
- [ ] Restarted backend container
- [ ] Checked API quota limits

#### Frontend Can't Reach Backend
- [ ] Verified REACT_APP_API_URL
- [ ] Checked CORS settings
- [ ] Verified network connectivity

## Maintenance Tasks

### Daily
- [ ] Monitor logs
- [ ] Check disk space
- [ ] Verify backups

### Weekly
- [ ] Review error logs
- [ ] Check performance metrics
- [ ] Update dependencies (if needed)

### Monthly
- [ ] Security updates
- [ ] Database optimization
- [ ] Review and clean old data

## Success Criteria

✅ All items checked = Ready for use!

### Minimum Requirements
- [ ] Application accessible
- [ ] No critical errors
- [ ] Core features working
- [ ] Documentation reviewed

### Production Ready
- [ ] HTTPS enabled
- [ ] Backups configured
- [ ] Monitoring active
- [ ] Performance optimized
- [ ] Security hardened

## Support

If you encounter issues:

1. Check logs: `make logs`
2. Review documentation
3. Search GitHub issues
4. Create new issue with:
   - Checklist status
   - Error messages
   - Environment details

## Notes

Date installed: ___________  
Installed by: ___________  
Environment: ☐ Development ☐ Production  
Domain: ___________  

---

**Need help?** Check [README.md](README.md) or [DEPLOYMENT.md](DEPLOYMENT.md)
