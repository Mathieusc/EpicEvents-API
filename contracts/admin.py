from django.contrib import admin
from contracts.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    model = Contract

    list_display = ["sales_contact", "client", "amount", "is_signed"]
    list_filter = ["sales_contact", "client", "amount"]
    search_fields = ["customer"]
