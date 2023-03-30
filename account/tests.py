from django.test import TestCase
from .forms import SignUpForm, UpdateProfileForm
from .models import CustomUser, Profile
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core import mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from .models import CustomUser, Profile
from forum.models import Post
from unittest.mock import patch, MagicMock
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from . import views

# These test cases are for the models


# Define a test case to test CustomUser model and its methods
class CustomUserTests(TestCase):
    
    # Set up users to be used in tests
    def setUp(self):
        # Create a regular user
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            password='testpass',
            is_active=True
        )
        # Create a superuser
        self.superuser = CustomUser.objects.create_superuser(
            email='superuser@example.com',
            username='superuser',
            password='superpass',
        )
    
    # Test that a user was created with the expected attributes
    def test_create_user(self):
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpass'))
        self.assertFalse(self.user.is_staff)
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_mod)
    
    # Test that a superuser was created with the expected attributes
    def test_create_superuser(self):
        self.assertEqual(self.superuser.email, 'superuser@example.com')
        self.assertEqual(self.superuser.username, 'superuser')
        self.assertTrue(self.superuser.check_password('superpass'))
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_active)
        self.assertTrue(self.superuser.is_mod)
        self.assertTrue(self.superuser.is_superuser)
    
    # Test that a moderator was created with the expected attributes
    def test_create_moderator(self):
        # Create a moderator
        moderator = CustomUser.objects.create_moderator(
            email='moderator@example.com',
            username='moderator',
            password='modpass',
        )
        # Check moderator attributes
        self.assertFalse(moderator.is_superuser)
        self.assertTrue(moderator.is_mod)
    
    # Test that a profile was created when a user was created
    def test_profile_creation(self):
        # Check that user has an associated Profile instance
        self.assertIsInstance(self.user.profile, Profile)
        # Check initial Profile attributes
        self.assertEqual(self.user.profile.name, '')
        self.assertEqual(self.user.profile.bio, 'Hello, I am new')
        self.assertEqual(str(self.user.profile.image), 'images/default.png')
    
    # Test that a profile can be updated
    def test_profile_update(self):
        # Update user profile
        self.user.profile.name = 'Test User'
        self.user.profile.bio = 'This is a test profile'
        self.user.profile.save()
        # Check updated Profile attributes
        self.assertEqual(self.user.profile.name, 'Test User')
        self.assertEqual(self.user.profile.bio, 'This is a test profile')


# These test cases are for the views


class SignUpTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('account:signup')

        # Define some test user data
        self.user = {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'test1234',
            'password2': 'test1234',
        }

        # Define valid form data
        self.valid_form_data = {
            'username': 'user1',
            'email': 'user1@example.com',
            'password1': 'test1234',
            'password2': 'test1234',
        }

        # Define invalid form data
        self.invalid_form_data = {
            'username': 'user1',
            'email': 'user1@example.com',
            'password1': 'test1234',
            'password2': 'test123',  # password2 is not the same as password1
        }

    def test_signup_form_valid_data(self):
        # Test submitting the signup form with valid data
        response = self.client.post(self.signup_url, self.valid_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form_invalid_data(self):
        # Test submitting the signup form with invalid data
        response = self.client.post(self.signup_url, self.invalid_form_data)
        form = SignUpForm(response.request)
        # validate form, submit and redirect to post pages
        self.assertFalse(form.is_valid())

        

    def test_signup_form_get(self):
        # Test getting the signup form
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], SignUpForm)

    def test_signup_form_invalid_method(self):
        # Test submitting the signup form with an invalid HTTP method
        response = self.client.put(self.signup_url, self.valid_form_data)
        self.assertEqual(response.status_code, 200)  # Method Not Allowed



# These test cover the urls


# Define a TestCase class to test the URL configurations of the project
class TestUrls(TestCase):
    # Test that the URL for account signup resolves to the correct view function
    def test_signup_url_resolves(self):
        url = reverse('account:signup')
        self.assertEqual(resolve(url).func, views.signup)


    # Test that the URL for redirecting to the user's profile page resolves to the correct view function
    def test_to_profile_url_resolves(self):
        url = reverse('account:redirect')
        self.assertEqual(resolve(url).func, views.to_profile)

    # Test that the URL for the user's profile page resolves to the correct view function
    def test_profile_url_resolves(self):
        url = reverse('account:profile', args=['test_user'])
        self.assertEqual(resolve(url).func, views.profile)

    # Test that the URL for updating the user's profile page resolves to the correct view function
    def test_update_profile_url_resolves(self):
        url = reverse('account:update_profile', args=['test_user'])
        self.assertEqual(resolve(url).func, views.update_profile)

    # Test that the URL for activating an account resolves to the correct view function
    def test_activate_url_resolves(self):
        url = reverse('account:activate', args=['uidb64', 'token'])
        self.assertEqual(resolve(url).func, views.activate)

    # Test that the word 'auth/' is included in the account login URL
    def test_auth_included(self):
        url = reverse('account:login')
        self.assertIn('auth/', url)

    # Test that the account login URL resolves to the Django built-in LoginView class
    def test_auth_login_url(self):
        url = reverse('account:login')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    # Test that the account logout URL resolves to the Django built-in LogoutView class
    def test_auth_logout_url(self):
        url = reverse('account:logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

    # Test that the URL for activating an account includes the correct arguments
    def test_activate_url_name(self):
        url = reverse('account:activate', args=['uidb64', 'token'])
        self.assertEqual(url, '/account/activate/uidb64/token/')



# A class to test SignUpForm
class SignUpFormTest(TestCase):
    # Setup method to create user data
    def setUp(self):
        self.user_data = {
            'email': 'testuser@example.com',
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }

    # Test SignUpForm with valid data
    def test_form_with_valid_data(self):
        form = SignUpForm(data=self.user_data)
        self.assertTrue(form.is_valid())

    # Test SignUpForm with missing required fields
    def test_form_with_missing_required_fields(self):
        # Create a copy of the user data and delete the email field
        data = self.user_data.copy()
        del data['email']
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid()) # Expect the form to be invalid
        self.assertIn('email', form.errors) # Expect the 'email' field to be missing

    # Test SignUpForm with invalid email
    def test_form_with_invalid_email(self):
        # Create a copy of the user data and change the email to an invalid one
        data = self.user_data.copy()
        data['email'] = 'invalid email'
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid()) # Expect the form to be invalid
        self.assertIn('email', form.errors) # Expect the 'email' field to be invalid

    # Test SignUpForm with non-matching passwords
    def test_form_with_non_matching_passwords(self):
        # Create a copy of the user data and change the second password to a non-matching one
        data = self.user_data.copy()
        data['password2'] = 'notmatching'
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid()) # Expect the form to be invalid
        self.assertIn('password2', form.errors) # Expect the 'password2' field to not match

