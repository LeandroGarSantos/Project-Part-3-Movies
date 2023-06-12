from storage_json import StorageJson
from storage_csv import StorageCsv

from movie_app import MovieApp


def main():
    storage = StorageJson('movies.json')
    movie_app = MovieApp(storage)
    movie_app.run()


"""
        To run the csv storage class, you have to discount the line below and 
        comment the line referring to JSON
"""

    # storage = StorageCsv('movies.csv')
    # movie_app = MovieApp(storage)
    # movie_app.run()


if __name__ == '__main__':
    main()
