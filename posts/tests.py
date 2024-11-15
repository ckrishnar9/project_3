from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(username='testuser')
        cls.post = Post.objects.create(title='Test Post', body='Test body', author=cls.user)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        cls.post.delete()

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.body, 'Test body')
        self.assertEqual(self.post.author, self.user)

    def test_post_retrieval(self):
        retrieved_post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(retrieved_post, self.post)

    def test_post_update(self):
        self.post.title = 'Updated Title'
        self.post.save()
        updated_post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(updated_post.title, 'Updated Title')

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')
