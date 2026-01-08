#!/bin/bash

set -e

echo "🛠️  StudyHub Initial Setup"
echo "=========================="

# Check if .env exists
if [ ! -f .env ]; then
    echo "📋 Creating .env file from template..."
    cp .env.example .env
    echo "✅ .env file created. Please edit it with your API keys."
    echo ""
    echo "Required API keys:"
    echo "  - YOUTUBE_API_KEY: https://console.cloud.google.com/apis/credentials"
    echo "  - OPENAI_API_KEY: https://platform.openai.com/api-keys"
    echo ""
    read -p "Press Enter after updating .env file..."
fi

echo "🐳 Building Docker images..."
docker-compose build

echo "🚀 Starting services..."
docker-compose up -d

echo "⏳ Waiting for database to be ready..."
sleep 10

echo "📊 Running migrations..."
docker-compose exec backend python manage.py migrate

echo "🌱 Seeding database with sample data..."
docker-compose exec backend python manage.py seed_data

echo "👤 Creating superuser..."
docker-compose exec backend python manage.py createsuperuser --noinput --username admin --email admin@example.com || true

echo ""
echo "✅ Setup complete!"
echo ""
echo "🌐 Access the application:"
echo "  Frontend: http://localhost"
echo "  Backend:  http://localhost:8000"
echo "  Admin:    http://localhost:8000/admin"
echo ""
echo "📝 Next steps:"
echo "  1. Visit http://localhost to see the app"
echo "  2. Login to admin panel with username: admin"
echo "  3. Explore the API at http://localhost:8000/api/"
echo ""
