from langich import langich
import psycopg2
from psycopg2 import Error
from former import former

try:
    conn = psycopg2.connect(user="postgres",
                                password="iwasbornfree",
                                host="127.0.0.1",
                                port="5432",
                                database="luck")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

pho = 'https://imbt.ga/ZFdnBeO4pg'

class temps(object):
        def fl():
            return('Choose language\nВыберите язык')
        def inter(message):
            return(f'*Приветствую {message.from_user.id}♦* \nЭтот бот представляет собой игру-симулятор фермера\n\nВыбрав язык вы принимаете Пользовательское соглашение: telegra.ph/Polzovatelskoe-soglashenie-07-06\nВы также можете бонусный код, если его у вас нет введите BONUS\n\nУдачи!🍀\n\n*Welcome {message.from_user.id}♦*\nThis bot is a farming simulator\n\nBy choosing the language you accept the User Agreement: telegra.ph/Polzovatelskoe-soglashenie-07-06\nYou can also get a bonus, if you dont have one, enter BONUS\n\nGood luck!🍀\n{pho}')
        def intererr(message):
            return(f'*Reg. error, {message.from_user.id}!*')
        ###
        def market(message, plod, course):
            if langich(message) == "English":
                return(f'Here you can *exchange* your 🌟 to 💲 and 💸 to 💲\nFor exchange you have {plod} 🌟\n\nCurrent exchange course for 🌟 to 💲: \n1 🔄 = {course} 🌟\nFrom each *exchange* you will receive 70% 💲 and 30% 💸\n\nFor exchange 💸 to 💲 current course: 1 💸 = 1.3 💲')
            else:
                return(f'Здесь вы можете *обменять* ваши 🌟 на 💲 и 💸 на 💲\nУ вас для продажи {plod} 🌟\n\nТекущий курс для обмена 🌟 на 💲: \n1 🔄 = {course} 🌟\nС каждого *обмена* вы получите 70% 💲 и 30% 💸\n\nПри переводе 💸 на 💲 курс: 1 💸 = 1.3 💲')
        ###
        def main(message):
            return(f'*Приветствую {message.from_user.first_name}♦* \nВы находитесь в главном меню CoinLuck Game\n{pho}')
        ###
        def trans(id, message):
            if langich(message) == "English":
                return(f'Here you can *transfer* 💲 to other users by *id*. \nYour id: {id}\n\nTo transfer in a reply message, first enter *id*, then *transfer amount* separated by *space*.\nExample: 12 700\nYou can transfer one time from *10* 💲 to *10.000* 💲')
            else:
                return(f'Здесь вы можете *перевести* 💲 другим пользователям по *id*. \nВаш id: {id}\n\nДля перевода в ответном сообщении введите сначала *id* пользователя, затем *сумму перевода* через *пробел*.\nПример: 12 700\nЕдиноразово вы можете перевести от *10* 💲 до *10.000* 💲')
        def err(message):
            if langich(message) == "English":
                return('Error!')
            else:
                return('Ошибка!')
        def transsucc(message, plods, rubs, vivc, rub):
            if langich(message) == "English":
                return(f'*Done!*\n\nYou exchanged {plods} 🌟 to {rubs} 💲 and to {vivc} 💸\n\nYou have: {rub} 💲')
            else:
                return(f'*Готово!*\n\nВы обменяли {plods} 🌟 на {rubs} 💲 и на {vivc} 💸\n\nУ вас на балансе: {rub} 💲')
        def transerr(message):
            if langich(message) == "English":
                return(f'Not enough actives!')
            else:
                return(f'Недостаточно средств!')
        def transsucc2(message, vivc, rubs, rub):
            if langich(message) == "English":
                return(f'*Done!*\n\nYou exchanged {vivc} 💸 to {rubs} 💲\n\nYou have: {rub} 💲')
            else:
                return(f'*Готово!*\n\nВы обменяли {vivc} 💸 на {rubs} 💲\n\nУ вас на балансе: {rub} 💲')
        ###
        def choose(message):
            if langich(message) == "English":
                return('Select game')
            else:
                return('Выберите игру')
        ###
        def stavka13():
            return('Делайте *ставку*\n\nСтавка должна быть от 10 до 10.000\nВы также можете ввести свою сумму введя ее в ответном сообщении')
        def number13():
            return('Введите число от 1 до 3')
        def wrongent():
            return('Неверный ввод!')
        def normstavka():
            return('Ставка должна быть от 10 💲 до 10000 💲')
        def win13(stavka, money, keff, cc):
            return(f'*Поздравляем!👏*\nВаш выйгрыш: {stavka * 3} 💲\n\nВаш текущий баланс: {money} 💲\nВаша ставка: {stavka} 💲\n\nВаше число: {keff}\nВыпавшее число: {cc}')
        def lose13(keff, cc):
            return(f'Сожалеем, вы проиграли!\n\nВаше число:  {keff} \nЧисло:  {cc} ')
        def keffs():
            return('Введите коэффициент\nКоэффицент должен быть от 1.2 до 1000\n\nВведеная вами ставка обрежется до 2 нулей после точки\nПрим: 2.4235 > 2.42')
        def otri():
            return('Введите число от  1  до  30 \n\nПри выйгрыше вы получите *30x* от вашей ставки')
        def otrwin(stavka, money, keff, cc):
            return(f'Поздравляем!👏 \nВаш выйгрыш: {stavka * 30} 💲\n\nВаш текущий баланс   *{money} 💲*\nВаша ставка: {stavka} 💲\n\nВаше число: {keff}\nЧисло: {cc}')
        def otrlose(keff, cc):
            return(f'Сожалеем, вы проиграли!\n\nВаше число: {keff}\nЧисло: {cc}')
        def crashwin(keff, money, stavka, cc):
            return(f'Поздравляем!👏 \nВаш выйгрыш: {keff * stavka} 💲\n\nВаш текущий баланс   *{money} 💲*\nВаша ставка: *{stavka}* 💲\n\nВаш коэффицент: *{keff}*\nКоэффицент: {cc}')
        def crashlose(keff, cc):
            return(f'Сожалеем, вы проиграли!\n\nВаш коэффицент: {keff}\nКоэффицент: {cc}')
        def oirs(message):
            if langich(message) == "English":
                return ('*Choose a side*\n\nCoefficient for sides:\n\n*Tail/Head* 2x \n*Edge* 25x')
            else:
                return('*Выберите сторону*\n\nКоэффиценты для сторон:\n\n*Орел/Решка* 2x \n*Ребро* 25x')
        def oirep(wiin, money, rubb):
            return(f'{wiin} \n\nВаш текущий баланс *{money} 💲*\nВаша ставка: {rubb} 💲')
        def bal(money, vivc):
            return(f'Здесь вы можете пополнить или вывести ваш баланс\n\nВаш баланс для покупок: {money} 💲\nВаш баланс для вывода: {vivc} 💸')
        def pop():
            return('Введите сумму пополнения вашего счета (минимальная сумма пополнения 150 ₽)\n\nКурс:\n1 рубль = 100 💲\nПри пополнении 25% от суммы вашего пополнения станут 💵')
        def link():
            return('Ваша ссылка для пополнения')
        def viv():
            return('Введите сумму')
        def farm(all, plod):
            return(f'Это ваша небольшая горная ферма на севере Калифорнии у необычайно красивого берега \nЗдесь вы можете купить еще фруктовых растений или собрать спелые плоды \n\nУ вас на ферме {str(plod)} 🌟\n\nВ час вы зарабатываете {all} 🌟')
        def sbor(plod):
            return(f'Готово вы собрали {plod} 🌟!')    
        def allf(myplod):
            return(f'У вас: \n\n{myplod[2]} грядок клубники 🍓\n\n{myplod[3]} вишневых деревьев 🍒\n\n{myplod[4]} яблочных деревьев 🍎\n\n{myplod[5]} банановых деревьев 🍌\n\n{myplod[6]} персиковых деревьев 🍑\n\n{myplod[7]} виноградных деревьев 🍇')
        def buyf(money):
            return(f'Здесь вы можете купить растения на вашу ферму: \n\n🍓 - 1.000 💲\nПриносит 100 🌟 в час\n\n🍒 - 5.000 💲\nПриносит 600 🌟 в час\n\n🍎 - 25.000 💲\nПриносит 3.200 🌟 в час\n\n🍌 - 100.000 💲\nПриносит 14.000 🌟 в час\n\n🍑 - 500.000 💲\nПриносит 80.000 🌟 в час\n\n🍇 - 1.000.000 💲\nПриносит 200.000 🌟 в час \n\nУ вас на балансе: {former(money)} 💲')
        def succ():
            return('Успешно!')
        def bon1():
            return('Поздравляем!👏 Ваш бонус: 250 💲')
        def bone():
            return('Отлично!👏 Вы получили ваш ежедневный бонус на сумму 200 💲')
        def rev():
            return('Здесь вы можете прочитать или написать отзывы')
        def goodrev():
            return('В ответном сообщении вы можете оставить отзыв, за каждый качественный отзыв вы получите 50 💲')
        def refl(message, refff):
            return(f'Ваша реферальная ссылка: \nt.me/coinluck_bot?start={message.from_user.id} \n\nУ вас {refff} рефералов!')
        def transucc(mess, mon):
            return (f'*Готово!* Вы перевели пользователю *{mess[0]}*  {mon}  💲')
        def langu(l):
            return (f'Ваш текущий язык: {l}\nВы можете изменить его в любое время в этой вкладке.')
        def langu2(ll):
            return (f'Готово!\nВаш новый язык: {ll}')
        def winn(won, message):
            if langich(message) == "English":
                return f'Congrats!👏 \nYour winnings: {won} 💲'
            else:
                return f'Поздравляем!👏 \nВаш выйгрыш: {won} 💲'
        def orel(message):
            if langich(message) == "English":
                return 'Tail! \nYou lose'
            else:
                return 'Орел! \nВы проиграли'
        def edge(message):
            if langich(message) == "English":
                return 'Edge! \nYou lose'
            else:
                return 'Ребро! \nВы проиграли'
        def head(message):
            if langich(message) == "English":
                return 'Head! \nYou lose'
            else:
                return 'Решка! \nВы проиграли'
