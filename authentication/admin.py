from django import forms
from django.contrib import admin
from authentication.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email", "role", "is_staff")
    search_fields = ("first_name", "email")
    list_filter = ("role",)
