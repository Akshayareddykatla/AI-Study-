from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('hub/', views.NotesHubView.as_view(), name='hub'),
    path('upload-note/', views.NoteUploadView.as_view(), name='upload_note'),
    path('upload-cert/', views.CertUploadView.as_view(), name='upload_cert'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='detail'),
]
