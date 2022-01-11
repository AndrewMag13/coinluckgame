from selec import selec
from postgresso import *

def mainnn(message):
    cursor = conn.cursor()
    if selec(message) == 99990:
        cursor.execute(f"UPDATE users SET lang = '{message.text}' WHERE userid = {message.from_user.id}")
    cursor.execute(f'UPDATE users SET cc = 0 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()