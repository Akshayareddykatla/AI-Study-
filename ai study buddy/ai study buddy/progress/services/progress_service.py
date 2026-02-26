from django.utils import timezone
import datetime
from quizzes.models import Result
from ..models import UserProgress

class ProgressService:
    @staticmethod
    def calculate_subject_performance(user):
        results = Result.objects.filter(user=user).select_related('quiz')
        cat_perf = {}
        
        for res in results:
            cat = res.quiz.get_category_display()
            if cat not in cat_perf:
                cat_perf[cat] = {'score': 0, 'total': 0}
            cat_perf[cat]['score'] += res.score
            cat_perf[cat]['total'] += res.total_points
            
        if not cat_perf:
            return None, None
            
        # Sort by percentage
        sorted_cats = sorted(
            cat_perf.items(), 
            key=lambda x: (x[1]['score'] / x[1]['total']) if x[1]['total'] > 0 else 0
        )
        
        weakest = sorted_cats[0][0]
        strongest = sorted_cats[-1][0]
        return strongest, weakest

    @staticmethod
    def update_streak(progress):
        today = timezone.now().date()
        if progress.last_activity_date == today:
            return
        
        if progress.last_activity_date == today - datetime.timedelta(days=1):
            progress.current_streak += 1
        else:
            progress.current_streak = 1
        
        if progress.current_streak > progress.longest_streak:
            progress.longest_streak = progress.current_streak
        
        progress.last_activity_date = today

    @staticmethod
    def check_badges(progress, result=None):
        new_badges = list(progress.badges)
        
        # Engagement Badges
        if progress.total_quizzes_taken >= 1 and "First Quiz" not in new_badges:
            new_badges.append("First Quiz")
        if progress.total_quizzes_taken >= 10 and "Decathlon" not in new_badges:
            new_badges.append("Decathlon")
            
        # Performance Badges
        if result and result.score == result.total_points and "Perfect Score" not in new_badges:
            new_badges.append("Perfect Score")
            
        # Streak Badges
        if progress.current_streak >= 3 and "3-Day Streak" not in new_badges:
            new_badges.append("3-Day Streak")
            
        progress.badges = new_badges

    @staticmethod
    def update_highest_score(progress, result_score):
        if result_score > progress.highest_score:
            progress.highest_score = result_score
