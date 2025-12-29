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

    # Combine shoe names from inventory and upcoming releases using UNION
    cursor.execute("""
    SELECT
        shoe_name AS name,
        'Inventory' AS source
    FROM shoe

    UNION

    SELECT
        collection_name AS name,
        'Upcoming Release' AS source
    FROM upcoming;
    """)

    # Print results using the required format
    print(', '.join(str(row) for row in cursor.fetchall()))

    cursor.close()
    mydb.close()