import time
import datetime
import random
from postgresso import *

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