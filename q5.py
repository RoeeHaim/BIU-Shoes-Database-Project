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

    # Add 'pre_order_available' bit column with default 0
    cursor.execute("""
        ALTER TABLE upcoming
        ADD COLUMN pre_order_available BIT(1) DEFAULT 0;
    """)

    mydb.commit()
    cursor.close()
    mydb.close()