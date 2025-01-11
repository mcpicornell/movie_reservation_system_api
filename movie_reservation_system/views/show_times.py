from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from movie_reservation_system.models import ShowTime
from movie_reservation_system.permissions.is_staff import IsStaffPermission
from movie_reservation_system.serializers import ShowTimeSerializer
from movie_reservation_system.views.filters import ShowTimeFilter
from movie_reservation_system.views.paginators import ShowTimePagination


class ShowTimeViewSet(viewsets.ModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = ShowTimeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShowTimeFilter
    pagination_class = ShowTimePagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsStaffPermission]
        return super().get_permissions()
