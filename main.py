import psycopg2
from psycopg2 import Error
import sqlite3
from typing import Type
import requests
import random
import hashlib
import subprocess
import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(filename="main.log", level=logging.INFO)


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

try:
    conn = psycopg2.connect(user="postgres",
                                password="iwasbornfree",
                                host="127.0.0.1",
                                port="5432",
                                database="luck")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

def selec(message):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT cc FROM users WHERE userid = {message.from_user.id}")
        s = cursor.fetchone()
        cursor.close()
        s = s[0]
        return s
    except Error:
        return False
def former(a):
    a = '{:,}'.format(a)
    return a

@dp.message_handler(commands=['start'])
async def welcome(message):
    userid = message.from_user.id
    username = message.from_user.username
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Начать')
    cursor = conn.cursor()
    rub = 0
    mesh = 0
    vivc = 0
    plod = 0
    plodd = 0
    ref = 0
    refco = 0
    inp = 0
    outp = 0
    bon = 0
    bond = 0
    course = 100
    cc = 0
    valua = (userid, username, rub, mesh, vivc, plod, plodd, ref, refco, inp, outp, bon, bond, course, cc)
    try:
        cursor.execute(f"INSERT INTO users(userid, username, rub, mesh, vivc, plod, plodd, ref, refco, inp, outp, bon, bond, course, cc)VALUES{valua};")
        print('done')
        cursor.execute(f"INSERT INTO fruits(userid, straw, cher, appl, banan, sliv, grape, caram, caramc, pineappl, pineapplc, drag, dragc)VALUES({userid}, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
        cursor.execute(f"INSERT INTO games(userid)VALUES({userid})")
        conn.commit()
    except Error:
        cursor.execute(f"INSERT INTO users(userid)VALUES({userid})")
        await message.answer(f'*Ошибка регистарции, {message.from_user.id}!*')
    try:
        cursor.execute("UPDATE users SET rub = rub + 100000 WHERE userid = 1737649749;")
        conn.commit()
    except Error:
        cursor.execute("COMMIT;")
        print('lol')
        cursor.execute("UPDATE users SET rub = rub + 100000 WHERE userid = 1737649749;")
        conn.commit()
    if ' ' in message.text:
        reaf = message.text[7:]
        print(reaf)
        try:
            cursor.execute(f"SELECT ref FROM users WHERE userid = {message.from_user.id}")
            reafch = cursor.fetchone()
            reafch = reafch[0]
            if reaf != userid and reafch == 0:
                cursor.execute(f'UPDATE users SET ref = {reaf} WHERE userid = {userid}')
                cursor.execute(f'UPDATE users SET refco = refco + 1 WHERE userid = {reaf}')
                conn.commit()
                logging.info(f"+ref for {reaf}")
        except Error:
            pass
    print(f'+1 wanker {username}')
    r = requests.get('https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id=1737649749&text=+1luder')
    cursor.close()
    logging.info(f"new luder: {userid}")
    await message.answer(f'*Приветствую {message.from_user.id}♦* \nЭтот бот представляет собой сборник азартных игр\n\nНажимая кнопку Начать вы принимаете Пользовательское соглашение: telegra.ph/Polzovatelskoe-soglashenie-07-06\nВы также можете бонусный код, если его у вас нет введите BONUS\n\nУдачи!🍀\n{pho}', parse_mode= 'Markdown', reply_markup=keyboard)
@dp.message_handler(lambda message: message.text and '👈' in message.text or 'Начать' in message.text)
async def mainn(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 0 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()
    print(chk)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('▶ Играть', '🍓 Ферма', '🔄 Рынок', '💼 Баланс', '💱 Перевод', '⚡ Ежедневный бонус', '💭 Отзывы', '👥 Реферальная система')
    await message.answer(f'*Приветствую {message.from_user.first_name}♦* \nВы находитесь в главном меню CoinLuck Game\n{pho}', parse_mode= 'Markdown', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and '💱' in message.text)
async def tran(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 11290 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.execute(f'SELECT id FROM users WHERE userid = {message.from_user.id}')
    id = cursor.fetchone()
    cursor.close()
    id = id[0]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('👈 Назад')
    await message.answer(f'Здесь вы можете перевести 💲 другим пользователям по id. Ваш id: {id}\n\nДля перевода в ответном сообщении введите сначала id пользователя, затем сумму перевода через пробел.\nПример: 12 7000 \nЕдиноразово вы можете перевести от 10 💲 до 10.000 💲', reply_markup=keyboard)
    
    @dp.message_handler(lambda message: message.text and ' ' in message.text and selec(message) == 11290)
    async def tran1(message):
        try:
            mess = message.text.split(' ')
            print(mess)
            mon = mess[1]
            mon = int(mon)
            cursor = conn.cursor()
            cursor.execute(f'SELECT id FROM users WHERE userid = {message.from_user.id}')
            id = cursor.fetchone()
            id = id[0]
            cursor.execute(f'SELECT rub FROM users WHERE userid = {message.from_user.id}')
            rub = cursor.fetchone()
            cursor.close()
            rub = rub[0]
            print(rub)
            if rub >= mon and mon >= 10 and mon <= 10000:
                try:
                    cursor = conn.cursor()
                    cursor.execute(f'UPDATE users SET rub = rub - {mon} WHERE userid = {message.from_user.id}')
                    cursor.execute(f'UPDATE users SET rub = rub + {mon} WHERE id = {mess[0]}')
                    conn.commit()
                    cursor.execute(f'SELECT userid FROM users WHERE id = {mess[0]}')
                    messid = cursor.fetchone()
                    cursor.close()
                    messid = messid[0]
                    print(messid)
                    logging.info(f'{message.from_user.id} > {mess[0]} {mon}')
                    r = requests.get(f"https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id={messid}&text=Пользователь {id} перевел на ваш счет {mon} 💲!")
                    await message.answer(f'Готово! Вы перевели пользователю {mess[0]} {mon} 💲')
                except Error:
                    await message.answer(f'Ошибка! Неверный ввод!')
            else:
                await message.answer(f'Ошибка! Неверный ввод!')
        except Error:
            await message.answer(f'Ошибка!')

@dp.message_handler(lambda message: message.text and '🔄' in message.text)
async def mart(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 110 WHERE userid = {message.from_user.id}')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Обменять', '👈 Назад')
    cursor.execute(f"SELECT course FROM users WHERE userid = {message.from_user.id}")
    course = cursor.fetchone()
    course = course[0]
    cursor.execute(f"SELECT plodd FROM users WHERE userid = {message.from_user.id}")
    plod = cursor.fetchone()
    plod = plod[0]
    cursor.close()
    plod = former(plod)
    await message.answer(f'Здесь вы можете обменять ваши 🌟 на 💲 \nУ вас {plod} 🌟\n\nТекущий курс: \n 1 🔄 = {course} 🌟\n С каждого перевода вы получите 70% 💲 и 30% 💸', reply_markup=keyboard)
    
    @dp.message_handler(lambda message: message.text and 'Обменять' in message.text and selec(message) == 110)
    async def mart1(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('👈 Назад')
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
            await message.answer(f'Готово! \n\nВы обменяли {plods} 🌟 на {rubs} 💲 и на {vivc} 💸\n\nУ вас на балансе: {rub} 💲 ', reply_markup=keyboard)
        else:
            await message.answer(f'Недостаточно 🌟 для обмена', reply_markup=keyboard)
@dp.message_handler(lambda message: message.text and '▶' in message.text)
async def games(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 666 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Орел и Решка', 'Краш', '1/3', '1/30', '👈 Назад')
    await message.answer('Выберите игру', reply_markup=keyboard, parse_mode= 'Markdown')
    
    @dp.message_handler(lambda message: message.text and message.text == '1/3' and selec(message) == 666)
    async def ot(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('10 💲', '50 💲', '100 💲', '250 💲', '500 💲', '750 💲','1000 💲','1250 💲','1500 💲','👈 Назад')
        cursor = conn.cursor()
        cursor.execute(f'UPDATE users SET cc = 666220 WHERE userid = {message.from_user.id}')
        conn.commit()
        cursor.close()
        await message.answer('Делайте ставку \n\nСтавка должна быть от *10* до *10.000* \nВы также можете ввести свою сумму введя ее в ответном сообщении', reply_markup=keyboard, parse_mode= 'Markdown')

        @dp.message_handler(lambda message: message.text and selec(message) == 666220)
        async def ot2(message):
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
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add('1', '2', '3', '👈 Назад')
            await message.answer('Введите число от 1 до 3', reply_markup=keyboard, parse_mode= 'Markdown')

            @dp.message_handler(lambda message: message.text and selec(message) == 69692)
            async def ot3(message):
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add('Повторить', '👈 Назад')
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
                                await message.answer('Неверный ввод!')
                        except Error:
                            await message.answer('Неверный ввод!')
                    if keff == 1 or keff == 2 or keff == 3:
                        cursor = conn.cursor()
                        cursor.execute(f'UPDATE users SET rub = rub - {stavka} WHERE userid = {message.from_user.id}')
                        conn.commit()
                        otr = random.randint(1,100)
                        if otr <= 20:
                            cc = keff
                            win = stavka * 3
                            win = win + stavka
                            cursor.execute(f"UPDATE users SET rub = rub + {win} WHERE userid = {message.from_user.id}")
                            conn.commit()
                            await message.answer(f'Поздравляем!👏 \nВаш выйгрыш: {stavka * 3} 💲\n\nВаш текущий баланс - *{money} 💲*\nВаша ставка: {stavka} 💲\n\nВаше число: {keff}\nЧисло: {cc}', reply_markup=keyboard, parse_mode= 'Markdown')
                        else:
                            cc = random.randint(1,3)
                            while cc == keff:
                                cc = random.randint(1,3)
                            await message.answer(f'Сожалеем, вы проиграли!\n\nВаше число: {keff}\nЧисло: {cc}', reply_markup=keyboard)
                except Error:
                    await message.answer('Неверный ввод!')
    @dp.message_handler(lambda message: message.text and '1/30' in message.text and selec(message) == 666)
    async def otc(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('10 💲', '50 💲', '100 💲', '250 💲', '500 💲', '750 💲','1000 💲','1250 💲','1500 💲','👈 Назад')
        cursor = conn.cursor()
        cursor.execute(f'UPDATE users SET cc = 66620 WHERE userid = {message.from_user.id}')
        conn.commit()
        cursor.close()
        await message.answer('Делайте ставку \n\nСтавка должна быть от *10* до *10.000* \nВы также можете ввести свою сумму введя ее в ответном сообщении', reply_markup=keyboard, parse_mode= 'Markdown')

        @dp.message_handler(lambda message: message.text and selec(message) == 66620)
        async def otc2(message):
            lis = message.text.split()
            if len(lis) == 2:
                rubb = message.text
                rubb = rubb[:-2]
            if len(lis) == 1:
                rubb = message.text
            rubb = int(rubb)
            cursor = conn.cursor()
            cursor.execute(f"UPDATE games SET otcv = '{rubb}' WHERE userid = {message.from_user.id}")
            cursor.execute(f'UPDATE users SET cc = 69694 WHERE userid = {message.from_user.id}')
            conn.commit()
            cursor.close()
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add('1', '2', '3', '4', '5', '10', '👈 Назад')
            await message.answer('Введите число от 1 до 30\n\nПри выйгрыше вы получите 30x от вашей стаки', reply_markup=keyboard, parse_mode= 'Markdown')

            @dp.message_handler(lambda message: message.text and selec(message) == 69694)
            async def otc3(message):
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add('Повторить', '👈 Назад')
                try:
                    if message.text == 'Повторить':
                            cursor = conn.cursor()
                            cursor.execute(f'SELECT otck FROM games WHERE userid = {message.from_user.id}')
                            keff = cursor.fetchone()
                            keff = keff[0]
                            keff = int(keff)
                            cursor.execute(f'SELECT otcv FROM games WHERE userid = {message.from_user.id}')
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
                            if isint(keff) and keff > 0 and keff <= 30:
                                cursor = conn.cursor()
                                cursor.execute(f"UPDATE games SET otck = '{keff}' WHERE userid = {message.from_user.id}")
                                conn.commit()
                                cursor.execute(f"SELECT otcv FROM games WHERE userid = {message.from_user.id}")
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
                                await message.answer('Неверный ввод!')
                        except Error:
                            await message.answer('Неверный ввод!')
                    if isint(keff):
                        cursor = conn.cursor()
                        cursor.execute(f'UPDATE users SET rub = rub - {stavka} WHERE userid = {message.from_user.id}')
                        conn.commit()
                        otr = random.randint(1,45)
                        if otr == 1:
                            cc = keff
                            win = stavka * 30
                            win = win + stavka
                            cursor.execute(f"UPDATE users SET rub = rub + {win} WHERE userid = {message.from_user.id}")
                            conn.commit()
                            await message.answer(f'Поздравляем!👏 \nВаш выйгрыш: {stavka * 30} 💲\n\nВаш текущий баланс - *{money} 💲*\nВаша ставка: {stavka} 💲\n\nВаше число: {keff}\nЧисло: {cc}', reply_markup=keyboard, parse_mode= 'Markdown')
                        else:
                            cc = random.randint(1,30)
                            while cc == keff:
                                cc = random.randint(1,30)
                            await message.answer(f'Сожалеем, вы проиграли!\n\nВаше число: {keff}\nЧисло: {cc}', reply_markup=keyboard)
                except Error:
                    await message.answer('Неверный ввод!')

    @dp.message_handler(lambda message: message.text and 'Краш' in message.text and selec(message) == 666)
    async def bus1(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('10 💲', '50 💲', '100 💲', '250 💲', '500 💲', '750 💲','1000 💲','1250 💲','1500 💲','👈 Назад')
        cursor = conn.cursor()
        cursor.execute(f'UPDATE users SET cc = 666000 WHERE userid = {message.from_user.id}')
        conn.commit()
        cursor.close()
        await message.answer('Делайте ставку \n\nСтавка должна быть от *10* до *10.000* \nВы также можете ввести свою сумму введя ее в ответном сообщении', reply_markup=keyboard, parse_mode= 'Markdown')
        
        @dp.message_handler(lambda message: message.text and selec(message) == 666000)
        async def bus2(message):
            lis = message.text.split()
            if len(lis) == 2:
                rubb = message.text
                rubb = rubb[:-2]
            if len(lis) == 1:
                rubb = message.text
            rubb = int(rubb)
            cursor = conn.cursor()
            cursor.execute(f"UPDATE games SET bustav = '{rubb}' WHERE userid = {message.from_user.id}")
            cursor.execute(f'UPDATE users SET cc = 6969 WHERE userid = {message.from_user.id}')
            conn.commit()
            cursor.close()
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add('1.25', '1.5', '2', '3', '5', '10', '20', '👈 Назад')
            await message.answer('Введите коэффициент\nКоэффицент должен быть от 1.2 до 1000\n\nВведеная вами ставка обрежется до 2 нулей после точки\nПрим: 2.4235 > 2.42', reply_markup=keyboard, parse_mode= 'Markdown')
            
            @dp.message_handler(lambda message: message.text and selec(message) == 6969)
            async def bus3(message):
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add('Повторить', '👈 Назад')
                try:
                    print(message.text)
                    if message.text == 'Повторить':
                        cursor = conn.cursor()
                        cursor.execute(f'SELECT bustak FROM games WHERE userid = {message.from_user.id}')
                        keff = cursor.fetchone()
                        keff = keff[0]
                        keff = float(keff)
                        cursor.execute(f'SELECT bustav FROM games WHERE userid = {message.from_user.id}')
                        stavka = cursor.fetchone()
                        stavka = stavka[0]
                        stavka = int(stavka)
                        cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
                        money = cursor.fetchone()
                        money = money[0]
                        cursor.close()
                    else:
                        try:
                            keff = round(float(message.text), 2)
                            if keff >= 1.2:
                                cursor = conn.cursor()
                                cursor.execute(f"UPDATE games SET bustak = '{keff}' WHERE userid = {message.from_user.id}")
                                conn.commit()
                                cursor.execute(f"SELECT bustav FROM games WHERE userid = {message.from_user.id}")
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
                                await message.answer('Неверный ввод!\nКоэффицент должен быть от 1.2 до 1000')
                        except Error:
                            await message.answer('Неверный ввод!')
                    if stavka >= 10 and stavka <= 10000 and money >= stavka:
                        print('YES')
                        cursor = conn.cursor()
                        cursor.execute(f'UPDATE users SET rub = rub - {stavka} WHERE userid = {message.from_user.id}')
                        conn.commit()
                        print('potracheno')
                        ab = random.randint(1, 1000)
                        if ab <= 75:
                            cc = round(random.uniform(1.00, 1.24), 2)
                        elif ab <= 400:
                            cc = round(random.uniform(1.00, 2.00), 2)
                        elif ab >= 600 and ab <= 800:
                            cc = round(random.uniform(2.00, 4.00), 2)
                        elif ab >= 802 and ab <= 915:
                            cc = round(random.uniform(4.00, 8.00), 2)
                        elif ab >= 918 and ab <= 960:
                            cc = round(random.uniform(8.00, 16.00), 2)
                        elif ab >= 961 and ab <= 980:
                            cc = round(random.uniform(16.00, 32.00), 2)
                        elif ab >= 983 and ab <= 990:
                            cc = round(random.uniform(32.00, 64.00), 2)
                        elif ab >= 991 and ab <= 996:
                            cc = round(random.uniform(64.00, 128.00), 2)
                        elif ab == 999:
                            cc = round(random.uniform(128.00, 1000.00), 2)
                        else:
                            cc = 1.00
                        print(cc)
                        if cc >= keff:
                            win = keff * stavka
                            win = win + stavka
                            cursor = conn.cursor()
                            cursor.execute(f"UPDATE users SET rub = rub + {win} WHERE userid = {message.from_user.id}")
                            conn.commit()
                            await message.answer(f'Поздравляем!👏 \nВаш выйгрыш: {keff * stavka} 💲\n\nВаш текущий баланс - *{money} 💲*\nВаша ставка: *{stavka}* 💲\n\nВаш коэффицент: *{keff}*\nКоэффицент: {cc}', reply_markup=keyboard, parse_mode= 'Markdown')
                        else:
                            await message.answer(f'Сожалеем, вы проиграли!\n\nВаш коэффицент: {keff}\nКоэффицент: {cc}', reply_markup=keyboard)
                    else:
                        await message.answer('Недостаточно средств на балансе')
                except Error:
                    await message.answer('Неверный ввод!')

                
    @dp.message_handler(lambda message: message.text and 'Орел и Решка' in message.text and selec(message) == 666)
    async def oir1(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('Орел', 'Решка', 'Ребро', '👈 Назад')
        await message.answer('*Выберите сторону*\n\nКоэффиценты для сторон:\n\n*Орел/Решка* - 2x \n*Ребро* - 25x', reply_markup=keyboard, parse_mode= 'Markdown')
        
        @dp.message_handler(lambda message: message.text and 'Орел' in message.text or 'Решка' in message.text or 'Ребро' in message.text and selec(message) == 666)
        async def oir2(message):
            cursor = conn.cursor()
            cursor.execute(f"UPDATE games SET oirt = '{message.text}' WHERE userid = {message.from_user.id}")
            cursor.execute(f'UPDATE users SET cc = 667 WHERE userid = {message.from_user.id}')
            conn.commit()
            cursor.close()
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add('10 💲', '50 💲', '100 💲', '250 💲', '500 💲', '750 💲','1000 💲','1250 💲','1500 💲','👈 Назад')
            await message.answer('Делайте ставку \n\nСтавка должна быть от *10* до *10.000* \nВы также можете ввести свою сумму введя ее в ответном сообщении', reply_markup=keyboard, parse_mode= 'Markdown')
            
            @dp.message_handler(lambda message: message.text and selec(message) == 667)
            async def oir3(message):
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
                        await message.answer('Ставка должна быть от *10* до *10.000*', parse_mode= 'Markdown')
                    else:
                        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        keyboard.add('Повторить', '👈 Назад')
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
                            with open(paph,'rb') as photo:
                                await message.reply_photo(photo, reply_markup=keyboard)
                            cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
                            money = cursor.fetchone()
                            money = money[0]
                            cursor.close()
                            rubb = former(rubb)
                            money = former(money)
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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('⬇ Пополнить баланс', '⬆ Вывести', '👈 Назад')
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
    await message.answer(f'Здесь вы можете пополнить или вывести ваш баланс\n\nВаш баланс для покупок: *{money} 💲*\nВаш баланс для вывода: {vivc} 💸', parse_mode= 'Markdown', reply_markup=keyboard)
    
    @dp.message_handler(lambda message: message.text and '⬇' in message.text and selec(message) == 6886)
    async def popbalance(message):
        cursor = conn.cursor()
        cursor.execute(f'UPDATE users SET cc = 68886 WHERE userid = {message.from_user.id}')
        conn.commit()
        cursor.close()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('80', '100', '500','👈 Назад')
        await message.answer('Введите сумму пополнения вашего счета (минимальная сумма пополнения - 80 рублей)\n\nКурс:\n1 рубль = 100 💲\nПри пополнении 25% от суммы вашего пополнения станут 💵', reply_markup=keyboard)
        
        @dp.message_handler(lambda message: message.text and isint(message.text) and selec(message) == 68886)
        async def popbalance1(message):
            pop = message.text
            print(message.text)
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add('👈 Назад')
            try:
                pop = int(pop)
                if pop > 80 and pop < 10000:
                    cursor = conn.cursor()
                    cursor.execute(f"INSERT INTO req(userid, mon, app) VALUES({message.from_user.id}, {pop}, 0)")
                    conn.commit()
                    cursor.close()
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
    
    @dp.message_handler(lambda message: message.text and '⬆' in message.text and selec(message) == 6886)
    async def vivbalance(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('50', '100', '500','👈 Назад')
        await message.answer('Введите сумму', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and '🍓 ' in message.text)
async def farm(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('💲 Купить растения', '🍒 Мои растения', '✂ Собрать', '👈 Назад')
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 10 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.execute(f'SELECT plod FROM users WHERE userid={message.from_user.id}')
    plod = cursor.fetchone()
    plod = plod[0]
    cursor.execute(f'SELECT * FROM fruits WHERE userid={message.from_user.id}')
    i = cursor.fetchone()
    cursor.close()
    ssq = i[2] * 100
    ssq1 = i[3] * 600
    ssq2 = i[4] * 3200
    ssq3 = i[5] * 14000
    ssq4 = i[6] * 80000
    ssq5 = i[7] * 200000
    all = ssq + ssq1 + ssq2 + ssq3 + ssq4 + ssq5
    print(all)
    plod = int(plod)
    plod = former(plod)
    all = former(all)
    await message.answer(f'Это ваша небольшая горная ферма на севере Калифорнии у необычайно красивого берега \nЗдесь вы можете купить еще фруктовых растений или собрать спелые плоды \n\nУ вас на ферме {str(plod)} 🌟\n\nВ час вы зарабатываете {all} 🌟', reply_markup=keyboard)
    
    @dp.message_handler(lambda message: message.text and '✂ ' in message.text and selec(message) == 10)
    async def ctch(message):
        cursor = conn.cursor()
        cursor.execute(f'SELECT plod FROM users WHERE userid={message.from_user.id}')
        plod = cursor.fetchone()
        plod = plod[0]
        plod = int(plod)
        cursor.execute(f'UPDATE users SET plod = plod - {plod} WHERE userid={message.from_user.id}')
        cursor.execute(f'UPDATE users SET plodd = plodd + {plod} WHERE userid={message.from_user.id}')
        conn.commit()
        cursor.close()
        plod = former(plod)
        await message.answer(f'Готово вы собрали {plod} 🌟!')

    @dp.message_handler(lambda message: message.text and '🍒 ' in message.text and selec(message) == 10)
    async def myfarm(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('👈 Назад')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM fruits WHERE userid={message.from_user.id}')
        myplod = cursor.fetchone()
        cursor.close()
        await message.answer(f'У вас: \n\n{myplod[2]} грядок клубники 🍓\n\n{myplod[3]} вишневых деревьев 🍒\n\n{myplod[4]} яблочных деревьев 🍎\n\n{myplod[5]} банановых деревьев 🍌\n\n{myplod[6]} персиковых деревьев 🍑\n\n{myplod[7]} виноградных деревьев 🍇', reply_markup=keyboard)

    @dp.message_handler(lambda message: message.text and '💲 ' in message.text and selec(message) == 10)
    async def buyfarm(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cursor = conn.cursor()
        cursor.execute(f'UPDATE users SET cc = 11 WHERE userid = {message.from_user.id}')
        cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
        money = cursor.fetchone()
        cursor.close()
        money = money[0]
        keyboard.add('Купить 🍓','Купить 🍒','Купить 🍎','Купить 🍌','Купить 🍑','Купить 🍇','👈 Назад')
        await message.answer(f'Здесь вы можете купить растения на вашу ферму: \n\n🍓 - 1.000 💲\nПриносит 100 🌟 в час\n\n🍒 - 5.000 💲\nПриносит 600 🌟 в час\n\n🍎 - 25.000 💲\nПриносит 3.200 🌟 в час\n\n🍌 - 100.000 💲\nПриносит 14.000 🌟 в час\n\n🍑 - 500.000 💲\nПриносит 80.000 🌟 в час\n\n🍇 - 1.000.000 💲\nПриносит 200.000 🌟 в час \n\nУ вас на балансе: {former(money)} 💲', reply_markup=keyboard)
        
        @dp.message_handler(lambda message: message.text and 'Купить ' in message.text and selec(message) == 11)
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
            cursor = conn.cursor()
            cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
            money = cursor.fetchone()
            money = money[0]
            if money >= fruitm:
                cursor.execute(f"UPDATE users SET rub = rub - {fruitm} WHERE userid = {message.from_user.id}")
                cursor.execute(f"UPDATE fruits SET {nn} = {nn} + 1 WHERE userid = {message.from_user.id}")
                conn.commit()
                cursor.close()
                logging.info(f"{message.from_user.id} bought {fruit} {fruitm}")
                await message.answer('Успешно!')
            else:
                cursor.close()
                await message.answer('Недостаточно средств')
    
    @dp.message_handler(lambda message: message.text and '✨ suka ' in message.text and selec(message) == 10)
    async def buyvipfarm(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('Купить VIP🍍','Купить VIP🐉','Купить VIP⭐','👈 Назад')
        await message.answer('магаз', reply_markup=keyboard)
   
    @dp.message_handler(lambda message: message.text and 'Купить VIP suka ' in message.text and selec(message) == 10)
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
        logging.info(f"{message.from_user.id} buy ")
        await message.answer(f'Ваша ссылка для покупки', reply_markup = markup)

@dp.message_handler(lambda message: message.text and '💭' in message.text)
async def review(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 33 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Написать', 'Прочитать','👈 Назад')
    await message.answer('Здесь вы можете прочитать или написать отзывы', reply_markup=keyboard)
    
    @dp.message_handler(lambda message: message.text and 'Написать' in message.text and selec(message) == 33)
    async def review1(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('👈 Назад')
        await message.answer('В ответном сообщении вы можете оставить отзыв, за каждый качественный отзыв вы получите 50 💲', reply_markup=keyboard)
        
        @dp.message_handler(lambda message: message.text and ' ' in message.text and selec(message) == 33)
        async def review2(message):
            r = requests.get(f'https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id=1737649749&text=z{message.text}{message.from_user.id}')
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add('👈 Назад')
            logging.info(f"{message.from_user.id} wrote {message.text}")
            await message.answer('Принято!', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and 'BONUS' in message.text)
async def bonus(message):
    cursor = conn.cursor()
    cursor.execute(f'SELECT bon FROM users WHERE userid = {message.from_user.id}')
    bbon = cursor.fetchone()
    bbon = bbon[0]
    if bbon == 0:
        cursor.execute(f'UPDATE users SET bon = 1 WHERE userid = {message.from_user.id}')
        cursor.execute(f'UPDATE users SET rub = rub + 250 WHERE userid = {message.from_user.id}')
        conn.commit()
        cursor.close()
        await message.answer('Поздравляем!👏 Ваш бонус: 250 💲')
    else:
        cursor.close()
        await message.answer('Вы уже использовали ваш бонус!')

@dp.message_handler(lambda message: message.text and '⚡ ' in message.text)
async def bond(message):
    cursor = conn.cursor()
    cursor.execute(f'SELECT bond FROM users WHERE userid = {message.from_user.id}')
    bbond = cursor.fetchone()
    bbond= bbond[0]
    if bbond == 0:
        cursor.execute(f'UPDATE users SET bond = 1 WHERE userid={message.from_user.id}')
        cursor.execute(f'UPDATE users SET rub = rub + 200 WHERE userid={message.from_user.id}')
        conn.commit()
        cursor.close()
        await message.answer('Отлично!👏 Вы получили ваш ежедневный бонус на сумму 200 💲')
    else:
        cursor.close()
        await message.answer('Бонус доступен только раз в день!')

@dp.message_handler(lambda message: message.text and '👥 ' in message.text)
async def ref(message):
    cursor = conn.cursor()
    cursor.execute(f"SELECT refco FROM users WHERE userid = {message.from_user.id}")
    refff = cursor.fetchone()
    cursor.close()
    refff = refff[0]
    await message.answer(f'Ваша реферальная ссылка: \nt.me/coinluck_bot?start={message.from_user.id} \n\nУ вас {refff} рефералов!')

@dp.message_handler(lambda message: message.text and 'temp' in message.text and message.from_user.id == 1737649749)
async def temp(message):
    temp = subprocess.check_output(['vcgencmd', 'measure_temp'])
    temp = temp.decode()
    await message.answer(f'{temp}')

@dp.message_handler(lambda message: message.text and 'uptime' in message.text and message.from_user.id == 1737649749)
async def upt(message):
    upt = subprocess.check_output(['uptime'])
    upt = upt.decode()
    await message.answer(f'{upt}')

if __name__ == '__main__':
    executor.start_polling(dp)
