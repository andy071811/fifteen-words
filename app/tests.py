from django.test import TestCase, Client

from .models import Comment

# Create your tests here.

class CommentTestCase(TestCase):
    def setUp(self):
        Comment.objects.create(text="This is a test comment.")
        
    def test_comment_creation(self):
        comment = Comment.objects.get(text="This is a test comment.")
        self.assertEqual(comment.text, "This is a test comment.")
        
class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_home_view_status_code(self):
        response = self.client.get('/app/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_view_template(self):
        response = self.client.get('/app/')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_home_view_context(self):
        Comment.objects.create(text="Another test comment.")
        response = self.client.get('/app/')
        self.assertIn('comments', response.context)
        self.assertEqual(len(response.context['comments']), 1)
