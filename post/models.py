from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
    name = models.CharField("Title", max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    image = models.ImageField(upload_to="posts/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField("Active", default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", null=True)
    comment = models.TextField("Comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.comment)[:50]

