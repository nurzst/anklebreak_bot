import telebot
from telebot import types

TOKEN = "8305432442:AAFGczXJuA14ySRVbz2aDwnuWWcKdYeFMxk"

bot = telebot.TeleBot(TOKEN)

# СТАРТ
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Каталог")
    btn2 = types.KeyboardButton("Контакты")

    markup.add(btn1, btn2)

    bot.send_message(
        message.chat.id,
        "Добро пожаловать в магазин ANKLEBREAK 🔥",
        reply_markup=markup
    )


# СООБЩЕНИЯ
@bot.message_handler(content_types=['text'])
def message(message):

    if message.text == "Каталог":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Штаны")
        btn2 = types.KeyboardButton("Кофты")
        btn3 = types.KeyboardButton("Назад")

        markup.add(btn1, btn2, btn3)

        bot.send_message(
            message.chat.id,
            "Выберите категорию:",
            reply_markup=markup
        )


    elif message.text == "Штаны":

        text = """
ШТАНЫ 👖

1️⃣ Штаны Suvene
Цвета: Черный, Серый
Размеры: S–2XL
Цена: 8.990 тг

2️⃣ Штаны Episode
Цвета: Черный, Серый
Размеры: S–XL
Цена: 7.990 тг

3️⃣ Джинсы Сакура 1
Цвет: Черный
Размеры: S–2XL
Цена: 8.990 тг

4️⃣ Джинсы Dime
Цвета: Черный, Синий, Белый, Голубой
Размеры: 3XS–XL
Цена: 9.990 тг
"""

        bot.send_message(message.chat.id, text)


    elif message.text == "Кофты":

        text = """
КОФТЫ 🧥

1️⃣ Zip-Худи Suvene
Цвета: Черный, Серый
Размеры: S–2XL
Цена: 9.990 тг

2️⃣ Худи ANKLBRK
Цвета: Черный, Серый, Темно-синий, Светло-серый
Размеры: M–2XL
Цена: 9.990 тг

3️⃣ Zip-худи Broken Planet
Цвета: Черный (черный принт), Черный (белый принт), Серый, Камуфляж, Коричневый, Бежевый, Розовый
Размеры: S–XL
Цена: 11.990 тг

4️⃣ Свитер Saint Lorant
Цвет: Черный
Размеры: S–2XL
Цена: 9.990 тг
"""

        bot.send_message(message.chat.id, text)


    elif message.text == "Контакты":

        bot.send_message(
            message.chat.id,
            "Для заказа напишите менеджеру:\n@anklebreakstore"
        )


    elif message.text == "Назад":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Каталог")
        btn2 = types.KeyboardButton("Контакты")

        markup.add(btn1, btn2)

        bot.send_message(
            message.chat.id,
            "Главное меню",
            reply_markup=markup
        )


bot.polling()