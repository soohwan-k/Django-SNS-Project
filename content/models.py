from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Feed(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='content/images/%Y/%m/%d/')
    profile_image = models.TextField()
    user_id = models.CharField(max_length=30)
    like = models.IntegerField()

    def __str__(self):
        return f'[{self.pk}] {self.content}'

    def get_absolute_url(self):
        return f'/main/'

