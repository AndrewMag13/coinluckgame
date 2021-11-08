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
def referals(message):
    cursor = conn.cursor()
    cursor.execute(f"SELECT refco FROM users WHERE userid = {message.from_user.id}")
    refff = cursor.fetchone()
    cursor.close()
    refff = refff[0]
    return refff