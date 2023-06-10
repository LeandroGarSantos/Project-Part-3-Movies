import movie_storage


def main():
    while True:
        print("\033[31m Menu:\033")
        print("\033[33m1 0. Exit")
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
            movie_storage.list_movies()
        elif choice == '2':
            movie_storage.add_movie()
        elif choice == '3':
            movie_storage.delete_movie()
        elif choice == '4':
            movie_storage.update_movie()
        elif choice == '5':
            movie_storage.stats()
        elif choice == '6':
            movie_storage.random_movie()
        elif choice == '7':
            movie_storage.search_movie()
        elif choice == '8':
            movie_storage.sort_movies_by_rating()
        elif choice == '9':
            movie_storage.create_website()
        else:
            print("\033[31m Invalid choice.\033")


if __name__ == '__main__':
    main()

