from rest_framework.routers import DefaultRouter

from .views import (HotelView, RoomView, RoomTypeView, RoomReservationView)

router = DefaultRouter()
router.register('hotels', HotelView)
router.register('rooms', RoomView)
router.register('room-types', RoomTypeView)
router.register('room-reservations', RoomReservationView)

urlpatterns = router.urls
