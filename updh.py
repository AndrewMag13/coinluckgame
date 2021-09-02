import psycopg2
from psycopg2 import Error
import time
import datetime
import random
try:
    conn = psycopg2.connect(user="postgres",
                                    password="iwasbornfree",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="luck")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
def upd():
    while True:
        now = datetime.datetime.now()
        print(now.second)
        if now.minute%10 == 0 and now.second%5 == 0:
            ss()
        time.sleep(1)
def ss():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    table = cursor.fetchall()
    for i in table:
        cursor = conn.cursor()
        rendy = random.randint(97, 105)
        print(rendy)
        cursor.execute(f'UPDATE users SET course = {rendy}')
    conn.commit()
    cursor.close()
upd()