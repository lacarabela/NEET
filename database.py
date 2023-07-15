import psycopg2  # Allows the use of postgresSQL queries
from psycopg2 import pool

min_connections = 1
max_connections = 10

connection_pool = None


def create_connection_pool():
    global connection_pool
    connection_pool = psycopg2.pool.SimpleConnectionPool(
        min_connections, max_connections,
        database="manga_database",
        host="localhost",
        user="postgres",
        password="postgres"
    )


def get_connection():
    if connection_pool is None:
        create_connection_pool()
    return connection_pool.getconn()


def release_connection(conn):
    connection_pool.putconn(conn)


def close_connection_pool():
    if connection_pool is not None:
        connection_pool.closeall()
