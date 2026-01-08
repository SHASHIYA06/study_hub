from django.contrib import admin
from .models import (
    Grade, Subject, Chapter, StudyMaterial, Quiz, Question,
    QuestionChoice, StudentProgress, Flashcard
)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['level', 'description']
    search_fields = ['level']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade', 'description']
    list_filter = ['grade']
    search_fields = ['name']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'chapter_number', 'created_at']
    list_filter = ['subject']
    search_fields = ['title']


@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ['title', 'chapter', 'material_type', 'source', 'created_at']
    list_filter = ['material_type', 'source']
    search_fields = ['title']


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'chapter', 'created_at']
    search_fields = ['title']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'quiz', 'question_type', 'difficulty']
    list_filter = ['question_type', 'difficulty']


@admin.register(QuestionChoice)
class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'question', 'is_correct', 'order']
    list_filter = ['is_correct']


@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ['student', 'chapter', 'status', 'progress_percentage', 'last_studied']
    list_filter = ['status']


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ['question', 'chapter', 'created_at']
    search_fields = ['question']
