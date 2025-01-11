from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from movie_reservation_system.models import Movie, MovieGenre
from movie_reservation_system.permissions.is_staff import IsStaffPermission
from movie_reservation_system.serializers import MovieSerializer, MovieGenreSerializer
from movie_reservation_system.views.filters.movie import MovieFilter
from movie_reservation_system.views.paginators import MoviePagination
from movie_reservation_system.views.paginators.movie import MovieGenrePagination


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter
    pagination_class = MoviePagination

    # filterset_fields = ['user', 'is_active']


    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsStaffPermission]
        return super().get_permissions()

class MovieGenreViewSet(viewsets.ModelViewSet):
    queryset = MovieGenre.objects.all()
    serializer_class = MovieGenreSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    pagination_class = MovieGenrePagination

    # filterset_fields = ['user', 'is_active']


    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsStaffPermission]
        return super().get_permissions()