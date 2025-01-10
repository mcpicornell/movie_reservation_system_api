import os

import requests
from django.core.management.base import BaseCommand

from movie_reservation_system.models import Movie
from movie_reservation_system.models.movie import MovieGenre


class Command(BaseCommand):
    help = 'Populate the database with movies from TMDb'
    API_KEY = os.environ.get('TMDB_API_KEY')
    API_TOKEN = os.environ.get('TMDB_API_TOKEN')
    BASE_URL = 'https://api.themoviedb.org/3'

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write('Connecting to TMDb...')

            page = 1
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {self.API_TOKEN}"
            }
            while page < 10:
                url = f'{self.BASE_URL}/movie/top_rated?api_key={self.API_KEY}&language=en-US&page={page}'
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    movies = data['results']

                    for movie in movies:
                        title = movie['title']
                        description = movie['overview']
                        release_date = movie.get('release_date', None)
                        rating = movie['vote_average']
                        poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"

                        if not all([title, description, release_date, rating, poster_url]):
                            continue

                        movie_instance, movie_created = Movie.objects.update_or_create(
                            title=title,
                            defaults={
                                'description': description,
                                'release_date': release_date,
                                'rating': rating,
                                'poster_url': poster_url,
                                'tmdb_id': movie['id'],
                            },
                        )

                        genres_to_add = []
                        for genre_id in movie['genre_ids']:
                            genre, genre_created = MovieGenre.objects.get_or_create(tmdb_id=genre_id)
                            genres_to_add.append(genre)
                        movie_instance.genres.add(*genres_to_add)
                        movie_instance.save()

                        if movie_created:
                            self.stdout.write(f'Added: {title}')
                        else:
                            self.stdout.write(f'Updated: {title}')
                else:
                    self.stderr.write(f'Error connecting to TMDb: {response.status_code}')
                page += 1

            self.stdout.write('Database populated successfully!')
        except Exception as e:
            print(str(e))
