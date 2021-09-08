import sqlite3
import requests
import random
import time

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1840809585:AAG841k0MzuQ2HhGQ6u2j9BTt6DFAWbhr1A'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.channel_post_handler()
async def upp(message):
    print(message.text)
    lil = message.text.split(':')
    print(lil)
    conn = sqlite3.connect("/home/nail/oir/luck.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users SET rub = rub + {lil[1]*100} WHERE userid = {lil[3]}")
    cursor.execute(f"UPDATE users SET inp = inp + {lil[1]} WHERE userid = {lil[3]}")
    cursor.execute(f"UPDATE req SET app = 1 WHERE userid = {lil[3]}")
    conn.commit()
    conn.close()




    

if __name__ == '__main__':
    executor.start_polling(dp)
