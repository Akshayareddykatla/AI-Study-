from django.db import models
from django.contrib.auth.models import User

class VideoSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_searches')
    query = models.CharField(max_length=255)
    ai_response = models.TextField()  # Stores the AI's suggestions/text
    suggested_search_terms = models.JSONField(default=list) # List of direct YouTube search queries
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.query} ({self.timestamp.date()})"

class FavoriteVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_videos')
    video_id = models.CharField(max_length=50) # Remove unique=True
    title = models.CharField(max_length=255)
    thumbnail_url = models.URLField()
    video_url = models.URLField()
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_at']
        unique_together = ['user', 'video_id']

    def __str__(self):
        return f"{self.user.username} - {self.title}"
