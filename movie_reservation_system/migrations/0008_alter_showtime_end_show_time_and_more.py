# Generated by Django 5.1.4 on 2025-01-11 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reservation_system', '0007_remove_showtime_is_active_showtime_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='end_show_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='start_show_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]