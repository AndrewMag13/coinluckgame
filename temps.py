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

class temps:
        def fl():
            return('Choose language\nВыберите язык')
        def inter(message):
            return(f'''*Приветствую {message.from_user.id}♦* 
            \nЭтот бот представляет собой игру-симулятор фермера\n\nВыбрав язык вы принимаете Пользовательское соглашение: telegra.ph/Polzovatelskoe-soglashenie-07-06\nВы также можете бонусный код, если его у вас нет введите BONUS\n\nУдачи!🍀\n\n*Welcome {message.from_user.id}♦*
            \nThis bot is a farming simulator\n\nBy choosing the language you accept the User Agreement: telegra.ph/Polzovatelskoe-soglashenie-07-06\nYou can also get a bonus, if you dont have one, enter BONUS\n\nGood luck!🍀\n{pho}''')
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
            if langich(message) == "English":
                return(f'*Hello {message.from_user.first_name}♦* \nYou are now in CoinLuck Game main menu\n{pho}')
            else:
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
        def stavka13(message):
            if langich(message) == "English":
                return('Place your *bet*\n\Bet must be from 10 💲 to 10000 💲\nYou can also enter custom bet in reply message')
            else:
                return('Делайте *ставку*\n\nСтавка должна быть от 10 💲 до 10.000 💲\nВы также можете ввести свою сумму введя ее в ответном сообщении')
        def number13(message):
            if langich(message) == "English":
                return('Enter number from 1 to 3')
            else:
                return('Введите число от 1 до 3')
        def wrongent(message):
            if langich(message) == "English":
                return('Wrong enter!')
            else:
                return('Неверный ввод!')
        def normstavka(message):
            if langich(message) == "English":
                return('Bet must be from 10 💲 to 10000 💲')
            else:
                return('Ставка должна быть от 10 💲 до 10000 💲')
        def win13(stavka, money, keff, cc, message):
            if langich(message) == "English":
                return(f'*Congratulations!👏*\nYour winnings: {stavka * 3} 💲\n\nYour current balance: {money} 💲\nYour bet: {stavka} 💲\n\nYour number: {keff}\nActual number: {cc}')
            else:  
                return(f'*Поздравляем!👏*\nВаш выйгрыш: {stavka * 3} 💲\n\nВаш текущий баланс: {money} 💲\nВаша ставка: {stavka} 💲\n\nВаше число: {keff}\nВыпавшее число: {cc}')
        def lose13(keff, cc, message):
            if langich(message) == "English":
                return(f'Sorry, you lose!\n\nYour number: {keff}\nActual number: {cc}')
            else:
                return(f'Сожалеем, вы проиграли!\n\nВаше число: {keff}\nЧисло: {cc}')
        def keffs(message):
            if langich(message) == "English":
                return('Enter coefficient\nCoefficient must be from 1.2 to 1000\n\nEntered coefficient will be truncate to 2 zeros after point\nExample: 2.4235 > 2.42')
            else:
                return('Введите коэффициент\nКоэффицент должен быть от 1.2 до 1000\n\nВведенный вами коэффицент обрежется до 2 нулей после точки\nПример: 2.4235 > 2.42')
        def otri(message):
            if langich(message) == "English":
                return('Enter number from 1 to 30\n\nIf you win you will get *30x* from your bet')
            else:
                return('Введите число от 1 до 30\n\nПри выйгрыше вы получите *30x* от вашей ставки')
        def otrwin(stavka, money, keff, cc, message):
            if langich(message) == "English":
                return(f'Congratulations!👏 \nYour winnings: {stavka * 30} 💲\n\nYour current balance *{money} 💲*\nYour bet: {stavka} 💲\n\nYour number: {keff}\nActual nubmer: {cc}')
            else:
                return(f'Поздравляем!👏 \nВаш выйгрыш: {stavka * 30} 💲\n\nВаш текущий баланс *{money} 💲*\nВаша ставка: {stavka} 💲\n\nВаше число: {keff}\nЧисло: {cc}')
        def otrlose(keff, cc, message):
            if langich(message) == "English":
                return(f'Sorry, you lose!\n\nYour number: {keff}\nActual number: {cc}')
            else:
                return(f'Сожалеем, вы проиграли!\n\nВаше число: {keff}\nЧисло: {cc}')
        def crashwin(keff, money, stavka, cc, message):
            if langich(message) == "English":
                return(f'Congratulations!👏\nYour winnings: {keff * stavka} 💲\n\nYour current balance: *{money} 💲*\nYour bet: *{stavka}* 💲\n\nYour coefficient: *{keff}*\nActual coefficient: {cc}')
            else:
                return(f'Поздравляем!👏\nВаш выйгрыш: {keff * stavka} 💲\n\nВаш текущий баланс: *{money} 💲*\nВаша ставка: *{stavka}* 💲\n\nВаш коэффицент: *{keff}*\nКоэффицент: {cc}')
        def crashlose(keff, cc, message):
            if langich(message) == "English":
                return(f'Sorry, you lose!\n\nYour coefficient: {keff}\nActual coefficient: {cc}')
            else:
                return(f'Сожалеем, вы проиграли!\n\nВаш коэффицент: {keff}\nКоэффицент: {cc}')
        def oirs(message):
            if langich(message) == "English":
                return ('*Choose a side*\n\nCoefficient for sides:\n\n*Tail/Head* 2x \n*Edge* 25x')
            else:
                return('*Выберите сторону*\n\nКоэффиценты для сторон:\n\n*Орел/Решка* 2x \n*Ребро* 25x')
        def oirep(wiin, money, rubb, message):
            if langich(message) == "English":
                return(f'{wiin}\n\nYour current balance:*{money} 💲*\nYour bet: {rubb} 💲')
            else:
                return(f'{wiin}\n\nВаш текущий баланс: *{money} 💲*\nВаша ставка: {rubb} 💲')
        def bal(money, vivc, message):
            if langich(message) == "English":
                return(f'Here you can top-up or withdraw your balance\n\nYour balance for shopping: {money} 💲\nYour balance for withdraw: {vivc} 💸')
            else:
                return(f'Здесь вы можете пополнить или вывести ваш баланс\n\nВаш баланс для покупок: {money} 💲\nВаш баланс для вывода: {vivc} 💸')
        def pop(message):
            if langich(message) == "English":
                return("Enter the amount to top-up your account (minimal amount to top-up is 150 ₽)\n\nCourse:\n1 ₽ = 100 💲\n25 % of the amount of your top-up will become 💵")
            else:
                return('Введите сумму пополнения вашего счета (минимальная сумма пополнения 150 ₽)\n\nКурс:\n1 рубль = 100 💲\nПри пополнении 25% от суммы вашего пополнения станут 💵')
        def link(message):
            if langich(message) == "English":
                return('Your top-up link')
            else:
                return('Ваша ссылка для пополнения')
        def farm(all, plod, message):
            if langich(message) == "English":
                return(f'Thats your moderate mountain farm in the north of California by an extraordinarily beautiful rocky coast\nHere you can buy more fruit plants or collect ripe fruits\n\nOn your farm {str(plod)} 🌟\n\nYou earn {all} 🌟 per hour')
            else:
                return(f'Это ваша небольшая горная ферма на севере Калифорнии у необычайно красивого берега\nЗдесь вы можете купить еще фруктовых растений или собрать спелые плоды\n\nУ вас на ферме {str(plod)} 🌟\n\nВ час вы зарабатываете {all} 🌟')
        def sbor(plod, message):
            if langich(message) == "English":
                return(f'Done! You collect {plod} 🌟!')
            else:
                return(f'Готово вы собрали {plod} 🌟!')
        def water(message):
            if langich(message) == "English":
                return('Great! You watered your plants.\nWatering gives you a 1.2x for all your plants.\nThe bonus works until the beginning of the next hour and available only once a day')
            else:
                return('Отлично! Вы полили ваши растения.\nПоливка растений дает вам 1.2 множитель для всех ваших растений.\nБонус работает до начала следующего часа и доступен раз в день')
        def waterf(message):
            if langich(message) == "English":
                return('The bonus available only once a day')
            else:
                return('Бонус доступен только раз в день')
        def allf(myplod, message):
            if langich(message) == "English":
                return(f'You have: \n\n{myplod[2]} beds of strawberry 🍓\n\n{myplod[3]} cherry trees 🍒\n\n{myplod[4]} apple trees🍎\n\n{myplod[5]} banana trees 🍌\n\n{myplod[6]} peach trees 🍑\n\n{myplod[7]} grape trees 🍇')
            else:
                return(f'У вас: \n\n{myplod[2]} грядок клубники 🍓\n\n{myplod[3]} вишневых деревьев 🍒\n\n{myplod[4]} яблочных деревьев 🍎\n\n{myplod[5]} банановых деревьев 🍌\n\n{myplod[6]} персиковых деревьев 🍑\n\n{myplod[7]} виноградных деревьев 🍇')
        def buyf(money, message):
            if langich(message) == "English":
                return(f'Here you can buy plants for your farm: \n\n🍓 - 1.000 💲\nBrings 100 🌟 per hour\n\n🍒 - 5.000 💲\nBrings 600 🌟 per hour\n\n🍎 - 25.000 💲\nBrings 3.200 🌟 per hour\n\n🍌 - 100.000 💲\nBrings 14.000 🌟 per hour\n\n🍑 - 500.000 💲\nBrings 80.000 🌟 per hour\n\n🍇 - 1.000.000 💲\nBrings 200.000 🌟 per hour\n\nYour balance: {former(money)} 💲')
            else:
                return(f'Здесь вы можете купить растения на вашу ферму: \n\n🍓 - 1.000 💲\nПриносит 100 🌟 в час\n\n🍒 - 5.000 💲\nПриносит 600 🌟 в час\n\n🍎 - 25.000 💲\nПриносит 3.200 🌟 в час\n\n🍌 - 100.000 💲\nПриносит 14.000 🌟 в час\n\n🍑 - 500.000 💲\nПриносит 80.000 🌟 в час\n\n🍇 - 1.000.000 💲\nПриносит 200.000 🌟 в час\n\nУ вас на балансе: {former(money)} 💲')
        def succ(message):
            if langich(message) == "English":
                return('Success!')
            else:
                return('Успешно!')
        def bon1(message):
            if langich(message) == "English":
                return('Congratulations!👏 Your bonus: 250 💲')
            else:
                return('Поздравляем!👏 Ваш бонус: 250 💲')
        def bone(message):
            if langich(message) == "English":
                return('Great!👏 You have received your daily bonus in the amount of 200 💲')
            else:
                return('Отлично!👏 Вы получили ваш ежедневный бонус на сумму 200 💲')
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
        def refl(message, refff):
            if langich(message) == "English":
                return(f'Your referal link: \nt.me/coinluck_bot?start={message.from_user.id} \n\nYou have {refff} referals!')
            else:
                return(f'Ваша реферальная ссылка: \nt.me/coinluck_bot?start={message.from_user.id} \n\nУ вас {refff} рефералов!')
        def transucc(mess, mon, message):
            if langich(message) == "English":
                return (f'*Done!* You transfer user *{mess[0]}* {mon} 💲')
            else:
                return (f'*Готово!* Вы перевели пользователю *{mess[0]}* {mon} 💲')
        def langu(l, message):
            if langich(message) == "English":
                return (f'Your current language: {l}\nHere you can change it anytime.')
            else:
                return (f'Ваш текущий язык: {l}\nВы можете изменить его в любое время в этой вкладке.')
        def langu2(ll, message):
            if langich(message) == "English":
                return (f'Done!\nYour new language: {ll}')
            else:
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
