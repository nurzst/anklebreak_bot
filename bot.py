import telebot
from telebot import types

TOKEN = "8305432442:AAFGczXJuA14ySRVbz2aDwnuWWcKdYeFMxk"
ADMIN_ID = 2139850377

bot = telebot.TeleBot(TOKEN)

cart = {}

# БАЗА ТОВАРОВ
products = {

"pants1":{
"name":"Штаны Suvene",
"price":8990,
"sizes":["S","M","L","XL","2XL"],
"category":"pants",
"photo":"pants1.jpg"
},

"pants2":{
"name":"Штаны Episode",
"price":7990,
"sizes":["S","M","L","XL"],
"category":"pants",
"photo":"pants2.jpg"
},

"pants3":{
"name":"Джинсы Classic",
"price":12990,
"sizes":["XXS","XS","S","M","L","XL","2XL"],
"category":"pants",
"photo":"pants3.jpg"
},

"pants4":{
"name":"Штаны Bershka",
"price":12990,
"sizes":["XS","S","M","L","XL"],
"category":"pants",
"photo":"pants4.jpg"
},

"hoodie1":{
"name":"Худи Polo Ralph Lauren",
"price":9990,
"sizes":["M","L","XL","2XL","3XL"],
"category":"hoodie",
"photo":"hoodie1.jpg"
},

"hoodie2":{
"name":"Zip-Худи Calvin Klein",
"price":9990,
"sizes":["M","L","XL","2XL","3XL"],
"category":"hoodie",
"photo":"hoodie2.jpg"
},

"hoodie3":{
"name":"Свитер Saint Lorant",
"price":9990,
"sizes":["S","M","L","XL","2XL"],
"category":"hoodie",
"photo":"hoodie3.jpg"
},

"hoodie4":{
"name":"Свитер Polo RL USA",
"price":10990,
"sizes":["S","M","L"],
"category":"hoodie",
"photo":"hoodie4.jpg"
},

"hoodie5":{
"name":"Черный Лонгслив Websur",
"price":7990,
"sizes":["S","M","L"],
"category":"hoodie",
"photo":"hoodie5.jpg"
},

"hoodie6":{
"name":"Белый Лонгслив Websur",
"price":7990,
"sizes":["S","M","L"],
"category":"hoodie",
"photo":"hoodie6.jpg"
},

"shirt1":{
"name":"Футболка CDG",
"price":5990,
"sizes":["XS","S","M","L","XL","2XL","3XL","4XL","5XL"],
"category":"shirts",
"photo":"tshirt1.jpg"
},

"shirt2":{
"name":"Футболка Polo RL",
"price":5990,
"sizes":["M","L","XL","2XL","3XL","4XL"],
"category":"shirts",
"photo":"tshirt2.jpg"
},

"acc1":{
"name":"Ремень LV",
"price":4500,
"sizes":["110см"],
"category":"accessories",
"photo":"acc1.jpg"
},

"jacket1":{
"name":"Ветровка Moncler Black",
"price":19990,
"sizes":["M","L","XL","2XL","3XL","4XL"],
"category":"jacket",
"photo":"jacket1.jpg"
},

"sneaker1":{
"name":"Maison Margiela Gats",
"price":17990,
"sizes":["37","38","39","40","41","42","43","44"],
"category":"sneakers",
"photo":"sneaker1.jpg"
},

"sneaker2":{
"name":"Golden Goose Super-Star",
"price":17990,
"sizes":["37","38","39","40","41","42","43","44"],
"category":"sneakers",
"photo":"sneaker2.jpg"
},

"sneaker3":{
"name":"Nike Air Force 1",
"price":15990,
"sizes":["37","38","39","40","41","42","43","44"],
"category":"sneakers",
"photo":"sneaker3.jpg"
},

"sneaker4":{
"name":"New Balance 1906D",
"price":17990,
"sizes":["37","38","39","40","41","42","43","44"],
"category":"sneakers",
"photo":"sneaker4.jpg"
},


}

# СТАРТ
@bot.message_handler(commands=['start'])
def start(message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add("🛍 Каталог")
    keyboard.add("🛒 Корзина")
    keyboard.add("📞 Контакты")

    bot.send_message(
        message.chat.id,
        "Добро пожаловать в AnkleBreakStore🔥",
        reply_markup=keyboard
    )

# КАТАЛОГ
@bot.message_handler(func=lambda message: message.text == "🛍 Каталог")
def catalog(message):

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton("👕 Футболки",callback_data="cat_shirts"))
    keyboard.add(types.InlineKeyboardButton("🧥 Кофты",callback_data="cat_hoodie"))
    keyboard.add(types.InlineKeyboardButton("👖 Штаны",callback_data="cat_pants"))
    keyboard.add(types.InlineKeyboardButton("🧥 Куртки",callback_data="cat_jacket"))
    keyboard.add(types.InlineKeyboardButton("🎒 Аксессуары",callback_data="cat_accessories"))
    keyboard.add(types.InlineKeyboardButton("👟Обувь",callback_data="cat_sneakers"))

    bot.send_message(message.chat.id,"Выберите категорию:",reply_markup=keyboard)

# ПОКАЗ КАТЕГОРИИ
@bot.callback_query_handler(func=lambda call: call.data.startswith("cat_"))
def show_category(call):

    category = call.data.split("_")[1]

    keyboard = types.InlineKeyboardMarkup()

    found = False

    for key, product in products.items():

        if product["category"] == category:

            keyboard.add(
                types.InlineKeyboardButton(
                    f"{product['name']} — {product['price']}₸",
                    callback_data=f"product_{key}"
                )
            )

            found = True

    if found:
        bot.send_message(call.message.chat.id,"Выберите товар:",reply_markup=keyboard)
    else:
        bot.send_message(call.message.chat.id,"Пока товаров нет")

# ПОКАЗ ТОВАРА
@bot.callback_query_handler(func=lambda call: call.data.startswith("product_"))
def show_product(call):

    key = call.data.split("_")[1]
    product = products[key]

    keyboard = types.InlineKeyboardMarkup()

    for size in product["sizes"]:

        keyboard.add(
            types.InlineKeyboardButton(
                size,
                callback_data=f"size_{key}_{size}"
            )
        )

    bot.send_photo(
        call.message.chat.id,
        open(product["photo"], "rb"),
        caption=f"{product['name']}\nЦена: {product['price']}₸\n\nВыберите размер:",
        reply_markup=keyboard
    )

# ДОБАВЛЕНИЕ В КОРЗИНУ
@bot.callback_query_handler(func=lambda call: call.data.startswith("size_"))
def add_to_cart(call):

    data = call.data.split("_")

    key = data[1]
    size = data[2]

    user = call.from_user.id

    if user not in cart:
        cart[user] = []

    cart[user].append({
        "name": products[key]["name"],
        "price": products[key]["price"],
        "size": size
    })

    bot.send_message(call.message.chat.id,"Товар добавлен в корзину 🛒")

# КОРЗИНА
@bot.message_handler(func=lambda message: message.text == "🛒 Корзина")
def show_cart(message):

    user = message.from_user.id

    if user not in cart or len(cart[user]) == 0:
        bot.send_message(message.chat.id,"Корзина пустая")
        return

    text = "Ваш заказ:\n\n"
    total = 0

    for item in cart[user]:

        text += f"{item['name']} ({item['size']}) — {item['price']}₸\n"
        total += item["price"]

    text += f"\nИтого: {total}₸"

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            "✅ Оформить заказ",
            callback_data="checkout"
        )
    )

    bot.send_message(message.chat.id,text,reply_markup=keyboard)

# ОФОРМЛЕНИЕ
@bot.callback_query_handler(func=lambda call: call.data == "checkout")
def checkout(call):

    user = call.from_user.id
    username = call.from_user.username
    first_name = call.from_user.first_name

    if username:
        buyer = f"@{username}"
    else:
        buyer = first_name

    text = "🔥 НОВЫЙ ЗАКАЗ\n\n"

    total = 0

    for item in cart[user]:

        text += f"{item['name']} ({item['size']}) — {item['price']}₸\n"
        total += item["price"]

    text += f"\nИтого: {total}₸\n\n"
    text += f"Покупатель: {buyer}\n"
    text += f"ID: {user}"

    bot.send_message(ADMIN_ID, text)

    bot.send_message(
        call.message.chat.id,
        "Заказ оформлен ✅\n\nОплата Kaspi:\n+7 705 303 8427"
    )

    cart[user] = []

# КОНТАКТЫ
@bot.message_handler(func=lambda message: message.text == "📞 Контакты")
def contacts(message):

    text = "Наш Менеджер: @sharastolica, обращайтесь при проблемах и вопросах"

    bot.send_message(message.chat.id,text)

bot.polling()
