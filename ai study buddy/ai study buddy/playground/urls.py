from django.urls import path
from .views import PlaygroundView
app_name = 'playground'

urlpatterns = [
    path('', PlaygroundView.as_view(), name='playground'),
]
