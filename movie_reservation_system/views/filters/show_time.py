import django_filters

from movie_reservation_system.models import ShowTime
from movie_reservation_system.views.filters.movie import MovieFilter


class ShowTimeFilter(django_filters.FilterSet):
    genre_name = django_filters.CharFilter(
        field_name='movie__genres__name',
        lookup_expr='iexact',
    )
    genre_ids = django_filters.BaseInFilter(
        field_name='movie__genres__id',
        lookup_expr='in',
    )
    movie_name = django_filters.CharFilter(field_name='movie__title', lookup_expr='icontains')

    movie = MovieFilter()

    class Meta:
        model = ShowTime
        fields = ['genre_name', 'movie_name', 'genre_ids']
