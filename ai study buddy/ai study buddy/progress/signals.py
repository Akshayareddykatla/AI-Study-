from django.db.models.signals import post_save
from django.dispatch import receiver
from buddy.models import Message
from quizzes.models import Result
from .models import UserProgress
from .services.progress_service import ProgressService

@receiver(post_save, sender=Message)
def update_questions_count(sender, instance, created, **kwargs):
    if created and instance.sender == 'user':
        progress, _ = UserProgress.objects.get_or_create(user=instance.conversation.user)
        progress.total_questions_asked += 1
        ProgressService.update_streak(progress)
        progress.save()

@receiver(post_save, sender=Result)
def update_quiz_progress_logic(sender, instance, created, **kwargs):
    if created:
        progress, _ = UserProgress.objects.get_or_create(user=instance.user)
        progress.total_quizzes_taken += 1
        progress.total_score_sum += instance.score
        progress.total_points_sum += instance.total_points
        
        # Performance Analytics via Service
        strongest, weakest = ProgressService.calculate_subject_performance(instance.user)
        progress.strongest_subject = strongest
        progress.weakest_subject = weakest
        
        # High Score Tracking
        ProgressService.update_highest_score(progress, instance.score)
        
        # Streak & Badges
        ProgressService.update_streak(progress)
        ProgressService.check_badges(progress, instance)
        
        progress.save()
