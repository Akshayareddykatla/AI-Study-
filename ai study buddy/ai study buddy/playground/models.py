from django.db import models
from django.contrib.auth.models import User

class CodeSubmission(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('html', 'HTML'),
        ('javascript', 'JavaScript'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='code_submissions')
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    code = models.TextField()
    output = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.language} ({self.timestamp.date()})"
