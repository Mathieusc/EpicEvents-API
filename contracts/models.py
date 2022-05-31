from django.db import models
from authentication.models import User
from clients.models import Client


class Contract(models.Model):
    sales_contact = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        limit_choices_to={"role": 3},
        related_name="sales_contract",
    )
    client = models.ForeignKey(
        to=Client, on_delete=models.RESTRICT, related_name="client_contract"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    amount = models.FloatField(blank=True)
    payment_due = models.DateTimeField(blank=True, null=True)
    # Replace by is_signed ?
    is_finished = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Client: {self.client.email}"
