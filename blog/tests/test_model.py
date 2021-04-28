from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone
from django.utils.text import slugify


class PostModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		 # Set up non-modified objects used by all test methods
		user=User.objects.create(username='john', email='john@gmail.com', password='john')
		Post.objects.create(author=user, title='Title of blog', body='Body of the blog', status=1, date_modified=timezone.now())

	def setUp(self):
		print('Setup: Run once for every test method to setup clean data/')
		pass

	def test_post_title(self):
		post = Post.objects.get(id=1)
		post_title = post.title
		self.assertEqual(post_title, 'Title of blog')

	def test_post_author(self):
		post = Post.objects.get(id=1)
		post_author = post.author.username
		self.assertEqual(post_author, 'john')

	def test_post_title_slug(self):
		post = Post.objects.get(id=1)
		post_slug = post.slug
		title = 'Title of blog'
		self.assertEqual(post_slug, slugify(title))

	def test_post_body(self):
		post = Post.objects.get(id=1)
		post_body = post.body
		self.assertEqual(post_body, 'Body of the blog')

