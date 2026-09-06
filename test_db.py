import mysql.connector

from config import DB_CONFIG


print("Connecting to MySQL...")

try:
    connection = mysql.connector.connect(**DB_CONFIG)

    print("SUCCESS: MySQL connection works!")

    cursor = connection.cursor()

    cursor.execute("SELECT DATABASE();")

    database = cursor.fetchone()

    print("Database:", database[0])

    cursor.close()
    connection.close()

    print("Connection closed.")

except Exception as error:
    print("ERROR:", error)