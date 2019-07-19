from django.db import models
from django.core.validators import (MinValueValidator, MaxValueValidator)

from users.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(
        default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return f'{self.name} ${str(self.price)}'


class Room(models.Model):
    room_number = models.CharField(max_length=3)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{RoomType.objects.filter(id=self.room_type.id)[0].name} Room NO. "{self.room_number}" in Hotel "{Hotel.objects.filter(id=self.hotel.id)[0].name}"'


class RoomReservation(models.Model):
    created = models.DateTimeField(
        verbose_name="Reservation Timestamp", auto_now=True)
    starting_date = models.DateField()
    expire_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
            return f'Reserved for {User.objects.filter(id=self.user.id)[0]}, Expires: {self.expire_date}'
