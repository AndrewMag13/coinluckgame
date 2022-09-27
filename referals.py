from postgresso import *
def referals(message):
    cursor = conn.cursor()
    cursor.execute(f"SELECT refco FROM users WHERE userid = {message.from_user.id}")
    refff = cursor.fetchone()
    cursor.close()
    refff = refff[0]
    return refff