import sqlite3
from typing import Type
import requests
import random
import hashlib
import subprocess
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

chk = 0

secret='Y[wUkLSn7W,U>wZ'
merchant_id='1159'

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

pho = 'https://imbt.ga/ZFdnBeO4pg'

@dp.message_handler(commands=['start'])
async def welcome(message):
    global userid
    global fname
    userid = message.from_user.id
    username = message.from_user.username
    fname = message.from_user.first_name
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Начать')
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    rub = 0
    mesh = 0
    vivc = 0
    plod = 0
    plodd = 0
    ref = 0
    refc = 0
    inp = 0
    outp = 0
    bon = 0
    bond = 0
    course = 100
    valua = (userid, username, fname, rub, mesh, vivc, plod, plodd, ref, refc, inp, outp, bon, bond, course)
    cursor.execute(f"INSERT OR IGNORE INTO users(userid, username, fname, rub, mesh, vivc, plod, plodd, ref, refco, inp, outp, bon, bond, course)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", valua)
    cursor.execute(f"INSERT OR IGNORE INTO fruits(userid, straw, cher, appl, banan, sliv, grape, caram, caramc, pineappl, pineapplc, drag, dragc)VALUES({userid}, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
    cursor.execute("UPDATE users SET rub = rub + 100000 WHERE userid = 1737649749")
    conn.commit()
    if ' ' in message.text:
        reaf = message.text[-10:]
        reafch = cursor.execute(f"SELECT ref FROM users WHERE userid = {message.from_user.id}")
        reafch = reafch.fetchone()
        reafch = reafch[0]
        print(reaf)
        print(reafch)
        if reaf != userid and reafch == 0:
            cursor.execute(f'UPDATE users SET ref = {reaf} WHERE userid = {userid}')
            cursor.execute(f'UPDATE users SET refco = refco + 1 WHERE userid = {reaf}')
            conn.commit()
    conn.close()
    global chk
    chk = 0
    global rev
    rev = 0
    print(f'+1 wanker {username}')
    r = requests.get('https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id=1737649749&text=+1luder')
    await message.answer(f'*Приветствую {fname}♦* \nЭтот бот представляет собой сборник азартных игр\n\nНажимая кнопку Начать вы принимаете Пользовательское соглашение: telegra.ph/Polzovatelskoe-soglashenie-07-06\nВы также можете бонусный код, если его у вас нет введите BONUS\n\nУдачи!🍀\n{pho}', parse_mode= 'Markdown', reply_markup=keyboard)
@dp.message_handler(lambda message: message.text and '👈' in message.text or 'Начать' in message.text)
async def mainn(message):
    global smm
    global chk
    global rev
    rev = 0
    chk = 0
    smm = 0
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('▶ Играть', '🍓 Ферма', '🔄 Рынок', '💼 Баланс', '⚡ Ежедневный бонус', '💭 Отзывы', '👥 Реферальная система')
    fname = message.from_user.first_name
    await message.answer(f'*Приветствую {fname}♦* \nВы находитесь в главном меню CoinLuck Game\n{pho}', parse_mode= 'Markdown', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and '🔄' in message.text)
async def mart(message):
    global chk
    chk = 110
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Обменять', '👈 Назад')
    global courses
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT course FROM users WHERE userid = {message.from_user.id}")
    course = cursor.fetchone()
    course = course[0]
    courses = course
    cursor.execute(f"SELECT plodd FROM users WHERE userid = {message.from_user.id}")
    plod = cursor.fetchone()
    plod = plod[0]
    plod = int(plod)
    global plodd 
    plodd = plod
    conn.close()
    await message.answer(f'Здесь вы можете обменять ваши 🌟 на 💲 \nУ вас {plod} 🌟\n\nТекущий курс: \n 1 🔄 = {course} 🌟\n С каждого перевода вы получите 70% 💲 и 30% 💸', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and 'Обменять' in message.text and chk == 110)
async def mart1(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('👈 Назад')
    if plodd > courses:
        conn = sqlite3.connect("/home/nail/oir/luck.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
        rubs = cursor.fetchone()
        rubs = rubs[0]
        cursor.execute(f"SELECT plodd FROM users WHERE userid = {message.from_user.id}")
        plod = cursor.fetchone()
        plod = plod[0]
        plod = int(plod)
        plods = int(plod)
        rubs = plod // courses
        vivc = rubs / 100 * 30
        print(vivc)
        vivc = int(vivc)
        rubs = rubs - vivc
        plod = plod % courses
        plods = plods - plod
        print(rubs)
        print(plod)
        print(plods)
        print(courses)
        cursor.execute(f"UPDATE users SET rub = rub + {rubs} WHERE userid = {message.from_user.id}")
        cursor.execute(f"UPDATE users SET plodd = plodd - {plods} WHERE userid = {message.from_user.id}")
        cursor.execute(f"UPDATE users SET vivc = vivc + {vivc} WHERE userid = {message.from_user.id}")
        cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
        rub = cursor.fetchone()
        rub = rub[0]
        conn.commit()
        conn.close()
        await message.answer(f'Готово! \n\nВы обменяли {plods} 🌟 на {rubs} 💲 и на {vivc} 💸\n\nУ вас на балансе: {rub} 💲 ', reply_markup=keyboard)
    else:
        await message.answer(f'Недостаточно 🌟 для обмена', reply_markup=keyboard)
@dp.message_handler(lambda message: message.text and '▶' in message.text)
async def games(message):
    global smm
    smm = 1
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Орел и Решка', '👈 Назад')
    await message.answer('Выберите игру', reply_markup=keyboard, parse_mode= 'Markdown')

@dp.message_handler(lambda message: message.text and 'Орел и Решка' in message.text)
async def oir1(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Орел', 'Решка', 'Ребро', '👈 Назад')
    await message.answer('*Выберите сторону*\n\nКоэффиценты для сторон:\n\n*Орел/Решка* - 2x \n*Ребро* - 25x', reply_markup=keyboard, parse_mode= 'Markdown')
@dp.message_handler(lambda message: message.text and 'Орел' in message.text or 'Решка' in message.text or 'Ребро' in message.text and smm==1)
async def oir2(message):
    global chk
    chk = 1
    global oirnum
    oirnum = message.text
    print(oirnum)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('10 💲', '50 💲', '100 💲', '250 💲', '500 💲', '750 💲','1000 💲','1250 💲','1500 💲','👈 Назад')
    await message.answer('Делайте ставку \n\nСтавка должна быть от *10* до *10000* \nВы также можете ввести свою сумму введя ее в ответном сообщении', reply_markup=keyboard, parse_mode= 'Markdown')
@dp.message_handler(lambda message: message.text and chk == 1)
async def oir3(message):
    try:
        rubb = message.text
        rubb = rubb[:-2]
        rubb= int(rubb)
        if rubb > 10000 or rubb < 10:
            await message.answer('Ставка должна быть от *10* до *10000*', parse_mode= 'Markdown')
        else:
            print(rubb)
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add('10 💲', '50 💲', '100 💲', '250 💲', '500 💲', '750 💲','1000 💲','1250 💲','1500 💲','👈 Назад')
            conn = sqlite3.connect("/home/nail/oir/luck.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
            money = cursor.fetchone()
            money = money[0]
            if money >= rubb and money >= 10:
                cursor.execute(f"UPDATE users SET rub = rub - {rubb} WHERE {message.from_user.id}")
                money = money - rubb
                z = random.randint(1,101)
                if oirnum == 'Решка':
                    if z <= 48:
                        print('YES РЕШКА')
                        won = rubb * 2
                        wiin = f'Поздравляем!👏 \nВаш выйгрыш: {won} 💲'
                        paph = 'resh.png'
                    elif z >= 53:
                        won = 0
                        print('NO ОРЕЛ')
                        wiin = 'Орел! \nВы проиграли'
                        paph = 'orel.jpg'
                    else:
                        won = 0
                        print('РЕБРО')
                        wiin = 'Ребро! \nВы проиграли'
                        paph = 'reb.jpg'
                elif oirnum == 'Орел':
                    if z <= 48:
                        print('YES ОРЕЛ')
                        won = rubb * 2
                        wiin = f'Поздравляем!👏 \nВаш выйгрыш: {won} 💲'
                        print(rubb)
                        paph = 'orel.jpg'
                    elif z >= 53:
                        won = 0
                        print('NO РЕШКА')
                        wiin = 'Решка! \nВы проиграли'
                        paph = 'resh.png'
                    else:
                        won = 0
                        print('РЕБРО')
                        wiin = 'Ребро! \nВы проиграли'
                        paph = 'reb.jpg'
                elif oirnum == 'Ребро':
                    if z <= 50:
                        won = 0
                        print('NO ОРЕЛ')
                        wiin = 'Орел! \nВы проиграли'
                        paph = 'orel.jpg'
                    elif z >= 54:
                        won = 0
                        print('NO РЕШКА')
                        wiin = 'Решка! \nВы проиграли'
                        paph = 'resh.png'
                    else:
                        print('РЕБРО')
                        won = rubb * 25
                        wiin = f'Поздравляем!👏 \nВаш выйгрыш: {won} 💲'
                        print(rubb)
                        paph = 'reb.jpg'
                else:
                    pass
                with open(paph,'rb') as photo:
                    await message.reply_photo(photo, reply_markup=keyboard)
                cursor.execute(f"UPDATE users SET rub = rub + {won} WHERE userid = {message.from_user.id}")
                conn.commit()
                cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
                money = cursor.fetchone()
                money = money[0]
                await message.answer(f'{wiin} \n\nВаш текущий баланс - *{money} 💲*\nВаша ставка: {rubb} 💲', reply_markup=keyboard, parse_mode= 'Markdown')
            else:
                await message.answer(f'Недостаточно средств на балансе', reply_markup=keyboard)
    except ValueError:
        await message.answer('Неверно введено число')
    except TypeError:
        await message.answer('Неверно введено число')

#

@dp.message_handler(lambda message: message.text and '💼' in message.text)
async def balance(message):
    global chk
    chk = 2
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('⬇ Пополнить баланс', '⬆ Вывести', '👈 Назад')
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
    money = cursor.fetchone()
    money = money[0]
    cursor.execute(f"SELECT vivc FROM users WHERE userid = {message.from_user.id}")
    vivc = cursor.fetchone()
    conn.close()
    vivc = vivc[0]
    await message.answer(f'Здесь вы можете пополнить или вывести ваш баланс\n\nВаш баланс для покупок: *{money} 💲*\nВаш баланс для вывода: {vivc} 💸', parse_mode= 'Markdown', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and '⬇' in message.text)
async def popbalance(message):
    global chk
    chk = 2
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('80', '100', '500','👈 Назад')
    await message.answer('Введите сумму пополнения вашего счета (минимальная сумма пополнения - 80 рублей)\n\nКурс:\n1 рубль = 100 💲\nПри пополнении 25% от суммы вашего пополнения станут 💵', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and isint(message.text) and chk == 2)
async def popbalance1(message):
    pop = message.text
    print(message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('👈 Назад')
    try:
        pop = int(pop)
        if pop > 80 and pop < 10000:
            conn = sqlite3.connect("/home/nail/oir/luck.db")
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO req(userid, mon, app) VALUES({message.from_user.id}, {pop}, 0)")
            conn.commit()
            conn.close()
            opl = hashlib.md5(f'{merchant_id}:{pop}:{secret}:RUB:{message.from_user.id}'.encode('utf-8')).hexdigest()
            print(opl)
            urrl = f'https://pay.freekassa.ru/?m={merchant_id}&oa={pop}&o={message.from_user.id}&s={opl}&currency=RUB'
            markup = types.InlineKeyboardMarkup()
            btn_my_site= types.InlineKeyboardButton(text='Оплатить', url=urrl)
            markup.add(btn_my_site)
            #payment_link = requests.get(f'https://clck.ru/--?url={urrl}')
            await message.answer(f'Ваша ссылка для пополнения', reply_markup = markup)
    except ValueError:
        await message.answer('Неверно введена сумма!', reply_markup=keyboard)
    except TypeError:
        await message.answer('Неверно введена сумма!', reply_markup=keyboard)
@dp.message_handler(lambda message: message.text and '⬆' in message.text)
async def vivbalance(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('50', '100', '500','👈 Назад')
    await message.answer('Введите сумму', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and '🍓 ' in message.text)
async def farm(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('💲 Купить растения', '🍒 Мои растения', '✂ Собрать', '👈 Назад')
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    plod = cursor.execute(f'SELECT plod FROM users WHERE userid={message.from_user.id}')
    plod = plod.fetchone()
    plod = plod[0]
    cursor.execute(f'SELECT * FROM fruits WHERE userid={message.from_user.id}')
    i = cursor.fetchone()
    conn.close()
    ssq = i[2] * 100
    ssq1 = i[3] * 600
    ssq2 = i[4] * 3200
    ssq3 = i[5] * 14000
    ssq4 = i[6] * 80000
    ssq5 = i[7] * 200000
    all = ssq + ssq1 + ssq2 + ssq3 + ssq4 + ssq5
    print(all)
    await message.answer(f'Это ваша небольшая горная ферма на севере Калифорнии у необычайно красивого берега \nЗдесь вы можете купить еще фруктовых растений или собрать спелые плоды \n\nУ вас на ферме {int(plod)} 🌟\n\n В час вы зарабатываете {all} 🌟', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and '✂ ' in message.text)
async def ctch(message):
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    plod = cursor.execute(f'SELECT plod FROM users WHERE userid={message.from_user.id}')
    plod = plod.fetchone()
    plod = plod[0]
    plod = int(plod)
    cursor.execute(f'UPDATE users SET plod = plod - {plod} WHERE userid={message.from_user.id}')
    cursor.execute(f'UPDATE users SET plodd = plodd + {plod} WHERE userid={message.from_user.id}')
    conn.commit()
    conn.close()
    await message.answer(f'Готово вы собрали {plod} 🌟!')

@dp.message_handler(lambda message: message.text and '🍒 ' in message.text)
async def myfarm(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('👈 Назад')
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    myplod = cursor.execute(f'SELECT * FROM fruits WHERE userid={message.from_user.id}')
    myplod = myplod.fetchone()
    conn.close()
    await message.answer(f'У вас: \n\n{myplod[2]} грядок клубники 🍓\n\n{myplod[3]} вишневых деревьев 🍒\n\n{myplod[4]} яблочных деревьев 🍎\n\n{myplod[5]} банановых деревьев 🍌\n\n{myplod[6]} персиковых деревьев 🍑\n\n{myplod[7]} виноградных деревьев 🍇', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and '💲 ' in message.text)
async def buyfarm(message):
    global chk
    chk = 5
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
    money = cursor.fetchone()
    conn.close()
    money = money[0]
    keyboard.add('Купить 🍓','Купить 🍒','Купить 🍎','Купить 🍌','Купить 🍑','Купить 🍇','👈 Назад')
    await message.answer(f'Здесь вы можете купить растения на вашу ферму: \n\n🍓 - 1.000 💲\nПриносит 100 🌟 в час\n\n🍒 - 5.000 💲\nПриносит 600 🌟 в час\n\n🍎 - 25.000 💲\nПриносит 3.200 🌟 в час\n\n🍌 - 100.000 💲\nПриносит 14.000 🌟 в час\n\n🍑 - 500.000 💲\nПриносит 80.000 🌟 в час\n\n🍇 - 1.000.000 💲\nПриносит 20.0000 🌟 в час \n\nУ вас на балансе: {money} 💲', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and '✨ ' in message.text)
async def buyvipfarm(message):
    global chk
    chk = 6
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Купить VIP🍍','Купить VIP🐉','Купить VIP⭐','👈 Назад')
    await message.answer('магаз', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and 'Купить VIP' in message.text and chk == 6)
async def buyvipfarm1(message):
    fruit = message.text[-1]
    if fruit == "🍍":
        fruitm = 99
    elif fruit == "🐉":
        fruitm = 299
    elif fruit == "⭐":
        fruitm = 499
    else:
        await message.answer('Не могу тебя понять')
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO req(userid, mon, app) VALUES({message.from_user.id}, {fruitm}, 0)")
    conn.commit()
    conn.close()
    opl = hashlib.md5(f'{merchant_id}:{fruitm}:{secret}:RUB:{message.from_user.id}'.encode('utf-8')).hexdigest()
    print(opl)
    urrl = f'https://pay.freekassa.ru/?m={merchant_id}&oa={fruitm}&o={message.from_user.id}&s={opl}&currency=RUB&us_key={fruitm}'
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Оплатить', url=urrl)
    markup.add(btn_my_site)
    await message.answer(f'Ваша ссылка для покупки', reply_markup = markup)
@dp.message_handler(lambda message: message.text and 'Купить ' in message.text and chk == 5)
async def buyfarm1(message):
    fruit = message.text[-1]
    print(fruit)
    if fruit == "🍓":
        fruitm = 1000
        nn = 'straw'
    elif fruit == "🍒":
        fruitm = 5000
        nn = 'cher'
    elif fruit == "🍎":
        fruitm = 25000
        nn = 'appl'
    elif fruit == "🍌":
        fruitm = 100000
        nn = 'banan'
    elif fruit == "🍑":
        fruitm = 500000
        nn = 'sliv'
    elif fruit == "🍇":
        fruitm = 1000000
        nn = 'grape'
    else:
        await message.answer('Не могу тебя понять')
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
    money = cursor.fetchone()
    money = money[0]
    if money >= fruitm:
        cursor.execute(f"UPDATE users SET rub = rub - {fruitm} WHERE userid = {message.from_user.id}")
        cursor.execute(f"UPDATE fruits SET {nn} = {nn} + 1 WHERE userid = {message.from_user.id}")
        conn.commit()
        await message.answer('Успешно!')
    else:
        await message.answer('Недостаточно средств')

@dp.message_handler(lambda message: message.text and '💭' in message.text)
async def review(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Написать', 'Прочитать','👈 Назад')
    await message.answer('Здесь вы можете прочитать или написать отзывы', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and 'Написать' in message.text)
async def review1(message):
    global rev
    rev = 1
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('👈 Назад')
    await message.answer('В ответном сообщении вы можете оставить отзыв, за каждый качественный отзыв вы получите 50💲', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and ' ' in message.text and rev == 1)
async def review2(message):
    r = requests.get(f'https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id=1737649749&text={message.text}{message.from_user.id}')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('👈 Назад')
    await message.answer('Принято!', reply_markup=keyboard)
@dp.message_handler(lambda message: message.text and 'BONUS' in message.text)
async def bonus(message):
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    bbon = cursor.execute(f'SELECT bon FROM users WHERE userid = {message.from_user.id}')
    bbon = bbon.fetchone()
    bbon = bbon[0]
    print(bbon)
    if bbon == 0:
        cursor.execute(f'UPDATE users SET bon = 1 WHERE userid = {message.from_user.id}')
        cursor.execute(f'UPDATE users SET rub = rub + 250 WHERE userid = {message.from_user.id}')
        conn.commit()
        await message.answer('Поздравляем!👏 Ваш бонус: 250 💲')
    else:
        await message.answer('Вы уже использовали ваш бонус!')

@dp.message_handler(lambda message: message.text and '⚡ ' in message.text)
async def bond(message):
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    bbond = cursor.execute(f'SELECT bond FROM users WHERE userid = {message.from_user.id}')
    bbond = bbond.fetchone()
    bbond= bbond[0]
    if bbond == 0:
        cursor.execute(f'UPDATE users SET bond = 1 WHERE userid={message.from_user.id}')
        cursor.execute(f'UPDATE users SET rub = rub + 200 WHERE userid={message.from_user.id}')
        conn.commit()
        await message.answer('Отлично!👏 Вы получили ваш ежедневный бонус на сумму 200 💲')
    else:
        await message.answer('Бонус доступен только раз в день!')

@dp.message_handler(lambda message: message.text and '👥 ' in message.text)
async def ref(message):
    reff = message.from_user.id
    await message.answer(f'Ваша реферальная ссылка: \nt.me/coinluck_bot?start={reff} \nЗа каждого приглашенного реферала вы получите 3% от суммы пополнения его баланса и 1% от суммы пополнения реферала вашего реферала.')

@dp.message_handler(lambda message: message.text and 'temp' in message.text and message.from_user.id == 1737649749)
async def temp(message):
    temp = subprocess.check_output(['vcgencmd', 'measure_temp'])
    await message.answer(f'{temp}')
@dp.message_handler(lambda message: message.text and 'uptime' in message.text and message.from_user.id == 1737649749)
async def upt(message):
    upt = subprocess.check_output(['uptime'])
    await message.answer(f'{upt}')

if __name__ == '__main__':
    executor.start_polling(dp)
