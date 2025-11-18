from django.urls import path
from iot import views


urlpatterns = [
    path("", views.RoomInfoCreateAPIView.as_view(), name="room_info"),
    path("create/", views.RoomInfoCreateAPIView.as_view(), name="create_room_info"),
    path("<int:room_id>/", views.RoomInfoDetailsAPIView.as_view(), name="room_info_details"),
]