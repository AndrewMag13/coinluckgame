from former import former
import logging
from postgresso import *

def s2d(message):
        cursor = conn.cursor()
        cursor.execute(f"SELECT course FROM users WHERE userid = {message.from_user.id}")
        course = cursor.fetchone()
        course = course[0]
        cursor.execute(f'SELECT plodd FROM users WHERE userid={message.from_user.id}')
        plodd = cursor.fetchone()
        cursor.close
        plodd = plodd[0]
        if plodd > course:
            cursor = conn.cursor()
            cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
            rubs = cursor.fetchone()
            rubs = rubs[0]
            cursor.execute(f"SELECT plodd FROM users WHERE userid = {message.from_user.id}")
            plod = cursor.fetchone()
            plod = plod[0]
            plod = int(plod)
            plods = int(plod)
            rubs = plod // course
            vivc = rubs / 100 * 30
            vivc = int(vivc)
            rubs = rubs - vivc
            plod = plod % course
            plods = plods - plod
            cursor.execute(f"UPDATE users SET rub = rub + {rubs} WHERE userid = {message.from_user.id}")
            cursor.execute(f"UPDATE users SET plodd = plodd - {plods} WHERE userid = {message.from_user.id}")
            cursor.execute(f"UPDATE users SET vivc = vivc + {vivc} WHERE userid = {message.from_user.id}")
            cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
            rub = cursor.fetchone()
            rub = rub[0]
            conn.commit()
            cursor.close()
            logging.info(f"change {plods} > {rubs} and {vivc} userid: {message.from_user.id}")
            plods = former(plods)
            rubs = former(rubs)
            vivc = former(vivc)
            rub = former(rub)
            return plods, rubs, vivc, rub
        else:
            return None
def v2d(message):
        cursor = conn.cursor()
        cursor.execute(f"SELECT course FROM users WHERE userid = {message.from_user.id}")
        course = cursor.fetchone()
        course = course[0]
        cursor.execute(f'SELECT vivc FROM users WHERE userid={message.from_user.id}')
        vivc = cursor.fetchone()
        cursor.close
        vivc = vivc[0]
        if vivc >= 10:
            cursor = conn.cursor()
            cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
            rubs = cursor.fetchone()
            rubs = rubs[0]
            rubs = int(rubs)
            cursor.execute(f"SELECT vivc FROM users WHERE userid = {message.from_user.id}")
            vivc = cursor.fetchone()
            vivc = vivc[0]
            vivc = int(vivc)
            rubs = vivc * 1.3
            rubs = int(rubs)
            cursor.execute(f"UPDATE users SET rub = rub + {rubs} WHERE userid = {message.from_user.id}")
            cursor.execute(f"UPDATE users SET vivc = 0 WHERE userid = {message.from_user.id}")
            cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
            rub = cursor.fetchone()
            rub = rub[0]
            conn.commit()
            cursor.close()
            logging.info(f"change {vivc} > {rubs} userid: {message.from_user.id}")
            rubs = former(rubs)
            vivc = former(vivc)
            rub = former(rub)
            return rubs, vivc, rub
        else:
            return None
def plodcourse(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 110 WHERE userid = {message.from_user.id}')
    cursor.execute(f"SELECT course FROM users WHERE userid = {message.from_user.id}")
    course = cursor.fetchone()
    course = course[0]
    cursor.execute(f"SELECT plodd FROM users WHERE userid = {message.from_user.id}")
    plod = cursor.fetchone()
    plod = plod[0]
    cursor.close()
    plod = former(plod)
    return plod, course