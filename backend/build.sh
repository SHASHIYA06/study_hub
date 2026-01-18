#!/usr/bin/env bash
# Build script for Render deployment
set -o errexit

echo "🔧 Installing dependencies..."
pip install -r requirements.txt

echo "📦 Collecting static files..."
python manage.py collectstatic --no-input

echo "🗄️  Running database migrations..."
python manage.py migrate --no-input

echo "🌱 Seeding database with initial data..."
python manage.py seed_data || echo "⚠️  Seeding skipped (may already exist)"

echo "✅ Build complete!"
