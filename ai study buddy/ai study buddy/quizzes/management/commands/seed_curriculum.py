from django.core.management.base import BaseCommand
from quizzes.models import Quiz, Question, Choice

class Command(BaseCommand):
    help = 'Seeds a structured multi-level curriculum (Beginner, Intermediate, Advanced)'

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old curriculum data...")
        # Optional: Quiz.objects.all().delete() 
        
        curriculum_data = [
            {
                'title': 'GenAI Foundations (Part 1)',
                'category': 'gen_ai',
                'difficulty': 'beginner',
                'description': 'Learn the basics of Generative AI, LLMs, and simple prompts.',
                'questions': [
                    {
                        'text': 'What does LLM stand for?',
                        'choices': [
                            ('Large Language Model', True),
                            ('Linear Logic Module', False),
                            ('Long Language Map', False)
                        ]
                    },
                    {
                        'text': 'Which of these is a Generative AI tool?',
                        'choices': [
                            ('ChatGPT', True),
                            ('Excel', False),
                            ('Calculator', False)
                        ]
                    }
                ]
            },
            {
                'title': 'Intermediate Prompt Engineering',
                'category': 'prompt',
                'difficulty': 'intermediate',
                'description': 'Master Chain-of-Thought and Few-Shot prompting techniques.',
                'questions': [
                    {
                        'text': 'What is "Chain-of-Thought" prompting?',
                        'choices': [
                            ('Asking AI to explain its reasoning step-by-step', True),
                            ('Linking different prompts together', False),
                            ('Deleting prompt history', False)
                        ]
                    },
                    {
                        'text': 'What does "temperature" control in an LLM?',
                        'choices': [
                            ('Randomness and creativity of the output', True),
                            ('The speed of the response', False),
                            ('The hardware heat level', False)
                        ]
                    }
                ]
            },
            {
                'title': 'Advanced Machine Learning Mastery',
                'category': 'ml',
                'difficulty': 'advanced',
                'description': 'Deep dive into Neural Networks, Gradient Descent, and fine-tuning.',
                'questions': [
                    {
                        'text': 'What is "Gradient Descent"?',
                        'choices': [
                            ('An optimization algorithm to minimize the loss function', True),
                            ('A way to sort data alphabetically', False),
                            ('A type of hardware for AI', False)
                        ]
                    },
                    {
                        'text': 'What is "Backpropagation"?',
                        'choices': [
                            ('The method used to calculate gradients in neural networks', True),
                            ('A way to undo code changes', False),
                            ('Sending data back to the user', False)
                        ]
                    }
                ]
            },
            {
                'title': 'Python for Data Science (Beginner)',
                'category': 'data',
                'difficulty': 'beginner',
                'description': 'Introduction to Python syntax for data analysis.',
                'questions': [
                    {
                        'text': 'Which library is primarily used for data manipulation in Python?',
                        'choices': [
                            ('Pandas', True),
                            ('Pygame', False),
                            ('Flash', False)
                        ]
                    }
                ]
            },
            {
                'title': 'Cloud AI Architecture (Advanced)',
                'category': 'cloud',
                'difficulty': 'advanced',
                'description': 'Designing scalable AI systems on AWS and Azure.',
                'questions': [
                    {
                        'text': 'Which service is AWS’s fully managed machine learning platform?',
                        'choices': [
                            ('SageMaker', True),
                            ('S3', False),
                            ('Lambda', False)
                        ]
                    }
                ]
            }
        ]

        for q_data in curriculum_data:
            quiz, created = Quiz.objects.get_or_create(
                title=q_data['title'],
                category=q_data['category'],
                difficulty=q_data['difficulty'],
                defaults={'description': q_data['description']}
            )
            
            if created:
                for quest in q_data['questions']:
                    question = Question.objects.create(quiz=quiz, text=quest['text'])
                    for choice_text, correct in quest['choices']:
                        Choice.objects.create(question=question, text=choice_text, is_correct=correct)
                self.stdout.write(self.style.SUCCESS(f"Created: {quiz.title} ({quiz.difficulty})"))
            else:
                self.stdout.write(f"Skipped (Exists): {quiz.title}")

        self.stdout.write(self.style.SUCCESS('Curriculum Seeding Completed!'))
