# from django.test import TestCase
# from .forms import SignUpForm, UpdateProfileForm
# from .models import CustomUser, Profile
# from django.utils import timezone
# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from django.core import mail
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.http import urlsafe_base64_encode
# from django.contrib.auth.tokens import default_token_generator
# from .models import CustomUser, Profile
# from .forms import SignUpForm, UpdateProfileForm
# from forum.models import Post
# from unittest.mock import patch, MagicMock
# from django.test import TestCase
# from django.urls import reverse, resolve
# from django.contrib.auth import views as auth_views
# from . import views

# # These test cases are for the models


# class CustomUserTests(TestCase):
#     def setUp(self):
#         self.user = CustomUser.objects.create_user(
#             email='testuser@example.com',
#             username='testuser',
#             password='testpass',
#             birthday=timezone.now(),
#             is_active=True
#         )
#         self.superuser = CustomUser.objects.create_superuser(
#             email='superuser@example.com',
#             username='superuser',
#             password='superpass',
#             birthday=timezone.now()
#         )

#     def test_create_user(self):
#         # Test that a user was created with the expected attributes
#         self.assertEqual(self.user.email, 'testuser@example.com')
#         self.assertEqual(self.user.username, 'testuser')
#         self.assertTrue(self.user.check_password('testpass'))
#         self.assertEqual(self.user.birthday, timezone.now())
#         self.assertFalse(self.user.is_staff)
#         self.assertTrue(self.user.is_active)
#         self.assertFalse(self.user.is_mod)

#     def test_create_superuser(self):
#         # Test that a superuser was created with the expected attributes
#         self.assertEqual(self.superuser.email, 'superuser@example.com')
#         self.assertEqual(self.superuser.username, 'superuser')
#         self.assertTrue(self.superuser.check_password('superpass'))
#         self.assertEqual(self.superuser.birthday, timezone.now())
#         self.assertTrue(self.superuser.is_staff)
#         self.assertTrue(self.superuser.is_active)
#         self.assertTrue(self.superuser.is_mod)
#         self.assertTrue(self.superuser.is_superuser)

#     def test_create_moderator(self):
#         # Test that a moderator was created with the expected attributes
#         moderator = CustomUser.objects.create_moderator(
#             email='moderator@example.com',
#             username='moderator',
#             password='modpass',
#             birthday=timezone.now()
#         )
#         self.assertFalse(moderator.is_superuser)
#         self.assertTrue(moderator.is_mod)

#     def test_profile_creation(self):
#         # Test that a profile was created when a user was created
#         self.assertIsInstance(self.user.profile, Profile)
#         self.assertEqual(self.user.profile.name, '')
#         self.assertEqual(self.user.profile.bio, 'Hello, I am new')
#         self.assertEqual(str(self.user.profile.image), 'images/default.png')

#     def test_profile_update(self):
#         # Test that a profile can be updated
#         self.user.profile.name = 'Test User'
#         self.user.profile.bio = 'This is a test profile'
#         self.user.profile.save()
#         self.assertEqual(self.user.profile.name, 'Test User')
#         self.assertEqual(self.user.profile.bio, 'This is a test profile')

# # These test cases are for the views


# class SignUpTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.signup_url = reverse('account:signup')
#         self.user = {
#             'username': 'testuser',
#             'email': 'testuser@gmail.com',
#             'password1': 'test1234',
#             'password2': 'test1234',
#         }
#         self.valid_form_data = {
#             'username': 'user1',
#             'email': 'user1@example.com',
#             'password1': 'test1234',
#             'password2': 'test1234',
#         }
#         self.invalid_form_data = {
#             'username': 'user1',
#             'email': 'user1@example.com',
#             'password1': 'test1234',
#             'password2': 'test123',  # password2 is not the same as password1
#         }

#     def test_signup_form_valid_data(self):
#         response = self.client.post(self.signup_url, self.valid_form_data)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration/confirm.html')
#         self.assertEqual(len(mail.outbox), 1)
#         self.assertIn('Activate your Hear It Here account.',
#                       mail.outbox[0].subject)

#     def test_signup_form_invalid_data(self):
#         response = self.client.post(self.signup_url, self.invalid_form_data)
#         self.assertEqual(response.status_code, 200)
#         self.assertFormError(response, 'form', 'password2',
#                              'The two password fields didn\'t match.')

#     def test_signup_form_get(self):
#         response = self.client.get(self.signup_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertIsInstance(response.context['form'], SignUpForm)

#     def test_signup_form_invalid_method(self):
#         response = self.client.put(self.signup_url, self.valid_form_data)
#         self.assertEqual(response.status_code, 405)  # Method Not Allowed


# # These test cover the urls


# class TestUrls(TestCase):

#     def test_auth_url_resolves(self):
#         url = reverse('account:login')
#         self.assertEqual(resolve(url).func, views.login)

#     def test_signup_url_resolves(self):
#         url = reverse('account:signup')
#         self.assertEqual(resolve(url).func, views.signup)

#     def test_login_url_resolves(self):
#         url = reverse('account:login')
#         self.assertEqual(resolve(url).func, views.login)

#     def test_logout_url_resolves(self):
#         url = reverse('account:logout')
#         self.assertEqual(resolve(url).func, views.logout)

#     def test_to_profile_url_resolves(self):
#         url = reverse('account:redirect')
#         self.assertEqual(resolve(url).func, views.to_profile)

#     def test_profile_url_resolves(self):
#         url = reverse('account:profile', args=['test_user'])
#         self.assertEqual(resolve(url).func, views.profile)

#     def test_update_profile_url_resolves(self):
#         url = reverse('account:update_profile', args=['test_user'])
#         self.assertEqual(resolve(url).func, views.update_profile)

#     def test_activate_url_resolves(self):
#         url = reverse('account:activate', args=['uidb64', 'token'])
#         self.assertEqual(resolve(url).func, views.activate)

#     def test_auth_included(self):
#         url = reverse('account:login')
#         self.assertIn('auth/', url)

#     def test_auth_login_url(self):
#         url = reverse('account:login')
#         self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

#     def test_auth_logout_url(self):
#         url = reverse('account:logout')
#         self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

#     def test_activate_url_name(self):
#         url = reverse('account:activate', args=['uidb64', 'token'])
#         self.assertEqual(url, '/account/activate/uidb64/token/')


# class SignUpFormTest(TestCase):
#     def setUp(self):
#         self.user_data = {
#             'email': 'testuser@example.com',
#             'username': 'testuser',
#             'password1': 'testpass123',
#             'password2': 'testpass123',
#             'birthday': '1990-01-01'
#         }

#     def test_form_with_valid_data(self):
#         form = SignUpForm(data=self.user_data)
#         self.assertTrue(form.is_valid())

#     def test_form_with_missing_required_fields(self):
#         data = self.user_data.copy()
#         del data['email']
#         form = SignUpForm(data=data)
#         self.assertFalse(form.is_valid())
#         self.assertIn('email', form.errors)

#     def test_form_with_invalid_email(self):
#         data = self.user_data.copy()
#         data['email'] = 'invalid email'
#         form = SignUpForm(data=data)
#         self.assertFalse(form.is_valid())
#         self.assertIn('email', form.errors)

#     def test_form_with_non_matching_passwords(self):
#         data = self.user_data.copy()
#         data['password2'] = 'notmatching'
#         form = SignUpForm(data=data)
#         self.assertFalse(form.is_valid())
#         self.assertIn('password2', form.errors)
