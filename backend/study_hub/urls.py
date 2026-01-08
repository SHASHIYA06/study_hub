from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from app.views import (
    GradeViewSet, SubjectViewSet, ChapterViewSet, StudyMaterialViewSet,
    QuizViewSet, StudentProgressViewSet, DoubtSolverViewSet, 
    ExplainConceptViewSet, FlashcardViewSet
)

router = DefaultRouter()
router.register(r'grades', GradeViewSet, basename='grade')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'chapters', ChapterViewSet, basename='chapter')
router.register(r'materials', StudyMaterialViewSet, basename='material')
router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'progress', StudentProgressViewSet, basename='progress')
router.register(r'doubt-solver', DoubtSolverViewSet, basename='doubt-solver')
router.register(r'explain', ExplainConceptViewSet, basename='explain')
router.register(r'flashcards', FlashcardViewSet, basename='flashcard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
