from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.


class User(AbstractBaseUser):
    profile_image = models.TextField()
    nickname = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = "User"
