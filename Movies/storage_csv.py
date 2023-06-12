import csv
import os
from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        movies = []
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row['title']
                rating = float(row['rating'])
                year = int(row['year'])
                movies.append({'title': title, 'rating': rating, 'year': year})
        return movies

    def add_movie(self, title, year, rating, poster):
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, str(rating), str(year), ''])

    def delete_movie(self, title):
        rows = []
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] != title:
                    writer.writerow(row)

    def update_movie(self, title, notes):
        rows = []
        with open(self.file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        updated_rows = []
        for row in rows:
            if row[0] == title:
                row[3] = notes  # Update the notes for the matching movie title
            updated_rows.append(row)

        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)


