from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Quiz, Question, Choice, Result
from django.urls import reverse

class QuizSystemTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teststudent', password='password123')
        self.client = Client()
        self.client.login(username='teststudent', password='password123')
        
        # Create a sample quiz
        self.quiz = Quiz.objects.create(
            title="AI Foundations",
            category="gen_ai",
            difficulty="beginner",
            description="Test Quiz"
        )
        self.q1 = Question.objects.create(quiz=self.quiz, text="What is AI?")
        self.c1_correct = Choice.objects.create(question=self.q1, text="Artificial Intelligence", is_correct=True)
        self.c1_wrong = Choice.objects.create(question=self.q1, text="Apples Inside", is_correct=False)

    def test_quiz_difficulty_levels(self):
        """Verify that difficulty levels are correctly stored."""
        self.assertEqual(self.quiz.difficulty, 'beginner')
        
    def test_quiz_list_access(self):
        """Verify the Curriculum Hub is accessible."""
        response = self.client.get(reverse('quizzes:quiz_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AI Foundations")

    def test_quiz_scoring_logic(self):
        """Verify that correct answers result in a perfect score."""
        post_data = {
            f'question_{self.q1.id}': self.c1_correct.id
        }
        response = self.client.post(reverse('quizzes:take_quiz', args=[self.quiz.id]), post_data)
        
        # Should redirect to results
        self.assertEqual(response.status_code, 302)
        
        # Check result in DB
        result = Result.objects.get(user=self.user, quiz=self.quiz)
        self.assertEqual(result.score, 1)
        self.assertEqual(result.total_points, 1)

    def test_quiz_failure_logic(self):
        """Verify that wrong answers result in a zero score."""
        # Note: In the view, if a choice doesn't exist or is wrong, score stays 0
        post_data = {
            f'question_{self.q1.id}': self.c1_wrong.id
        }
        self.client.post(reverse('quizzes:take_quiz', args=[self.quiz.id]), post_data)
        result = Result.objects.get(user=self.user, quiz=self.quiz)
        self.assertEqual(result.score, 0)
