import requests
import logging
import psycopg2
from former import former
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


def farm1(message):
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
    plod = int(plod)
    plod = former(plod)
    all = former(all)
    return all, plod


def catch1(message):
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
    return plod

def farmall(message):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM fruits WHERE userid={message.from_user.id}')
    myplod = cursor.fetchone()
    cursor.close()
    return myplod

def buyfarm11(message):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET cc = 11 WHERE userid = {message.from_user.id}')
    cursor.execute(f"SELECT rub FROM users WHERE userid = {message.from_user.id}")
    money = cursor.fetchone()
    cursor.close()
    money = money[0]
    return money

def waters(message):
    pass

def buyfruit(message):
    fruit = message.text[-1]
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
        return None
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
        return '1'
    else:
        cursor.close()
        return None
