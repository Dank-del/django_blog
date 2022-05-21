import typing
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to="post_pics")

    # image = models.ImageField()

    def __str__(self) -> typing.Text:
        return self.title

    def get_absolute_url(self) -> typing.Text:
        return reverse("post-detail", kwargs={"pk": self.pk})
