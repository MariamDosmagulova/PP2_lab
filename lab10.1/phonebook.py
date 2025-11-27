import psycopg2
import csv
import os
from psycopg2 import sql



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
        print("Connection to the database is successful")
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

def create_table():
    """Создает таблицу phonebook если она не существует"""
    conn = create_connection()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        # Создаем таблицу
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                phone VARCHAR(20) NOT NULL
            )
        """)
        conn.commit()
        print("The 'phonebook' table has been created or already exists")
    except psycopg2.Error as e:
        print(f"Error creating the table: {e}")
    finally:
        cur.close()
        conn.close()



def insert_from_csv(filename='phonebook.csv'):
    """Добавляет данные из CSV файла"""
    conn = create_connection()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count = 0
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                    (row['name'], row['phone'])
                )
                count += 1
        conn.commit()
        print(f"Added {count} contacts from the CSV file")
    except (psycopg2.Error, FileNotFoundError) as e:
        print(f"Error when adding from CSV: {e}")
    finally:
        cur.close()
        conn.close()

def insert_from_console():
    """Добавляет данные через консоль"""
    conn = create_connection()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        print("\n Adding a new contact:")
        name = input("Enter a name: ")
        phone = input("Enter your phone number: ")
        
        cur.execute(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Contact successfully added!")
    except psycopg2.Error as e:
        print(f"Error when adding: {e}")
    finally:
        cur.close()
        conn.close()



def update_contact():
    """Изменяет имя или телефон контакта"""
    conn = create_connection()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        print("\n Updating a contact:")
        old_name = input("Enter the current contact name: ")
        
        # Проверяем существует ли контакт
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (old_name,))
        if not cur.fetchone():
            print("The contact was not found")
            return
        
        print("What do you want to change?")
        print("1. Name")
        print("2. Phone")
        choice = input("Select option (1 or 2): ")
        
        if choice == '1':
            new_name = input("Enter a new name: ")
            cur.execute(
                "UPDATE phonebook SET name = %s WHERE name = %s",
                (new_name, old_name)
            )
            print("Name changed successfully!")
        elif choice == '2':
            new_phone = input("Enter a new phone number: ")
            cur.execute(
                "UPDATE phonebook SET phone = %s WHERE name = %s",
                (new_phone, old_name)
            )
            print("The phone number has been successfully changed")
        else:
            print("Wrong choice")
            return
        
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error during the update: {e}")
    finally:
        cur.close()
        conn.close()



def query_data():
    """Поиск контактов с разными фильтрами"""
    conn = create_connection()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        print("\n🔍Contact Search:")
        print("1. Show all contacts")
        print("2. Name Search")
        print("3. Phone search")
        print("4. Search by part of the name")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            cur.execute("SELECT * FROM phonebook ORDER BY name")
        elif choice == '2':
            name = input("Enter a name to search for: ")
            cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
        elif choice == '3':
            phone = input("Enter the phone number for the search: ")
            cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
        elif choice == '4':
            partial_name = input("Enter part of the name: ")
            cur.execute("SELECT * FROM phonebook WHERE name LIKE %s", (f'%{partial_name}%',))
        else:
            print("Wrong choice")
            return
        
        results = cur.fetchall()
        if results:
            print(f"\n Contacts found: {len(results)}")
            print("-" * 40)
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
        else:
            print("No contacts found")
            
    except psycopg2.Error as e:
        print(f"Error in the search: {e}")
    finally:
        cur.close()
        conn.close()



def delete_contact():
    """Удаление контактов по имени или телефону"""
    conn = create_connection()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        print("\n Deleting a contact:")
        print("1. Delete by Name")
        print("2. Delete by phone")
        
        choice = input("Choose an option (1 или 2): ")
        
        if choice == '1':
            name = input("Enter a name to delete: ")
            cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
        elif choice == '2':
            phone = input("Enter the phone number to delete: ")
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        else:
            print("Wrong choice")
            return
        
        conn.commit()
        print(f"Deleted {cur.rowcount} contact(s)")
    except psycopg2.Error as e:
        print(f"Error when deleting: {e}")
    finally:
        cur.close()
        conn.close()


def main():
    """Главное меню программы"""
    print("=" * 50)
    print("WELCOME TO PHONEBOOK")
    print("=" * 50)
    
    # Создаем таблицу при запуске
    create_table()
    
    while True:
        print("\n" + "=" * 30)
        print("MAIN MENU")
        print("=" * 30)
        print("1. Download data from CSV")
        print("2. Add a contact manually")
        print("3. Change a contact")
        print("4. Find contacts")
        print("5. Delete a contact")
        print("6. Exit")
        
        choice = input("\n Select an action (1-6): ")
        
        if choice == '1':
            insert_from_csv()
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\n BB")
            break
        else:
            print("Wrong choice! Try again.")

if __name__ == "__main__":
    main()