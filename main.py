from manga_library import view_library, edit_library
from database import connect_to_database


def display_menu():
    print('* * * 📚 Manga Database 📚 * * * ')
    print('1️⃣: View Library')
    print('2️⃣: Edit Library')
    print('3️⃣: Exit')  # Stretch


conn, cursor = connect_to_database()

while True:
    display_menu()
    user_input = input("Select an option (1-3): ")

    try:
        user_input = int(user_input)
        if user_input == 1:
            view_library(cursor)
        elif user_input == 2:
            edit_library(cursor, conn)
        elif user_input == 3:
            print("Thank you, Goodbye!")
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid option.")
    except ValueError:
        print("Invalid input. Please enter a number (1-3).")
