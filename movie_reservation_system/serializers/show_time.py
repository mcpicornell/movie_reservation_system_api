from rest_framework import serializers
from movie_reservation_system.models import ShowTime
from movie_reservation_system.serializers.movie import MovieSerializer


class ShowTimeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = ShowTime
        exclude = ['created_at']