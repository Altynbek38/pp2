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
        else: print(Fore.RED + 'Command is not defined. TRY AGAIN!')
        

def create_table():
    command = """
    CREATE TABLE IF NOT EXISTS PhoneBook (
        Name VARCHAR(255) NOT NULL,
        Surname VARCHAR(255),
        Number VARCHAR(20)
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

def create_procedure():
    command = """
    CREATE OR REPLACE PROCEDURE insert_or_update(
        new_name VARCHAR(255),
        new_surname VARCHAR(255),
        new_number VARCHAR(20)
    )
    AS $$
    DECLARE

    BEGIN
        IF EXISTS(SELECT * FROM Phonebook WHERE Name = new_name AND Surname = new_surname) THEN
            UPDATE PhoneBook SET Number = new_number WHERE Name = new_name AND Surname = new_surname;
        ELSE
            INSERT INTO PhoneBook (Name, Surname, Number) VALUES (new_name, new_surname, new_number);
        END IF;
    END;
    $$
    LANGUAGE PLPGSQL;
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

def create_find_function(key):
    command = f"""
    CREATE OR REPLACE FUNCTION find_by_parts(value VARCHAR)
        RETURNS SETOF PhoneBook AS $$
    BEGIN
        RETURN QUERY

        SELECT 
            Name,
            Surname,
            Number

        FROM 
            PhoneBook
        
        WHERE
        {key} ILIKE '%' || value || '%';
    END; $$
    LANGUAGE plpgsql;

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

def create_insert_function():
    command = """
    CREATE OR REPLACE FUNCTION insert_contacts(users_list TEXT[])
    RETURNS TEXT 
    AS $$
    DECLARE
        user_record TEXT;
        user_name VARCHAR(255);
        user_surname VARCHAR(255);
        user_phone VARCHAR(20);
        incorrect_data TEXT := '';
    BEGIN
        FOR user_record IN SELECT unnest(users_list)
        LOOP
            user_name := split_part(user_record, ',', 1);
            user_surname := split_part(user_record, ',', 2);
            user_phone := split_part(user_record, ',', 3);
        
            -- Check phone number correctness
            IF length(regexp_replace(user_phone, '[^0-9]', '')) <> 11 THEN
                incorrect_data := incorrect_data || user_name || ',' || user_surname || ',' || user_phone || ';';
                CONTINUE;
            END IF;
        
            -- Insert user into database
            INSERT INTO PhoneBook (Name, Surname, Number) VALUES (user_name, user_surname, user_phone);
        END LOOP;
    
        RETURN incorrect_data;
    END;
    $$ LANGUAGE plpgsql;
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

def pagination_function():
    command = """CREATE OR REPLACE FUNCTION paginate_contacts(limit_val INTEGER, offset_val INTEGER)
    RETURNS TABLE (Name VARCHAR(255), Surname VARCHAR(255), Number VARCHAR(20)) AS $$
    BEGIN
    RETURN QUERY 
        SELECT * FROM PhoneBook
        LIMIT limit_val
        OFFSET offset_val;
    END;
    $$ LANGUAGE plpgsql;

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

def delete_procedure(key):
    command = f"""
    CREATE OR REPLACE PROCEDURE delete_contact (value VARCHAR)
    AS $$
    BEGIN
        DELETE FROM PhoneBook WHERE {key} = value;
    END;
    $$
    LANGUAGE plpgsql;
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
    action = (input(Fore.WHITE + "Downloading contacts from a [1]ist or [2]directly entering contacts or [3]go to main menu: "))
    if action == "1":
        create_insert_function()
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            users = ['John,Smith,1234567890', 'Arman,Dulat,555-1234', 'Bake,Jake,0987654321', 'Aslanbek,Zholdybay,+77083900680']
            cur.callproc('insert_contacts', [users])
            # Fetch the result from the stored procedure
            result = cur.fetchall()
            print(result)
            conn.commit()
            cur.close()
            print(Fore.GREEN + "Data inserted successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    elif action == "2":
        # sql = """INSERT INTO PhoneBook(Name, Surname, Number) VALUES (%s, %s, %s)"""
        create_procedure()
        name = input("Name: ")
        surname = input("Surname: ")
        number = input("Phone Number: ")
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute('CALL insert_or_update(%s, %s, %s)', (name, surname, number,))
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
    action = input(Fore.WHITE + "What do you want to change: [N]ame, [S]urname, [P]hone Number. [M]Go to main menu: ").strip().lower()

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
    action = input(Fore.WHITE + 'With what do you want to delete: [N]ame, [S]urname, [P]hone number.[M]Got to main menu: ').strip().lower()
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
    value = input('Delete contact: ')
    conn = None
    delete_procedure(column)
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('CALL delete_contact(%s)', (value,))
        conn.commit()
        cur.close()
        print(Fore.GREEN + "The contact has been successfully deleted")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def find_data():
    action = input(Fore.WHITE + 'With what do you want to find: [N]ame, [S]urname, [P]hone number. [M]Go to main menu:  ').strip().lower()
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
    create_find_function(column)
    conn = None
    try:
        param = config()
        conn = psycopg2.connect(**param)
        cur = conn.cursor()
        cur.callproc('find_by_parts', (search,))
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
    pagination_function()
    page = int(input("Which page: "))
    try:
        param = config()
        conn = psycopg2.connect(**param)
        cur = conn.cursor()
        cur.callproc("paginate_contacts",(5, (page - 1) * 5))
        rows = cur.fetchall()
        print('Count of contacs in the phone book:', cur.rowcount)
        print()
        for row in rows:
            # print(row)
            print(Fore.GREEN + f'Name: {row[0]}, Surname: {row[1]}, Phone Number: {row[2]}')
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        pass


if __name__ == "__main__":
    main()