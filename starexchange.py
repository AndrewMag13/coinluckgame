from former import former
import psycopg2
from psycopg2 import Error
import logging
try:
    conn = psycopg2.connect(user="postgres",
                                password="iwasbornfree",
                                host="127.0.0.1",
                                port="5432",
                                database="luck")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
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
            print(vivc)
            vivc = int(vivc)
            rubs = rubs - vivc
            plod = plod % course
            plods = plods - plod
            print(rubs)
            print(plod)
            print(plods)
            print(course)
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