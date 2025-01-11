from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from movie_reservation_system.models import Room, Row, Seat
from movie_reservation_system.permissions.is_staff import IsStaffPermission
from movie_reservation_system.serializers import RoomSerializer, RowSerializer, SeatSerializer
from movie_reservation_system.views.filters import SeatFilter
from movie_reservation_system.views.paginators import SeatPagination, RowPagination, RoomPagination


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    pagination_class = RoomPagination

    # filterset_fields = ['user', 'is_active']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsStaffPermission]
        return super().get_permissions()


class RowViewSet(viewsets.ModelViewSet):
    queryset = Row.objects.all()
    serializer_class = RowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    pagination_class = RowPagination

    # filterset_fields = ['user', 'is_active']

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsStaffPermission]
        return super().get_permissions()


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SeatFilter
    pagination_class = SeatPagination

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsStaffPermission]
        return super().get_permissions()

    def get_queryset(self):
        queryset = self.queryset
        room_id = self.request.query_params.get('room_id')
        if room_id:
            queryset = queryset.filter(room_id=room_id)
        return queryset

    def list(self, request, *args, **kwargs):
        show_time_id = request.query_params.get('show_time_id')
        show_time_day = request.query_params.get('show_time_day')
        context = {'show_time_id': show_time_id,
                   'show_time_day': show_time_day} if show_time_day and show_time_id else {}
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context=context)

        return Response(serializer.data)
