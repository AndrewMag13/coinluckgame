import subprocess
import requests
from postgresso import *

def temperature():
    temp = subprocess.check_output(['vcgencmd', 'measure_temp'])
    temp = temp.decode()
    return temp
def uptime():
    upt = subprocess.check_output(['uptime'])
    upt = upt.decode()
    return upt
def logger():
    logg = subprocess.check_output(['cat','main.log'])
    logg = logg.decode()
    return logg
def ally(message):
    try:
        meess = message.text.split(' ')
        meess = meess[1:]
        meess = " ".join(meess)
        cursor = conn.cursor()
        cursor.execute('SELECT userid FROM users')
        listin = cursor.fetchall()
        print(listin)
        for i in listin:
            i = i[0]
            print(i)
            r = requests.get(f'https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id={i}&text={meess}')
        return meess
    except Error:
        return None