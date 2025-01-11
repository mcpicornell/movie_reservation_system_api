import django_filters

from movie_reservation_system.models import ShowTime


class ShowTimeFilter(django_filters.FilterSet):
    genre_name = django_filters.CharFilter(field_name='show_time__movie__genre__name', lookup_expr='iexact')
    movie_name = django_filters.CharFilter(field_name='show_time__movie__name', lookup_expr='icontains')

    class Meta:
        model = ShowTime
        fields = ['genre_name', 'movie_name']