from ntpath import realpath
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
    company_name = models.CharField(max_length=64, null=False)
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, unique=True, null=False)
    mobile = models.CharField(max_length=20, unique=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Client: {self.email} | Company: {self.company_name}"


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
    status = models.BooleanField(default=False)
    amount = models.FloatField(blank=True)
    payment_due = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Client: {self.client.email}"


class Event(models.Model):
    CHOICES_STATUS = ((1, "Not attributed"), (2, "In progress"), (3, "Ended"))
    status = models.PositiveSmallIntegerField(choices=CHOICES_STATUS, default=1)
    contract = models.OneToOneField(
        to=Contract, on_delete=models.RESTRICT, related_name="contract_event"
    )
    support_contact = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        limit_choices_to={"role": 2},
        related_name="support",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    attendees = models.IntegerField(blank=True, null=True)
    event_dates = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return f"Contract: {self.contract} | Status: {self.status} | Support Staff: {self.support_contact}"
