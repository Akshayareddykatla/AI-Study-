from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import VideoSearch, FavoriteVideo
from .services.gemini_video_service import GeminiVideoService
import json

class VideoChatView(LoginRequiredMixin, View):
    def get(self, request):
        history = VideoSearch.objects.filter(user=request.user).order_by('-timestamp')[:5]
        return render(request, 'video_buddy/chat.html', {'history': history})

    def post(self, request):
        query = request.POST.get('query')
        if not query:
            return redirect('video_buddy:video_chat')
        
        service = GeminiVideoService()
        ai_response, search_data = service.get_video_recommendations(query)
        
        VideoSearch.objects.create(
            user=request.user,
            query=query,
            ai_response=ai_response,
            suggested_search_terms=search_data  # Now stores list of dicts: {'query': ..., 'explanation': ...}
        )
        
        return redirect('video_buddy:video_chat')

class FavoriteListView(LoginRequiredMixin, View):
    def get(self, request):
        favorites = FavoriteVideo.objects.filter(user=request.user)
        return render(request, 'video_buddy/favorites.html', {'favorites': favorites})

class ToggleFavoriteView(LoginRequiredMixin, View):
    def post(self, request):
        data = json.loads(request.body)
        video_id = data.get('video_id')
        title = data.get('title')
        thumbnail_url = data.get('thumbnail_url')
        video_url = data.get('video_url')

        favorite, created = FavoriteVideo.objects.get_or_create(
            user=request.user,
            video_id=video_id,
            defaults={
                'title': title,
                'thumbnail_url': thumbnail_url,
                'video_url': video_url
            }
        )

        if not created:
            favorite.delete()
            return JsonResponse({'status': 'removed'})
        
        return JsonResponse({'status': 'added'})
