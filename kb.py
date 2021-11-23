from langich import langich
class kb:
    def welcome():
        return('English', 'Русский')
    def start(message):
        if langich(message) == "English":
            return('▶ Games', '🌄 Farm', '🔄 Market', '💼 Balance', '💱 Transfer', '⚡ Daily bonus', '💭 Messenger', '👥 Referals', '🏴‍☠️ Language')
        else:
            print(langich(message))
            return('▶ Играть', '🌄 Ферма', '🔄 Рынок', '💼 Баланс', '💱 Перевод', '⚡ Ежедневный бонус', '💭 Мессенджер', '👥 Рефералы', '🏴‍☠️ Язык')
    def ots():
        return ('10 💲', '50 💲', '100 💲', '250 💲', '500 💲', '750 💲','1000 💲','1250 💲','1500 💲')
    def back(message):
        if langich(message) == "English":
            return('👈 Back')
        else:
            return('👈 Назад')
    def repeat(message):
        if langich(message) == "English":
            return('Repeat')
        else:
            return('Повторить')
    def keff():
        return ('1.25', '1.5', '2', '3', '5', '10', '20')
    def nums():
        return ('1', '2', '3', '4', '5', '10')
    def games(message):
        if langich(message) == "English":
            return ('Heads and Tails', 'Busta', '1/3', '1/30')
        else:
            return ('Орел и Решка', 'Краш', '1/3', '1/30')
    def oir(message):
        if langich(message) == "English":
            return ('Tail', 'Head', 'Edge')
        else:
            return ('Орел', 'Решка', 'Ребро')
    def popb(message):
        if langich(message) == "English":
            return ('⬇ Top-up')
        else:
            return ('⬇ Пополнить баланс')
    def popm():
        return ('150 ₽', '300 ₽', '500 ₽','1000 ₽')
    def fruit(message):
        if langich(message) == "English":
            return ('💲 Buy plants', '🍒 My plants', '🌊 Water plants', '✂ Collect')
        else:
            return ('💲 Купить растения', '🍒 Мои растения', '🌊 Полить растения', '✂ Собрать')
    def fruitb(message):
        if langich(message) == "English":
            return ('Buy 🍓', 'Buy 🍒', 'Buy 🍎', 'Buy 🍌', 'Buy 🍑', 'Buy 🍇')
        else:
            return ('Купить 🍓', 'Купить 🍒', 'Купить 🍎', 'Купить 🍌', 'Купить 🍑', 'Купить 🍇')
    def fruitbv(message):
        if langich(message) == "English":
            return ('Buy 🍓', 'Buy 🍒', 'Buy 🍎', 'Buy 🍌', 'Buy 🍑', 'Buy 🍇')
        else:
            return ('Купить 🍓', 'Купить 🍒', 'Купить 🍎', 'Купить 🍌', 'Купить 🍑', 'Купить 🍇')
    def rev(message):
        if langich(message) == "English":
            return ('Messages', 'Friends')
        else:
            return ('Сообщения', 'Друзья')
    def tr(message):
        if langich(message) == "English":
            return ('Exchange 🌟 to 💲', 'Exchange 💸 to 💲')
        else:
            return ('Обменять 🌟 на 💲', 'Обменять 💸 на 💲')