import psycopg2
from psycopg2 import Error
import logging
import requests

try:
    conn = psycopg2.connect(user="postgres",
                            password="iwasbornfree",
                            host="127.0.0.1",
                            port="5432",
                            database="luck")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

def transfer1(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 11290 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.execute(f'SELECT id FROM users WHERE userid = {message.from_user.id}')
    id = cursor.fetchone()
    cursor.close()
    id = id[0]
    return id

def transfer2(message):
    try:
            mess = message.text.split(' ')
            mon = mess[1]
            mon = int(mon)
            cursor = conn.cursor()
            cursor.execute(f'SELECT id FROM users WHERE userid = {message.from_user.id}')
            id = cursor.fetchone()
            id = id[0]
            cursor.execute(f'SELECT rub FROM users WHERE userid = {message.from_user.id}')
            rub = cursor.fetchone()
            cursor.close()
            rub = rub[0]
            if rub >= mon and mon >= 10 and mon <= 10000:
                try:
                    cursor = conn.cursor()
                    cursor.execute(f'UPDATE users SET rub = rub - {mon} WHERE userid = {message.from_user.id}')
                    cursor.execute(f'UPDATE users SET rub = rub + {mon} WHERE id = {mess[0]}')
                    conn.commit()
                    cursor.execute(f'SELECT userid FROM users WHERE id = {mess[0]}')
                    messid = cursor.fetchone()
                    cursor.close()
                    messid = messid[0]
                    logging.info(f'{message.from_user.id} > {mess[0]} {mon}')
                    r = requests.get(f"https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id={messid}&text=Пользователь {id} перевел на ваш счет {mon} 💲!")
                    return mon, mess
                except Error:
                    return None
            else:
                return None
    except Error:
            return None