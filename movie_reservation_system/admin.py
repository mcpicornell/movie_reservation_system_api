from django.contrib import admin
from .models import Movie, MovieGenre

# Registrar MovieGenre
@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registrar Movie
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'rating')
    list_filter = ('release_date', 'rating')
    search_fields = ('title', 'description')
    date_hierarchy = 'release_date'