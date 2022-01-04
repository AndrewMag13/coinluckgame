import psycopg2
from psycopg2 import Error
import logging
import base64
from aiogram import Bot, Dispatcher, executor, utils
from aiohttp import client_exceptions
logging.basicConfig(filename="inputer.log", level=logging.INFO)

try:
    conn = psycopg2.connect(user="postgres",
                                    password="iwasbornfree",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="luck")
except (Exception, Error) as error:
    print("connError", error)

API_TOKEN = '1840809585:AAFI1EUEsjO5EORDIaijJ3ZTJsg_rZOkAgQ'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
try:
    @dp.channel_post_handler()
    async def upp(message):
        lil = base64.b64decode(message.text)
        lil = lil.decode()
        lil = lil.split(',')
        logging.info(f"{lil}")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE users SET rub = rub + {lil[0]*100} WHERE userid = {lil[1]}")
        cursor.execute(f"UPDATE users SET inp = inp + {lil[0]} WHERE userid = {lil[1]}")
        cursor.execute(f"UPDATE req SET app = 1 WHERE userid = {lil[1]}")
        conn.commit()
        cursor.execute(f"SELECT ref from users WHERE userid = {lil[1]}")
        ref = cursor.fetchone()
        ref = ref[0]
        if ref != 0:
            cursor.execute(f"UPDATE users SET rub = rub + {(lil[0]) / 100 * 5} WHERE userid = {ref}")
            conn.commit()
        conn.close()
except (client_exceptions.ClientConnectorError, utils.exceptions.NetworkError) as error:
    print('conn err')
if __name__ == '__main__':
    executor.start_polling(dp)
