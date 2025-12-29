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

    # Calculate average price of shoes per size
    cursor.execute("""
    SELECT
        sz.european_number,
        sz.us_number,
        AVG(sh.price) AS avg_price
    FROM size sz
    JOIN shoe_size ss
        ON sz.size_id = ss.size_id
    JOIN shoe sh
        ON ss.shoe_id = sh.shoe_id
    GROUP BY sz.size_id, sz.european_number, sz.us_number
    ORDER BY avg_price DESC;
    """)

    # Print results using the format
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()