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

def langich(message):
    cursor = conn.cursor()
    cursor.execute(f"SELECT lang FROM users WHERE userid = {message.from_user.id}")
    slang = cursor.fetchone()
    slang = slang[0]
    cursor.close()
    return slang