# Generated by Django 5.1.4 on 2025-01-11 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reservation_system', '0004_room_movie_duration_row_seat_showtime_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtime',
            name='end_time',
        ),
    ]
