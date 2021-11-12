from selec import selec
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

def mainnn(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 0 WHERE userid = {message.from_user.id}')
    if selec(message) == 9990:
        cursor.execute(f"UPDATE users SET lang = '{message.text}' WHERE userid = {message.from_user.id}")
    conn.commit()
    cursor.close()