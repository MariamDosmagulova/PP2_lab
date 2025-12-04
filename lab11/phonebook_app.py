import psycopg2
import csv

DB_CONFIG = {
    'host': 'localhost',
    'database': 'phonebook',
    'user': 'postgres',
    'password': 'Cici!4566',
    'port': '5432'
}

def create_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"Connection error: {e}")
        return None



def create_table():
    conn = create_connection()
    if conn is None: return
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                phone VARCHAR(20) NOT NULL
            )
        """)
        conn.commit()
        print("Table created successfully.")
    finally:
        conn.close()



def insert_from_csv(filename='phonebook.csv'):
    conn = create_connection()
    if conn is None: return

    try:
        cur = conn.cursor()
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                    (row['name'], row['phone'])
                )
        conn.commit()
        print("CSV data inserted.")
    except Exception as e:
        print(e)
    finally:
        conn.close()



def insert_or_update(name, phone):
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
        conn.commit()
        print("User inserted/updated.")
    finally:
        conn.close()

def insert_many(names, phones):
    conn = create_connection()
    try:
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM insert_many_users(%s, %s);", (names, phones))
        result = cur.fetchone()
        conn.commit()
        
        print("Mass insert completed.")
        if result and result[0]:
            print("Invalid entries:", result[0])
        else:
            print("All entries were valid.")
    finally:
        conn.close()

def search_by_pattern(pattern):
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM search_pattern(%s);", (pattern,))
        rows = cur.fetchall()
        for r in rows:
            print(r)
    finally:
        conn.close()

def get_page(limit, offset):
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_page(%s, %s);", (limit, offset))
        rows = cur.fetchall()
        for r in rows:
            print(r)
    finally:
        conn.close()

def delete_value(value):
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("CALL delete_by_value(%s);", (value,))
        conn.commit()
        print("Deleted matching records.")
    finally:
        conn.close()



def main():
    create_table()

    while True:
        print("\n===== PHONEBOOK MENU =====")
        print("1. Load CSV")
        print("2. Add/Update User")
        print("3. Insert Many Users")
        print("4. Search by Pattern")
        print("5. Pagination")
        print("6. Delete")
        print("7. Exit")
        
        choice = input("Choose: ")

        if choice == '1':
            insert_from_csv()

        elif choice == '2':
            n = input("Name: ")
            p = input("Phone: ")
            insert_or_update(n, p)

        elif choice == '3':
            count = int(input("How many users?: "))
            names = []
            phones = []
            for _ in range(count):
                names.append(input("Name: "))
                phones.append(input("Phone: "))
            insert_many(names, phones)

        elif choice == '4':
            pattern = input("Search: ")
            search_by_pattern(pattern)

        elif choice == '5':
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
            get_page(limit, offset)

        elif choice == '6':
            value = input("Name or phone to delete: ")
            delete_value(value)

        elif choice == '7':
            print("Bye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
