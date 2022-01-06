import psycopg2
from psycopg2 import Error

try:
    conn = psycopg2.connect(user="postgres",
                                password="iwasbornfree",
                                host="127.0.0.1",
                                port="5432",
                                database="luck")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
except (Exception, Error) as error:
    print("connError", error)

def hh():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    table = cursor.fetchall()
    for i in table:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE users SET bond = 0')
        cursor.execute(f'UPDATE users SET waterc = 1')
    conn.commit()
    cursor.close()