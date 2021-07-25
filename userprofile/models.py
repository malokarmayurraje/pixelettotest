from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class MasterUser(AbstractUser):
    '''All users are here'''
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
