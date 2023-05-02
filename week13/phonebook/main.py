import psycopg2
import csv
from colorama import Fore
from config import config

def main():
    create_table()
    while True:
        show_commands()
        action = input().strip().lower()

        if action == 'i':
            insert_data()
        elif action == 'u':
            update_data()
        elif action == 'r':
            remove_data()
        elif action == 's':
            show_data()
        elif action == 'f':
            find_data()
        elif action == 'e':
            exit()
        

def create_table():
    command = """
    CREATE TABLE IF NOT EXISTS PhoneBook (
        Name VARCHAR(255) NOT NULL,
        Surname VARCHAR(255),
        Number VARCHAR(255)
    )
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def show_commands():
    print(Fore.WHITE + 'What action would you like to take:')
    print('[I]nsert data')
    print('[U]pdate data')
    print('[R]emove data')
    print('[S]how all contacs from the phone book')
    print('[F]find a contact from the phone book')
    print("[E]xit from app")

def insert_data():
    action = (input(Fore.WHITE + "Downloading contacts from a [1]file or [2]directly entering contacts or [3]go to main menu: "))
    if action == "1":
        filename = input("Filename: ")
        sql = """INSERT INTO PhoneBook(Name, Surname, Number) VALUES (%s, %s, %s)"""
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            with open(filename, 'r') as file:
                data = csv.reader(file)
                for contact in data:
                    cur.execute(sql, contact)
            conn.commit()
            cur.close()
            print(Fore.GREEN + "Data inserted successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    elif action == "2":
        sql = """INSERT INTO PhoneBook(Name, Surname, Number) VALUES (%s, %s, %s)"""
        name = input("Name: ")
        surname = input("Surname: ")
        number = input("Phone Number: ")
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, (name, surname, number,))
            conn.commit()
            cur.close()
            print(Fore.GREEN + "Data inserted successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    elif action == "3":
        return
    else:
        print(Fore.RED + "The command has not been identified. Please try again!")
        insert_data()


def update_data():
    action = input(Fore.WHITE + "What do you want to change: [N]ame, [S]urname, [P]hone Number. [M]Got main menu: ").strip().lower()

    if action == 'n':
        name = input("The contact you want to change: ")
        change = input("New name: ")
        sql = """UPDATE PhoneBook
            SET Name = %s
            WHERE Name = %s
        """
    elif action == 's':
        name = input("The contact you want to change: ")
        change = input("New surname: ")
        sql = """UPDATE PhoneBook
            SET Surname = %s
            WHERE Name = %s
        """
    elif action == 'p':
        name = input("The contact you want to change: ")        
        change = input("New phone Number: ")
        sql = """UPDATE PhoneBook
            SET Number = %s
            WHERE Name = %s
        """
    elif action == 'm':
        return
    else:
        print(Fore.RED + "The command has not been identified. Please try again!")
        return
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (change, name))
        conn.commit()
        cur.close()
        print(Fore.GREEN + "The contact has been successfully updated")
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error)
    finally:
        if conn is not None:
            conn.close()

def remove_data():
    name = input('The name of the contact you want to delete: ')
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("DELETE FROM PhoneBook WHERE Name = %s", (name,))
        conn.commit()
        cur.close()
        print(Fore.GREEN + "The contact has been successfully deleted")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def find_data():
    action = input('With what do you want to find: [N]ame, [S]urname, [P]hone number. [M]Go to main menu:  ').strip().lower()
    if action == 'n':
        column = 'Name'
    elif action == 's':
        column = 'Surname' 
    elif action == 'p':
        column = 'Number'
    elif action == 'm':
        return
    else:
        print(Fore.RED + "The command has not been identified. Please try again!")
        return
    search = input('Search: ')
    conn = None
    
    try:
        param = config()
        conn = psycopg2.connect(**param)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM PhoneBook WHERE {column} ILIKE '%{search}%'")
        rows = cur.fetchall()
        for row in rows:
            print(Fore.GREEN + f'Name: {row[0]}, Surname: {row[1]}, Phone Number: {row[2]}')
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def show_data():
    try:
        param = config()
        conn = psycopg2.connect(**param)
        cur = conn.cursor()
        cur.execute('SELECT * FROM PhoneBook')
        rows = cur.fetchall()
        print('Count of contacs in the phone book:', cur.rowcount)
        print()
        for row in rows:
            print(Fore.GREEN + f'Name: {row[0]}, Surname: {row[1]}, Phone Number: {row[2]}')
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        pass


if __name__ == "__main__":
    main()