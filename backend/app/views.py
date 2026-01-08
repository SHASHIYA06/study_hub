from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from .models import (
    Grade, Subject, Chapter, StudyMaterial, Quiz, Question, 
    QuestionChoice, StudentProgress, Flashcard
)
from .serializers import (
    GradeSerializer, SubjectSerializer, ChapterSerializer, 
    StudyMaterialSerializer, QuizSerializer, StudentProgressSerializer, FlashcardSerializer
)
from .youtube_utils import fetch_educational_videos, prioritize_videos_by_quality
from .ai_utils import (
    generate_summary, generate_mcq_quiz, solve_doubt, 
    generate_flashcards, explain_concept
)


class GradeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [AllowAny]


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        grade_id = self.request.query_params.get('grade_id')
        if grade_id:
            return Subject.objects.filter(grade_id=grade_id)
        return Subject.objects.all()


class ChapterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ChapterSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        subject_id = self.request.query_params.get('subject_id')
        if subject_id:
            return Chapter.objects.filter(subject_id=subject_id)
        return Chapter.objects.all()
    
    @action(detail=True, methods=['get'])
    def fetch_videos(self, request, pk=None):
        """
        Fetch educational videos for a chapter from YouTube
        """
        chapter = self.get_object()
        videos = fetch_educational_videos(
            topic=chapter.title,
            grade=chapter.subject.grade.level
        )
        
        # Prioritize by quality
        videos = prioritize_videos_by_quality(videos)
        
        return Response({'videos': videos[:5]})
    
    @action(detail=True, methods=['post'])
    def generate_summary(self, request, pk=None):
        """
        Generate AI summary of chapter content
        """
        chapter = self.get_object()
        if not chapter.content:
            return Response(
                {'error': 'Chapter has no content to summarize'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        summary = generate_summary(chapter.content, bullet_points=10)
        
        return Response({
            'summary': summary,
            'chapter_id': chapter.id
        })
    
    @action(detail=True, methods=['post'])
    def generate_quiz(self, request, pk=None):
        """
        Auto-generate MCQ quiz from chapter content
        """
        chapter = self.get_object()
        if not chapter.content:
            return Response(
                {'error': 'Chapter has no content to generate quiz from'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        num_questions = request.data.get('num_questions', 10)
        
        quiz_data = generate_mcq_quiz(chapter.content, num_questions=num_questions)
        
        if not quiz_data:
            return Response(
                {'error': 'Failed to generate quiz'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Save quiz to database
        quiz = Quiz.objects.create(title=f"AI Generated Quiz - {chapter.title}", chapter=chapter)
        
        for idx, q in enumerate(quiz_data):
            question = Question.objects.create(
                quiz=quiz,
                question_text=q['question'],
                question_type='mcq',
                difficulty=1 if q.get('difficulty') == 'easy' else 2 if q.get('difficulty') == 'medium' else 3
            )
            
            for i, option in enumerate(q['options']):
                QuestionChoice.objects.create(
                    question=question,
                    choice_text=option,
                    is_correct=(i == q['correct_answer']),
                    order=i
                )
        
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def generate_flashcards(self, request, pk=None):
        """
        Auto-generate flashcards from chapter content
        """
        chapter = self.get_object()
        if not chapter.content:
            return Response(
                {'error': 'Chapter has no content to generate flashcards from'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        num_cards = request.data.get('num_cards', 20)
        
        flashcards_data = generate_flashcards(chapter.content, num_cards=num_cards)
        
        if not flashcards_data:
            return Response(
                {'error': 'Failed to generate flashcards'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Save flashcards to database
        for card in flashcards_data:
            Flashcard.objects.create(
                chapter=chapter,
                question=card['question'],
                answer=card['answer']
            )
        
        flashcards = Flashcard.objects.filter(chapter=chapter)
        serializer = FlashcardSerializer(flashcards, many=True)
        return Response(serializer.data)


class StudyMaterialViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudyMaterialSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        chapter_id = self.request.query_params.get('chapter_id')
        if chapter_id:
            return StudyMaterial.objects.filter(chapter_id=chapter_id)
        return StudyMaterial.objects.all()


class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        chapter_id = self.request.query_params.get('chapter_id')
        if chapter_id:
            return Quiz.objects.filter(chapter_id=chapter_id)
        return Quiz.objects.all()


class StudentProgressViewSet(viewsets.ModelViewSet):
    serializer_class = StudentProgressSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return StudentProgress.objects.filter(student=self.request.user)
    
    @action(detail=False, methods=['post'])
    def update_progress(self, request):
        """
        Update student progress for a chapter
        """
        chapter_id = request.data.get('chapter_id')
        progress_status = request.data.get('status')
        progress = request.data.get('progress_percentage', 0)
        
        chapter = get_object_or_404(Chapter, id=chapter_id)
        
        student_progress, created = StudentProgress.objects.update_or_create(
            student=request.user,
            chapter=chapter,
            defaults={
                'status': progress_status,
                'progress_percentage': progress
            }
        )
        
        serializer = self.get_serializer(student_progress)
        return Response(serializer.data)


class DoubtSolverViewSet(viewsets.ViewSet):
    """
    Endpoint to solve student doubts using AI
    """
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['post'])
    def ask_doubt(self, request):
        problem = request.data.get('problem_description')
        image = request.FILES.get('image', None)
        
        if not problem:
            return Response(
                {'error': 'problem_description is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        solution = solve_doubt(problem, problem_image=image)
        
        return Response({
            'solution': solution,
            'problem': problem
        })


class ExplainConceptViewSet(viewsets.ViewSet):
    """
    Get AI-powered concept explanation
    """
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['post'])
    def explain(self, request):
        concept = request.data.get('concept')
        grade = request.data.get('grade')
        
        if not concept or not grade:
            return Response(
                {'error': 'Both concept and grade are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        explanation = explain_concept(concept, grade)
        
        return Response({
            'concept': concept,
            'explanation': explanation
        })


class FlashcardViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FlashcardSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        chapter_id = self.request.query_params.get('chapter_id')
        if chapter_id:
            return Flashcard.objects.filter(chapter_id=chapter_id)
        return Flashcard.objects.all()
