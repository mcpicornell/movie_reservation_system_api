from rest_framework import serializers
from movie_reservation_system.models import Movie, MovieGenre


class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        exclude = ['tmdb_id']

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        exclude = ['tmdb_id', 'created_at']

    @staticmethod
    def get_genres(obj):
        return list(MovieGenre.objects.filter(movies__id=obj.id).values_list('name', flat=True))
