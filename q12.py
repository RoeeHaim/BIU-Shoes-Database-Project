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

    # Find shoes that have not been ordered yet
    cursor.execute("""
    SELECT
        sh.shoe_name
    FROM shoe sh
    LEFT JOIN order_shoe os
        ON sh.shoe_id = os.shoe_id
    WHERE os.shoe_id IS NULL;
    """)

    # Print results using the required format
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()