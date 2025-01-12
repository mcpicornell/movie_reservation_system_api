import django_filters

from movie_reservation_system.models import Movie


class MovieFilter(django_filters.FilterSet):

    class Meta:
        model = Movie
        fields = {
            'genres__name': ['in'],
            'genres__id': ['in'],
            'title': ['icontains']
        }