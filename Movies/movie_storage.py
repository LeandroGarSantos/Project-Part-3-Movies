import json
import requests
import random


class MovieManager:
    def __init__(self):
        self.API_KEY = '7cee3b97'
        self.MOVIE_FILE = 'data.json'
        self.movies = []

    def load_movies(self):
        try:
            with open(self.MOVIE_FILE, 'r') as f:
                self.movies = json.load(f)
        except FileNotFoundError:
            self.movies = []

    def save_movies(self):
        with open(self.MOVIE_FILE, 'w') as f:
            json.dump(self.movies, f)

    def list_movies(self):
        self.load_movies()
        movies_total = len(self.movies)
        print(f"\033[32m {movies_total} Movies in Total")
        for movie in self.movies:
            print(f"\033[32m {movie['title']} ({movie['year']}) - {movie['director']} - Rating: {movie['rating']:.1f}")

    def add_movie(self):
        title = input("Title: ")
        api_url = f"http://www.omdbapi.com/?apikey={self.API_KEY}&t={title}"

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            if data['Response'] == 'False':
                print(f"\033Movie {title} not found on the API")
            else:
                rating = data['imdbRating']
                if rating == 'N/A':
                    rating = 0.0
                else:
                    rating = float(rating)
                movie = {
                    'title': data['Title'],
                    'year': data['Year'],
                    'director': data['Director'],
                    'rating': rating,
                    'poster_url': data['Poster']
                }
                self.load_movies()
                self.movies.append(movie)
                self.save_movies()
                print(f"\033[32m Movie {title} added successfully!")
        except requests.exceptions.HTTPError as e:
            print(f"\033[31m Failed to fetch movie data for {title}. Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"\033[31m Failed to connect to the API. Error: {e}")

    def delete_movie(self):
        title = input("Title: ")
        self.load_movies()
        new_movies = [movie for movie in self.movies if movie['title'] != title]
        if len(new_movies) < len(self.movies):
            self.movies = new_movies
            self.save_movies()
            print(f"\033[32m Movie {title} removed successfully!")
        else:
            print(f"\033[31m <Movie ({title}) not found.>")

    def update_movie(self):
        title = input("Title: ")
        self.load_movies()
        for movie in self.movies:
            if movie['title'] == title:
                note = input("Enter movie notes:")
                if 'notes' in movie:
                    movie['notes'].append(note)
                else:
                    movie['notes'] = [note]
                self.save_movies()
                print(f"Movie {title} successfully updated")
                break
        else:
            print("Movie not found.")

    def stats(self):
        self.load_movies()
        total_movies = len(self.movies)
        total_rating = sum(movie['rating'] for movie in self.movies)
        avg_rating = total_rating / total_movies if total_movies > 0 else 0
        print(f"Total movies: {total_movies}")
        print(f"Average rating: {avg_rating:.1f}")

    def random_movie(self):
        self.load_movies()
        if self.movies:
            movie = random.choice(self.movies)
            print(f"\033[32m{movie['title']} ({movie['year']}) - {movie['director']} - Rating: {movie['rating']:.1f}")
        else:
            print("No movies.")

    def search_movie(self):
        query = input("Search query: ")
        self.load_movies()
        found_movies = []

        for movie in self.movies:
            if query.lower() in movie['title'].lower() or query.lower() in movie['director'].lower():
                found_movies.append(movie)
        if found_movies:
            for movie in found_movies:
                print(f"{movie['title']} ({movie['year']}) - {movie['director']} - Rating: {movie['rating']:.1f}")
        else:
            print("No movies found.")

    def sort_movies_by_rating(self):
        self.load_movies()
        sorted_movies = sorted(self.movies, key=lambda x: x['rating'], reverse=True)
        for movie in sorted_movies:
            print(f"{movie['title']} ({movie['year']}) - {movie['director']} - Rating: {movie['rating']:.1f}")

    def create_website(self):
        with open(self.MOVIE_FILE, 'r') as f:
            self.movies = json.load(f)

            movies_html = ''
            for movie in self.movies:
                imdb_link = f'http://www.omdbapi.com/?apikey=7cee3b97&t={movie["title"]}'
                movies_html += f'<div class="movie"><a href="{imdb_link}" target="_blank"><img class="movie-poster" src="{movie["poster_url"]}"></a>'
                movies_html += f'<div class="movie-details"><div class="movie-title">{movie["title"]}</div>'
                movies_html += f'<div class="movie-rating">Rating: {movie["rating"]}</div>'
                movies_html += f'<div class="movie-year">{movie["year"]}</div>'
                if movie.get("notes"):
                    movies_html += f'<div class="movie-notes">Notes about the movie: {", ".join(movie.get("notes"))}</div>'
                movies_html += '</div></div>'

            with open('index_template.html', 'r') as template_file:
                template_content = template_file.read()

            html_content = template_content.replace('__TEMPLATE_MOVIE_GRID__', movies_html)

            with open('movies.html', 'w') as output_file:
                output_file.write(html_content)

            print("Website was successfully generated to the file movies.html.")
