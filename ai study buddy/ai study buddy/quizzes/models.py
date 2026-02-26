from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    CATEGORY_CHOICES = [
        ('gen_ai', 'Generative AI'),
        ('ml', 'Machine Learning'),
        ('prompt', 'Prompt Engineering'),
        ('llm', 'Large Language Models'),
        ('ethics', 'AI Ethics'),
        ('web_ai', 'AI in Web Development'),
        ('general', 'General AI'),
        ('cloud', 'Cloud Computing'),
        ('devops', 'DevOps & Git'),
        ('cyber', 'Cyber Security'),
        ('data', 'Data Science'),
        ('mobile', 'Mobile Development'),
        ('blockchain', 'Web3 & Blockchain'),
        ('iot', 'Internet of Things'),
        ('hr', 'HR Interview Prep'),
    ]

    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quizzes"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    points = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quiz.title}: {self.text[:50]}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text[:30]} - {self.text}"

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_points = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.score}/{self.total_points}"
