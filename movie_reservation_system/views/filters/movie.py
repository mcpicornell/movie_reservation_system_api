import django_filters

from movie_reservation_system.models import Movie


class MovieFilter(django_filters.FilterSet):
    genre_name = django_filters.CharFilter(
        field_name='movie__genres__name',
        lookup_expr='iexact',
    )
    genre_ids = django_filters.BaseInFilter(
        field_name='genres__id',
        lookup_expr='in',
    )
    movie_name = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
    )

    class Meta:
        model = Movie
        fields = ['genre_name', 'genre_ids', 'movie_name']