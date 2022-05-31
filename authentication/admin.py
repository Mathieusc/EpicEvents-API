from django import forms
from django.contrib import admin
from authentication.models import User


class UserForm(forms.ModelForm):
    """UserForm inherits from ModelForm for creating User form."""

    class Meta:
        """Meta options."""

        model = User
        fields = ("password", "first_name", "last_name", "email", "role")

    def save(self, commit=True):
        """Overrides method in BaseModelForm."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if self.cleaned_data.get("role") == 1:
            user.is_staff = True
        if commit:
            user.save()
        return user


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "email", "role", "is_staff")
    search_fields = ("first_name", "email")
    list_filter = ("role",)
