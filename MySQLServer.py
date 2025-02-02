import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                # Create database if it doesn't exist
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as err:
                print(f"Failed to create database: {err}")
            finally:
                cursor.close()
    except Error as err:
        print(f"Error: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __Steven_Banda__ == "__main__":
    create_database()

