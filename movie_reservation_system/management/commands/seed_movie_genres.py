import os

import requests
from django.core.management.base import BaseCommand

from movie_reservation_system.models.movie import MovieGenre


class Command(BaseCommand):
    help = 'Populate the database with movies from TMDb'
    API_KEY = os.environ.get('TMDB_API_KEY')
    API_TOKEN = os.environ.get('TMDB_API_TOKEN')
    BASE_URL = 'https://api.themoviedb.org/3'

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write('Connecting to TMDb...')

            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {self.API_TOKEN}"
            }
            url = f'{self.BASE_URL}/genre/movie/list?api_key={self.API_KEY}'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                movie_genres = data['genres']

                for movie_genre in movie_genres:
                    name = movie_genre['name']
                    id = movie_genre['id']

                    if not all([id, name]):
                        continue

                    movie_genre_instance, movie_genre_created = MovieGenre.objects.update_or_create(
                        tmdb_id=id,
                        defaults={
                            'name': name,
                        },
                    )

                    if movie_genre_created:
                        self.stdout.write(f'Added: {name}')
                    else:
                        self.stdout.write(f'Updated: {name}')
                else:
                    self.stderr.write(f'Error connecting to TMDb: {response.status_code}')

            self.stdout.write('Database populated successfully!')
        except Exception as e:
            print(str(e))
