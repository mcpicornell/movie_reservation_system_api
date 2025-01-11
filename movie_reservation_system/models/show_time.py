import datetime
import uuid

from django.db import models
from django.utils import timezone

from movie_reservation_system.models import Room, Movie


class ShowTime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_show_time = models.TimeField(null=True, blank=True)
    end_show_time = models.TimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.movie.title} - {self.start_show_time} - {self.end_show_time}"

    def is_active(self):
        return self.end_date <= datetime.datetime.now()

    def set_end_date(self, years):
        naive_date = datetime.datetime.now() + datetime.timedelta(days=365 * years)
        self.end_date = timezone.make_aware(naive_date)
        self.save(update_fields=['end_date'])

    def set_end_show_time(self):
        delta = datetime.timedelta(minutes=self.movie.duration)
        start_time = datetime.datetime.combine(datetime.date.today(), self.start_show_time)
        end_show_time = start_time + delta
        self.end_show_time = end_show_time.time()
        self.save(update_fields=['end_show_time'])
