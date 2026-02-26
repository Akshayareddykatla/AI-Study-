from django.urls import path
from .views import FileUploadView, FileSummaryView, FileHistoryView
app_name = 'analyzer'

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('summary/<int:pk>/', FileSummaryView.as_view(), name='file_summary'),
    path('history/', FileHistoryView.as_view(), name='file_history'),
]
