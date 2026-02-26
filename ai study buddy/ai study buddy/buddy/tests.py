from django.test import TestCase
from unittest.mock import patch
from .services.ai_service import generate_ai_response

class AIServiceTest(TestCase):
    @patch('requests.post')
    def test_ai_response_success(self, mock_post):
        """Verify that AI response is correctly parsed from API."""
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            'candidates': [{
                'content': {
                    'parts': [{'text': 'Hello! I am your AI Buddy.'}]
                }
            }]
        }
        
        response = generate_ai_response("Hello", "beginner")
        self.assertEqual(response, 'Hello! I am your AI Buddy.')

    @patch('requests.post')
    def test_ai_response_api_failure(self, mock_post):
        """Verify graceful error handling on API failure."""
        mock_post.side_effect = Exception("Connection Timeout")
        
        response = generate_ai_response("Hello", "beginner")
        self.assertIn("Error communicating with AI Buddy", response)
