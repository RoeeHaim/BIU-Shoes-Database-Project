import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port="3307",
    )

    cursor = mydb.cursor()
    cursor.execute("USE biu_shoes;")

    # Alter the size table to add 'uk_number' column
    cursor.execute("""
        ALTER TABLE size
        ADD COLUMN uk_number TINYINT;
    """)

    mydb.commit()
    cursor.close()
    mydb.close()