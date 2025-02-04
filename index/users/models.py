from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', 'password', 'first_name', 'last_name')

    def __str__(self):
        return self.first_name + " " + self.last_name
