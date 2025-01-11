import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from movie_reservation_system.models import ShowTime

@receiver(post_save, sender=ShowTime)
def set_end_show_time_on_creation(sender, instance, created, **kwargs):
    """
    Signal to calculate and update the end_show_time for a ShowTime instance after creation.
    """
    if created and not instance.end_show_time and instance.movie.duration:
        delta = datetime.timedelta(minutes=instance.movie.duration)
        start_time = datetime.datetime.combine(datetime.date.today(), instance.start_show_time)
        end_show_time = start_time + delta
        instance.end_show_time = end_show_time.time()
        instance.save()