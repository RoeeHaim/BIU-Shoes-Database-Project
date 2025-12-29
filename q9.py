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

    # List all shoes with count of available sizes
    cursor.execute("""
    SELECT
        sh.shoe_name,
        COUNT(ss.size_id) AS size_count
    FROM shoe sh
    LEFT JOIN shoe_size ss
        ON sh.shoe_id = ss.shoe_id
    GROUP BY sh.shoe_id, sh.shoe_name;
    """)

    # Print results using the required format
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()