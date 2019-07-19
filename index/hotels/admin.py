from django.contrib import admin

from .models import (Hotel, Room, RoomType, RoomReservation)

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(RoomReservation)
