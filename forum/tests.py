from django.test import TestCase
from .forms import PostForm, CommentForm
from .models import Post, Comment, Category
from django.urls import resolve, reverse
from .views import browse_posts, view_post, create_post, delete_post, delete_comment, search_forum
from account.models import CustomUser
from django.contrib.auth.models import User


class PostFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'title': 'Test Post',
            'description': 'This is a test post.'
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_title_field(self):
        form_data = {
            'title': '',
            'description': 'This is a test post.'
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_blank_description_field(self):
        form_data = {
            'title': 'Test Post',
            'description': ''
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())


class CommentFormTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post', description='This is a test post.')


class ForumUrlsTestCase(TestCase):
    def test_browse_posts_url_resolves(self):
        url = reverse('forum:posts', args=[1])
        self.assertEqual(resolve(url).func, browse_posts)

    def test_view_post_url_resolves(self):
        url = reverse('forum:view_post', args=[1, 1])
        self.assertEqual(resolve(url).func, view_post)

    def test_create_post_url_resolves(self):
        url = reverse('forum:create_post', args=[1])
        self.assertEqual(resolve(url).func, create_post)

    def test_delete_post_url_resolves(self):
        url = reverse('forum:delete_post', args=[1, 1])
        self.assertEqual(resolve(url).func, delete_post)

    def test_delete_comment_url_resolves(self):
        url = reverse('forum:delete_comment', args=[1])
        self.assertEqual(resolve(url).func, delete_comment)

    def test_search_forum_url_resolves(self):
        url = reverse('forum:search_forum')
        self.assertEqual(resolve(url).func, search_forum)


class CategoryModelTestCase(TestCase):
    def setUp(self):
        Category.objects.create(title='Test Category')

    def test_category_str_method(self):
        category = Category.objects.get(title='Test Category')
        self.assertEqual(str(category), 'Test Category')


class PostModelTestCase(TestCase):
    def setUp(self):
        user = CustomUser.objects.create(username='testuser')
        category = Category.objects.create(title='Test Category')
        Post.objects.create(
            title='Test Post', description='Test Description', user=user, category=category)


class CommentModelTestCase(TestCase):
    def setUp(self):
        user = CustomUser.objects.create(username='testuser')
        category = Category.objects.create(title='Test Category')
        post = Post.objects.create(
            title='Test Post', description='Test Description', user=user, category=category)
        Comment.objects.create(
            description='Test Comment', user=user, post=post)


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

