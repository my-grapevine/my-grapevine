import os
import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user=os.environ.get("DB_USERNAME"),
        password=os.environ.get("DB_PASSWORD")
    )


def create_database():
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as my_cursor:
            db_name = os.environ.get('DB_NAME')
            try:
                my_cursor.execute(f'CREATE DATABASE {db_name}')
                my_cursor.execute(f'USE {db_name}')
            except mysql.connector.errors.Error:
                my_cursor.execute(f'USE {db_name}')


def drop_database():
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as my_cursor:
            db_name = os.environ.get('DB_NAME')
            try:
                my_cursor.execute(f'DROP DATABASE {db_name}')
            except mysql.connector.errors.Error:
                pass
