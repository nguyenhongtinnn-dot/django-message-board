from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="Đây là bài post kiểm thử")

    def test_model_content(self):
        self.assertEqual(self.post.text, "Đây là bài post kiểm thử")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Đây là bài post kiểm thử")