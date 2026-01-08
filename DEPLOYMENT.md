# 🚀 Deployment Guide - StudyHub

Complete guide for deploying StudyHub to various platforms.

## 📋 Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Environment variables configured
- [ ] Database backups created
- [ ] SSL certificates ready (for production)
- [ ] DNS configured (if using custom domain)
- [ ] API keys verified
- [ ] CORS origins updated

## 🐳 Option 1: Docker-based Deployment (Recommended)

### On Any Server with Docker

1. **Install Docker and Docker Compose**
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

2. **Clone and configure**
   ```bash
   git clone https://github.com/yourusername/study-hub.git
   cd study_hub
   cp .env.example .env
   # Edit .env with production values
   ```

3. **Deploy**
   ```bash
   make build
   make up
   make migrate
   make seed
   make superuser
   ```

4. **Set up reverse proxy (Nginx)**
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;
       
       location / {
           proxy_pass http://localhost:80;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

## ☁️ Option 2: AWS EC2 Deployment

### Step 1: Launch EC2 Instance

1. **Create EC2 instance**
   - AMI: Ubuntu 22.04 LTS
   - Instance type: t3.medium (or larger)
   - Storage: 30GB SSD

2. **Security Group Rules**
   | Type  | Port | Source    |
   |-------|------|-----------|
   | SSH   | 22   | Your IP   |
   | HTTP  | 80   | 0.0.0.0/0 |
   | HTTPS | 443  | 0.0.0.0/0 |

### Step 2: Connect and Setup

```bash
# SSH into instance
ssh -i your-key.pem ubuntu@your-instance-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Clone project
git clone https://github.com/yourusername/study-hub.git
cd study_hub

# Configure environment
cp .env.example .env
nano .env  # Edit with production settings

# Deploy
make build
make up
make migrate
make seed
```

### Step 3: Set up SSL with Let's Encrypt

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Get SSL certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal
sudo certbot renew --dry-run
```

## 🚂 Option 3: Railway Deployment

Railway provides automatic Docker deployment from Git.

### Step 1: Prepare for Railway

1. **Create `railway.json`** (optional)
   ```json
   {
     "$schema": "https://railway.app/railway.schema.json",
     "build": {
       "builder": "DOCKERFILE",
       "dockerfilePath": "backend/Dockerfile"
     },
     "deploy": {
       "restartPolicyType": "ON_FAILURE",
       "restartPolicyMaxRetries": 10
     }
   }
   ```

### Step 2: Deploy

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and deploy**
   ```bash
   railway login
   railway init
   railway up
   ```

3. **Add environment variables** in Railway dashboard
   - `DATABASE_URL` (Railway provisions PostgreSQL automatically)
   - `REDIS_URL`
   - `YOUTUBE_API_KEY`
   - `OPENAI_API_KEY`
   - `SECRET_KEY`
   - `ALLOWED_HOSTS`

4. **Deploy frontend separately**
   ```bash
   cd frontend
   railway up
   ```

**Cost**: Free tier available, paid plans start at $5/month

## 🎨 Option 4: Render Deployment

### Backend Deployment

1. **Create New Web Service**
   - Connect GitHub repository
   - Runtime: Docker
   - Branch: main
   - Root Directory: `backend/`

2. **Add Environment Variables**
   ```
   PYTHON_VERSION=3.11
   DATABASE_URL=[auto-filled by Render PostgreSQL]
   YOUTUBE_API_KEY=your_key
   OPENAI_API_KEY=your_key
   SECRET_KEY=your_secret
   DEBUG=False
   ```

3. **Create PostgreSQL Database**
   - Add PostgreSQL service
   - Link to web service

### Frontend Deployment

1. **Create Static Site**
   - Connect repository
   - Build Command: `cd frontend && npm install && npm run build`
   - Publish Directory: `frontend/build`

2. **Update API URL**
   ```env
   REACT_APP_API_URL=https://your-backend.onrender.com
   ```

**Cost**: Free tier available (spins down after inactivity)

## 🔵 Option 5: DigitalOcean Droplet

### 1. Create Droplet

- Choose Ubuntu 22.04
- Select plan ($12/month recommended)
- Add SSH key

### 2. Setup

```bash
# Connect
ssh root@your-droplet-ip

# Update and install Docker
apt update && apt upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Clone and deploy
git clone https://github.com/yourusername/study-hub.git
cd study_hub
cp .env.example .env
nano .env

make build
make up
make migrate
make seed
```

### 3. Configure Firewall

```bash
ufw allow 22
ufw allow 80
ufw allow 443
ufw enable
```

## 🔄 CI/CD Setup (GitHub Actions)

The project includes a GitHub Actions workflow at `.github/workflows/deploy.yml`.

### Enable Automatic Deployment

1. **Add GitHub Secrets**
   - `SSH_PRIVATE_KEY`: Your deployment server SSH key
   - `SSH_HOST`: Your server IP
   - `SSH_USER`: Username (e.g., ubuntu)
   - `DOCKER_USERNAME`: Docker Hub username
   - `DOCKER_PASSWORD`: Docker Hub password

2. **Workflow triggers on**
   - Push to `main` branch
   - Pull request to `main`

3. **Workflow steps**
   - Run tests
   - Build Docker images
   - Push to Docker Hub
   - Deploy to server

## 🔒 Security Best Practices

### Production Checklist

- [ ] Change default passwords
- [ ] Use strong SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Enable HTTPS
- [ ] Set up firewall
- [ ] Regular backups
- [ ] Monitor logs
- [ ] Rate limiting
- [ ] CORS configuration

### Environment Variables Security

Never commit `.env` file. Use secrets management:

- **AWS**: AWS Secrets Manager
- **Railway**: Environment Variables UI
- **Render**: Environment Variables UI
- **GitHub**: GitHub Secrets

## 📊 Monitoring and Logs

### View Logs

```bash
# All services
make logs

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Health Checks

- Backend: `http://yourdomain.com/api/grades/`
- Frontend: `http://yourdomain.com/`

### Set up Monitoring

1. **Sentry** for error tracking
2. **New Relic** for APM
3. **CloudWatch** (AWS)
4. **Railway Metrics** (Railway)

## 🔄 Updates and Maintenance

### Update Application

```bash
# Pull latest code
git pull origin main

# Rebuild and restart
make down
make build
make up
make migrate
```

### Database Backup

```bash
# Automated backup
make backup-db

# Manual backup
docker-compose exec -T db pg_dump -U study_hub_user study_hub > backup.sql
```

### Restore Database

```bash
make restore-db BACKUP_FILE=backup.sql
```

## 📈 Scaling

### Horizontal Scaling

1. **Load Balancer** (Nginx/HAProxy)
2. **Multiple Backend Instances**
   ```yaml
   backend:
     deploy:
       replicas: 3
   ```

3. **Separate Database Server**
   - Use managed PostgreSQL (AWS RDS, Railway DB)

4. **CDN for Static Files**
   - CloudFront (AWS)
   - Cloudflare

### Performance Optimization

- Enable Redis caching
- Use PostgreSQL connection pooling
- Optimize database queries
- Compress static assets
- Enable Gzip

## 🆘 Troubleshooting

### Common Issues

**Port already in use**
```bash
# Find and kill process
sudo lsof -i :8000
sudo kill -9 <PID>
```

**Database connection failed**
```bash
# Check database status
docker-compose ps db
docker-compose logs db
```

**Frontend can't reach backend**
- Check CORS settings
- Verify REACT_APP_API_URL
- Check network connectivity

**Migrations failing**
```bash
docker-compose exec backend python manage.py migrate --fake
```

## 💰 Cost Estimation

### Monthly Costs

| Platform | Configuration | Est. Cost |
|----------|--------------|-----------|
| AWS EC2 | t3.medium + RDS | $30-50 |
| Railway | Hobby plan | $5-20 |
| Render | Starter plan | $7-25 |
| DigitalOcean | Basic Droplet | $12-24 |
| Self-hosted | VPS | $5-15 |

### Cost Optimization

- Use free tiers initially
- Optimize database queries
- Implement caching
- Use CDN for static files
- Monitor usage

---

**Need Help?** Create an issue on GitHub or contact support.
