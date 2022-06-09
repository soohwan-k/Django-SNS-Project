from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from DjangoSNSProject import settings


class Feed(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='content/images/%Y/%m/%d/')
    profile_image = models.TextField()
    user_id = models.CharField(max_length=30)
    like = models.IntegerField()

    def __str__(self):
        return f'[{self.pk}] {self.content}'

    def get_absolute_url(self):
        return f'/main/{self.pk}/'

    # def get_absolute_url2(self):
    #     return f'/main/{self.pk}/'


# class Like(models.Model):
#     feed_id = models.IntegerField(default=0)
#     user_id = models.CharField(max_length=30)
#     is_like = models.BooleanField(default=True)

class Comment(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.user_id}::{self.content}'

    def get_absolute_url(self):
        return f'{self.feed.get_absolute_url()}#comment-{self.pk}'



# class Profile(models.Model):
#     content = models.TextField()
#     image = models.ImageField(upload_to='content/images/%Y/%m/%d/')
#     profile_image = models.TextField()
#     user_id = models.CharField(max_length=30)
#     like = models.IntegerField()
#
#     def __str__(self):
#         return f'[{self.pk}] {self.content}'
#
#     def get_absolute_url(self):
#         return f'/main/profile/'