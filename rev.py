import requests
import logging
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

'''
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