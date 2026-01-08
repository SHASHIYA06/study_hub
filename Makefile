.PHONY: help build up down logs test clean migrate shell seed

help:
	@echo "StudyHub Docker Commands"
	@echo "========================"
	@echo "make build          - Build Docker images"
	@echo "make up             - Start services"
	@echo "make down           - Stop services"
	@echo "make logs           - View logs"
	@echo "make migrate        - Run migrations"
	@echo "make seed           - Seed database with sample data"
	@echo "make shell          - Open Django shell"
	@echo "make superuser      - Create Django superuser"
	@echo "make clean          - Remove containers and volumes"
	@echo ""
	@echo "Development Commands:"
	@echo "make dev-build      - Build development images"
	@echo "make dev-up         - Start development services"
	@echo "make dev-down       - Stop development services"

# Production commands
build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

migrate:
	docker-compose exec backend python manage.py migrate

seed:
	docker-compose exec backend python manage.py seed_data

shell:
	docker-compose exec backend python manage.py shell

superuser:
	docker-compose exec backend python manage.py createsuperuser

test:
	docker-compose exec backend python manage.py test

clean:
	docker-compose down -v
	docker system prune -f

# Development commands
dev-build:
	docker-compose -f docker-compose.dev.yml build

dev-up:
	docker-compose -f docker-compose.dev.yml up -d

dev-down:
	docker-compose -f docker-compose.dev.yml down

dev-logs:
	docker-compose -f docker-compose.dev.yml logs -f

# Database backup
backup-db:
	docker-compose exec -T db pg_dump -U study_hub_user study_hub > backup_$(shell date +%Y%m%d_%H%M%S).sql

# Database restore
restore-db:
	@if [ -z "$(BACKUP_FILE)" ]; then \
		echo "Usage: make restore-db BACKUP_FILE=backup.sql"; \
	else \
		docker-compose exec -T db psql -U study_hub_user study_hub < $(BACKUP_FILE); \
	fi
