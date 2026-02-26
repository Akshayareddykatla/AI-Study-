import os
import sys
import django

# Set up Django environment
sys.path.append(r'c:\Users\rajes\OneDrive\Documents\study-ai\ai study buddy\ai study buddy')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_smart_buddy.settings')
django.setup()

from video_buddy.services.gemini_video_service import GeminiVideoService

def test_gemini():
    service = GeminiVideoService()
    print(f"Using API Key: {service.api_key[:5]}...{service.api_key[-5:]}")
    print(f"Using URL: {service.api_url.split('?')[0]}")
    
    ai_text, search_terms = service.get_video_recommendations("Python Programming")
    print(f"AI Response Snippet: {ai_text[:100]}...")
    print(f"Search Terms: {search_terms}")

if __name__ == "__main__":
    test_gemini()
