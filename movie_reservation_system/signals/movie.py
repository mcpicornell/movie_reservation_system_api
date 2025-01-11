import random

from django.db.models.signals import post_save
from django.dispatch import receiver

from movie_reservation_system.models import Movie


@receiver(post_save, sender=Movie)
def set_duration_on_creation(sender, instance, created, **kwargs):
    """
    Signal to set duration on creation of a movie.
    """
    if created and not instance.duration:
        instance.duration = random.randint(90, 180)
        instance.save()
