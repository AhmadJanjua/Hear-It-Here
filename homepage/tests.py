from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponse

class HomeResponseViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('homepage:home')

    def test_home_response(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, HttpResponse)
        self.assertContains(response, 'Welcome to the homepage!')

