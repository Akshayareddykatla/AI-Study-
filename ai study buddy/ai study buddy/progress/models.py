from django.db import models
from django.contrib.auth.models import User

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress')
    total_questions_asked = models.IntegerField(default=0)
    total_quizzes_taken = models.IntegerField(default=0)
    total_score_sum = models.IntegerField(default=0)
    total_points_sum = models.IntegerField(default=0)
    
    # Startup Features
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    badges = models.JSONField(default=list) # List of badge names
    highest_score = models.IntegerField(default=0)
    total_playground_uses = models.IntegerField(default=0)
    
    # Store subject performance as JSON or simple fields for now
    strongest_subject = models.CharField(max_length=100, blank=True, null=True)
    weakest_subject = models.CharField(max_length=100, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    last_activity_date = models.DateField(null=True, blank=True)
    last_activity_date = models.DateField(null=True, blank=True)

    @property
    def average_score_percentage(self):
        if self.total_points_sum == 0:
            return 0
        return round((self.total_score_sum / self.total_points_sum) * 100, 1)

    def __str__(self):
        return f"Progress for {self.user.username}"
