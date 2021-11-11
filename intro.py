from kb import kb
import logging
import requests
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

def intro(message):    
        userid = message.from_user.id
        username = message.from_user.username
        cursor = conn.cursor()
        rub = 0
        mesh = 0
        vivc = 0
        plod = 0
        plodd = 0
        ref = 0
        refco = 0
        inp = 0
        outp = 0
        bon = 0
        bond = 0
        course = 0
        cc = 0
        valua = (userid, rub, mesh, vivc, plod, plodd, ref, refco, inp, outp, bon, bond, course, cc)
        try:
            cursor.execute(f"INSERT INTO users(userid, rub, mesh, vivc, plod, plodd, ref, refco, inp, outp, bon, bond, course, cc)VALUES{valua};")
            print('done')
            cursor.execute(f"INSERT INTO fruits(userid, straw, cher, appl, banan, sliv, grape, caram, caramc, pineappl, pineapplc, drag, dragc)VALUES({userid}, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
            cursor.execute(f"INSERT INTO games(userid)VALUES({userid})")
            conn.commit()
        except Error:
            return None
        try:
            cursor.execute("UPDATE users SET rub = rub + 100000 WHERE userid = 1737649749;")
            conn.commit()
        except Error:
            cursor.execute("COMMIT;")
            cursor.execute("UPDATE users SET rub = rub + 100000 WHERE userid = 1737649749;")
            conn.commit()
        if ' ' in message.text:
            reaf = message.text[7:]
            print(reaf)
            try:
                cursor.execute(f"SELECT ref FROM users WHERE userid = {message.from_user.id}")
                reafch = cursor.fetchone()
                reafch = reafch[0]
                if reaf != userid and reafch == 0:
                    cursor.execute(f'UPDATE users SET ref = {reaf} WHERE userid = {userid}')
                    cursor.execute(f'UPDATE users SET refco = refco + 1 WHERE userid = {reaf}')
                    conn.commit()
                    logging.info(f"+ref for {reaf}")
            except Error:
                pass
        r = requests.get('https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id=1737649749&text=+1luder')
        cursor.close()
        logging.info(f"new luder: {userid}")
        return '1'