import os
import django
import sys

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_smart_buddy.settings')
django.setup()

from django.conf import settings
from buddy.services.ai_service import generate_ai_response
from video_buddy.services.gemini_video_service import GeminiVideoService
from analyzer.services.file_service import FileProcessingService

def test_buddy_chat():
    print("Testing Buddy Chat...")
    try:
        response = generate_ai_response("What is the capital of France?", "beginner")
        print(f"Response: {response[:100]}...")
        return "Paris" in response
    except Exception as e:
        print(f"Buddy Chat Error: {e}")
        return False

def test_video_buddy():
    print("\nTesting Video Buddy...")
    try:
        service = GeminiVideoService()
        text, queries = service.get_video_recommendations("Python Programming")
        print(f"Text: {text[:100]}...")
        print(f"Queries: {queries}")
        return len(queries) > 0 and "Error" not in text
    except Exception as e:
        print(f"Video Buddy Error: {e}")
        return False

def test_analyzer():
    print("\nTesting Analyzer (Summary & Questions)...")
    try:
        text = """
        Python is an interpreted, high-level, general-purpose programming language. 
        Created by Guido van Rossum and first released in 1991, Python's design philosophy 
        emphasizes code readability with its notable use of significant whitespace. 
        Its language constructs and object-oriented approach aim to help programmers 
        write clear, logical code for small and large-scale projects.
        """
        summary = FileProcessingService.generate_summary(text)
        print(f"Summary: {summary}")
        
        questions = FileProcessingService.generate_questions(text)
        print(f"Questions: {len(questions)} generated.")
        for q in questions:
            print(f"- {q['text']}")
        
        return len(summary) > 20 and len(questions) > 0 and "Error" not in summary
    except Exception as e:
        print(f"Analyzer Error: {e}")
        return False

if __name__ == "__main__":
    print(f"Using API Key: {settings.GEMINI_API_KEY[:10]}...")
    
    results = {
        "Buddy Chat": test_buddy_chat(),
        "Video Buddy": test_video_buddy(),
        "Analyzer": test_analyzer()
    }
    
    print("\n" + "="*20)
    print("FINAL RESULTS")
    print("="*20)
    for test, passed in results.items():
        print(f"{test}: {'PASSED' if passed else 'FAILED'}")
