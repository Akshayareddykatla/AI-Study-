"""
URL configuration for ai_smart_buddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from buddy.views import HomeView, DashboardView, ChatView, ChatAPIView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('chat/', ChatView.as_view(), name='chat'),
    path('chat-api/', ChatAPIView.as_view(), name='chat_api'),
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('quizzes/', include(('quizzes.urls', 'quizzes'))),
    path('progress/', include(('progress.urls', 'progress'))),
    path('analyzer/', include(('analyzer.urls', 'analyzer'))),
    path('playground/', include(('playground.urls', 'playground'))),
    path('videos/', include(('video_buddy.urls', 'video_buddy'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
