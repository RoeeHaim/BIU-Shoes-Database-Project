import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port="3307",
    )

    cursor = mydb.cursor()

    # 1. Drop view if exists and create the new view for total sales per shoe
    cursor.execute("DROP VIEW IF EXISTS total_sales_per_shoe;")

    cursor.execute("""
    CREATE VIEW total_sales_per_shoe AS
    SELECT
        sh.shoe_id,
        sh.shoe_name,
        SUM(sh.price) AS total_revenue
    FROM shoe sh
    JOIN order_shoe os
        ON sh.shoe_id = os.shoe_id
    GROUP BY sh.shoe_id, sh.shoe_name;
    """)

    # 2. Query to display the entire view data
    cursor.execute("SELECT * FROM total_sales_per_shoe;")

    # Print results using the required format
    print(', '.join(str(row) for row in cursor.fetchall()))

    mydb.commit()
    cursor.close()
    mydb.close()