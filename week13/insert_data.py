import psycopg2
from config import config

def insert_vendor(vendor_name):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO vendors(vendor_name)
            VALUES(%s) RETURNING vendor_id;"""
    
    conn = None
    vendor_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.excecute(sql, (vendor_name,))
        vendor_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id

def insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, vendor_list)
        conn.commit()
        conn.close()
    except  (Exception, psycopg2.DatabaseError) as error:
        print(error)        
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    insert_vendor("3M Co.")

    insert_vendor_list({
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd',),
        ('Dynacast International Inc.',),
        ('Murata Manufacturing Co, Ltd',)
    })