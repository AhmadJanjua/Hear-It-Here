from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponse

class HomeResponseViewTestCase(TestCase):
    def setUp(self):
        # Set up the client and URL to test against
        self.client = Client()
        self.home_url = reverse('homepage:home')

    def test_home_response(self):
        # Test that the home URL returns a 200 response status code
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_home_message(self):
        # Test that the home page contains the expected welcome message
        response = self.client.get(self.home_url)
        self.assertContains(response, 'General Discussions')

    def test_home_return_respose(self):
        # Test that the home URL returns an instance of the HttpResponse object
        response = self.client.get(self.home_url)
        self.assertIsInstance(response, HttpResponse)

