import logging
import requests
from postgresso import *

logging.basicConfig(filename="intro.log", level=logging.WARNING)

def intro(message):
        cursor = conn.cursor()
        try:
            cursor.execute(f"INSERT INTO users(userid, rub, mesh, vivc, plod, plodd, ref, refco, inp, outp, bon, bond, course, cc, waterc)VALUES({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1);")
            cursor.execute(f"INSERT INTO fruits(userid, straw, cher, appl, banan, sliv, grape, caram, caramc, pineappl, pineapplc, drag, dragc, waterx)VALUES({message.from_user.id}, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)")
            cursor.execute(f"INSERT INTO games(userid)VALUES({message.from_user.id})")
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
            try:
                cursor.execute(f"SELECT ref FROM users WHERE userid = {message.from_user.id}")
                reafch = cursor.fetchone()
                reafch = reafch[0]
                if reaf != message.from_user.id and reafch == 0:
                    cursor.execute(f'UPDATE users SET ref = {reaf} WHERE userid = {message.from_user.id}')
                    cursor.execute(f'UPDATE users SET refco = refco + 1 WHERE userid = {reaf}')
                    conn.commit()
                    logging.info(f"+ref for {reaf}")
            except Error:
                pass
        cursor.execute(f'UPDATE users SET cc = 99990 WHERE userid = {message.from_user.id}')
        conn.commit()
        r = requests.get('https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id=1737649749&text=+1luder')
        cursor.close()
        logging.info(f"new luder: {message.from_user.id}")
        return '1'