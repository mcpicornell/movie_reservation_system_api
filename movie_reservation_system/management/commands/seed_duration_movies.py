import random

from django.core.management.base import BaseCommand

from movie_reservation_system.models import Movie


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            for movie in Movie.objects.all():
                duration_minutes = random.randint(90, 180)
                movie.duration = duration_minutes
                movie.save()
                self.stdout.write(f"Updated '{movie.title}' with a random duration of {duration_minutes} minutes.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
