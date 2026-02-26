from django.urls import path

from .views import LeaderboardView
app_name = 'progress'

urlpatterns = [
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
]
