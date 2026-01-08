# 🚀 GitHub Setup Guide - StudyHub

Complete guide to push your StudyHub project to GitHub.

## 📍 Your Repository

**URL:** https://github.com/SHASHIYA06/study_hub.git

---

## ⚡ Quick Push (One Command)

```bash
cd study_hub
./PUSH_TO_GITHUB.sh
```

This script will:
1. Initialize Git repository
2. Add remote origin
3. Create .gitignore
4. Stage all files
5. Commit with descriptive message
6. Push to GitHub

---

## 🔐 Authentication Options

### Option 1: Personal Access Token (Recommended)

1. **Generate Token**
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Select scopes: `repo`, `workflow`
   - Click "Generate token"
   - **Copy the token immediately** (you won't see it again!)

2. **Use Token**
   ```bash
   # When prompted for password, paste your token
   git push -u origin main
   Username: SHASHIYA06
   Password: [paste your token here]
   ```

3. **Save Token (Optional)**
   ```bash
   # Cache credentials for 1 hour
   git config --global credential.helper cache
   
   # Or save permanently (use with caution)
   git config --global credential.helper store
   ```

### Option 2: SSH Key

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub:
# https://github.com/settings/keys

# Test connection
ssh -T git@github.com

# Change remote to SSH
git remote set-url origin git@github.com:SHASHIYA06/study_hub.git
```

---

## 📝 Manual Setup Steps

If you prefer manual setup:

### Step 1: Initialize Git

```bash
cd study_hub
git init
```

### Step 2: Add Remote

```bash
git remote add origin https://github.com/SHASHIYA06/study_hub.git
```

### Step 3: Create .gitignore

Already created by the script, but verify:

```bash
cat .gitignore
```

**Important files to ignore:**
- `.env` (contains API keys!)
- `.env.production`
- `db.sqlite3`
- `__pycache__/`
- `node_modules/`
- `*.log`

### Step 4: Stage Files

```bash
git add .
```

### Step 5: Commit

```bash
git commit -m "Initial commit: StudyHub application with Gemini AI"
```

### Step 6: Push

```bash
git branch -M main
git push -u origin main
```

---

## 🔒 Security Checklist

Before pushing, verify these sensitive files are NOT included:

```bash
# Check what will be committed
git status

# These should NOT appear:
# ❌ .env
# ❌ .env.production
# ❌ *.pem (SSH keys)
# ❌ API keys in plain text
```

### Verify .gitignore

```bash
# Test if .env is ignored
git check-ignore -v .env

# Should output: .gitignore:XX:.env    .env
```

---

## 📊 Repository Setup on GitHub

### After First Push

1. **Visit your repo:** https://github.com/SHASHIYA06/study_hub

2. **Add Description:**
   ```
   🎓 StudyHub - AI-powered educational platform for students (Nursery to Class 12)
   Features: Django REST API, React frontend, Google Gemini AI integration, Docker deployment
   ```

3. **Add Topics:**
   ```
   education, django, react, ai, gemini, docker, rest-api, 
   learning-platform, educational-technology, python, javascript
   ```

4. **Update README:** The repository already has comprehensive README.md

5. **Add License Badge** (Already MIT licensed)

---

## 🔐 GitHub Secrets (For CI/CD)

Set up secrets for automated deployment:

1. Go to: https://github.com/SHASHIYA06/study_hub/settings/secrets/actions

2. Add these secrets:

| Secret Name | Description | Value |
|-------------|-------------|-------|
| `YOUTUBE_API_KEY` | YouTube Data API key | Your YouTube key |
| `GOOGLE_GEMINI_API_KEY` | Google Gemini API key | AIzaSyBg12HDcPqhLTUmLUJ4un_n7S3D5ITeZlM |
| `SSH_HOST` | Deployment server IP | Your server IP |
| `SSH_USER` | SSH username | ubuntu/root |
| `SSH_PRIVATE_KEY` | SSH private key | Your SSH key |
| `DOCKER_USERNAME` | Docker Hub username | Optional |
| `DOCKER_PASSWORD` | Docker Hub token | Optional |

---

## 🚀 Enable GitHub Actions

Your repository includes `.github/workflows/deploy.yml`

### Activate CI/CD:

1. Go to: https://github.com/SHASHIYA06/study_hub/actions

2. Click "I understand my workflows, go ahead and enable them"

3. **Workflow will run on:**
   - Push to `main` branch
   - Pull requests to `main`

### What the workflow does:
- ✅ Runs backend tests
- ✅ Runs frontend tests
- ✅ Builds Docker images
- ✅ Pushes to GitHub Container Registry
- ✅ Deploys to production server (if configured)

---

## 📋 Post-Push Checklist

- [ ] Repository visible on GitHub
- [ ] README.md displays correctly
- [ ] Documentation files readable
- [ ] .env files NOT in repository
- [ ] GitHub Actions enabled
- [ ] Secrets configured (if deploying)
- [ ] Repository description added
- [ ] Topics added
- [ ] License visible

---

## 🌟 Make Repository Public/Private

### Set Visibility:

1. Go to: https://github.com/SHASHIYA06/study_hub/settings

2. Scroll to "Danger Zone"

3. Choose:
   - **Public:** Anyone can see
   - **Private:** Only you and collaborators

**Recommendation:** Start private, make public when ready

---

## 🤝 Collaboration

### Add Collaborators:

1. Go to: https://github.com/SHASHIYA06/study_hub/settings/access

2. Click "Add people"

3. Enter GitHub username/email

---

## 📈 Repository Statistics

After pushing, you'll see:

- **Languages:** Python, JavaScript, CSS, HTML
- **Framework:** Django, React
- **License:** MIT
- **Stars:** (Share to get stars!)
- **Forks:** Others can fork and contribute

---

## 🔄 Update Repository

After making changes locally:

```bash
# Stage changes
git add .

# Commit
git commit -m "Description of changes"

# Push
git push origin main
```

### Quick update script:

```bash
# Create update script
cat > study_hub/git_update.sh << 'EOF'
#!/bin/bash
echo "Updating repository..."
git add .
git commit -m "${1:-Updated project files}"
git push origin main
echo "✅ Repository updated!"
EOF

chmod +x git_update.sh

# Usage:
./git_update.sh "Added new feature"
```

---

## 🎨 Customize Repository

### Add Badges to README:

```markdown
![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-4.2-green)
![React](https://img.shields.io/badge/react-18-blue)
![License](https://img.shields.io/badge/license-MIT-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)
```

### Create GitHub Pages:

1. Go to: https://github.com/SHASHIYA06/study_hub/settings/pages
2. Select source: `main` branch
3. Choose folder: `/docs` or root
4. Save

---

## 🐛 Troubleshooting

### Issue: "Permission denied"

```bash
# Solution: Use Personal Access Token or SSH
git remote set-url origin https://YOUR_TOKEN@github.com/SHASHIYA06/study_hub.git
```

### Issue: "Repository not found"

```bash
# Solution: Verify repository exists
# Visit: https://github.com/SHASHIYA06/study_hub

# If doesn't exist, create it:
# https://github.com/new
```

### Issue: "Failed to push"

```bash
# Solution: Pull first, then push
git pull origin main --allow-unrelated-histories
git push origin main
```

### Issue: "Large files"

```bash
# Check file sizes
find . -type f -size +50M

# Add to .gitignore if too large
# Or use Git LFS for large files
```

---

## 📚 Resources

- **GitHub Docs:** https://docs.github.com
- **Git Tutorial:** https://git-scm.com/docs/gittutorial
- **GitHub CLI:** https://cli.github.com
- **Your Repository:** https://github.com/SHASHIYA06/study_hub

---

## ✅ Quick Command Reference

```bash
# Push to GitHub
./PUSH_TO_GITHUB.sh

# Check status
git status

# View remote
git remote -v

# View commits
git log --oneline

# Create branch
git checkout -b feature-name

# Switch branch
git checkout main

# Pull latest
git pull origin main

# View differences
git diff
```

---

## 🎉 You're All Set!

Your StudyHub project is now on GitHub! 

**Repository:** https://github.com/SHASHIYA06/study_hub

Share it with the world! 🌟

---

**Need help?** Check GitHub documentation or repository Issues tab.
