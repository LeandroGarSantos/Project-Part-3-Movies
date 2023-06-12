from random import random


class MovieApp:
    """
        A movie application that allows users to manage and interact with a collection of movies.
    """
    def __init__(self, storage):
        """
                Initialize the MovieApp object.

                Args:
                    storage (IStorage): The storage object for accessing and manipulating movie data.
        """
        self._storage = storage
        self.movies = []  # Initialize an empty list for movies

    def load_movies(self):
        """
                Load movies from the storage.
        """
        self._storage.load_movies()

    def _command_list_movies(self):
        """
               List all Movies
        """
        movies = self._storage.list_movies()
        if movies:
            for movie in movies:
                title = movie.get('title', 'N/A')
                year = movie.get('year', 'N/A')
                rating = movie.get('rating', 'N/A')
                director = movie.get('director', 'N/A')
                print(f"{title} ({year}) - Director: {director} - Rating: {rating:.1f}")
        else:
            print("No movies found.")

    def _command_add_movie(self):
        """
                        Add a movie to the collection.
        """
        title = input("Enter the title: ")
        year = input("Enter the year: ")
        rating = float(input("Enter the rating: "))
        poster = input("Enter the poster URL: ")
        self._storage.add_movie(title, year, rating, poster)
        print(f"\033[32m Movie {title} added successfully!")

    def _command_delete_movie(self):
        """
                Delete a movie from the collection.
        """

        title = input("Enter the title of the movie to delete: ")
        self._storage.delete_movie(title)
        print(f"\033[32m Movie {title} removed successfully!")

    def _command_update_movie(self):
        """
                Update a movie's notes.
        """
        title = input("Enter the title of the movie to update: ")
        notes = input("Enter the notes: ")
        self._storage.update_movie(title, notes)
        print(f"Movie {title} successfully updated")

    def _command_movie_stats(self):
        # Implement the logic to calculate and display movie statistics
        movies = self._storage.list_movies()
        if movies:
            total_movies = len(movies)
            total_rating = sum(movie['rating'] for movie in movies)
            avg_rating = total_rating / total_movies
            print(f"Total movies: {total_movies}")
            print(f"Average rating: {avg_rating:.1f}")
        else:
            print("No movies found.")

    def _command_random_movie(self):
        """
                Display statistics about the movies collection.
        """

        movies = self._storage.list_movies()
        if movies:
            movie = random.choice(movies)
            print(f"\033[32m{movie['title']} ({movie['year']}) - {movie['director']} - Rating: {movie['rating']:.1f}")
        else:
            print("No movies found.")

    def _command_search_movie(self):
        """
                Search for movies by title or director.
        """
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

    def _command_sort_movies_by_rating(self):
        """
            Sort and display movies in descending order of rating.
        """
        self.load_movies()
        sorted_movies = sorted(self.movies, key=lambda x: x['rating'], reverse=True)
        for movie in sorted_movies:
            print(f"{movie['title']} ({movie['year']}) - {movie['director']} - Rating: {movie['rating']:.1f}")

    def _command_generate_website(self):
        """
            Generate a website showcasing the movies collection.
        """

        movies = self._storage.list_movies()
        if movies:
            movies_html = ""
            for movie in movies:
                # Generate HTML code for each movie
                imdb_link = f"http://www.omdbapi.com/?apikey=7cee3b97&t={movie['title']}"
                movie_html = f"""
                            <div class="movie">
                                <a href="{imdb_link}" target="_blank">
                                    <img class="movie-poster" src="{movie['poster_url']}">
                                </a>
                                <div class="movie-details">
                                    <div class="movie-title">{movie['title']}</div>
                                    <div class="movie-rating">Rating: {movie['rating']}</div>
                                    <div class="movie-year">{movie['year']}</div>
                                    {'<div class="movie-notes">Notes: ' + ', '.join(movie.get('notes', [])) + '</div>' if movie.get('notes') else ''}
                                </div>
                            </div>
                        """
                movies_html += movie_html

            with open("index_template.html", "r") as template_file:
                template_content = template_file.read()

            html_content = template_content.replace("__TEMPLATE_MOVIE_GRID__", movies_html)

            with open("movies.html", "w") as output_file:
                output_file.write(html_content)

            print("Website was successfully generated to the file movies.html.")
        else:
            print("No movies found.")

    def run(self):
        """
            Run the movie application.
        """
        while True:
            print("\033[31m Menu:\033[0m")
            print("\033[33m0. Exit")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("4. Update movie")
            print("5. Stats")
            print("6. Random movie")
            print("7. Search movie")
            print("8. Movies sorted by rating")
            print("9. Generate website")

            choice = input("Enter your choice: ")

            if choice == '0':
                print("Bye!")
                break
            elif choice == '1':
                self._command_list_movies()
            elif choice == '2':
                self._command_add_movie()
            elif choice == '3':
                self._command_delete_movie()
            elif choice == '4':
                self._command_update_movie()
            elif choice == '5':
                self._command_movie_stats()
            elif choice == '6':
                self._command_random_movie()
            elif choice == '7':
                self._command_search_movie()
            elif choice == '8':
                self._command_sort_movies_by_rating()
            elif choice == '9':
                self._command_generate_website()
            else:
                print("\033[31m Invalid choice.\033[0m")


