from postgresso import *

def topup(message, am, cu):
    cursor = conn.cursor()
    am = int(am)
    if cu == 'RUB':
        cursor.execute(f'UPDATE users SET rub = rub + {am * 100} WHERE userid = {message.from_user.id}')
    elif cu == 'USD':
        cursor.execute(f'UPDATE users SET rub = rub + {am * 100 * 80} WHERE userid = {message.from_user.id}')
    conn.commit()