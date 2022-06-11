from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from DjangoSNSProject import settings


class Feed(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='content/images/%Y/%m/%d/')
    profile_image = models.TextField()
    user_id = models.CharField(max_length=30)

    like = models.IntegerField(default=0)
    favorite = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_feed', blank=True)

    def __str__(self):
        return f'[{self.pk}] {self.content}'

    def get_absolute_url(self):
        return f'/main/{self.pk}/'


class Comment(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.user_id}::{self.content}'

    def get_absolute_url(self):
        return f'{self.feed.get_absolute_url()}#comment-{self.pk}'



