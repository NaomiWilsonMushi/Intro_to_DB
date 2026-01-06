import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # connect to MySQL safely
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="my_mysql_password"  
        )

        # create cursor inside try
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # close cursor and connection safely
        try:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
        except NameError:
            # if cursor or connection was never created
            pass

if __name__ == "__main__":
    create_database()

