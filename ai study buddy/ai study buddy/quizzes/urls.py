from django.urls import path
from .views import QuizListView, TakeQuizView, QuizResultView
app_name = 'quizzes'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_list'),
    path('<int:pk>/', TakeQuizView.as_view(), name='take_quiz'),
    path('result/<int:result_id>/', QuizResultView.as_view(), name='quiz_result'),
]
