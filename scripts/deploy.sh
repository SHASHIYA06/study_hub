#!/bin/bash

set -e

echo "🚀 StudyHub Production Deployment"
echo "===================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
DOMAIN=${1:-yourdomain.com}
ENV_FILE=".env"

echo -e "${YELLOW}Step 1: Pre-deployment checks${NC}"
if [ ! -f "$ENV_FILE" ]; then
    echo -e "${RED}Error: $ENV_FILE not found!${NC}"
    exit 1
fi

echo -e "${GREEN}✓ .env file found${NC}"

echo -e "${YELLOW}Step 2: Stopping existing services${NC}"
docker-compose down || true
echo -e "${GREEN}✓ Services stopped${NC}"

echo -e "${YELLOW}Step 3: Building Docker images${NC}"
docker-compose build --no-cache
echo -e "${GREEN}✓ Images built${NC}"

echo -e "${YELLOW}Step 4: Starting services${NC}"
docker-compose up -d
echo -e "${GREEN}✓ Services started${NC}"

echo -e "${YELLOW}Step 5: Waiting for services to be ready${NC}"
sleep 10

echo -e "${YELLOW}Step 6: Running migrations${NC}"
docker-compose exec -T backend python manage.py migrate
echo -e "${GREEN}✓ Migrations completed${NC}"

echo -e "${YELLOW}Step 7: Collecting static files${NC}"
docker-compose exec -T backend python manage.py collectstatic --noinput
echo -e "${GREEN}✓ Static files collected${NC}"

echo -e "${YELLOW}Step 8: Health checks${NC}"
sleep 5

# Check backend
if curl -f http://localhost:8000/api/grades/ > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Backend API is responding${NC}"
else
    echo -e "${RED}✗ Backend API check failed!${NC}"
    exit 1
fi

# Check frontend
if curl -f http://localhost/ > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Frontend is responding${NC}"
else
    echo -e "${RED}✗ Frontend check failed!${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}===================================="
echo "✅ DEPLOYMENT SUCCESSFUL!"
echo "====================================${NC}"
echo ""
echo "📊 Service Status:"
docker-compose ps
echo ""
echo "🌐 Access URLs:"
echo "  Frontend:  http://$DOMAIN"
echo "  Backend:   http://$DOMAIN:8000"
echo "  Admin:     http://$DOMAIN:8000/admin"
echo ""
echo "📝 Useful Commands:"
echo "  View logs:     docker-compose logs -f"
echo "  Stop:          docker-compose down"
echo "  Restart:       docker-compose restart"
echo ""
