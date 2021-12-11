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


def selec(message):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT cc FROM users WHERE userid = {message.from_user.id}")
        s = cursor.fetchone()
        cursor.close()
        s = s[0]
        return s
    except Error:
        return False