from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Quiz, Question, Choice, Result
from django.contrib import messages

class QuizListView(LoginRequiredMixin, ListView):
    model = Quiz
    template_name = 'quizzes/quiz_list.html'
    context_object_name = 'quizzes'

class TakeQuizView(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = 'quizzes/take_quiz.html'
    context_object_name = 'quiz'

    def post(self, request, *args, **kwargs):
        quiz = self.get_object()
        questions = quiz.questions.all()
        
        # Check if quiz has questions
        if not questions.exists():
            messages.error(request, "This quiz has no questions yet.")
            return redirect('quizzes:quiz_list')

        score = 0
        total_points = quiz.questions.count() # Each question counts as 1 point for total

        # Better score calculation:
        # We iterate through the POST data and check answers
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                try:
                    # Ensure the choice belongs to the current question
                    choice = Choice.objects.get(id=selected_choice_id, question=question)
                    if choice.is_correct:
                        score += 1 # Increment score by 1 for each correct answer
                except Choice.DoesNotExist:
                    # If choice doesn't exist or doesn't belong to the question, ignore it
                    pass

        # Create the result record
        result = Result.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total_points=total_points
        )

        messages.success(request, f"Quiz submitted successfully! You scored {score}/{total_points}.")
        return redirect('quizzes:quiz_result', result_id=result.id)

class QuizResultView(LoginRequiredMixin, DetailView):
    model = Result
    template_name = 'quizzes/result.html'
    context_object_name = 'result'
    pk_url_kwarg = 'result_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # We can still add calculations if needed
        result = self.get_object()
        context['percentage'] = (result.score / result.total_points * 100) if result.total_points > 0 else 0
        return context
