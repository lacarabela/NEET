import psycopg2  # Allows the use of postgresSQL queries


def connect_to_database():
    conn = psycopg2.connect(database="manga_database",
                            host="localhost",
                            user="postgres",
                            password="postgres")

    cursor = conn.cursor()
    return conn, cursor
