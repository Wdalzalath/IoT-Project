from django.db import models


# Create your models here.
class RoomInfo(models.Model):
    room_no     = models.CharField(max_length=25, blank=False, null=False)
    room_status = models.IntegerField(blank=False, null=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_no
