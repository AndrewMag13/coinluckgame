import psycopg2
from psycopg2 import Error
import time
import datetime
import random
import subprocess
import logging
#import logging
#logging.basicConfig(filename="upd.log", level=logging.INFO)
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
        global now
        now = datetime.datetime.now()
        print(now.second)
        if now.second%6 == 0:
            ss()
        elif now.minute%10 == 0 and now.second == 3:
            mm()
        elif now.hour == 1 and now.minute == 1 and now.second == 3:
            hh()
        elif now.hour == 1 and now.minute == 16 and now.second == 3:
            bck()
        time.sleep(1)
def ss():
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM fruits')
        tbl = cursor.fetchall()
        print(tbl)
        for i in tbl:
            print ('userid:', i[1])
            abobus = i[1]
            ssq = i[2] * 0.16
            ssq1 = i[3] * 1
            ssq2 = i[4] * 5.3
            ssq3 = i[5] * 23.3
            ssq4 = i[6] * 133.3
            ssq5 = i[7] * 333.3
            all = ssq + ssq1 + ssq2 + ssq3 + ssq4 + ssq5
            print(all)
            #logging.info(f'userid:{i[1]} {all}')
            cursor.execute(f"UPDATE users SET plod = plod + {ssq} WHERE userid = {abobus}")
            cursor.execute(f"UPDATE users SET plod = plod + {ssq1} WHERE userid = {abobus}")
            cursor.execute(f"UPDATE users SET plod = plod + {ssq2} WHERE userid = {abobus}")
            cursor.execute(f"UPDATE users SET plod = plod + {ssq3} WHERE userid = {abobus}")
            cursor.execute(f"UPDATE users SET plod = plod + {ssq4} WHERE userid = {abobus}")
            cursor.execute(f"UPDATE users SET plod = plod + {ssq5} WHERE userid = {abobus}")
        conn.commit()
        cursor.close()
        print('Готово')
    except conn.Error:
        print('fail')
def mm():
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
def hh():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    table = cursor.fetchall()
    for i in table:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE users SET bond = 0')
        cursor.execute(f'UPDATE users SET waterc = 0')
    conn.commit()
    cursor.close()
def bck():
    subprocess.call(['pg_dump', 'luck', '-f', '/home/nail/oir/pg/bck.dump'])
    print("BACKUP DONE!")
upd()
