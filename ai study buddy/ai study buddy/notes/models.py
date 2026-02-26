from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='study_notes/', blank=True, null=True)
    content = models.TextField(blank=True, help_text="Type your note here if you don't have a file.")
    extracted_text = models.TextField(blank=True, null=True)
    ai_summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='certificates/')
    issuer = models.CharField(max_length=200, blank=True)
    date_earned = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.issuer}"
