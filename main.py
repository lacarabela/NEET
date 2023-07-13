import psycopg2  # Allows the use of postgresSQL queries


# TODO: Finish the completed table; would also like to possibly include genres etc, eventually create a gui
# TODO: and would also like to maybe expand to anime

def print_menu():
    print('* * * 📚 Manga Database 📚 * * * ')
    print('1️⃣: View Library')
    print('2️⃣: Edit Library')
    print('3️⃣: Exit')  # Stretch


conn = psycopg2.connect(database="manga_database",
                        host="localhost",
                        user="postgres",
                        password="Mamita0011!!")

cursor = conn.cursor()


def view():  # Allows you to view what you are currently reading
    print('1️⃣: Currently Reading')
    print('2️⃣: Completed Library')
    view_input = int(input("Which would you like to view? "))
    if view_input == 1:  # Access the currently reading tables
        cursor.execute("SELECT * FROM reading")
        manga_list = cursor.fetchall()
        if len(manga_list) == 0:
            print("No manga is currently being read.")
        else:
            for manga in manga_list:
                print(f"Title: {manga[1]}")
                print(f"Author: {manga[2]}")
                print(f"Artist: {manga[3]}")
                print(f"Last Read Volume: {manga[4]}")
                print(f"Volume Count: {manga[5]}")
                print(f"Start Date: {manga[6]}")
                print("-------------------------------------")
    elif view_input == 2:  # Access the completed table
        cursor.execute("SELECT * FROM completed")
        manga_list = cursor.fetchall()
        if len(manga_list) == 0:
            print("No completed manga found.")
        else:
            for manga in manga_list:
                print(f"Title: {manga[1]}")
                print(f"Author: {manga[2]}")
                print(f"Artist: {manga[3]}")
                print(f"Last Read Volume: {manga[4]}")
                print(f"Volume Count: {manga[5]}")
                print(f"Start Date: {manga[6]}")
                print("-------------------------------------")
    else:
        print("Invalid Input.")


def edit():  # Allows the user to edit various things from a chosen table
    print('1️⃣: Currently Reading')
    print('2️⃣: Completed Library')
    edit_input = int(input("Which would you like to edit? "))
    if edit_input == 1:  # Editing the currently reading table
        print('1️⃣: Mark Manga as Complete')
        print('2️⃣: Add New Manga')
        print('3️⃣: Edit Manga Specifics')
        print('4️⃣: Remove Manga')

        extra1_input = int(input("What would you like to do? "))

        if extra1_input == 1:  # Marking manga as complete
            cursor.execute("SELECT * FROM reading")  # Showing the tables
            manga_list = cursor.fetchall()
            if len(manga_list) == 0:
                print("No manga is currently being read.")
            else:
                for manga in manga_list:  # Showing the tables with the manga ID
                    print(f"Manga ID: {manga[0]}")
                    print(f"Title: {manga[1]}")
                    print(f"Author: {manga[2]}")
                    print(f"Artist: {manga[3]}")
                    print(f"Last Read Volume: {manga[4]}")
                    print(f"Volume Count: {manga[5]}")
                    print(f"Start Date: {manga[6]}")
                    print("-------------------------------------")
            manga_input = int(input("Enter the Manga ID to be moved to completed: "))
            select_query = "SELECT * FROM Reading WHERE manga_id = %s"
            cursor.execute(select_query, (manga_input,))
            manga = cursor.fetchone()
            if manga:
                print("Manga found:")
                print(f"Title: {manga[1]}")
                print(f"Author: {manga[2]}")
                print(f"Artist: {manga[3]}")
                print(f"Last Read Volume: {manga[4]}")
                print(f"Volume Count: {manga[5]}")
                print(f"Start Date: {manga[6]}")

                completion_date = input("Enter the Completion Date (YYYY-MM-DD): ")

                insert_query = """
                                INSERT INTO Completed (manga_id, title, author, artist, last_read_volume, volume_count, 
                                start_date, completion_date)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            """

                cursor.execute(insert_query,
                               (manga[0], manga[1], manga[2], manga[3], manga[4], manga[5], manga[6], completion_date))
                conn.commit()

                delete_query = "DELETE FROM Reading WHERE manga_id = %s"
                cursor.exceute(delete_query, (manga_input,))
                conn.commit()

                print("Manga has successfully been moved to the Completed table.")
            else:
                print("Manga not found in the Reading table.")

        elif extra1_input == 2:  # Adding a new manga
            title = input("What is the name of the manga? ")
            author = input("Who is the author of " + title + "? ")
            artist = input("Is " + author + " the artist as well? (y/n) ")

            if artist.lower() == "y":
                artist = "NULL"
            elif artist.lower() == "n":
                artist = input("Who is the artist of " + title + "? ")
            else:
                print("Invalid Input.")

            last_read_volume = int(input("What was the last volume you read? "))
            volume_count = int(input("Whats the total amount of volumes released? "))
            start_date = input("Enter your start date (YYYY-MM-DD): ")

            insert_query = """
                            INSERT INTO Reading (title, author, artist, last_read_volume, volume count, start_date)
                            VALUES(%s, %s, %s, %s, %s, %s)
                        """
            cursor.execute(insert_query, (title, author, artist, last_read_volume, volume_count, start_date))
            conn.commit()
            print("The manga has successfully been added to the Reading table.")

        elif extra1_input == 3:  # Edit a specific variable
            cursor.execute("SELECT * FROM reading")  # Showing the tables
            manga_list = cursor.fetchall()

            if len(manga_list) == 0:
                print("No manga is currently being read.")
            else:
                for manga in manga_list:  # Showing the tables with the manga ID
                    print(f"Manga ID: {manga[0]}")
                    print(f"Title: {manga[1]}")
                    print(f"Author: {manga[2]}")
                    print(f"Artist: {manga[3]}")
                    print(f"Last Read Volume: {manga[4]}")
                    print(f"Volume Count: {manga[5]}")
                    print(f"Start Date: {manga[6]}")
                    print("-------------------------------------")
                manga_input = int(input("Enter the Manga ID to be edited: "))
                select_query = "SELECT * FROM Reading WHERE manga_id = %s"
                cursor.execute(select_query, (manga_input,))
                manga = cursor.fetchone()

                if manga:
                    print("Manga found:")
                    print(f"Manga ID: {manga[0]}")
                    print(f"Title: {manga[1]}")
                    print(f"Author: {manga[2]}")
                    print(f"Artist: {manga[3]}")
                    print(f"Last Read Volume: {manga[4]}")
                    print(f"Volume Count: {manga[5]}")
                    print(f"Start Date: {manga[6]}")

                    field = input("Enter the field you want to edit (title, author, artist, last_read_volume, "
                                  "volume_count, start_date): ")

                    if field in ['title', 'author', 'artist', 'last_read_volume', 'volume_count', 'start_date']:
                        value = input(f"Enter the new value for {field}: ")

                        update_query = f"UPDATE Reading SET {field} = %s WHERE manga_input = %s"
                        cursor.execute(update_query, (value, manga_input))
                        conn.commit()

                        print("The manga has successfully been update.")
                    else:
                        print("Invalid Input.")
                else:
                    print("Manga was not found in the reading table.")

        elif extra1_input == 4:  # Remove manga
            cursor.execute("SELECT * FROM reading")  # Showing the tables
            manga_list = cursor.fetchall()

            if len(manga_list) == 0:
                print("No manga is currently being read.")
            else:
                for manga in manga_list:  # Showing the tables with the manga ID
                    print(f"Manga ID: {manga[0]}")
                    print(f"Title: {manga[1]}")
                    print(f"Author: {manga[2]}")
                    print(f"Artist: {manga[3]}")
                    print(f"Last Read Volume: {manga[4]}")
                    print(f"Volume Count: {manga[5]}")
                    print(f"Start Date: {manga[6]}")
                    print("-------------------------------------")
                manga_input = int(input("Enter the Manga ID to be edited: "))
                select_query = "SELECT * FROM Reading WHERE manga_id = %s"
                cursor.execute(select_query, (manga_input,))
                manga = cursor.fetchone()
                if manga:
                    delete_query = "DELETE FROM Reading WHERE manga_input = %s"
                    cursor.excute(delete_query, (manga_input,))
                    conn.commit()

                    print("The manga has successfully been removed from the reading table.")
                else:
                    print("Manga was not found in the reading table.")
        else:
            print("Invalid Input.")
    elif edit_input == 2:  # Editing the completed table
        print('1️⃣: Mark a Completed Title as currently reading')
        print('2️⃣: Add New Manga')
        print('3️⃣: Edit Manga Specifics')
        print('4️⃣: Remove Manga')

        extra2_input = int(input("What would you like to do? "))

        if extra2_input == 1:  # Marking completed manga as reading
            cursor.execute("SELECT * FROM completed")  # Showing the tables
            manga_list = cursor.fetchall()
            if len(manga_list) == 0:
                print("No manga has been completed.")
            else:
                for manga in manga_list:  # Showing the tables with the manga ID
                    print(f"Manga ID: {manga[0]}")
                    print(f"Title: {manga[1]}")
                    print(f"Author: {manga[2]}")
                    print(f"Artist: {manga[3]}")
                    print(f"Last Read Volume: {manga[4]}")
                    print(f"Volume Count: {manga[5]}")
                    print(f"Start Date: {manga[6]}")
                    print(f"Completion Date: {manga[7]}")
                    print("-------------------------------------")
            manga_input = int(input("Enter the Manga ID to be moved to reading: "))
            select_query = "SELECT * FROM Completed WHERE manga_id = %s"
            cursor.execute(select_query, (manga_input,))
            manga = cursor.fetchone()
            if manga:
                print("Manga found:")
                print(f"Title: {manga[1]}")
                print(f"Author: {manga[2]}")
                print(f"Artist: {manga[3]}")
                print(f"Last Read Volume: {manga[4]}")
                print(f"Volume Count: {manga[5]}")
                print(f"Start Date: {manga[6]}")
                print(f"Completion Date: {manga[7]}")

                start_date = input("Enter the new Start Date (YYYY-MM-DD): ")

                insert_query = """
                                INSERT INTO Reading (manga_id, title, author, artist, last_read_volume, volume_count, 
                                start_date)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """

                cursor.execute(insert_query,
                               (manga[0], manga[1], manga[2], manga[3], manga[4], manga[5], start_date))
                conn.commit()

                delete_query = "DELETE FROM Completed WHERE manga_id = %s"
                cursor.exceute(delete_query, (manga_input,))
                conn.commit()

                print("Manga has successfully been moved to the Reading table.")
            else:
                print("Manga not found in the Completed table.")

        elif extra2_input == 2:  # Adding a new manga to the completed table
            title = input("What is the name of the manga? ")
            author = input("Who is the author of " + title + "? ")
            artist = input("Is " + author + " the artist as well? (y/n) ")

            if artist.lower() == "y":
                artist = "NULL"
            elif artist.lower() == "n":
                artist = input("Who is the artist of " + title + "? ")
            else:
                print("Invalid Input.")

            last_read_volume = int(input("What was the last volume you read? "))
            volume_count = int(input("Whats the total amount of volumes released? "))
            start_date = input("Enter your start date (YYYY-MM-DD): ")
            completion_date = input("Enter your completion date (YYYY-MM-DD): ")

            insert_query = """
                            INSERT INTO Completed (title, author, artist, last_read_volume, volume count, start_date, 
                            completion_date)
                            VALUES(%s, %s, %s, %s, %s, %s, %s)
                        """
            cursor.execute(insert_query, (title, author, artist, last_read_volume, volume_count, start_date,
                                          completion_date))
            conn.commit()
            print("The manga has successfully been added to the completed table.")

        elif extra2_input == 3:  # Edit a specific variable
            cursor.execute("SELECT * FROM Completed")  # Showing the tables
            manga_list = cursor.fetchall()

            if len(manga_list) == 0:
                print("No manga has been completed.")
            else:
                for manga in manga_list:  # Showing the tables with the manga ID
                    print(f"Manga ID: {manga[0]}")
                    print(f"Title: {manga[1]}")
                    print(f"Author: {manga[2]}")
                    print(f"Artist: {manga[3]}")
                    print(f"Last Read Volume: {manga[4]}")
                    print(f"Volume Count: {manga[5]}")
                    print(f"Start Date: {manga[6]}")
                    print(f"Completion Date: {manga[7]}")
                    print("-------------------------------------")
                manga_input = int(input("Enter the Manga ID to be edited: "))
                select_query = "SELECT * FROM Completed WHERE manga_id = %s"
                cursor.execute(select_query, (manga_input,))
                manga = cursor.fetchone()

                if manga:
                    print("Manga found:")
                    print(f"Manga ID: {manga[0]}")
                    print(f"Title: {manga[1]}")
                    print(f"Author: {manga[2]}")
                    print(f"Artist: {manga[3]}")
                    print(f"Last Read Volume: {manga[4]}")
                    print(f"Volume Count: {manga[5]}")
                    print(f"Start Date: {manga[6]}")
                    print(f"Completion Date: {manga[7]}")

                    field = input("Enter the field you want to edit (title, author, artist, last_read_volume, "
                                  "volume_count, start_date, completion_date): ")

                    if field in ['title', 'author', 'artist', 'last_read_volume', 'volume_count', 'start_date',
                                 'completion_date']:
                        value = input(f"Enter the new value for {field}: ")

                        update_query = f"UPDATE Completed SET {field} = %s WHERE manga_input = %s"
                        cursor.execute(update_query, (value, manga_input))
                        conn.commit()

                        print("The manga has successfully been update.")
                    else:
                        print("Invalid Input.")
                else:
                    print("Manga was not found in the Completed table.")

        elif extra2_input == 4:  # Remove manga
            cursor.execute("SELECT * FROM completed")  # Showing the tables
            manga_list = cursor.fetchall()

            if len(manga_list) == 0:
                print("No manga has been completed.")
            else:
                for manga in manga_list:  # Showing the tables with the manga ID
                    print(f"Manga ID: {manga[0]}")
                    print(f"Title: {manga[1]}")
                    print(f"Author: {manga[2]}")
                    print(f"Artist: {manga[3]}")
                    print(f"Last Read Volume: {manga[4]}")
                    print(f"Volume Count: {manga[5]}")
                    print(f"Start Date: {manga[6]}")
                    print(f"Completion Date: {manga[7]}")
                    print("-------------------------------------")
                manga_input = int(input("Enter the Manga ID to be removed: "))
                select_query = "SELECT * FROM Completed WHERE manga_id = %s"
                cursor.execute(select_query, (manga_input,))
                manga = cursor.fetchone()
                if manga:
                    delete_query = "DELETE FROM Completed WHERE manga_input = %s"
                    cursor.excute(delete_query, (manga_input,))
                    conn.commit()

                    print("The manga has successfully been removed from the completed table.")
                else:
                    print("Manga was not found in the reading table.")
    else:
        print("Invalid Input.")


while True:
    print_menu()
    user_input = int(input("Select an option (1-3): "))
    if user_input == 1:
        view()
    elif user_input == 2:
        edit()
    elif user_input == 3:
        print("Thank you, Goodbye!")
        cursor.close()
        conn.close()
        break
    else:
        print("Invalid option.")
