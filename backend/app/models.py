from django.db import models
from django.contrib.auth.models import User


class Grade(models.Model):
    LEVEL_CHOICES = [
        ('nursery', 'Nursery'),
        ('ukg', 'UKG'),
        ('kg', 'KG'),
    ] + [(f'class_{i}', f'Class {i}') for i in range(1, 13)]
    
    level = models.CharField(max_length=20, unique=True, choices=LEVEL_CHOICES)
    description = models.TextField()
    
    def __str__(self):
        return self.level


class Subject(models.Model):
    SUBJECT_CHOICES = [
        ('english', 'English'),
        ('mathematics', 'Mathematics'),
        ('science', 'Science'),
        ('social_studies', 'Social Studies'),
        ('hindi', 'Hindi'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('biology', 'Biology'),
        ('history', 'History'),
        ('geography', 'Geography'),
        ('economics', 'Economics'),
    ]
    
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    description = models.TextField()
    
    class Meta:
        unique_together = ('grade', 'name')
    
    def __str__(self):
        return f"{self.grade.level} - {self.name}"


class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=200)
    description = models.TextField()
    chapter_number = models.IntegerField()
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['chapter_number']
        unique_together = ('subject', 'chapter_number')
    
    def __str__(self):
        return f"Chapter {self.chapter_number}: {self.title}"


class StudyMaterial(models.Model):
    MATERIAL_TYPE_CHOICES = [
        ('video', 'Video'),
        ('note', 'Note'),
        ('formula', 'Formula Sheet'),
        ('quiz', 'Quiz'),
        ('article', 'Article'),
    ]
    
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=200)
    material_type = models.CharField(max_length=20, choices=MATERIAL_TYPE_CHOICES)
    content = models.TextField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    video_id = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, default='YouTube')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.material_type})"


class Quiz(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('mcq', 'Multiple Choice'),
        ('short_answer', 'Short Answer'),
        ('essay', 'Essay'),
    ]
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES)
    difficulty = models.IntegerField(default=1, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])
    
    def __str__(self):
        return self.question_text[:50]


class QuestionChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    order = models.IntegerField()
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.choice_text


class StudentProgress(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('mastered', 'Mastered'),
        ('difficult', 'Difficult'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    progress_percentage = models.IntegerField(default=0)
    last_studied = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('student', 'chapter')
    
    def __str__(self):
        return f"{self.student.username} - {self.chapter.title}"


class Flashcard(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='flashcards')
    question = models.CharField(max_length=500)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.question[:50]
