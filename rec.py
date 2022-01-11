from postgresso import *

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