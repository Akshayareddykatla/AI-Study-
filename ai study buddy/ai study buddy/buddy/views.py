import json
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Conversation, Message, Subject
from progress.models import UserProgress

class HomeView(TemplateView):
    template_name = 'home.html'

from quizzes.models import Result

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        progress, created = UserProgress.objects.get_or_create(user=self.request.user)
        context['progress'] = progress
        # Latest 5 quiz results
        context['recent_results'] = Result.objects.filter(user=self.request.user).order_by('-timestamp')[:5]
        return context

class ChatView(LoginRequiredMixin, TemplateView):
    template_name = 'chat.html'

from .services.ai_service import generate_ai_response

class ChatAPIView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            user_text = data.get('message')
            
            # Get user level from profile
            user_level = request.user.profile.learning_level
            
            # Get or create an active conversation
            conversation, created = Conversation.objects.get_or_create(user=request.user)
            
            # Save user message
            Message.objects.create(
                conversation=conversation,
                sender='user',
                text=user_text
            )
            
            # Generate AI response using the service
            buddy_text = generate_ai_response(user_text, user_level)
            
            # Save buddy message
            Message.objects.create(
                conversation=conversation,
                sender='buddy',
                text=buddy_text
            )
            
            return JsonResponse({
                'status': 'success',
                'buddy_response': buddy_text
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
