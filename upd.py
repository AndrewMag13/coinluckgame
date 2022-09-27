import time
import datetime
import random
import subprocess
from postgresso import *

def upd():
    while True:
        global now
        now = datetime.datetime.now()
        if now.second%6 == 0:
            ss()
        if now.minute%10 == 0 and now.second == 3:
            mm()
        if now.hour == 7 and now.minute == 6 and now.second == 3:
            hh()
        if now.hour == 7 and now.minute == 16 and now.second == 3:
            bck()
        if now.minute == 0 and now.second == 1:
            wat()
        time.sleep(1)
def ss():
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM fruits')
        tbl = cursor.fetchall()
        for i in tbl:
            print ('userid:', i[1])
            abobus = i[1]
            ssq = i[2] * 0.16
            ssq1 = i[3] * 1
            ssq2 = i[4] * 5.3
            ssq3 = i[5] * 23.3
            ssq4 = i[6] * 133.3
            ssq5 = i[7] * 333.3
            ww = i[14]
            all = (ssq + ssq1 + ssq2 + ssq3 + ssq4 + ssq5) * ww
            cursor.execute(f"UPDATE users SET plod = plod + {all} WHERE userid = {abobus}")
        conn.commit()
        cursor.close()
    except conn.Error:
        pass
def mm():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    table = cursor.fetchall()
    for i in table:
        cursor = conn.cursor()
        rendy = random.randint(97, 105)
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
        cursor.execute(f'UPDATE users SET waterc = 1')
    conn.commit()
    cursor.close()
def bck():
    subprocess.call(['pg_dump', 'luck', '-f', '/home/nail/oir/pg/bck.dump'])
    print("BACKUP DONE!")

def wat():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM fruits')
    table = cursor.fetchall()
    for i in table:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE fruits SET waterx = 1')
    conn.commit()
    cursor.close()
upd()
