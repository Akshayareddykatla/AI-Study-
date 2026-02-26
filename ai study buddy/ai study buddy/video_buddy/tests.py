from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import VideoSearch, FavoriteVideo
from unittest.mock import patch

class VideoBuddyTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = Client()
        self.client.login(username='testuser', password='password')

    def test_video_search_model(self):
        search = VideoSearch.objects.create(
            user=self.user,
            query='Python tutorial',
            ai_response='Check these videos',
            suggested_search_terms=['python basic', 'django tips']
        )
        self.assertEqual(search.query, 'Python tutorial')
        self.assertEqual(len(search.suggested_search_terms), 2)

    def test_favorite_video_model(self):
        fav = FavoriteVideo.objects.create(
            user=self.user,
            video_id='lyu7v7nVzfo',
            title='Sample Video',
            thumbnail_url='http://img.com/1.jpg',
            video_url='http://youtube.com/v/1'
        )
        self.assertEqual(fav.video_id, 'lyu7v7nVzfo')

    def test_video_chat_view_get(self):
        response = self.client.get(reverse('video_buddy:video_chat'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'video_buddy/chat.html')

    @patch('video_buddy.services.gemini_video_service.GeminiVideoService.get_video_recommendations')
    def test_video_chat_view_post(self, mock_gemini):
        mock_gemini.return_value = ("AI recommendations...", ["term1", "term2"])
        response = self.client.post(reverse('video_buddy:video_chat'), {'query': 'Machine Learning'})
        self.assertEqual(response.status_code, 302) # Redirect to self
        self.assertEqual(VideoSearch.objects.count(), 1)
        self.assertEqual(VideoSearch.objects.first().query, 'Machine Learning')

    def test_toggle_favorite_view(self):
        data = {
            'video_id': 'abc12345678',
            'title': 'Test Video',
            'thumbnail_url': 'http://img.com/thumb.jpg',
            'video_url': 'https://www.youtube.com/watch?v=abc12345678'
        }
        # Add favorite
        response = self.client.post(
            reverse('video_buddy:toggle_favorite'),
            data=data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'added')
        self.assertEqual(FavoriteVideo.objects.count(), 1)

        # Remove favorite
        response = self.client.post(
            reverse('video_buddy:toggle_favorite'),
            data=data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'removed')
        self.assertEqual(FavoriteVideo.objects.count(), 0)

    def test_favorites_list_view(self):
        FavoriteVideo.objects.create(
            user=self.user,
            video_id='v1',
            title='Title 1',
            thumbnail_url='u1',
            video_url='u1'
        )
        response = self.client.get(reverse('video_buddy:video_favorites'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Title 1')
