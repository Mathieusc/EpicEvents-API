from django.db import models
from authentication.models import User


class Client(models.Model):
    sales_contact = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        limit_choices_to={"role": 3},
        related_name="sales",
    )
    company_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Client: {self.email} | Company: {self.company_name}"
