from postgresso import *

def langich(message):
    cursor = conn.cursor()
    cursor.execute(f"SELECT lang FROM users WHERE userid = {message.from_user.id}")
    slang = cursor.fetchone()
    slang = slang[0]
    cursor.close()
    return slang