# 🚀 StudyHub Startup Commands - Quick Reference

## First Time Setup

```bash
# 1. Clone and navigate
git clone https://github.com/yourusername/study-hub.git
cd study_hub

# 2. Configure environment
cp .env.example .env
nano .env  # Add your API keys

# 3. One-command setup
./scripts/setup.sh
```

## Daily Development

```bash
# Start everything
make up

# View logs
make logs

# Stop everything
make down
```

## Docker Compose Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# Rebuild and start
docker-compose up -d --build

# View logs (all services)
docker-compose logs -f

# View logs (specific service)
docker-compose logs -f backend
docker-compose logs -f frontend

# Check status
docker-compose ps

# Restart specific service
docker-compose restart backend
```

## Database Commands

```bash
# Run migrations
make migrate
# or
docker-compose exec backend python manage.py migrate

# Create migrations
docker-compose exec backend python manage.py makemigrations

# Seed database
make seed
# or
docker-compose exec backend python manage.py seed_data

# Database shell
docker-compose exec db psql -U study_hub_user study_hub

# Backup database
make backup-db

# Restore database
make restore-db BACKUP_FILE=backup.sql
```

## Backend Commands

```bash
# Django shell
make shell
# or
docker-compose exec backend python manage.py shell

# Create superuser
make superuser
# or
docker-compose exec backend python manage.py createsuperuser

# Collect static files
docker-compose exec backend python manage.py collectstatic

# Run tests
make test
# or
docker-compose exec backend python manage.py test
```

## Frontend Commands

```bash
# Access frontend container
docker-compose exec frontend sh

# View frontend logs
docker-compose logs -f frontend
```

## Development Mode

```bash
# Start development environment
make dev-up

# Stop development environment
make dev-down

# View development logs
make dev-logs
```

## Cleaning Up

```bash
# Stop and remove containers
docker-compose down

# Stop and remove containers + volumes (⚠️ deletes data)
docker-compose down -v

# Remove unused Docker resources
docker system prune -f

# Complete cleanup
make clean
```

## Troubleshooting Commands

```bash
# Check container status
docker-compose ps

# View all logs
docker-compose logs

# Restart all services
docker-compose restart

# Rebuild specific service
docker-compose build backend
docker-compose up -d backend

# Access backend shell
docker-compose exec backend bash

# Check database connection
docker-compose exec backend python manage.py check

# Test database
docker-compose exec db pg_isready -U study_hub_user
```

## Production Deployment

```bash
# Deploy to production
./scripts/deploy.sh yourdomain.com

# Or manually:
docker-compose build
docker-compose up -d
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic --noinput
```

## Monitoring

```bash
# View resource usage
docker stats

# Check container logs
make logs

# Health check
curl http://localhost:8000/api/grades/
curl http://localhost/
```

## Quick Access URLs

- **Frontend**: http://localhost
- **Backend API**: http://localhost:8000/api/
- **Admin Panel**: http://localhost:8000/admin/
- **API Docs**: http://localhost:8000/api/schema/

## Environment Variables

```bash
# View current environment
docker-compose exec backend env | grep -E 'YOUTUBE|OPENAI|DEBUG'

# Restart after changing .env
docker-compose restart
```

## Useful Aliases (Add to ~/.bashrc or ~/.zshrc)

```bash
alias sh-up='cd ~/study_hub && make up'
alias sh-down='cd ~/study_hub && make down'
alias sh-logs='cd ~/study_hub && make logs'
alias sh-shell='cd ~/study_hub && make shell'
alias sh-migrate='cd ~/study_hub && make migrate'
```

## Emergency Commands

```bash
# Force stop all containers
docker-compose kill

# Remove stuck containers
docker-compose rm -f

# Reset everything (⚠️ DANGER: deletes all data)
docker-compose down -v
rm -rf backend/media backend/staticfiles
docker-compose up -d --build
make migrate
make seed
```

## Performance Commands

```bash
# Check disk usage
docker system df

# Clean up unused images
docker image prune -a

# View container resource usage
docker stats --no-stream
```

---

**Pro Tip**: Use `make help` to see all available Makefile commands!
