import logging
from aiogram import Bot, Dispatcher, executor, types, utils
from aiohttp import client_exceptions
import time
from unitool import *
from exchange import *
from temps import *
from kb import *
from selec import *
from referals import *
from bonus import *
from mainnn import *
from transfer import *
from games import *
from popbalance import *
from farm import *
from intro import *
from lang import *
from rec import *
import topup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from glQiwiApi import QiwiWrapper
import glQiwiApi.types as qiwi_types
from typing import Union
from aiogram.dispatcher import FSMContext

logging.basicConfig(filename="main.log", level=logging.DEBUG)

storage = MemoryStorage()
wallet = QiwiWrapper(secret_p2p="eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Ink0NmN6Mi0wMCIsInVzZXJfaWQiOiI3OTM3MTM4NDQ0MCIsInNlY3JldCI6ImQzZGQ2NTNlNzg3MGRkYjhlOGExOGJiMTQ5NWRlY2M2ZGJiMGM2YWIyOTFlOWI2MWY5YzMwZjRjNWNkYjRhMjQifX0=")
API_TOKEN = '1825655292:AAGsFy3QJPFf6k2kRcq3JIm9nYEM9sItsWk'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage = storage)

try:
    @dp.message_handler(commands=['start'])
    async def welcome(message):
        lang = kb.welcome()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(lang[0], lang[1])
        if intro(message) == None:
            await message.answer(temps.intererr(message))
        else:
            await message.answer(temps.inter(message), reply_markup=keyboard, parse_mode= 'Markdown')

    @dp.message_handler(lambda message: message.text and ('👈' in message.text or selec(message) == 99990))
    async def mainn(message):
        mainnn(message)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kk = kb.start(message)
        keyboard.add(kk[0], kk[1], kk[2], kk[3], kk[4], kk[5], kk[6], kk[7])
        await message.answer(temps.main(message), parse_mode= 'Markdown', reply_markup=keyboard)

    @dp.message_handler(lambda message: message.text and '💱' in message.text)
    async def tran(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(kb.back(message))
        await message.answer(temps.trans(transfer1(message), message), reply_markup=keyboard, parse_mode='Markdown')
        
        @dp.message_handler(lambda message: message.text and ' ' in message.text and selec(message) == 11290)
        async def tran1(message):
            tt = transfer2(message)
            if tt != None:
                await message.answer(temps.transucc(tt[1], tt[0], message), parse_mode= 'Markdown')
            else:
                await message.answer(temps.err(message))
                
    @dp.message_handler(lambda message: message.text and '🔄' in message.text)
    async def mart(message):
        tr = kb.tr(message)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(tr[0], tr[1], kb.back(message))
        a = plodcourse(message)
        with open('/home/nail/oir/market.jpg', 'rb') as photo:
            await message.reply_photo(photo, reply_markup=keyboard)
        await message.answer(temps.market(message, a[0], a[1]), reply_markup=keyboard, parse_mode= 'Markdown')
        
        @dp.message_handler(lambda message: message.text and '🌟' in message.text and selec(message) == 110)
        async def mart1(message):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(kb.back(message))
            a = s2d(message)
            if a == None:
                await message.answer(temps.transerr(message), reply_markup=keyboard)
            else:
                await message.answer(temps.transsucc(message, a[0], a[1], a[2], a[3]), reply_markup=keyboard, parse_mode= 'Markdown')

        @dp.message_handler(lambda message: message.text and '💸' in message.text and selec(message) == 110)
        async def mart2(message):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(kb.back(message))
            a = v2d(message)
            if a == None:
                await message.answer(temps.transerr(message), reply_markup=keyboard, parse_mode= 'Markdown')
            else:
                await message.answer(temps.transsucc2(message, a[1], a[0], a[2]), reply_markup=keyboard, parse_mode= 'Markdown')

    @dp.message_handler(lambda message: message.text and '▶' in message.text)
    async def games(message):
        gg = kb.games(message)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(gg[0], gg[1], gg[2], gg[3], kb.back(message))
        gamesintro(message)
        await message.answer(temps.choose(message), reply_markup=keyboard, parse_mode= 'Markdown')
        
        @dp.message_handler(lambda message: message.text and message.text == '1/3' and selec(message) == 666)
        async def ot(message):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ss = kb.ots()
            keyboard.add(ss[0], ss[1], ss[2], ss[3], ss[4], ss[5], ss[6], ss[7], ss[8], kb.back(message))
            ot11(message)
            await message.answer(temps.stavka13(message), reply_markup=keyboard, parse_mode= 'Markdown')

            @dp.message_handler(lambda message: message.text and selec(message) == 666220)
            async def ot2(message):
                ot12(message)
                ns = kb.nums()
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(ns[0], ns[1], ns[2], kb.back(message))
                await message.answer(temps.number13(message), reply_markup=keyboard, parse_mode= 'Markdown')

                @dp.message_handler(lambda message: message.text and selec(message) == 69692)
                async def ot3(message):
                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    keyboard.add(kb.repeat(message), kb.back(message))
                    res = ot13(message)
                    if res == 'wrongent':
                        await message.answer(temps.wrongent(message))
                    elif res == 'transerr':
                        await message.answer(temps.transerr(message), reply_markup=keyboard)
                    elif res == 'normstavka':
                        await message.answer(temps.normstavka(message), reply_markup=keyboard, parse_mode= 'Markdown')
                    elif res[0] == 'lose':
                        await message.answer(temps.lose13(res[1], res[2], message), reply_markup=keyboard, parse_mode= 'Markdown')
                    elif res[0] == 'win':
                        await message.answer(temps.win13(res[1], res[2], res[3], res[4], message), reply_markup=keyboard, parse_mode= 'Markdown')
                        
        @dp.message_handler(lambda message: message.text and '1/30' in message.text and selec(message) == 666)
        async def otc(message):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ss = kb.ots()
            keyboard.add(ss[0], ss[1], ss[2], ss[3], ss[4], ss[5], ss[6], ss[7], ss[8], kb.back(message))
            othr1(message)
            await message.answer(temps.stavka13(message), reply_markup=keyboard, parse_mode= 'Markdown')

            @dp.message_handler(lambda message: message.text and selec(message) == 66620)
            async def otc2(message):
                othr2(message)
                nn = kb.nums()
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(nn[0], nn[1], nn[2], nn[3], nn[4], nn[5], kb.back(message))
                await message.answer(temps.otri(message), reply_markup=keyboard, parse_mode= 'Markdown')

                @dp.message_handler(lambda message: message.text and selec(message) == 69694)
                async def otc3(message):
                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    keyboard.add(kb.repeat(message), kb.back(message))
                    othrser = othr3(message)
                    if othrser == 'Wrongent':
                        await message.answer(temps.wrongent(message), reply_markup=keyboard)
                    elif othrser == 'Transerr':
                        await message.answer(temps.transerr(message), reply_markup=keyboard)
                    elif othrser == 'Norms':
                        await message.answer(temps.normstavka(message), reply_markup=keyboard, parse_mode= 'Markdown')
                    elif othrser[0] == 'win':
                        await message.answer(temps.otrwin(othrser[1], othrser[2], othrser[3], othrser[4], message), reply_markup=keyboard, parse_mode= 'Markdown')
                    elif othrser[0] == 'lose':
                        await message.answer(temps.otrlose(othrser[1], othrser[2], message), reply_markup=keyboard)
                    else:
                        await message.answer(temps.err(message), reply_markup=keyboard)

        @dp.message_handler(lambda message: message.text and ('Краш' in message.text or 'Busta' in message.text) and selec(message) == 666)
        async def bus1(message):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ss = kb.ots()
            keyboard.add(ss[0], ss[1], ss[2], ss[3], ss[4], ss[5], ss[6], ss[7], ss[8], kb.back(message))
            crash1(message)
            await message.answer(temps.stavka13(message), reply_markup=keyboard, parse_mode= 'Markdown')
            
            @dp.message_handler(lambda message: message.text and selec(message) == 666000)
            async def bus2(message):
                crash2(message)
                kf = kb.keff()
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(kf[0], kf[1], kf[2], kf[3], kf[4], kf[5], kf[6], kb.back(message))
                await message.answer(temps.keffs(message), reply_markup=keyboard, parse_mode= 'Markdown')
                
                @dp.message_handler(lambda message: message.text and selec(message) == 6969)
                async def bus3(message):
                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    keyboard.add(kb.repeat(message), kb.back(message))
                    crashres = crash3(message)
                    if crashres == 'wrongent':
                        await message.answer(temps.wrongent(message))
                    elif crashres == 'transerr':
                        await message.answer(temps.transerr(message))
                    elif crashres[0] == 'win':
                        await message.answer(temps.crashwin(crashres[3], crashres[1], crashres[2], crashres[4], message), reply_markup=keyboard, parse_mode= 'Markdown')
                    elif crashres[0] == 'lose':
                        await message.answer(temps.crashlose(crashres[1], crashres[2], message), reply_markup=keyboard)
                    else:
                        await message.answer(temps.err(message), reply_markup=keyboard)

        @dp.message_handler(lambda message: message.text and ('Орел и Решка' in message.text or 'Heads and Tails' in message.text) and selec(message) == 666)
        async def oir1(message):
            oir = kb.oir(message)
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(oir[0], oir[1], oir[2], kb.back(message))
            await message.answer(temps.oirs(message), reply_markup=keyboard, parse_mode= 'Markdown')
            
            @dp.message_handler(lambda message: message.text and ('Орел' in message.text or 'Решка' in message.text or 'Ребро' in message.text or 'Tail' in message.text or 'Head' in message.text or 'Edge' in message.text) and selec(message) == 666)
            async def oir2(message):
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                ss = kb.ots()
                keyboard.add(ss[0], ss[1], ss[2], ss[3], ss[4], ss[5], ss[6], ss[7], ss[8], kb.back(message))
                oirm(message)
                await message.answer(temps.stavka13(message), reply_markup=keyboard, parse_mode= 'Markdown')
                
                @dp.message_handler(lambda message: message.text and selec(message) == 667)
                async def oir3(message):
                        oirres = oirm2(message)
                        if oirres == 'Norms':
                            await message.answer(temps.normstavka(message), parse_mode= 'Markdown')
                        elif oirres == 'Wrongent':
                            await message.answer(temps.wrongent(message))
                        else:
                            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                            keyboard.add(kb.repeat(message), kb.back(message))
                            with open(oirres[3],'rb') as photo:
                                await message.reply_photo(photo, reply_markup=keyboard)
                            await message.answer(temps.oirep(oirres[0], oirres[1], oirres[2], message), reply_markup=keyboard, parse_mode= 'Markdown')

    @dp.message_handler(lambda message: message.text and '💼' in message.text)
    async def balance(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(kb.popb(message), kb.back(message))
        pop1 = popbal1(message)
        await message.answer(temps.bal(pop1[0], pop1[1], message), reply_markup=keyboard, parse_mode= 'Markdown')
        
        @dp.message_handler(lambda message: message.text and '⬇' in message.text and selec(message) == 6886)
        async def popbalance(message):
            popbal2(message)
            pm = kb.popm()
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(pm[0], pm[1], pm[2], pm[3], kb.back(message))
            await message.answer(temps.pop(message), reply_markup=keyboard, parse_mode= 'Markdown')
            
            #@dp.message_handler(lambda message: message.text and selec(message) == 68886)
            #async def popbalance1(message: types.Message, state: FSMContext):
                #keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                #pop = message.text.split()
                #pop = pop[0]
                #print(message.text)
                #try:
                #    pop = int(pop)
                #    #if pop >= 50:
                #    bill = await create_payment(pop)
                #    #else:
                #   #    return None
                #except ValueError:
                #    return None
                #except TypeError:
                #    return None
                #if bill == None:
                #    await message.answer(temps.wrongent(message), reply_markup=keyboard, parse_mode= 'Markdown')
                #else:
                #    keyboard.add(kb.op(message), kb.opc(message))
                #    await message.answer(temps.inv(message, bill), reply_markup=keyboard)
                #    await state.set_state("payment")
                #    await state.update_data(bill=bill)

            @dp.message_handler(state="payment", text="Done")
            async def successful_payment(message: types.Message, state: FSMContext):
                async with state.proxy() as data:
                    bill: qiwi_types.Bill = data.get("bill")
                status = await bill.check()
                am = bill.amount.value
                cu = bill.amount.currency
                if status:
                    topup.topup(message, am, cu)
                    await message.answer(temps.ops(message))
                    await state.finish()
                else:
                    await message.answer(temps.opf(message))
            
            @dp.message_handler(state="payment", text="Cancel")
            async def canc(message: types.Message, state: FSMContext):
                async with state.proxy() as data:
                    bill: qiwi_types.Bill = data.get("bill")
                await bill.reject()
                await state.finish()
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(kb.back(message))
                await message.answer(temps.canceled(message), reply_markup=keyboard)

    @dp.message_handler(lambda message: message.text and '🌄' in message.text)
    async def farm(message):
        ff = kb.fruit(message)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(ff[0], ff[1], ff[2], ff[3], kb.back(message))
        farmer = farm1(message)
        with open('/home/nail/oir/cali.jpg', 'rb') as photo:
            await message.reply_photo(photo, reply_markup=keyboard)
        await message.answer(temps.farm(farmer[0], farmer[1], message), reply_markup=keyboard, parse_mode= 'Markdown')
        
        @dp.message_handler(lambda message: message.text and '✂' in message.text and selec(message) == 10)
        async def ctch(message):
            await message.answer(temps.sbor(catch1(message), message))

        @dp.message_handler(lambda message: message.text and '🌊' in message.text and selec(message) == 10)
        async def wtr(message):
            if waters(message) == 'good':
                await message.answer(temps.water(message))
            else:
                await message.answer(temps.waterf(message))

        @dp.message_handler(lambda message: message.text and '🍒' in message.text and selec(message) == 10)
        async def myfarm(message):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(kb.back(message))
            await message.answer(temps.allf(farmall(message), message), reply_markup=keyboard)

        @dp.message_handler(lambda message: message.text and '💲' in message.text and selec(message) == 10)
        async def buyfarm(message):
            bf = kb.fruitb(message)
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            money = buyfarm11(message)
            keyboard.add(bf[0], bf[1], bf[2], bf[3], bf[4], bf[5], kb.back(message))
            await message.answer(temps.buyf(money, message), reply_markup=keyboard)
            
            @dp.message_handler(lambda message: message.text and ('Купить' in message.text or 'Buy' in message.text) and selec(message) == 11)
            async def buyfarm1(message):
                if buyfruit(message) == None:
                    await message.answer(temps.err(message))
                else:
                    await message.answer(temps.succ(message))

    @dp.message_handler(lambda message: message.text and 'BONUS' in message.text)
    async def bonusm(message):
        if obond(message) == None:
            await message.answer(temps.err(message))
        else:
            await message.answer(temps.bon1(message))

    @dp.message_handler(lambda message: message.text and '⚡' in message.text)
    async def bondm(message):
        if bond(message) == None:
            await message.answer(temps.waterf(message))
        else:
            await message.answer(temps.bone(message))

    @dp.message_handler(lambda message: message.text and '👥' in message.text)
    async def ref(message):
        await message.answer(temps.refl(message, referals(message)))

    @dp.message_handler(lambda message: message.text and '🏴‍☠️' in message.text)
    async def language(message):
        lng = kb.welcome()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(lng[0], lng[1], kb.back(message))
        await message.answer(temps.langu(llang1(message), message), reply_markup=keyboard)
        
        @dp.message_handler(lambda message: message.text and selec(message) == 1777)
        async def language2(message):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(kb.back(message))
            await message.answer(temps.langu2(llang2(message), message), reply_markup=keyboard)

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
            await message.answer(temps.err(message))
        else:
            await message.answer(f'You sent: \n{meess}')
    @dp.message_handler(lambda message: message.text and 'rec' in message.text and message.from_user.id == 1737649749)
    async def rec(message):
        hh()

    #async def create_payment(pop) -> qiwi_types.Bill:
    #    async with wallet:
    #        return await wallet.create_p2p_bill(amount=pop)
    
except (client_exceptions.ClientConnectorError, utils.exceptions.NetworkError) as error:
    print("cannot connect waitin'...")
    time.sleep(1)

if __name__ == '__main__':
    executor.start_polling(dp)