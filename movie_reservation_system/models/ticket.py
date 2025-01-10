import uuid

from django.contrib.auth.models import User
from django.db import models

from movie_reservation_system.models import ShowTime
from movie_reservation_system.models.room import Seat


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show_time = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.show_time.movie.title}: R{self.seat.row.name}-S{self.seat.name}"