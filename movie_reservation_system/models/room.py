import uuid

from django.db import models

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Seat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    room = models.ForeignKey('Room', related_name='seats', on_delete=models.CASCADE)
    row = models.ForeignKey('Row', related_name='seats', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('name', 'room', 'row'),)

    def __str__(self):
        return self.name

    def is_available(self, show_time_id, show_time_day):
        from movie_reservation_system.models import Ticket
        return not Ticket.objects.filter(
            seat_id=self.id,
            show_time_id=show_time_id,
            show_time_day=show_time_day
        ).exists()

class Row(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    room = models.ForeignKey('Room', related_name='rows', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name