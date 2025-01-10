from django.contrib import admin

from .models import Movie, MovieGenre, Ticket, Room, Row, Seat


# Registrar MovieGenre
@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'rating')
    list_filter = ('release_date', 'rating')
    search_fields = ('title', 'description')
    date_hierarchy = 'release_date'


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'show_time', 'seat')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Row)
class RowAdmin(admin.ModelAdmin):
    list_display = ('name', 'room')


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('name', 'row', 'room')
