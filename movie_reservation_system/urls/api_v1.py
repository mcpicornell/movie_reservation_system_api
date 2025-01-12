from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie_reservation_system.views import RoomViewSet, RowViewSet, MovieViewSet, TicketViewSet, ShowTimeViewSet, \
    SeatViewSet, MovieGenreViewSet

router = DefaultRouter()

router.register(r'tickets', TicketViewSet, basename='tickets')
router.register(r'rooms', RoomViewSet, basename='rooms')
router.register(r'show-times', ShowTimeViewSet, basename='show-times')
router.register(r'movies', MovieViewSet, basename='movies')
router.register(r'movie-genres', MovieGenreViewSet, basename='movie-genres')
router.register(r'rows', RowViewSet, basename='rows')
router.register(r'seats', SeatViewSet, basename='seats')

urlpatterns = router.urls + [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
