import django_filters

from movie_reservation_system.models import Seat


class SeatFilter(django_filters.FilterSet):
    room_id = django_filters.UUIDFilter(field_name="room__id", lookup_expr='exact')
    show_time_id = django_filters.UUIDFilter(field_name="show_time__id", lookup_expr='exact')
    show_time_day = django_filters.DateFilter(field_name="show_time_day", lookup_expr='exact')

    class Meta:
        model = Seat
        fields = ['room_id', 'show_time_id', 'show_time_day']