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