import os
import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user=os.environ.get("DB_USERNAME"),
        password=os.environ.get("DB_PASSWORD"),
    )


with get_db_connection() as connection:

    with connection.cursor(dictionary=True) as my_cursor:
        try:
            my_cursor.execute('CREATE DATABASE website')
            my_cursor.execute('USE website')
            print('Success')
        except:
            my_cursor.execute('USE website')
            for db in my_cursor:
                print('DB in use')
