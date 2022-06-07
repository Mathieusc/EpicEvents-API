from django.contrib import admin
from events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event

    list_display = [
        "status",
        "client",
        "support_contact",
        "attendees",
        "event_dates",
    ]
    list_filter = ["status", "client"]
    search_fields = ["client"]
