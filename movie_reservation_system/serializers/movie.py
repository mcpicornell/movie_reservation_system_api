from rest_framework import serializers
from movie_reservation_system.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['tmdb_id', 'created_at']