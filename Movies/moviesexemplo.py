import random
import matplotlib.pyplot as plt
# from fuzzywuzzy import process
import numpy as np


def main():
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    # Menu:
    while True:
        movies_list = list(movies.items())  # update the new movies
        movies_total = len(movies_list)

        print("\033[31m---Menu ---\033[0m")
        print("\033[33m1. List movies")
        print("2. Add movie")
        print("3. Delete movie")
        print("4. Update movie")
        print("5. Stats")
        print("6. Random movie")
        print("7. Search movie")
        print("8. Movies sorted by rating")
        print("9. Create Rating Histogram")
        print("Enter 'q' to Quit")

        choice = input("Enter choice (1-9): ")

        if choice == '1':
            # code for list movies
            print(f"{movies_total} movies in total!")
            for movie in movies_list:
                print(f"\033[32m{movie[0]} - {movie[1]}")
            input("\033[33mPress enter to continue")
            pass
        elif choice == '2':
            # code for Add movie
            movie_new = input("Enter new movie name:")
            rate = float(input("Enter new movie rating (0-10): "))
            movies.update({movie_new: rate})  # added to my list "MOVIEs"
            print(f'\033[32mMovie {movie_new} successfully added')
            input("\033[33mPress enter to continue")
            pass
        elif choice == '3':
            # code for delete movies
            movie_name = input("Enter movie name to delete: ")
            if movie_name in movies:
                del movies[movie_name]
                print(f"\033[32mMovie {movie_name} successfully deleted!")
            else:
                print(f"\033[31mMovie {movie_name} not found!")
            input("\033[33mPress enter to continue")
            pass
        elif choice == '4':
            # code for update movie
            movie_name = input("Enter the name of the movie you want to update:")
            if movie_name in movies:
                new_rating = float(input("Enter new movie rating (0-10):"))
                movies[movie_name] = new_rating
                print(f"\033[32mMovie {movie_name} successfully updated")
            else:
                print(f"\033[32mMovie '{movie_name}' doesn't exist!")
            input("\033[33mPress enter to continue")
            pass
        elif choice == '5':
            # code for calculate the average
            avg_rating = sum(movies.values()) / len(movies)
            # The Highest movie
            highest_rated_movie = max(movies, key=movies.get)
            # The worst movie
            lowest_rated_movie = min(movies, key=movies.get)

            print(f"\033[32mMedian rating: {avg_rating}")
            print(f"\033[32mBest movie: {highest_rated_movie} - {movies[highest_rated_movie]}")
            print(f"\033[32mThe Worst movie: {lowest_rated_movie} - {movies[lowest_rated_movie]}")
            input("\033[33mPress enter to continue")
            pass
        elif choice == '6':
            # code for Random movie
            random_movie = random.choice(movies_list)
            print(f"\033[32mYour movie for tonight: {random_movie} - it's rated ")
            input("\033[33mPress enter to continue")
            pass
        elif choice == '7':
            # code for search movie
            search_term = input("Enter part of movie name: ")
            while len(search_term) == 0:
                search_term = input("Please type one letter to search the movie in our list:")
            results = []
            for movie, rating in movies.items():
                if search_term.lower() in movie.lower():
                    results.append((movie, rating))
            if len(results) > 0:
                print(f"\033[32mWe found {len(results)} with the term '{search_term}'")
                for movie, rating in results:
                    print(f"{movie} - {rating}")
            else:
                print(f"\033[32mWe didn't find any movie with the term '{search_term}'")
            input("\033[33mPress enter to continue")
            pass
        elif choice == '8':
            # code for Movies sorted by rating
            my_sorted_list = sorted(movies_list, key=lambda x: x[1], reverse=True)
            for movie in my_sorted_list:
                print(f"\033[32m{movie[0]} - {movie[1]}")
            input("\033[33mPress enter to continue")
            pass
        elif choice == '9':
            #  create a histogram of the ratings of the movies.
            ratings = [rating for movie, rating in movies.items()]
            plt.hist(ratings, bins=10)
            plt.title("Movie Ratings Histogram")
            plt.xlabel("Rating")
            plt.ylabel("Frequency")

            # prompt the user for a file name to save the plot
            filename = input("\033[32mEnter file name to save histogram plot: ")
            plt.savefig(filename)

            plt.show()
            input("\033[33mPress enter to continue")
            pass
        elif choice == 'q':
            break
        else:
            print("\033[31mInvalid choice, please try (1-8):\033[0m")
            input("\033[43mPress enter to continue\033[0m")


if __name__ == "__main__":
    main()
