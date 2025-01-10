import random

from django.core.management.base import BaseCommand

from movie_reservation_system.models import Movie, Room, Row
from movie_reservation_system.models.room import Seat


class Command(BaseCommand):

        def handle(self, *args, **kwargs):
            try:
                room_limit = 10

                while room_limit > 0:
                    room_name = f"{room_limit}"
                    room, created = Room.objects.get_or_create(name=room_name)

                    row_limit = 10
                    row_counter = 1
                    while row_counter <= row_limit:
                        row_name = f"{row_counter}"
                        row, created = Row.objects.get_or_create(name=row_name, room=room)

                        seat_limit = 15
                        for seat_number in range(1, seat_limit + 1):
                            seat_name = f"{seat_number}"
                            Seat.objects.get_or_create(name=seat_name, room=room, row=row)

                        row_counter += 1

                    room_limit -= 1

                self.stdout.write(
                    self.style.SUCCESS('Successfully populated the database with rooms, rows, and seats.'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))