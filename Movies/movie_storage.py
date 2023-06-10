import json
import requests


API_KEY = '7cee3b97'
MOVIE_FILE = 'data.json'


def load_movies():
    """
        Load movies from a JSON file and return them as a list.

        Returns:
            List: A list of dictionaries, where each dictionary represents a movie.
                  Each dictionary has the following keys: 'title', 'year', 'director',
                  'rating', and 'poster_url'.
        """
    try:
        with open(MOVIE_FILE, 'r') as f:
            movies = json.load(f)
    except FileNotFoundError:
        movies = []
    return movies


def save_movies(movies):
    with open(MOVIE_FILE, 'w') as f:
        json.dump(movies, f)


# Function for list movies
def list_movies():
    movies = load_movies()
    movies_total = len(movies)
    print(f"\033[32m {movies_total} Movies in Total")
    for movie in movies:
        print(f"\033[32m {movie['title']} ({movie['year']}) - {movie['director']} - Rating: {movie['rating']:.1f}")


# Function Add movie
def add_movie():
    title = input("Title: ")
    api_url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"

# THIS try-except blocks. handles errors THROUGH CONNECTIONS AND SEARCHES"
    try:
        response = requests.get(api_url)
        response.raise_for_status() # raise an exception if response status is not 200
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
            movies = load_movies()
            movies.append(movie)
            save_movies(movies)
            print(f"\033[32m Movie {title} added successfully!")
    except requests.exceptions.HTTPError as e:
        print(f"\033[31m Failed to fetch movie data for {title}. Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"\033[31m Failed to connect to the API. Error: {e}")


# Function delete movies
def delete_movie():
    title = input("Title: ")
    movies = load_movies()
    new_movies = [movie for movie in movies if movie['title'] != title]
    if len(new_movies) < len(movies):
        save_movies(new_movies)
        print(f"\033[32m Movie {title} removed successfully!")
    else:
        print(f"\033[31m <Movie ({title}) not found.>")


# Function update movie
def update_movie():
    title = input("Title: ")
    movies = load_movies()
    for movie in movies:
        if movie['title'] == title:
            note = input("Enter movie notes:")
            if 'notes' in movie:
                movie['notes'].append(note)
            else:
                movie['notes'] = [note]
            save_movies(movies)
            print(f"Movie {title} successfully updated")
            break
    else:
        print("Movie not found.")


# Function for calculate the average
def stats():
    movies = load_movies()
    total_movies = len(movies)
    total_rating = sum(movie['rating'] for movie in movies)
    avg_rating = total_rating / total_movies if total_movies > 0 else 0
    print(f"Total movies: {total_movies}")
    print(f"Average rating: {avg_rating:.1f}")


# Function for Random movie
def random_movie():
    import random
    movies = load_movies()
    if movies:
        movie = random.choice(movies)
        print(f"\033[32m{movie['title']} ({movie['year']}) - {movie['director']} - Rating: {movie['rating']:.1f}")
    else:
        print("No movies.")


# Function for search movie
def search_movie():
    query = input("Search query: ")
    movies = load_movies()
    found_movies = []
    for movie in movies:
        if query.lower() in movie['title'].lower() or query.lower() in movie['director'].lower():
            found_movies.append(movie)
    if found_movies:
        for movie in found_movies:
            print(f"{movie['title']} ({movie['year']}) - {movie['director']} - Rating: {movie['rating']:.1f}")
    else:
        print("No movies found.")


# Function for Movies sorted by rating
def sort_movies_by_rating():
    movies = load_movies()
    sorted_movies = sorted(movies, key=lambda x: x['rating'], reverse=True)
    for movie in sorted_movies:
        print(f"{movie['title']} ({movie['year']}) - {movie['director']} - Rating: {movie['rating']:.1f}")


# Function to create the website
def create_website():
    # Load the movies from the data.json file
    with open(MOVIE_FILE, 'r') as f:
        movies = json.load(f)

    # Generate HTML code for each movie
    movies_html = ''
    for movie in movies:
        # Bonus  this next line link with the page IMDB
        imdb_link = f'http://www.omdbapi.com/?apikey=7cee3b97&t={movie["title"]}'
        movies_html += f'<div class="movie"><a href="{imdb_link}" target="_blank"><img class="movie-poster" src="{movie["poster_url"]}"></a>'
        movies_html += f'<div class="movie-details"><div class="movie-title">{movie["title"]}</div>'
        # Add rating after the movie title
        movies_html += f'<div class="movie-rating">Rating: {movie["rating"]}</div>'
        movies_html += f'<div class="movie-year">{movie["year"]}</div>'
        # Bonus add Notes at HTML if there are some
        if movie.get("notes"):
            movies_html += f'<div class="movie-notes">Notes  about  the movie: {movie.get("notes")}</div>'
        movies_html += '</div></div>'

    # Load the template HTML file
    with open('index_template.html', 'r') as template_file:
        template_content = template_file.read()

    # Replace the placeholder with movies' info
    html_content = template_content.replace('__TEMPLATE_MOVIE_GRID__', movies_html)

    # Write the new HTML content to a new file
    with open('movies.html', 'w') as output_file:
        output_file.write(html_content)

    print("Website was successfully generated to the file movies.html.")
