from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Note, Certificate
from .forms import NoteUploadForm, CertificateUploadForm
from .services.note_analyzer import GeminiNoteAnalyzer

class NotesHubView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/hub.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['certificates'] = Certificate.objects.filter(user=self.request.user).order_by('-created_at')
        context['note_form'] = NoteUploadForm()
        context['cert_form'] = CertificateUploadForm()
        return context

class NoteUploadView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteUploadForm
    template_name = 'notes/hub.html'
    success_url = reverse_lazy('notes:hub')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f"Note '{form.instance.title}' uploaded successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"Note Error ({field}): {error}")
        return redirect('notes:hub')

class CertUploadView(LoginRequiredMixin, CreateView):
    model = Certificate
    form_class = CertificateUploadForm
    template_name = 'notes/hub.html'
    success_url = reverse_lazy('notes:hub')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f"Certificate '{form.instance.title}' added to vault!")
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"Certificate Error ({field}): {error}")
        return redirect('notes:hub')

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/detail.html'
    context_object_name = 'note'

    def get_queryset(self):
        # Privacy: only allow users to see their own notes
        return Note.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        note = self.get_object()
        if 'ai_check' in request.POST:
            try:
                content = ""
                if note.file:
                    # Robust read: reset file pointer and try decoding with fallback
                    note.file.seek(0)
                    file_content = note.file.read()
                    try:
                        content = file_content.decode('utf-8')
                    except UnicodeDecodeError:
                        content = file_content.decode('latin-1') # Fallback for non-UTF8 text
                elif note.content:
                    content = note.content
                
                if not content:
                    messages.error(request, "Note has no content to analyze.")
                    return redirect('notes:detail', pk=note.pk)

                analyzer = GeminiNoteAnalyzer()
                note.ai_summary = analyzer.analyze_note(content, note.title)
                note.save()
                messages.success(request, "AI Check completed!")
            except Exception as e:
                messages.error(request, f"AI Check Failed: {str(e)}")
        return redirect('notes:detail', pk=note.pk)
