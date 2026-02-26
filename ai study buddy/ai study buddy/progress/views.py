from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProgress

class LeaderboardView(LoginRequiredMixin, ListView):
    model = UserProgress
    template_name = 'progress/leaderboard.html'
    context_object_name = 'rankings'

    def get_queryset(self):
        # Rank by total score sum
        return UserProgress.objects.all().order_by('-total_score_sum')[:10]
