import requests
import logging
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

def rev1(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 33 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()

def rev2(message):
    r = requests.get(f'https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id=1737649749&text=z{message.text}\n{message.from_user.id}')
    logging.info(f"{message.from_user.id} wrote {message.text}")

def rev11(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 34 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()