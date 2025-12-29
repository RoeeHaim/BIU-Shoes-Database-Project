import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="root",
        database="biu_shoes", port="3307"
    )
    cursor = mydb.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS shoe_size (
          shoe_id INT NOT NULL,
          size_id INT NOT NULL,
          PRIMARY KEY (shoe_id, size_id),
          FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id),
          FOREIGN KEY (size_id) REFERENCES size(size_id)
        );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()