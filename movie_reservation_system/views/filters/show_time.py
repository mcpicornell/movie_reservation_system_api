import django_filters

from movie_reservation_system.models import ShowTime


class ShowTimeFilter(django_filters.FilterSet):


    class Meta:
        model = ShowTime
        fields = {
            'movie__genres__name': ['exact'],
            'movie__genres__id': ['in'],
            'movie__title': ['icontains'],
            'end_date': ['exact', 'lt'],
        }
