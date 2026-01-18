#!/bin/bash

echo "╔═══════════════════════════════════════════════════════╗"
echo "║                                                       ║"
echo "║        🚀 PUSHING TO GITHUB RIGHT NOW! 🚀            ║"
echo "║                                                       ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "❌ Error: Not in study_hub directory"
    exit 1
fi

echo "📊 Checking repository status..."
git status

echo ""
echo "🔍 Files to be pushed:"
git ls-files | wc -l
echo " files ready"

echo ""
echo "📝 Last commit:"
git log --oneline -1

echo ""
echo "🌐 Remote repository:"
git remote -v

echo ""
echo "═══════════════════════════════════════════════════════"
echo ""
echo "⚡ PUSHING TO GITHUB..."
echo ""
echo "If prompted for credentials:"
echo "  Username: SHASHIYA06"
echo "  Password: [Your Personal Access Token]"
echo ""
echo "Get token from: https://github.com/settings/tokens"
echo ""
echo "═══════════════════════════════════════════════════════"
echo ""

# Push to GitHub
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "╔═══════════════════════════════════════════════════════╗"
    echo "║                                                       ║"
    echo "║          ✅ SUCCESSFULLY PUSHED TO GITHUB! 🎉        ║"
    echo "║                                                       ║"
    echo "╚═══════════════════════════════════════════════════════╝"
    echo ""
    echo "🌐 Your repository:"
    echo "   https://github.com/SHASHIYA06/study_hub"
    echo ""
    echo "📋 Next steps:"
    echo "   1. Visit your repository to verify"
    echo "   2. Read DEPLOY_COMPLETE_GUIDE.md"
    echo "   3. Deploy to Vercel + Railway"
    echo ""
else
    echo ""
    echo "❌ Push failed!"
    echo ""
    echo "Common solutions:"
    echo "1. Make sure you're using Personal Access Token (not password)"
    echo "2. Get token: https://github.com/settings/tokens"
    echo "3. Check internet connection"
    echo "4. Verify repository exists: https://github.com/SHASHIYA06/study_hub"
    echo ""
fi
