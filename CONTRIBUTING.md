# 🤝 Contributing to StudyHub

Thank you for considering contributing to StudyHub! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn

## How to Contribute

### Reporting Bugs

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with:
   - Clear title
   - Detailed description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots (if applicable)
   - Environment details

### Suggesting Features

1. **Open an issue** with label `enhancement`
2. **Describe the feature**:
   - Use case
   - Expected behavior
   - Mockups (if applicable)

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow coding standards
   - Add tests
   - Update documentation

4. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**
   - Clear title and description
   - Link related issues
   - Add screenshots for UI changes

## Development Setup

### Prerequisites
- Docker and Docker Compose
- Git
- Text editor (VS Code recommended)

### Setup
```bash
# Clone your fork
git clone https://github.com/yourusername/study-hub.git
cd study_hub

# Create environment file
cp .env.example .env

# Start development environment
make dev-up

# Run migrations
make migrate

# Seed database
make seed
```

## Coding Standards

### Python (Backend)

- Follow PEP 8
- Use type hints
- Write docstrings
- Keep functions small and focused

```python
def fetch_videos(topic: str, grade: str, limit: int = 5) -> list:
    """
    Fetch educational videos from YouTube.
    
    Args:
        topic: The subject or chapter name
        grade: Student grade level
        limit: Maximum number of videos
        
    Returns:
        List of video dictionaries
    """
    pass
```

### JavaScript (Frontend)

- Use ES6+ features
- Follow Airbnb style guide
- Use functional components
- Write PropTypes or TypeScript

```javascript
const VideoCard = ({ video }) => {
  return (
    <div className="video-card">
      <h3>{video.title}</h3>
      <p>{video.channel}</p>
    </div>
  );
};
```

### Commit Messages

Follow conventional commits:

```
feat: Add video fetching feature
fix: Resolve database connection issue
docs: Update API documentation
style: Format code with prettier
refactor: Simplify authentication logic
test: Add tests for AI utilities
chore: Update dependencies
```

## Testing

### Backend Tests
```bash
docker-compose exec backend python manage.py test
```

### Frontend Tests
```bash
cd frontend
npm test
```

### Write Tests for New Features

**Backend:**
```python
from django.test import TestCase
from app.models import Grade

class GradeTestCase(TestCase):
    def test_create_grade(self):
        grade = Grade.objects.create(
            level='class_9',
            description='Grade 9'
        )
        self.assertEqual(grade.level, 'class_9')
```

**Frontend:**
```javascript
import { render, screen } from '@testing-library/react';
import GradeSelection from './GradeSelection';

test('renders grade selection', () => {
  render(<GradeSelection />);
  expect(screen.getByText(/Choose Your Grade/i)).toBeInTheDocument();
});
```

## Documentation

- Update README.md for major features
- Add docstrings to functions
- Update API_DOCUMENTATION.md for API changes
- Include code comments for complex logic

## Project Structure

```
study_hub/
├── backend/
│   ├── app/
│   │   ├── models.py       # Add new models here
│   │   ├── views.py        # Add new API endpoints
│   │   ├── serializers.py  # Add serializers
│   │   └── tests.py        # Add backend tests
├── frontend/
│   ├── src/
│   │   ├── pages/          # Add new pages
│   │   ├── components/     # Add reusable components
│   │   └── api.js          # Add API calls
```

## Feature Branches

- `feature/*` - New features
- `fix/*` - Bug fixes
- `docs/*` - Documentation
- `refactor/*` - Code refactoring
- `test/*` - Adding tests

## Review Process

1. Maintainers will review your PR
2. Address feedback
3. Once approved, PR will be merged
4. Your contribution will be acknowledged

## Areas to Contribute

### High Priority
- [ ] User authentication system
- [ ] Mobile responsive design
- [ ] Performance optimization
- [ ] Additional test coverage
- [ ] Accessibility improvements

### Medium Priority
- [ ] More AI features
- [ ] Better error handling
- [ ] Internationalization (i18n)
- [ ] Dark mode
- [ ] Search functionality

### Good First Issues
- [ ] Add more sample data
- [ ] Improve documentation
- [ ] Fix UI/UX issues
- [ ] Add loading states
- [ ] Improve error messages

## Questions?

- Open a discussion on GitHub
- Join our community chat
- Email: contribute@studyhub.com

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for making StudyHub better! 🎉
