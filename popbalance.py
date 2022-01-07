from former import former
import hashlib
import psycopg2
from psycopg2 import Error

try:
    conn = psycopg2.connect(user="postgres",
                            password="iwasbornfree",
                            host="127.0.0.1",
                            port="5432",
                            database="luck")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
except (Exception, Error) as error:
    print("connError", error)

secret='gQj%Kgg17R&pWi%'
merchant_id='9519'

def popbal1(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 6886 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
    money = cursor.fetchone()
    money = money[0]
    cursor.execute(f"SELECT vivc FROM users WHERE userid = {message.from_user.id}")
    vivc = cursor.fetchone()
    cursor.close()
    vivc = vivc[0]
    money = former(money)
    vivc = former(vivc)
    return money, vivc

def popbal2(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 68886 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()

def popbal3(message):
    pop = message.text.split()
    pop = pop[0]
    print(message.text)
    try:
        pop = int(pop)
        if pop >= 150 and pop <= 10000:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO req(userid, mon, app) VALUES({message.from_user.id}, {pop}, 0)")
            conn.commit()
            cursor.close()
            opl = hashlib.md5(f'{merchant_id}:{pop}:{secret}:RUB:{message.from_user.id}'.encode('utf-8')).hexdigest()
            urrl = f'https://pay.freekassa.ru/?m={merchant_id}&oa={pop}&o={message.from_user.id}&s={opl}&currency=RUB'
            return urrl
    except ValueError:
        return None
    except TypeError:
        return None