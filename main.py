import psycopg2
from psycopg2 import Error
from typing import Type
import requests
import random
import logging
from aiogram import Bot, Dispatcher, executor, types
from former import former
from unitool import temperature, uptime, logger, ally
from exchange import s2d, v2d, plodcourse
from temps import temps
from selec import selec
from referals import referals
from bonus import bond, obond
from rev import rev1, rev2
from mainnn import mainnn
from transfer import transfer1, transfer2
from games import gamesintro, ot11, ot12, ot13, oirm, oirm2
from popbalance import popbal1, popbal2, popbal3
from farm import farm1, catch1, farmall, buyfarm11, buyfruit

logging.basicConfig(filename="main.log", level=logging.INFO)

API_TOKEN = '1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

chk = 0

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

try:
    conn = psycopg2.connect(user="postgres",
                                password="iwasbornfree",
                                host="127.0.0.1",
                                port="5432",
                                database="luck")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

@dp.message_handler(commands=['start'])
async def welcome(message):
    userid = message.from_user.id
    username = message.from_user.username
    lang = temps.start()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(lang[0], lang[1])
    cursor = conn.cursor()
    rub, mesh, vivc, plod, plodd, ref, refco, inp, outp, bon, bond, course, cc = 0
    valua = (userid, rub, mesh, vivc, plod, plodd, ref, refco, inp, outp, bon, bond, course, cc)
    try:
        cursor.execute(f"INSERT INTO users(userid, rub, mesh, vivc, plod, plodd, ref, refco, inp, outp, bon, bond, course, cc)VALUES{valua};")
        print('done')
        cursor.execute(f"INSERT INTO fruits(userid, straw, cher, appl, banan, sliv, grape, caram, caramc, pineappl, pineapplc, drag, dragc)VALUES({userid}, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
        cursor.execute(f"INSERT INTO games(userid)VALUES({userid})")
        conn.commit()
    except Error:
        await message.answer(temps.intererr(message))
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
    await message.answer(temps.inter(message), reply_markup=keyboard, parse_mode= 'Markdown')
@dp.message_handler(lambda message: message.text and temps.back() in message.text or 'English' in message.text or 'Русский' in message.text)
async def mainn(message):
    mainnn(message)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kk = temps.startb()
    keyboard.add(kk[0], kk[1], kk[2], kk[3], kk[4], kk[5], kk[6], kk[7])
    await message.answer(temps.main(message), parse_mode= 'Markdown', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and '💱' in message.text)
async def tran(message):
    id = transfer1(message)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(temps.back())
    await message.answer(temps.trans(id), reply_markup=keyboard, parse_mode='Markdown')
    
    @dp.message_handler(lambda message: message.text and ' ' in message.text and selec(message) == 11290)
    async def tran1(message):
        tt = transfer2(message)
        if tt != None:
            mon = tt[0]
            mess = tt[1]
            await message.answer(temps.transucc(mess, mon), parse_mode= 'Markdown')
        else:
            await message.answer(temps.err())
            

@dp.message_handler(lambda message: message.text and '🔄' in message.text)
async def mart(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Обменять 🌟 на 💲', 'Обменять 💸 на 💲', temps.back())
    a = plodcourse(message)
    plod = a[0]
    course = a[1]
    await message.answer(temps.market(message, plod, course), reply_markup=keyboard, parse_mode= 'Markdown')
    
    @dp.message_handler(lambda message: message.text and 'Обменять 🌟 на 💲' in message.text and selec(message) == 110)
    async def mart1(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(temps.back())
        a = s2d(message)
        if a == None:
            await message.answer(temps.transerr(), reply_markup=keyboard)
        else:
            plods = a[0]
            rubs = a[1]
            vivc = a[2]
            rub = a[3]
            await message.answer(temps.transsucc(plods, rubs, vivc, rub), reply_markup=keyboard, parse_mode= 'Markdown')

    @dp.message_handler(lambda message: message.text and 'Обменять 💸 на 💲' in message.text and selec(message) == 110)
    async def mart2(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(temps.back())
        a = v2d(message)
        if a == None:
            await message.answer(temps.transerr(), reply_markup=keyboard, parse_mode= 'Markdown')
        else:
            rubs = a[0]
            vivc = a[1]
            rub = a[2]
            await message.answer(temps.transsucc2(vivc, rubs, rub), reply_markup=keyboard, parse_mode= 'Markdown')

@dp.message_handler(lambda message: message.text and '▶' in message.text)
async def games(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Орел и Решка', 'Краш', '1/3', '1/30', temps.back())
    gamesintro(message)
    await message.answer(temps.choose(), reply_markup=keyboard, parse_mode= 'Markdown')
    
    @dp.message_handler(lambda message: message.text and message.text == '1/3' and selec(message) == 666)
    async def ot(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ss = temps.standarts()
        keyboard.add(ss[0], ss[1], ss[2], ss[3], ss[4], ss[5], ss[6], ss[7], ss[8], ss[9])
        ot11(message)
        await message.answer(temps.stavka13(), reply_markup=keyboard, parse_mode= 'Markdown')

        @dp.message_handler(lambda message: message.text and selec(message) == 666220)
        async def ot2(message):
            ot12(message)
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add('1', '2', '3', temps.back())
            await message.answer(temps.number13(), reply_markup=keyboard, parse_mode= 'Markdown')

            @dp.message_handler(lambda message: message.text and selec(message) == 69692)
            async def ot3(message):
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add('Повторить', temps.back())
                res = ot13(message)
                if res == 'wrongent':
                    await message.answer(temps.wrongent())
                elif res == 'transerr':
                    await message.answer(temps.transerr(), reply_markup=keyboard)
                elif res == 'normstavka':
                    await message.answer(temps.normstavka(), reply_markup=keyboard, parse_mode= 'Markdown')
                elif res[0] == 'lose':
                    await message.answer(temps.lose13(res[1], res[2]), reply_markup=keyboard, parse_mode= 'Markdown')
                elif res[0] == 'win':
                    await message.answer(temps.win13(res[1], res[2], res[3], res[4]), reply_markup=keyboard, parse_mode= 'Markdown')
                       
    @dp.message_handler(lambda message: message.text and '1/30' in message.text and selec(message) == 666)
    async def otc(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ss = temps.standarts()
        keyboard.add(ss[0], ss[1], ss[2], ss[3], ss[4], ss[5], ss[6], ss[7], ss[8], ss[9])
        cursor = conn.cursor()
        cursor.execute(f'UPDATE users SET cc = 66620 WHERE userid = {message.from_user.id}')
        conn.commit()
        cursor.close()
        await message.answer(temps.stavka13(), reply_markup=keyboard, parse_mode= 'Markdown')

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
            cursor.execute(f"UPDATE games SET otvc = {rubb} WHERE userid = {message.from_user.id}")
            cursor.execute(f'UPDATE users SET cc = 69694 WHERE userid = {message.from_user.id}')
            conn.commit()
            cursor.close()
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add('1', '2', '3', '4', '5', '10', temps.back())
            await message.answer(temps.otri(), reply_markup=keyboard, parse_mode= 'Markdown')

            @dp.message_handler(lambda message: message.text and selec(message) == 69694)
            async def otc3(message):
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add('Повторить', temps.back())
                try:
                    if message.text == 'Повторить':
                            cursor = conn.cursor()
                            cursor.execute(f'SELECT otvk FROM games WHERE userid = {message.from_user.id}')
                            keff = cursor.fetchone()
                            keff = keff[0]
                            keff = int(keff)
                            cursor.execute(f'SELECT otvc FROM games WHERE userid = {message.from_user.id}')
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
                                cursor.execute(f"UPDATE games SET otvk = '{keff}' WHERE userid = {message.from_user.id}")
                                conn.commit()
                                cursor.execute(f"SELECT otvc FROM games WHERE userid = {message.from_user.id}")
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
                                await message.answer(temps.wrongent())
                        except Error:
                            await message.answer(temps.wrongent())
                    if stavka < 10 and stavka > 10000:
                        await message.answer(temps.wrongent(), reply_markup=keyboard)
                    if isint(keff) and money >= stavka and stavka >= 10 and stavka <= 10000:
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
                            await message.answer(temps.otrwin(stavka, money, keff, cc), reply_markup=keyboard, parse_mode= 'Markdown')
                        else:
                            cc = random.randint(1,30)
                            while cc == keff:
                                cc = random.randint(1,30)
                            await message.answer(temps.otrlose(keff, cc), reply_markup=keyboard)
                    else:
                        await message.answer(temps.transerr(), reply_markup=keyboard)
                    
                except Error:
                    await message.answer(temps.wrongent())

    @dp.message_handler(lambda message: message.text and 'Краш' in message.text and selec(message) == 666)
    async def bus1(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ss = temps.standarts()
        keyboard.add(ss[0], ss[1], ss[2], ss[3], ss[4], ss[5], ss[6], ss[7], ss[8], ss[9])
        cursor = conn.cursor()
        cursor.execute(f'UPDATE users SET cc = 666000 WHERE userid = {message.from_user.id}')
        conn.commit()
        cursor.close()
        await message.answer(temps.stavka13(), reply_markup=keyboard, parse_mode= 'Markdown')
        
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
            keyboard.add('1.25', '1.5', '2', '3', '5', '10', '20', temps.back())
            await message.answer(temps.keffs(), reply_markup=keyboard, parse_mode= 'Markdown')
            
            @dp.message_handler(lambda message: message.text and selec(message) == 6969)
            async def bus3(message):
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add('Повторить', temps.back())
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
                                await message.answer(temps.wrongent())
                        except Error:
                            await message.answer(temps.wrongent())
                    if stavka >= 10 and stavka <= 10000 and money >= stavka:
                        print('YES')
                        cursor = conn.cursor()
                        cursor.execute(f'UPDATE users SET rub = rub - {stavka} WHERE userid = {message.from_user.id}')
                        conn.commit()
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
                            await message.answer(temps.crashwin(keff, money, stavka, cc), reply_markup=keyboard, parse_mode= 'Markdown')
                        else:
                            await message.answer(temps.crashlose(keff, cc), reply_markup=keyboard)
                    else:
                        await message.answer(temps.transerr())
                except Error:
                    await message.answer(temps.wrongent())

                
    @dp.message_handler(lambda message: message.text and 'Орел и Решка' in message.text and selec(message) == 666)
    async def oir1(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('Орел', 'Решка', 'Ребро', temps.back())
        await message.answer(temps.oirs(), reply_markup=keyboard, parse_mode= 'Markdown')
        
        @dp.message_handler(lambda message: message.text and 'Орел' in message.text or 'Решка' in message.text or 'Ребро' in message.text and selec(message) == 666)
        async def oir2(message):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ss = temps.standarts()
            keyboard.add(ss[0], ss[1], ss[2], ss[3], ss[4], ss[5], ss[6], ss[7], ss[8], ss[9])
            oirm(message)
            await message.answer(temps.stavka13(), reply_markup=keyboard, parse_mode= 'Markdown')
            
            @dp.message_handler(lambda message: message.text and selec(message) == 667)
            async def oir3(message):
                    oirres = oirm2(message)
                    if oirres == 'Norms':
                        await message.answer(temps.normstavka(), parse_mode= 'Markdown')
                    elif oirres == 'Wrongent':
                        await message.answer(temps.wrongent())
                    else:
                        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        keyboard.add('Повторить', temps.back())
                        wiin = oirres[0]
                        money = oirres[1]
                        rubb = oirres[2]
                        paph = oirres[3]
                        with open(paph,'rb') as photo:
                            await message.reply_photo(photo, reply_markup=keyboard)
                        await message.answer(temps.oirep(wiin, money, rubb), reply_markup=keyboard, parse_mode= 'Markdown')
#
@dp.message_handler(lambda message: message.text and '💼' in message.text)
async def balance(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('⬇ Пополнить баланс', '⬆ Вывести', temps.back())
    pop1 = popbal1(message)
    await message.answer(temps.bal(pop1[0], pop1[1]), reply_markup=keyboard, parse_mode= 'Markdown')
    
    @dp.message_handler(lambda message: message.text and '⬇' in message.text and selec(message) == 6886)
    async def popbalance(message):
        popbal2(message)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('150 ₽', '300 ₽', '500 ₽','1000 ₽', temps.back())
        await message.answer(temps.pop(), reply_markup=keyboard)
        
        @dp.message_handler(lambda message: message.text and selec(message) == 68886)
        async def popbalance1(message):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(temps.back())
            popp = popbal3(message)
            if popp == None:
                await message.answer(temps.wrongent(), reply_markup=keyboard)
            else:
                markup = types.InlineKeyboardMarkup()
                btn_my_site= types.InlineKeyboardButton(text='Оплатить', url=popp)
                markup.add(btn_my_site)
                await message.answer(temps.link(), reply_markup = markup)
    
    @dp.message_handler(lambda message: message.text and '⬆' in message.text and selec(message) == 6886)
    async def vivbalance(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('50', '100', '500', temps.back())
        await message.answer(temps.viv(), reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and '🍓 ' in message.text)
async def farm(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('💲 Купить растения', '🍒 Мои растения', '✂ Собрать', temps.back())
    farmer = farm1(message)
    await message.answer(temps.farm(farmer[0], farmer[1]), reply_markup=keyboard)
    
    @dp.message_handler(lambda message: message.text and '✂ ' in message.text and selec(message) == 10)
    async def ctch(message):
        catcher = catch1(message)
        await message.answer(temps.sbor(catcher))

    @dp.message_handler(lambda message: message.text and '🍒 ' in message.text and selec(message) == 10)
    async def myfarm(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(temps.back())
        myplod = farmall(message)
        await message.answer(temps.allf(myplod), reply_markup=keyboard)

    @dp.message_handler(lambda message: message.text and '💲 ' in message.text and selec(message) == 10)
    async def buyfarm(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        money = buyfarm11(message)
        keyboard.add('Купить 🍓','Купить 🍒','Купить 🍎','Купить 🍌','Купить 🍑','Купить 🍇', temps.back())
        await message.answer(temps.buyf(money), reply_markup=keyboard)
        
        @dp.message_handler(lambda message: message.text and 'Купить ' in message.text and selec(message) == 11)
        async def buyfarm1(message):
            buyf = buyfruit(message)
            if buyf == None:
                await message.answer(temps.err())
            else:
                await message.answer(temps.succ())

@dp.message_handler(lambda message: message.text and '💭' in message.text)
async def review(message):
    rev1()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Написать', 'Прочитать', temps.back())
    await message.answer(temps.rev(), reply_markup=keyboard)
    
    @dp.message_handler(lambda message: message.text and 'Написать' in message.text and selec(message) == 33)
    async def review1(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(temps.back())
        await message.answer(temps.goodrev(), reply_markup=keyboard)
        
        @dp.message_handler(lambda message: message.text and ' ' in message.text and selec(message) == 33)
        async def review2(message):
            rev2(message)
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(temps.back())
            await message.answer(temps.succ(), reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and 'BONUS' in message.text)
async def bonusm(message):
    oebonus = obond(message)
    if oebonus == None:
        await message.answer(temps.err())
    else:
        await message.answer(temps.bon1())

@dp.message_handler(lambda message: message.text and '⚡ ' in message.text)
async def bondm(message):
    ebonus = bond(message)
    print(ebonus)
    if ebonus == None:
        await message.answer(temps.err())
    else:
        await message.answer(temps.bone())

@dp.message_handler(lambda message: message.text and '👥 ' in message.text)
async def ref(message):
    await message.answer(temps.refl(message, referals(message)))

@dp.message_handler(lambda message: message.text and 'temp' in message.text and message.from_user.id == 1737649749)
async def temp(message):
    await message.answer(temperature())

@dp.message_handler(lambda message: message.text and 'uptime' in message.text and message.from_user.id == 1737649749)
async def upt(message):
    await message.answer(uptime())

@dp.message_handler(lambda message: message.text and 'log' in message.text and message.from_user.id == 1737649749)
async def upt(message):
    await message.answer(logger())

@dp.message_handler(lambda message: message.text and 'all' in message.text and message.from_user.id == 1737649749)
async def usender(message):
    meess = ally(message)
    if meess == None:
        await message.answer(temps.err())
    else:
        await message.answer(f'You sent: \n{meess}')
    
if __name__ == '__main__':
    executor.start_polling(dp)
