import mysql.connector

if __name__ == '__main__':
    # Establish connection to MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port="3307",
    )

    cursor = mydb.cursor()

    # Create the database if it doesn't exist
    cursor.execute("""
    CREATE DATABASE IF NOT EXISTS biu_shoes;
    """)

    # Commit changes and close connection
    mydb.commit()
    cursor.close()
    mydb.close()