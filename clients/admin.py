from django.contrib import admin
from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client

    list_display = [
        "id",
        "sales_contact",
        "company_name",
        "first_name",
        "last_name",
        "email",
        "mobile",
    ]
    list_filter = ["sales_contact", "company_name"]
    search_fields = ["first_name", "last_name"]
