import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="root",
        database="biu_shoes", port="3307"
    )
    cursor = mydb.cursor()

    # VIEW
    cursor.execute("""
    CREATE OR REPLACE VIEW total_sales_per_shoe AS
    SELECT 
        sh.shoe_id, 
        sh.shoe_name, 
        SUM(sh.price) AS total_revenue
    FROM shoe sh
    JOIN order_shoe os ON sh.shoe_id = os.shoe_id
    GROUP BY sh.shoe_id, sh.shoe_name;
    """)

    mydb.commit()
    cursor.close()
    mydb.close()