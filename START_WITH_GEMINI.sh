#!/bin/bash

echo "🚀 Starting StudyHub with Google Gemini AI..."
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file with Gemini API key..."
    cp .env.example .env
    # Add Gemini key
    sed -i.bak 's/GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key_here/GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM/' .env
    echo "✅ .env file created with Gemini API key"
else
    echo "✅ .env file exists"
    # Update Gemini key if needed
    if ! grep -q "AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM" .env; then
        echo "📝 Adding Gemini API key to .env..."
        sed -i.bak 's/GOOGLE_GEMINI_API_KEY=.*/GOOGLE_GEMINI_API_KEY=AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM/' .env
    fi
fi

echo ""
echo "🐳 Building Docker containers with Gemini support..."
docker-compose build backend

echo ""
echo "🚀 Starting all services..."
docker-compose up -d

echo ""
echo "⏳ Waiting for services to start (15 seconds)..."
sleep 15

echo ""
echo "🗄️ Running database migrations..."
docker-compose exec -T backend python manage.py migrate

echo ""
echo "🌱 Seeding database with sample data..."
docker-compose exec -T backend python manage.py seed_data

echo ""
echo "✅ Setup complete!"
echo ""
echo "🌐 Access your application:"
echo "   Frontend:  http://localhost"
echo "   Backend:   http://localhost:8000/api/"
echo "   Admin:     http://localhost:8000/admin/"
echo ""
echo "🤖 AI Features (powered by Google Gemini):"
echo "   • Generate Summaries"
echo "   • Create Quizzes"
echo "   • Generate Flashcards"
echo "   • Solve Doubts"
echo "   • Explain Concepts"
echo ""
echo "📚 Read GEMINI_SETUP.md for more details"
echo ""
