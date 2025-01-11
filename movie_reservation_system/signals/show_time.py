from django.db.models.signals import post_save
from django.dispatch import receiver

from movie_reservation_system.models import ShowTime


@receiver(post_save, sender=ShowTime)
def set_end_show_time_on_creation(sender, instance, created, **kwargs):
    """
    Signal to calculate and update the end_show_time for a ShowTime instance after creation.
    """
    if created and not instance.end_show_time and instance.movie.duration:
        instance.set_end_show_time()
