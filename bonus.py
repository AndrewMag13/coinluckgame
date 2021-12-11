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

def bond(message):
    cursor = conn.cursor()
    cursor.execute(f'SELECT bond FROM users WHERE userid = {message.from_user.id}')
    bbond = cursor.fetchone()
    bbond= bbond[0]
    if bbond == 0:
        cursor.execute(f'UPDATE users SET bond = 1 WHERE userid={message.from_user.id}')
        cursor.execute(f'UPDATE users SET rub = rub + 200 WHERE userid={message.from_user.id}')
        conn.commit()
        cursor.close()
        return 'Done!'
    else:
        return None

def obond(message):
    cursor = conn.cursor()
    cursor.execute(f'SELECT bon FROM users WHERE userid = {message.from_user.id}')
    bbon = cursor.fetchone()
    bbon = bbon[0]
    if bbon == 0:
        cursor.execute(f'UPDATE users SET bon = 1 WHERE userid = {message.from_user.id}')
        cursor.execute(f'UPDATE users SET rub = rub + 250 WHERE userid = {message.from_user.id}')
        conn.commit()
        cursor.close()
        return 'Done!'
    else:
        return None