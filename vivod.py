import requests
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
    print("Ошибка при работе с PostgreSQL", error)

def vivod1(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 6886990 WHERE userid = {message.from_user.id}')
    conn.commit()

def vivod2(message):
    r = requests.get(f'https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id=1737649749&text={message.text}')

'''
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
'''
'''
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