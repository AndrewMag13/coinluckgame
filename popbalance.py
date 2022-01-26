from former import former
import hashlib
from postgresso import *
from glQiwiApi import QiwiWrapper, types as qiwi_types


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

'''
def popbal3(message):
    pop = message.text.split()
    pop = pop[0]
    print(message.text)
    try:
        pop = int(pop)
        if pop >= 50:
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


async def popbal3(message):
    pop = await message.text.split()
    pop = pop[0]
    print(message.text)
    try:
        pop = int(pop)
        if pop >= 50:
            bill = await create_payment(pop)
            return bill.pay_url, bill
        else:
            return None
    except ValueError:
        return None
    except TypeError:
        return None
    
async def create_payment(pop) -> qiwi_types.Bill:
    async with wallet:
        return await wallet.create_p2p_bill(amount=pop)

'''