import os
import PyPDF2
import json
import requests
from django.conf import settings

class FileProcessingService:
    @staticmethod
    def extract_text(file_path):
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.txt':
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        elif ext == '.pdf':
            text = ""
            try:
                with open(file_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        text += page.extract_text() + "\n"
                return text
            except Exception as e:
                return f"Error reading PDF: {str(e)}"
        return ""

    @staticmethod
    def _call_gemini(prompt):
        api_key = getattr(settings, 'GEMINI_API_KEY', None)
        if not api_key:
            return None
        
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={api_key}"
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
        
        try:
            response = requests.post(api_url, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            return data['candidates'][0]['content']['parts'][0]['text']
        except Exception:
            return None

    @staticmethod
    def generate_summary(text):
        if not text or len(text.strip()) < 50:
            return "Content too short to summarize."

        prompt = f"""
        Summarize the following study material in 3-4 concise and helpful sentences.
        Focus on the core concepts for a student.
        Content:
        {text[:15000]}
        """
        
        summary = FileProcessingService._call_gemini(prompt)
        if not summary:
            # Fallback to simple logic if API fails
            import re
            sentences = re.split(r'(?<=[.!?]) +', text.strip())
            return " ".join(sentences[:3])
            
        return summary.strip()

    @staticmethod
    def generate_questions(text):
        if not text or len(text.strip()) < 100:
            return []

        prompt = f"""
        Based on the following study material, generate 5 high-quality multiple-choice questions.
        Each question must have:
        1. The question text.
        2. The correct answer.
        3. A list of 3 incorrect distractors.
        
        Format the response ONLY as a JSON array of objects with keys: 'text', 'correct_answer', 'distractors'.
        Example:
        [
          {{"text": "What is AI?", "correct_answer": "Artificial Intelligence", "distractors": ["Apple Inc", "Active Index", "Auto Ion"]}}
        ]
        
        Content:
        {text[:15000]}
        """
        
        ai_response = FileProcessingService._call_gemini(prompt)
        if ai_response:
            try:
                # Clean up markdown JSON blocks if present
                clean_json = ai_response.strip()
                if clean_json.startswith('```json'):
                    clean_json = clean_json[7:]
                if clean_json.endswith('```'):
                    clean_json = clean_json[:-3]
                
                return json.loads(clean_json.strip())
            except Exception:
                pass
        
        # Fallback to empty list or basic logic if API fails
        return []
