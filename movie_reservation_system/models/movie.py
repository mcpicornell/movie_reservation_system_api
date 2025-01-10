import uuid
import random
from django.db import models


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster_url = models.URLField(max_length=255)
    rating = models.FloatField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    genres = models.ManyToManyField('MovieGenre', related_name='movies')
    tmdb_id = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.duration:
            self.duration = random.randint(90, 180)

        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class MovieGenre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tmdb_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
