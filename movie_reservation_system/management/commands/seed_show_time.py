import datetime
import random

from django.core.management.base import BaseCommand

from movie_reservation_system.models import Room, Movie, ShowTime

SHOW_START_TIME = ((12, 00), (15, 30), (18, 00), (21, 30), (00, 30))


def get_time(hour, minute):
    return datetime.time(hour, minute)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            movies_list_included = []
            movies_all = Movie.objects.all()
            rooms = Room.objects.all()
            show_start_times = [get_time(hour, minute) for hour, minute in SHOW_START_TIME]
            for room in rooms:
                for start_show_time in show_start_times:
                    random_movie = random.choice(movies_all)

                    while random_movie in movies_list_included:
                        random_movie = random.choice(movies_all)
                    show_time = ShowTime(room=room, start_show_time=start_show_time, movie=random_movie)
                    show_time.save()
                    show_time.set_end_date(years=5)

            self.stdout.write(
                self.style.SUCCESS('Successfully populated the database with ShowTime'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))
