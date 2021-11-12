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
    print("Ошибка при работе с PostgreSQL", error)

def llang1(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 1777 WHERE userid = {message.from_user.id}')
    cursor.execute(f'SELECT lang FROM users WHERE userid = {message.from_user.id}')
    lil = cursor.fetchone()
    lil = lil[0]
    conn.commit()
    cursor.close()
    return lil

def llang2(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 1777 WHERE userid = {message.from_user.id}')
    cursor.execute(f"UPDATE users SET lang = '{message.text}' WHERE userid = {message.from_user.id}")
    conn.commit()
    cursor.execute(f'SELECT lang FROM users WHERE userid = {message.from_user.id}')
    lil2 = cursor.fetchone()
    lil2 = lil2[0]
    cursor.close()
    return lil2