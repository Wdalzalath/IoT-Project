from django.contrib import admin
from iot.models import RoomInfo

# Register your models here.
admin.register(RoomInfo)


class RoomInfoAdmin(admin.ModelAdmin):
    list_display = ["room_no", "room_status", "created_at", "updated_at"]
    list_filter = ["room_no", "room_status"]
    fieldsets = (
        (
            "Room Info",
            {
                "fields": (
                    "room_no",
                    "room_status",
                )
            },
        ),
    )
