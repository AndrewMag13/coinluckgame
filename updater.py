import psycopg2
from psycopg2 import Error
import requests
import random
import time
import logging
logging.basicConfig(filename="inputer.log", level=logging.INFO)

try:
    conn = psycopg2.connect(user="postgres",
                                    password="iwasbornfree",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="luck")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)


from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1840809585:AAG841k0MzuQ2HhGQ6u2j9BTt6DFAWbhr1A'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.channel_post_handler()
async def upp(message):
    print(message.text)
    lil = message.text.split(':')
    logging.info(f"{message.text}")
    print(lil)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users SET rub = rub + {lil[1]*100} WHERE userid = {lil[3]}")
    cursor.execute(f"UPDATE users SET inp = inp + {lil[1]} WHERE userid = {lil[3]}")
    cursor.execute(f"UPDATE req SET app = 1 WHERE userid = {lil[3]}")
    conn.commit()
    cursor.execute(f"SELECT ref from users WHERE userid = {lil[3]}")
    ref = cursor.fetchone()
    ref = ref[0]
    if ref != 0:
        cursor.execute(f"UPDATE users SET rub = rub + {(lil[1]) / 100 * 5} WHERE userid = {ref}")
        conn.commit()
    conn.close()




    

if __name__ == '__main__':
    executor.start_polling(dp)
