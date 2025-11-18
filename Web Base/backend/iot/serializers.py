from rest_framework import serializers
from iot.models import RoomInfo


class RoomInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomInfo
        fields = ["id", "room_no", "room_status"]

    def validate(self, attrs):
        if RoomInfo.objects.filter(room_no=attrs["room_no"]).exists():
            raise serializers.ValidationError("Room number already exists")
        return attrs


class RoomInfoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomInfo
        fields = ["id", "room_no", "room_status", "created_at", "updated_at"]

    def validate(self, attrs):
        room_no = attrs.get("room_no")
        instance = self.instance

        # If updating and room_no stays SAME — allow it
        if instance and instance.room_no == room_no:
            return attrs

        # If another room has same number — block it
        if RoomInfo.objects.filter(room_no=room_no).exclude(id=instance.id).exists():
            raise serializers.ValidationError("Room number already exists")

        return attrs