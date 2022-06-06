from django.db import models

# Create your models here.


class Feed(models.Model):
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    user_id = models.CharField(max_length=30)
    like = models.IntegerField()
