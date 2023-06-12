import json
from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = []

    def load_movies(self):
        try:
            with open(self.file_path, 'r') as f:
                self.movies = json.load(f)
        except FileNotFoundError:
            self.movies = []

    def save_movies(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.movies, f, indent=2)

    def list_movies(self):
        self.load_movies()
        if self.movies:
            for movie in self.movies:
                title = movie.get('title', 'N/A')
                year = movie.get('year', 'N/A')
                rating = movie.get('rating', 'N/A')
                director = movie.get('director', 'N/A')
                print(f"{title} ({year}) - Director: {director} - Rating: {rating:.1f}")
        else:
            print("No movies found.")

    def add_movie(self, title, year, rating, poster):
        movie = {
            'title': title,
            'year': year,
            'rating': rating,
            'poster_url': poster
        }
        self.load_movies()
        self.movies.append(movie)
        self.save_movies()
        print(f"Movie {title} added successfully!")

    def delete_movie(self, title):
        self.load_movies()
        updated_movies = []
        deleted = False

        for movie in self.movies:
            if movie.get('title', '').lower() == title.lower():
                deleted = True
            else:
                updated_movies.append(movie)

        if deleted:
            self.movies = updated_movies
            self.save_movies()
            print(f"Movie {title} deleted successfully!")
        else:
            print(f"Movie {title} not found.")

    def update_movie(self, title, notes):
        self.load_movies()
        for movie in self.movies:
            if movie['title'] == title:
                movie['notes'] = notes
                break
        self.save_movies()
        print(f"Movie {title} successfully updated!")
