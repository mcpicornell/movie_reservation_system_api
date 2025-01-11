from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from movie_reservation_system.models import Ticket
from movie_reservation_system.permissions.is_staff import IsStaffPermission
from movie_reservation_system.serializers import TicketSerializer
from movie_reservation_system.views.paginators import TicketPagination


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    pagination_class = TicketPagination

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsStaffPermission]
        return super().get_permissions()
