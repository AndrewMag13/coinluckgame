from postgresso import *

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