import psycopg2
from psycopg2 import Error
from typing import Type
import requests
import random
import subprocess
import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(filename="actual.log", level=logging.INFO)


API_TOKEN = '2097806471:AAEa_cYGzcXGB0NIw003ttKYsMJLAzvsspM'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('СЛИФФКИ')
    cursor = conn.cursor()
    valua = (userid, username)
    try:
        cursor.execute(f"INSERT INTO actual(userid,username)VALUES{valua};")
        conn.commit()
    except Error:
        pass
    print(f'+1 wanker {username}')
    r = requests.get('https://api.telegram.org/bot1825655292:AAHzXTkiiIQUDh-xPtLdpgNcOEs9jO4Jz74/sendMessage?chat_id=1737649749&text=+1luder')
    cursor.close()
    logging.info(f"new luder: {userid}")
    await message.answer(f'*Приветствую {message.from_user.id}♦*\n\nЭтот бот покажет вам актуальные ссылки на наши каналы', parse_mode= 'Markdown', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text and 'СЛИФФКИ' in message.text)
async def main(message):
    cursor = conn.cursor()
    cursor.execute(f'SELECT link FROM actual WHERE userid = {message.from_user.id}')
    link = cursor.fetchone()
    link = link[0]
    cursor.close()
    await message.answer(f'Ссылка:\nt.me/{link}')

@dp.message_handler(lambda message: message.text and 'add' in message.text and (message.from_user.id == 1737649749 or message.from_user.id == 1882355196))
async def add(message):
    #try:
        linked = message.text.split(' ')
        linked = linked[1]
        print(linked)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE actual SET link = '{linked}' WHERE id > 0")
        conn.commit()
        cursor.close()
        await message.answer(f'DONE\n{linked}')
    #except Error:
    #    await message.answer(f'Error')

if __name__ == '__main__':
    executor.start_polling(dp)
