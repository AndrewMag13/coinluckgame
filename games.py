import psycopg2
from psycopg2 import Error
import random
try:
    conn = psycopg2.connect(user="postgres",
                            password="iwasbornfree",
                            host="127.0.0.1",
                            port="5432",
                            database="luck")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)


def gamesintro(message):
    cursor = conn.cursor()
    cursor.execute(
        f'UPDATE users SET cc = 666 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()


def ot11(message):
    cursor = conn.cursor()
    cursor.execute(
        f'UPDATE users SET cc = 666220 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()


def ot12(message):
    lis = message.text.split()
    if len(lis) == 2:
        rubb = message.text
        rubb = rubb[:-2]
    if len(lis) == 1:
        rubb = message.text
        rubb = int(rubb)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE games SET otv = '{rubb}' WHERE userid = {message.from_user.id}")
    cursor.execute(f'UPDATE users SET cc = 69692 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()

def ot13(message):
    try:
                    if message.text == 'Повторить':
                            cursor = conn.cursor()
                            cursor.execute(f'SELECT otk FROM games WHERE userid = {message.from_user.id}')
                            keff = cursor.fetchone()
                            keff = keff[0]
                            keff = int(keff)
                            cursor.execute(f'SELECT otv FROM games WHERE userid = {message.from_user.id}')
                            stavka = cursor.fetchone()
                            stavka = stavka[0]
                            stavka = int(stavka)
                            cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
                            money = cursor.fetchone()
                            money = money[0]
                            cursor.close()
                    else:
                        try:
                            keff = int(message.text)
                            if keff == 1 or keff == 2 or keff == 3:
                                cursor = conn.cursor()
                                cursor.execute(f"UPDATE games SET otk = '{keff}' WHERE userid = {message.from_user.id}")
                                conn.commit()
                                cursor.execute(f"SELECT otv FROM games WHERE userid = {message.from_user.id}")
                                stavka = cursor.fetchone()
                                stavka = stavka[0]
                                stavka = int(stavka)
                                cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
                                money = cursor.fetchone()
                                money = money[0]
                                money = int(money)
                                print(f'is {stavka}')
                                print(money)
                                cursor.close()
                            else:
                                return 'wrongent'
                        except Error:
                            return 'wrongent'
                    if stavka < 10 and stavka > 10000:
                        return 'normstavka'
                    if money >= stavka and (keff == 1 or keff == 2 or keff == 3) and stavka >= 10 and stavka <= 10000:
                        cursor = conn.cursor()
                        cursor.execute(f'UPDATE users SET rub = rub - {stavka} WHERE userid = {message.from_user.id}')
                        conn.commit()
                        otr = random.randint(1, 100)
                        if otr <= 20:
                            cc = keff
                            win = stavka * 3
                            win = win + stavka
                            cursor.execute(f"UPDATE users SET rub = rub + {win} WHERE userid = {message.from_user.id}")
                            conn.commit()
                            return 'win', stavka, money, keff, cc
                        else:
                            cc = random.randint(1, 3)
                            while cc == keff:
                                cc = random.randint(1, 3)
                            return 'lose', keff, cc
                    else:
                        print(money, stavka, keff)
                        return 'transerr'
    except Error:
        return 'wrongent'