from rest_framework.viewsets import ModelViewSet

from .serializers import (HotelSerializer, RoomSerializer,
                          RoomTypeSerializer, RoomReservationSerializer)
from .models import (Hotel, Room, RoomType, RoomReservation)


class HotelView(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomTypeView(ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomReservationView(ModelViewSet):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer
