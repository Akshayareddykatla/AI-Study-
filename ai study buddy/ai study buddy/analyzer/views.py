from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.contrib import messages
from .models import UploadedFile, GeneratedQuestion
from .forms import FileUploadForm
from .services.file_service import FileProcessingService

class FileUploadView(LoginRequiredMixin, CreateView):
    model = UploadedFile
    form_class = FileUploadForm
    template_name = 'analyzer/upload.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.name = form.instance.file.name
        response = super().form_valid(form)
        
        # Process the file immediately
        file_path = form.instance.file.path
        text = FileProcessingService.extract_text(file_path)
        form.instance.processed_text = text
        form.instance.summary = FileProcessingService.generate_summary(text)
        form.instance.save()
        
        # Generate questions
        questions_data = FileProcessingService.generate_questions(text)
        for q_data in questions_data:
            GeneratedQuestion.objects.create(
                uploaded_file=form.instance,
                text=q_data['text'],
                correct_answer=q_data['correct_answer'],
                distractors=q_data['distractors']
            )
            
        messages.success(self.request, "File uploaded and analyzed successfully!")
        return response

    def get_success_url(self):
        return redirect('analyzer:file_summary', pk=self.object.pk).url

class FileSummaryView(LoginRequiredMixin, DetailView):
    model = UploadedFile
    template_name = 'analyzer/summary.html'
    context_object_name = 'file_obj'

class FileHistoryView(LoginRequiredMixin, ListView):
    model = UploadedFile
    template_name = 'analyzer/history.html'
    context_object_name = 'files'

    def get_queryset(self):
        return UploadedFile.objects.filter(user=self.request.user).order_by('-uploaded_at')
