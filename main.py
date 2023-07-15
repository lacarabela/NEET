from manga_library import view_library, edit_library
from database import get_connection, release_connection


def display_menu():
    print('* * * 📚 Manga Database 📚 * * * ')
    print('1️⃣: View Library')
    print('2️⃣: Edit Library')
    print('3️⃣: Exit')  # Stretch


while True:
    display_menu()
    user_input = input("Select an option (1-3): ")

    try:
        user_input = int(user_input)
        if user_input == 1:
            conn = get_connection()
            view_library(conn)
            release_connection(conn)
        elif user_input == 2:
            conn = get_connection()
            edit_library(conn)
            release_connection(conn)
        elif user_input == 3:
            print("Thank you, Goodbye!")
            break
        else:
            print("Invalid option.")
    except ValueError:
        print("Invalid input. Please enter a number (1-3).")