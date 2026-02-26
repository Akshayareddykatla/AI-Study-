import requests
from django.conf import settings
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_smart_buddy.settings')
django.setup()

def test_gemini_key():
    api_key = getattr(settings, 'GEMINI_API_KEY', None)
    if not api_key:
        print("Error: GEMINI_API_KEY not found in settings.")
        return

    # Using the models list endpoint to verify key activity
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if 'models' in data:
                print(f"Status: ACTIVE")
                print(f"Total Models Available: {len(data['models'])}")
                # Show first model as proof
                print(f"First Model: {data['models'][0]['displayName']}")
            else:
                print(f"Status: SEMI-ACTIVE (Response received but no models listed)")
        else:
            print(f"Status: INACTIVE/ERROR")
            print(f"Response Code: {response.status_code}")
            print(f"Error Detail: {response.text}")
    except Exception as e:
        print(f"Status: ERROR")
        print(f"Exception: {str(e)}")

if __name__ == "__main__":
    test_gemini_key()
