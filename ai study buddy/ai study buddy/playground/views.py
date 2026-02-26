from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CodeSubmission
from progress.models import UserProgress
import json

class PlaygroundView(LoginRequiredMixin, View):
    def get(self, request):
        from django.utils import timezone
        today = timezone.now().date()
        uses_today = CodeSubmission.objects.filter(user=request.user, timestamp__date=today).count()
        history = CodeSubmission.objects.filter(user=request.user).order_by('-timestamp')[:10]
        return render(request, 'playground/editor.html', {
            'history': history,
            'uses_today': uses_today
        })

    def post(self, request):
        language = request.POST.get('language')
        code = request.POST.get('code')
        
        # In a real app, we'd use a sandbox API. Here we simulate.
        output = "Simulation successful."
        if language == 'python':
            output = "Python execution simulated. Output: Hello from AI Buddy!"
        elif language == 'javascript':
            output = "JavaScript execution simulated."
        
        submission = CodeSubmission.objects.create(
            user=request.user,
            language=language,
            code=code,
            output=output
        )
        
        # Update progress stats
        progress, _ = UserProgress.objects.get_or_create(user=request.user)
        progress.total_playground_uses += 1
        progress.save()
        
        return redirect('playground:playground')
