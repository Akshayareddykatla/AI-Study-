import requests
from django.conf import settings

def generate_ai_response(question, level):
    """
    Generates a live AI response using the Gemini API.
    """
    api_key = getattr(settings, 'GEMINI_API_KEY', None)
    if not api_key:
        return "I'm sorry, but my AI brain isn't fully connected yet (API Key missing)."

    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={api_key}"
    
    # Custom prompt based on user level
    prompt = f"""
    You are an AI Study Buddy for a {level} level student.
    User Question: "{question}"
    
    Please provide an answer that is:
    1. Tailored to a {level} learner.
    2. Encouraging and helpful.
    3. Concise but informative.
    
    If appropriate, include a small code snippet or an example.
    """

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"Error communicating with AI Buddy: {str(e)}"
