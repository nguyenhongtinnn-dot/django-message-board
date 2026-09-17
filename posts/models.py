from django.db import models


class Post(models.Model):
    text = models.TextField(default="hello")

    def __str__(self):
        return self.text[:50]
