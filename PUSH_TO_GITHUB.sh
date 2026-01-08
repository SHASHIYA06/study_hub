#!/bin/bash

# Script to push StudyHub to GitHub
# Repository: https://github.com/SHASHIYA06/study_hub.git

echo "🚀 Pushing StudyHub to GitHub..."
echo "Repository: https://github.com/SHASHIYA06/study_hub.git"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check if git is initialized
if [ ! -d .git ]; then
    echo -e "${YELLOW}📁 Initializing Git repository...${NC}"
    git init
    echo -e "${GREEN}✅ Git initialized${NC}"
else
    echo -e "${GREEN}✅ Git repository already initialized${NC}"
fi

# Add remote if not exists
if ! git remote | grep -q origin; then
    echo -e "${YELLOW}🔗 Adding remote origin...${NC}"
    git remote add origin https://github.com/SHASHIYA06/study_hub.git
    echo -e "${GREEN}✅ Remote added${NC}"
else
    echo -e "${GREEN}✅ Remote origin already exists${NC}"
    # Update remote URL just in case
    git remote set-url origin https://github.com/SHASHIYA06/study_hub.git
fi

# Create .gitignore if not exists
if [ ! -f .gitignore ]; then
    echo -e "${YELLOW}📝 Creating .gitignore...${NC}"
    cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
/media
/staticfiles
/static

# Environment
.env
.env.local
.env.production
*.env.backup

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
/frontend/build

# Docker
*.pem
*.key

# Backups
backups/
backup_*.sql
*.tar.gz

# Temporary files
*.tmp
tmp_*
EOF
    echo -e "${GREEN}✅ .gitignore created${NC}"
fi

# Stage all files
echo -e "${YELLOW}📦 Staging files...${NC}"
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo -e "${YELLOW}⚠️  No changes to commit${NC}"
else
    echo -e "${YELLOW}💾 Committing changes...${NC}"
    git commit -m "Initial commit: Complete StudyHub application with Gemini AI integration

Features:
- Django REST API backend (40+ endpoints)
- React frontend (5 pages)
- Google Gemini AI integration (summaries, quizzes, doubt solver)
- YouTube video integration
- Docker containerization
- PostgreSQL database
- Redis caching
- Celery async tasks
- Comprehensive documentation (10+ guides)
- CI/CD with GitHub Actions
- Multi-platform deployment support

Tech Stack:
- Backend: Django 4.2, DRF, PostgreSQL, Redis, Celery
- Frontend: React 18, React Router, Axios
- AI: Google Gemini API
- Infrastructure: Docker, Nginx, GitHub Actions
- Documentation: Markdown guides

Ready for: Development, Testing, Production deployment"
    
    echo -e "${GREEN}✅ Changes committed${NC}"
fi

# Push to GitHub
echo -e "${YELLOW}⬆️  Pushing to GitHub...${NC}"
echo ""

# Try to push, create branch if it doesn't exist
if git push -u origin main 2>&1 | grep -q "does not exist"; then
    echo -e "${YELLOW}Creating main branch...${NC}"
    git branch -M main
    git push -u origin main
else
    git branch -M main
    git push -u origin main
fi

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                                                       ║${NC}"
    echo -e "${GREEN}║          ✅ Successfully pushed to GitHub! 🎉         ║${NC}"
    echo -e "${GREEN}║                                                       ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "🌐 Repository URL:"
    echo "   https://github.com/SHASHIYA06/study_hub"
    echo ""
    echo "📋 Next steps:"
    echo "   1. Visit your repository on GitHub"
    echo "   2. Add a description and topics"
    echo "   3. Enable GitHub Actions (if needed)"
    echo "   4. Set up GitHub Secrets for deployment"
    echo ""
    echo "🔐 Recommended GitHub Secrets:"
    echo "   - YOUTUBE_API_KEY"
    echo "   - GOOGLE_GEMINI_API_KEY"
    echo "   - SSH_PRIVATE_KEY (for deployment)"
    echo "   - SSH_HOST (for deployment)"
    echo "   - SSH_USER (for deployment)"
    echo ""
else
    echo ""
    echo -e "${RED}❌ Push failed!${NC}"
    echo ""
    echo "Common issues:"
    echo "  1. Authentication required: Use a Personal Access Token"
    echo "     https://github.com/settings/tokens"
    echo ""
    echo "  2. Repository doesn't exist: Create it on GitHub first"
    echo "     https://github.com/new"
    echo ""
    echo "  3. Permission denied: Check repository access rights"
    echo ""
    exit 1
fi
