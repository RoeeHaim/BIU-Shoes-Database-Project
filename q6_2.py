import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="root",
        database="biu_shoes", port="3307"
    )
    cursor = mydb.cursor()

    cursor.execute("UPDATE size SET uk_number = 6 WHERE size_id = 2;")

    mydb.commit()
    cursor.close()
    mydb.close()