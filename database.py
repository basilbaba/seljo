import mysql.connector
from mysql.connector import Error

# =========================
# DATABASE CONFIGURATION
# =========================
DB_USER = 'root'
DB_PASSWORD = ''   # Use '' if password is empty
DB_HOST = 'localhost'
DB_NAME = 'agnar'
DB_PORT = 3306


# =========================
# CREATE DATABASE CONNECTION
# =========================
def get_connection():
    try:
        cnx = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )

        if cnx.is_connected():
            print("✅ Database connected successfully!")
            return cnx

    except Error as e:
        print(f"❌ Database Connection Error: {e}")

    return None


# =========================
# SELECT QUERY
# =========================
def select(query, values=None):
    cnx = None
    cur = None

    try:
        cnx = get_connection()

        if cnx is None:
            return []

        cur = cnx.cursor(dictionary=True)

        if values:
            cur.execute(query, values)
        else:
            cur.execute(query)

        result = cur.fetchall()

        return result

    except Error as e:
        print(f"❌ SELECT Error: {e}")
        return []

    finally:
        if cur:
            cur.close()

        if cnx and cnx.is_connected():
            cnx.close()


# =========================
# INSERT QUERY
# =========================
def insert(query, values=None):
    cnx = None
    cur = None

    try:
        cnx = get_connection()

        if cnx is None:
            return None

        cur = cnx.cursor()

        if values:
            cur.execute(query, values)
        else:
            cur.execute(query)

        cnx.commit()

        print("✅ INSERT successful!")

        return cur.lastrowid

    except Error as e:
        print(f"❌ INSERT Error: {e}")

        if cnx:
            cnx.rollback()

        return None

    finally:
        if cur:
            cur.close()

        if cnx and cnx.is_connected():
            cnx.close()


# =========================
# UPDATE QUERY
# =========================
def update(query, values=None):
    cnx = None
    cur = None

    try:
        cnx = get_connection()

        if cnx is None:
            return 0

        cur = cnx.cursor()

        if values:
            cur.execute(query, values)
        else:
            cur.execute(query)

        cnx.commit()

        print("✅ UPDATE successful!")

        return cur.rowcount

    except Error as e:
        print(f"❌ UPDATE Error: {e}")

        if cnx:
            cnx.rollback()

        return 0

    finally:
        if cur:
            cur.close()

        if cnx and cnx.is_connected():
            cnx.close()


# =========================
# DELETE QUERY
# =========================
def delete(query, values=None):
    cnx = None
    cur = None

    try:
        cnx = get_connection()

        if cnx is None:
            return 0

        cur = cnx.cursor()

        if values:
            cur.execute(query, values)
        else:
            cur.execute(query)

        cnx.commit()

        print("✅ DELETE successful!")

        return cur.rowcount

    except Error as e:
        print(f"❌ DELETE Error: {e}")

        if cnx:
            cnx.rollback()

        return 0

    finally:
        if cur:
            cur.close()

        if cnx and cnx.is_connected():
            cnx.close()


# =========================
# TESTING
# =========================
if __name__ == "__main__":

    # Test Database Connection
    connection = get_connection()

    if connection:
        print("✅ Connection Test Passed!")
        connection.close()
    else:
        print("❌ Connection Test Failed!")

    # =========================
    # EXAMPLE SELECT
    # =========================
    users = select("SELECT * FROM users")

    if users:
        print("\n📌 Users List:")
        for user in users:
            print(user)
    else:
        print("\n⚠️ No users found or query failed.")

    # =========================
    # EXAMPLE INSERT
    # =========================
    """
    insert_query = "INSERT INTO users(name, email) VALUES(%s, %s)"
    insert_values = ("Basil", "basil@gmail.com")

    inserted_id = insert(insert_query, insert_values)

    print("Inserted ID:", inserted_id)
    """

    # =========================
    # EXAMPLE UPDATE
    # =========================
    """
    update_query = "UPDATE users SET name=%s WHERE id=%s"
    update_values = ("New Name", 1)

    updated_rows = update(update_query, update_values)

    print("Updated Rows:", updated_rows)
    """

    # =========================
    # EXAMPLE DELETE
    # =========================
    """
    delete_query = "DELETE FROM users WHERE id=%s"
    delete_values = (1,)

    deleted_rows = delete(delete_query, delete_values)

    print("Deleted Rows:", deleted_rows)
    """
