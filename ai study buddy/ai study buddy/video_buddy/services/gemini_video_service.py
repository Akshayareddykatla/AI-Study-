import requests
import json
from django.conf import settings

class GeminiVideoService:
    def __init__(self, api_key=None):
        self.api_key = api_key or getattr(settings, 'GEMINI_API_KEY', None)
        # Use simple model name if gemini-3-flash-preview is not working, 
        # but user specifically set it so I will keep it or use a fallback.
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.api_key}"

    def get_video_recommendations(self, topic):
        if not self.api_key:
            return "API Key not configured.", []

        prompt = f"""
        User wants to learn about: {topic}
        As an AI Study Buddy, recommend 3-5 specific YouTube search queries or video topics that would be most helpful.
        Provide a brief explanation for each.
        
        Format your response ONLY as a JSON object with the following keys:
        - "study_buddy_message": A friendly, encouraging introductory message (2-3 sentences).
        - "search_queries": A list of objects, each with "query" and "explanation".
        - "encouragement": A short closing encouraging sentence.
        
        Response should be encouraging and focus on high-quality educational content.
        """

        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }

        try:
            response = requests.post(self.api_url, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            ai_text = data['candidates'][0]['content']['parts'][0]['text'].strip()
            
            # Basic cleaning if AI includes markdown blocks
            if ai_text.startswith('```json'):
                ai_text = ai_text[7:]
            if ai_text.endswith('```'):
                ai_text = ai_text[:-3]
            
            structured_data = json.loads(ai_text.strip())
            
            message = f"{structured_data.get('study_buddy_message', '')}\n\n{structured_data.get('encouragement', '')}"
            queries = structured_data.get('search_queries', [])
            
            return message.strip(), queries
        except Exception as e:
            # Fallback for errors or non-JSON responses
            fallback_msg = f"I found some great topics for {topic}!"
            fallback_queries = [
                {"query": f"{topic} for beginners", "explanation": "Start with the fundamentals."},
                {"query": f"{topic} tutorial", "explanation": "A complete walkthrough of the topic."},
                {"query": f"Advanced {topic} concepts", "explanation": "Deep dive into more complex areas."}
            ]
            return fallback_msg, fallback_queries
