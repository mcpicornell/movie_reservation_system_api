from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from movie_reservation_system.views import RoomViewSet, RowViewSet, MovieViewSet, TicketViewSet, ShowTimeViewSet, \
    SeatViewSet

router = DefaultRouter()

router.register(r'tickets', TicketViewSet, basename='tickets')
router.register(r'rooms', RoomViewSet, basename='rooms')
router.register(r'show-times', ShowTimeViewSet, basename='show-times')
router.register(r'movies', MovieViewSet, basename='movies')
router.register(r'seats', SeatViewSet, basename='seats')

urlpatterns = router.urls + [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
