from django.test import TestCase
from .forms import PostForm, CommentForm
from .models import Post, Comment, Category
from django.urls import resolve, reverse
from .views import browse_posts, view_post, create_post, delete_post, delete_comment, search_forum
from account.models import CustomUser
from django.contrib.auth.models import User
from .views import (
    browse_posts,
    view_post,
    create_post,
    delete_post,
    delete_comment,
    search_forum
)


class PostFormTest(TestCase):
    # Test to ensure that the form is valid when all fields are filled out correctly
    def test_valid_form(self):
        form_data = {
            'title': 'Test Post',
            'description': 'This is a test post.'
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Test to ensure that the form is invalid when the title field is blank
    def test_blank_title_field(self):
        form_data = {
            'title': '',
            'description': 'This is a test post.'
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Test to ensure that the form is invalid when the description field is blank
    def test_blank_description_field(self):
        form_data = {
            'title': 'Test Post',
            'description': ''
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())


class CommentFormTest(TestCase):
    # Set up a Post object to use in testing the CommentForm
    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post', description='This is a test post.')

    # This test is currently commented out, but it appears to be testing the CommentForm
    # to ensure that it is invalid when the description field is blank.
    # It may have been left commented out for debugging purposes.
    # def test_comment_form_field(self):
    #     form_data = {
    #         'title': 'Test Post',
    #         'description': ''
    #     }
    #     form = PostForm(data=form_data)
    #     self.assertFalse(form.is_valid())


class ForumUrlsTestCase(TestCase):
    def test_browse_posts_url_resolves(self):
        # Get the URL for the 'posts' view with category ID of 1
        url = reverse('forum:posts', args=[1])
        # Check that the view function for this URL is 'browse_posts'
        self.assertEqual(resolve(url).func, browse_posts)

    def test_view_post_url_resolves(self):
        # Get the URL for viewing post with id 1 and category id 1
        url = reverse('forum:view_post', args=[1, 1])
        # Check if the URL is resolved to view_post view function
        self.assertEqual(resolve(url).func, view_post)

    def test_create_post_url_resolves(self):
        # Get the URL for creating a post with category id 1
        url = reverse('forum:create_post', args=[1])
        # Check if the URL is resolved to create_post view function
        self.assertEqual(resolve(url).func, create_post)

    def test_delete_post_url_resolves(self):
        # Get the URL for deleting a post with id 1 and category id 1
        url = reverse('forum:delete_post', args=[1, 1])
        # Check if the URL is resolved to delete_post view function
        self.assertEqual(resolve(url).func, delete_post)

    def test_delete_comment_url_resolves(self):
        # Get the URL for deleting a comment with id 1
        url = reverse('forum:delete_comment', args=[1])
        # Check if the URL is resolved to delete_comment view function
        self.assertEqual(resolve(url).func, delete_comment)

    def test_search_forum_url_resolves(self):
        # Get the URL for searching the forum
        url = reverse('forum:search_forum')
        # Check if the URL is resolved to search_forum view function
        self.assertEqual(resolve(url).func, search_forum)


# Define a test case for Category model
class CategoryModelTestCase(TestCase):
    # Define a setup method which will be called before running each test case
    # This method creates a category with the given title
    def setUp(self):
        Category.objects.create(title='Test Category')

    # Define a test case which tests the __str__ method of Category model
    # It gets the category instance and compares its string representation with the expected output
    def test_category_str_method(self):
        category = Category.objects.get(title='Test Category')
        self.assertEqual(str(category), 'Test Category')


# Define a test case for Post model
class PostModelTestCase(TestCase):

    # Define a setup method which will be called before running each test case
    # This method creates a user, a category and a post with given attributes
    def setUp(self):
        user = CustomUser.objects.create(username='testuser')
        category = Category.objects.create(title='Test Category')
        Post.objects.create(
            title='Test Post', description='Test Description', user=user, category=category)

# Define a test case for Comment model


class CommentModelTestCase(TestCase):

    # Define a setup method which will be called before running each test case
    # This method creates a user, a category, a post and a comment with given attributes
    def setUp(self):
        user = CustomUser.objects.create(username='testuser')
        category = Category.objects.create(title='Test Category')
        post = Post.objects.create(
            title='Test Post', description='Test Description', user=user, category=category)
        Comment.objects.create(
            description='Test Comment', user=user, post=post)


# create test cases for the forum
class ForumTestCase(TestCase):

    def setUp(self):
        # create test user
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        # create test category
        self.category = Category.objects.create(
            title='Test Category', content='Test content')
        # create test post
        self.post = Post.objects.create(
            title='Test Post', description='Test description', user=self.user, category=self.category)
        # create test comment
        self.comment = Comment.objects.create(
            description='Test comment', user=self.user, post=self.post)


# create test cases for PostForm
class PostFormTest(TestCase):
    def test_valid_form(self):
        # create form data with valid fields
        form_data = {
            'title': 'Test Post',
            'description': 'This is a test post.'
        }
        # create form object with form data
        form = PostForm(data=form_data)
        # assert that form is valid
        self.assertTrue(form.is_valid())

    def test_blank_title_field(self):
        # create form data with blank title field
        form_data = {
            'title': '',
            'description': 'This is a test post.'
        }
        # create form object with form data
        form = PostForm(data=form_data)
        # assert that form is not valid
        self.assertFalse(form.is_valid())

    def test_blank_description_field(self):
        # create form data with blank description field
        form_data = {
            'title': 'Test Post',
            'description': ''
        }
        # create form object with form data
        form = PostForm(data=form_data)
        # assert that form is not valid
        self.assertFalse(form.is_valid())


class ForumUrlsTestCase(TestCase):
    # Test if the URL for browsing posts resolves correctly
    def test_browse_posts_url_resolves(self):
        url = reverse('forum:posts', args=[1])
        self.assertEqual(resolve(url).func, browse_posts)

    # Test if the URL for viewing a post resolves correctly
    def test_view_post_url_resolves(self):
        url = reverse('forum:view_post', args=[1, 1])
        self.assertEqual(resolve(url).func, view_post)

    # Test if the URL for creating a post resolves correctly
    def test_create_post_url_resolves(self):
        url = reverse('forum:create_post', args=[1])
        self.assertEqual(resolve(url).func, create_post)

    # Test if the URL for deleting a post resolves correctly
    def test_delete_post_url_resolves(self):
        url = reverse('forum:delete_post', args=[1, 1])
        self.assertEqual(resolve(url).func, delete_post)

    # Test if the URL for deleting a comment resolves correctly
    def test_delete_comment_url_resolves(self):
        url = reverse('forum:delete_comment', args=[1])
        self.assertEqual(resolve(url).func, delete_comment)

    # Test if the URL for searching the forum resolves correctly
    def test_search_forum_url_resolves(self):
        url = reverse('forum:search_forum')
        self.assertEqual(resolve(url).func, search_forum)


# This test case is used to test the Category model.

class CategoryModelTestCase(TestCase):
    def setUp(self):
        # create a test Category
        Category.objects.create(title='Test Category')

    def test_category_str_method(self):
        # retrieve the test Category created in setUp()
        category = Category.objects.get(title='Test Category')
        # test that the category object's string representation is correct
        self.assertEqual(str(category), 'Test Category')


# This test case is used to test the Post model.

class PostModelTestCase(TestCase):
    def setUp(self):
        # create a test user
        user = CustomUser.objects.create(username='testuser')
        # create a test category
        category = Category.objects.create(title='Test Category')
        # create a test post
        Post.objects.create(
            title='Test Post', description='Test Description', user=user, category=category)


class PostFormTest(TestCase):
    # Test a valid post form
    def test_valid_form(self):
        # Form data to be tested
        form_data = {
            'title': 'Test Post',
            'description': 'This is a test post.'
        }
        # Create the form with the given data
        form = PostForm(data=form_data)
        # Ensure the form is valid
        self.assertTrue(form.is_valid())

    # Test an invalid post form with blank title field
    def test_blank_title_field(self):
        # Form data to be tested
        form_data = {
            'title': '',
            'description': 'This is a test post.'
        }
        # Create the form with the given data
        form = PostForm(data=form_data)
        # Ensure the form is invalid
        self.assertFalse(form.is_valid())

    # Test an invalid post form with blank description field
    def test_blank_description_field(self):
        # Form data to be tested
        form_data = {
            'title': 'Test Post',
            'description': ''
        }
        # Create the form with the given data
        form = PostForm(data=form_data)
        # Ensure the form is invalid
        self.assertFalse(form.is_valid())


# Define a test case for testing the URLs of the forum app
class ForumUrlsTestCase(TestCase):

    # Test whether the URL for browsing posts resolves to the correct view function
    def test_browse_posts_url_resolves(self):
        url = reverse('forum:posts', args=[1])
        self.assertEqual(resolve(url).func, browse_posts)

    # Test whether the URL for viewing a post resolves to the correct view function
    def test_view_post_url_resolves(self):
        url = reverse('forum:view_post', args=[1, 1])
        self.assertEqual(resolve(url).func, view_post)

    # Test whether the URL for creating a post resolves to the correct view function
    def test_create_post_url_resolves(self):
        url = reverse('forum:create_post', args=[1])
        self.assertEqual(resolve(url).func, create_post)

    # Test whether the URL for deleting a post resolves to the correct view function
    def test_delete_post_url_resolves(self):
        url = reverse('forum:delete_post', args=[1, 1])
        self.assertEqual(resolve(url).func, delete_post)

    # Test whether the URL for deleting a comment resolves to the correct view function
    def test_delete_comment_url_resolves(self):
        url = reverse('forum:delete_comment', args=[1])
        self.assertEqual(resolve(url).func, delete_comment)

    # Test whether the URL for searching the forum resolves to the correct view function
    def test_search_forum_url_resolves(self):
        url = reverse('forum:search_forum')
        self.assertEqual(resolve(url).func, search_forum)


# Define a test case for testing the Category model
class CategoryModelTestCase(TestCase):

    # Set up a test Category object to be used in the tests
    def setUp(self):
        Category.objects.create(title='Test Category')

    # Test the __str__ method of the Category model
    def test_category_str_method(self):
        category = Category.objects.get(title='Test Category')
        self.assertEqual(str(category), 'Test Category')
