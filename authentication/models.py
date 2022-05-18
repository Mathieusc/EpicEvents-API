from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    USER_ROLE = ((1, "managment"), (2, "support"), (3, "sales"))

    role = models.PositiveIntegerField(choices=USER_ROLE, verbose_name="team")

    def __str__(self):
        return f"User: {self.username} | Role: {self.role}"
