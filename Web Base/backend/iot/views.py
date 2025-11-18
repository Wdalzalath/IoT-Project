from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from iot.models import RoomInfo
from iot import serializers


class RoomInfoCreateAPIView(generics.GenericAPIView):
    serializer_class = serializers.RoomInfoCreateSerializer
    queryset = RoomInfo.objects.all()

    def get(self, request, *args, **kwargs):
        room_info = RoomInfo.objects.all().order_by("id")
        serializer = self.serializer_class(room_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoomInfoDetailsAPIView(generics.GenericAPIView):
    serializer_class = serializers.RoomInfoViewSerializer

    def get(self, request, room_id, *args, **kwargs):
        room_info = get_object_or_404(RoomInfo, pk=room_id)
        serializer = self.serializer_class(room_info)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, room_id, *args, **kwargs):
        room_info = get_object_or_404(RoomInfo, pk=room_id)
        serializer = self.serializer_class(room_info, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, room_id, *args, **kwargs):
        room_info = get_object_or_404(RoomInfo, pk=room_id)
        room_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)