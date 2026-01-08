from django.core.management.base import BaseCommand
from app.models import Grade, Subject, Chapter


class Command(BaseCommand):
    help = 'Seeds the database with initial data'
    
    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Create grades
        grades_data = [
            ('nursery', 'Early childhood education'),
            ('ukg', 'Upper Kindergarten'),
            ('kg', 'Kindergarten'),
            ('class_1', 'Elementary School - Grade 1'),
            ('class_2', 'Elementary School - Grade 2'),
            ('class_3', 'Elementary School - Grade 3'),
            ('class_4', 'Elementary School - Grade 4'),
            ('class_5', 'Elementary School - Grade 5'),
            ('class_6', 'Middle School - Grade 6'),
            ('class_7', 'Middle School - Grade 7'),
            ('class_8', 'Middle School - Grade 8'),
            ('class_9', 'Secondary School - Grade 9'),
            ('class_10', 'Secondary School - Grade 10'),
            ('class_11', 'Senior Secondary - Grade 11'),
            ('class_12', 'Senior Secondary - Grade 12'),
        ]
        
        for level, desc in grades_data:
            Grade.objects.get_or_create(level=level, defaults={'description': desc})
            self.stdout.write(f'✓ Created grade: {level}')
        
        # Create subjects for Class 9
        grade_9 = Grade.objects.get(level='class_9')
        subjects_data = [
            ('science', 'Physics, Chemistry, Biology'),
            ('mathematics', 'Algebra, Geometry, Trigonometry'),
            ('english', 'Literature, Grammar, Composition'),
            ('social_studies', 'History, Geography, Civics'),
        ]
        
        for name, desc in subjects_data:
            Subject.objects.get_or_create(
                grade=grade_9,
                name=name,
                defaults={'description': desc}
            )
            self.stdout.write(f'✓ Created subject: {name} for {grade_9.level}')
        
        # Create sample chapters for Science
        science = Subject.objects.filter(name='science', grade=grade_9).first()
        if science:
            chapters_data = [
                (1, 'Motion', 'Understanding motion, speed, velocity, and acceleration', 
                 'Motion is the change in position of an object with respect to time. Speed is the rate of change of distance, while velocity is the rate of change of displacement. Acceleration is the rate of change of velocity.'),
                (2, 'Force and Laws of Motion', 'Newton\'s laws of motion and their applications',
                 'Newton\'s First Law: An object at rest stays at rest and an object in motion stays in motion unless acted upon by an external force. Newton\'s Second Law: Force equals mass times acceleration (F=ma). Newton\'s Third Law: For every action, there is an equal and opposite reaction.'),
                (3, 'Gravitation', 'Universal law of gravitation and its effects',
                 'Every object in the universe attracts every other object with a force which is directly proportional to the product of their masses and inversely proportional to the square of the distance between them.'),
            ]
            
            for num, title, desc, content in chapters_data:
                Chapter.objects.get_or_create(
                    subject=science,
                    chapter_number=num,
                    defaults={
                        'title': title,
                        'description': desc,
                        'content': content
                    }
                )
                self.stdout.write(f'✓ Created chapter: {title}')
        
        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
