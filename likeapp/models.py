from django.db import models

# Create your models here.
from DjangoSNSProject import settings
from content.models import Feed


class LikeRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='like_record')
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='like_record')

    class Meta:
        unique_together = ('user', 'feed')


