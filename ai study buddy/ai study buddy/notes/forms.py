from django import forms
from .models import Note, Certificate

class NoteUploadForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your notes here...', 'rows': 4}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }

class CertificateUploadForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'file', 'issuer', 'date_earned']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Python Masterclass'}),
            'file': forms.FileInput(attrs={'class': 'form-control', 'required': 'required'}),
            'issuer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Coursera, Udemy'}),
            'date_earned': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }
