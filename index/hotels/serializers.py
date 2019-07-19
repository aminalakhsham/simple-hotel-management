from rest_framework.serializers import ModelSerializer

from .models import (Hotel, Room, RoomType)


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class RoomTypeSerializer(ModelSerializer):
    class Meta:
        model = RoomType
        fields = "__all__"


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"