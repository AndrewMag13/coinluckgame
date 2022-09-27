    #@dp.message_handler(lambda message: message.text and '✨ qswafukwafvb ' in message.text and selec(message) == 10)
    #async def buyvipfarm(message):
    #    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #    keyboard.add('Купить VIP🍍','Купить VIP🐉','Купить VIP⭐',temps.back())
    #    await message.answer('магаз', reply_markup=keyboard)
   
    #@dp.message_handler(lambda message: message.text and 'Купить VIP wsuwarasdfkaw ' in message.text and selec(message) == 10)
    #async def buyvipfarm1(message):
    #    fruit = message.text[-1]
    #    if fruit == "🍍":
    #        fruitm = 99
    #    elif fruit == "🐉":
    #        fruitm = 299
    #    elif fruit == "⭐":
    #        fruitm = 499
    #    else:
    #        await message.answer('Не могу тебя понять')
    #    cursor = conn.cursor()
    #    cursor.execute(f"INSERT INTO req(userid, mon, app) VALUES({message.from_user.id}, {fruitm}, 0)")
    #    conn.commit()
    #    conn.close()
    #    opl = hashlib.md5(f'{merchant_id}:{fruitm}:{secret}:RUB:{message.from_user.id}'.encode('utf-8')).hexdigest()
    #    print(opl)
    #    urrl = f'https://pay.freekassa.ru/?m={merchant_id}&oa={fruitm}&o={message.from_user.id}&s={opl}&currency=RUB&us_key={fruitm}'
    #    markup = types.InlineKeyboardMarkup()
    #    btn_my_site= types.InlineKeyboardButton(text='Оплатить', url=urrl)
    #    markup.add(btn_my_site)
    #    logging.info(f"{message.from_user.id} buy ")
    #    await message.answer(f'Ваша ссылка для покупки', reply_markup = markup)
'''
import requests
import logging
from postgresso import *

def rev1(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 33 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()

def rev2(message):
    r = requests.get(f'https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id=1737649749&text=z{message.text}\n{message.from_user.id}')
    logging.info(f"{message.from_user.id} wrote {message.text}")

def rev11(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 34 WHERE userid = {message.from_user.id}')
    conn.commit()
    cursor.close()


    @dp.message_handler(lambda message: message.text and '💭' in message.text)
    async def review(message):
        rev1(message)
        rr = kb.rev(message)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(rr[0], rr[1], kb.back(message))
        await message.answer(temps.rev(message), reply_markup=keyboard)
        
        @dp.message_handler(lambda message: message.text and ('Написать' in message.text or 'Write') and selec(message) == 33)
        async def review1(message):
            rev11(message)
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(kb.back(message))
            await message.answer(temps.goodrev(message), reply_markup=keyboard)
            
            @dp.message_handler(lambda message: message.text and ' ' in message.text and selec(message) == 34)
            async def review2(message):
                rev2(message)
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(kb.back(message))
                await message.answer(temps.succ(message), reply_markup=keyboard)


        def rev(message):
            if langich(message) == "English":
                return('Here you can read or write reviews')
            else:
                return('Здесь вы можете прочитать или написать отзывы')
        def goodrev(message):
            if langich(message) == "English":
                return('In reply message you can place your review, for every quality review you will recieve 50 💲')
            else:
                return('В ответном сообщении вы можете оставить отзыв, за каждый качественный отзыв вы получите 50 💲')

            
    def rev(message):
        if langich(message) == "English":
            return ('Messages', 'Friends')
        else:
            return ('Сообщения', 'Друзья')
'''

'''
import requests
from postgresso import *

def vivod1(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 6886990 WHERE userid = {message.from_user.id}')
    conn.commit()

def vivod2(message):
    r = requests.get(f'https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id=1737649749&text={message.text}')


@dp.message_handler(lambda message: message.text and '⬆' in message.text and selec(message) == 6886)
        async def vivbalance(message):
            vivod1(message)
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(kb.back(message))
            await message.answer(temps.viv(message), reply_markup=keyboard)
        
            @dp.message_handler(lambda message: message.text and ' ' in message.text and selec(message) == 6886990)
            async def vivbalance(message):
                vivod2(message)
                await message.answer(temps.viv2(message), reply_markup=keyboard)
        def viv(message):
            if langich(message) == "English":
                return('In reply message enter the amount and requisites\nCourse: 100 💸 = 1 ₽\nExample: 20000 qiwi +79XXXXXXXXX.')
            else:
                return('В ответном сообщении введите сумму вывода и реквизиты\nКурс: 100 💸 = 1 ₽\nПример: 20000 на киви +79XXXXXXXXX.')
        def viv2(message):
            if langich(message) == "English":
                return('Application sent!')
            else:
                return('Заявление отправлено!')
        '''