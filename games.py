import psycopg2
from psycopg2 import Error
from former import former
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
    cursor.execute(f'UPDATE users SET cc = 666 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()


def ot11(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 666220 WHERE userid = {message.from_user.id}')
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
                        return 'transerr'
    except Error:
        return 'wrongent'

def oirm(message):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE games SET oirt = '{message.text}' WHERE userid = {message.from_user.id}")
    cursor.execute(f'UPDATE users SET cc = 667 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()

def oirm2(message):
    try:
                    lis = message.text.split()
                    if len(lis) == 2:
                        rubb = message.text
                        rubb = rubb[:-2]
                    if len(lis) == 1:
                        rubb = message.text
                    if message.text == 'Повторить':
                        cursor = conn.cursor()
                        cursor.execute(f'SELECT oirv FROM games WHERE userid = {message.from_user.id}')
                        rubb = cursor.fetchone()
                        rubb = rubb[0]
                        cursor.close
                    rubb = int(rubb)
                    if rubb > 10000 or rubb < 10:
                        return 'Norms'
                    else:
                        cursor = conn.cursor()
                        if message.text == 'Повторить':
                            cursor.execute(f'SELECT oirt FROM games WHERE userid = {message.from_user.id}')
                            oirnum = cursor.fetchone()
                            oirnum = oirnum[0]
                        else:
                            cursor.execute(f'UPDATE games SET oirv = {rubb} WHERE userid = {message.from_user.id}')
                            cursor.execute(f'SELECT oirt FROM games WHERE userid = {message.from_user.id}')
                            oirnum = cursor.fetchone()
                            oirnum = oirnum[0]
                        cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
                        money = cursor.fetchone()
                        money = money[0]
                        if money >= rubb and money >= 10:
                            cursor.execute(f"UPDATE users SET rub = rub - {rubb} WHERE userid = {message.from_user.id}")
                            money = money - rubb
                            z = random.randint(1,101)
                            if oirnum == 'Решка':
                                if z <= 48:
                                    won = rubb * 2
                                    cursor.execute(f"UPDATE users SET rub = rub + {won} WHERE userid = {message.from_user.id}")
                                    conn.commit()
                                    won = former(won)
                                    wiin = f'Поздравляем!👏 \nВаш выйгрыш: {won} 💲'
                                    paph = 'resh.png'
                                elif z >= 53:
                                    won = 0
                                    wiin = 'Орел! \nВы проиграли'
                                    paph = 'orel.jpg'
                                else:
                                    won = 0
                                    wiin = 'Ребро! \nВы проиграли'
                                    paph = 'reb.jpg'
                            elif oirnum == 'Орел':
                                if z <= 48:
                                    won = rubb * 2
                                    cursor.execute(f"UPDATE users SET rub = rub + {won} WHERE userid = {message.from_user.id}")
                                    conn.commit()
                                    won = former(won)
                                    wiin = f'Поздравляем!👏 \nВаш выйгрыш: {won} 💲'
                                    paph = 'orel.jpg'
                                elif z >= 53:
                                    won = 0
                                    wiin = 'Решка! \nВы проиграли'
                                    paph = 'resh.png'
                                else:
                                    won = 0
                                    wiin = 'Ребро! \nВы проиграли'
                                    paph = 'reb.jpg'
                            elif oirnum == 'Ребро':
                                if z <= 50:
                                    won = 0
                                    wiin = 'Орел! \nВы проиграли'
                                    paph = 'orel.jpg'
                                elif z >= 54:
                                    won = 0
                                    wiin = 'Решка! \nВы проиграли'
                                    paph = 'resh.png'
                                else:
                                    won = rubb * 25
                                    cursor.execute(f"UPDATE users SET rub = rub + {won} WHERE userid = {message.from_user.id}")
                                    conn.commit()
                                    won = former(won)
                                    wiin = f'Поздравляем!👏 \nВаш выйгрыш: {won} 💲'
                                    paph = 'reb.jpg'
                            else:
                                pass
                            cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
                            money = cursor.fetchone()
                            money = money[0]
                            cursor.close()
                            rubb = former(rubb)
                            money = former(money)
                            return wiin, money, rubb, paph
                        else:
                            return 'NEM'
    except ValueError:
        return 'Wrongent'
    except TypeError:
        return 'Wrongent'