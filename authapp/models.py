from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
