from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# class UserManager(BaseUserManager):
#     def create_user(self, email, password, **kwargs):
#         if not email:
#             raise ValueError("The given email must be set")
#         user = self.model(email=self.normalize_email())
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **kwargs):
#         user = self.create_user(email=email, password=password)
#         user.is_admin = True
#         user.save()
#         return user


class User(AbstractUser):
    MANAGEMENT = 1
    SUPPORT = 2
    SALES = 3

    USER_ROLE = ((MANAGEMENT, "management"), (SUPPORT, "support"), (SALES, "sales"))

    role = models.PositiveIntegerField(
        choices=USER_ROLE, verbose_name="role", blank=True, null=True
    )

    # objects = UserManager()

    def __str__(self):
        return f"User: {self.email} | Role: {self.role}"
