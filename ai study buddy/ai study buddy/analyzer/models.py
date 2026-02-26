from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_files')
    file = models.FileField(upload_to='study_materials/')
    name = models.CharField(max_length=255)
    processed_text = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GeneratedQuestion(models.Model):
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    correct_answer = models.CharField(max_length=255)
    distractors = models.JSONField(default=list) # List of wrong choices

    def __str__(self):
        return f"Question for {self.uploaded_file.name}"
