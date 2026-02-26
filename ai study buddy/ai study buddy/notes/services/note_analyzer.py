import requests
from django.conf import settings

class GeminiNoteAnalyzer:
    def __init__(self, api_key=None):
        self.api_key = api_key or getattr(settings, 'GEMINI_API_KEY', None)
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={self.api_key}"

    def analyze_note(self, content, title):
        if not self.api_key:
            return "API Key not configured."

        prompt = f"""
        Analyze the following study notes titled: "{title}"
        Content:
        {content[:15000]}  # Limit content to stay within reasonable limits

        As an AI Study Buddy, providing the following:
        1. A 3-sentence high-level summary.
        2. 3 Key Concepts mentioned.
        3. A 'Self-Check' question for the user to test their understanding.

        Keep the tone professional yet encouraging.
        """

        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }

        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()
            data = response.json()
            return data['candidates'][0]['content']['parts'][0]['text']
        except Exception as e:
            return f"Error analyzing note: {str(e)}"
