from django.urls import path
from .views import VideoChatView, FavoriteListView, ToggleFavoriteView
app_name = 'video_buddy'

urlpatterns = [
    path('chat/', VideoChatView.as_view(), name='video_chat'),
    path('favorites/', FavoriteListView.as_view(), name='video_favorites'),
    path('toggle-favorite/', ToggleFavoriteView.as_view(), name='toggle_favorite'),
]
