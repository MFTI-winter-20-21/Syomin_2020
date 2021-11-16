import telebot

bot = telebot.TeleBot('1421501275:AAHkZlZ6wW48mM9DGJhHAzePepxAftOPPtI')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
keyboard1.row('да', 'нет')



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне ?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'да':
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard2.row('Хуй на', 'Пакет говна')
        bot.send_message(message.chat.id, 'пизда', reply_markup=keyboard2)

    elif message.text.lower() == 'хуй на':
        bot.send_message(message.chat.id, 'Звезда')
        bot.send_message(message.chat.id, 'Слит, иди нахуй')

    elif message.text.lower() == 'пакет говна':
        bot.send_message(message.chat.id, 'Манда, всё иди к лебедям не трать моё время')

    elif message.text.lower() == 'нет':
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard3.row('Пидора ответ', 'Шлюхи аргумент')
        bot.send_message(message.chat.id, 'минет', reply_markup=keyboard3)

    elif message.text.lower() == 'пидора ответ':
        keyboard4 = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard4.row('Анал мой вечен, твой увы помечен')
        bot.send_message(message.chat.id, 'Пидор засекречен, твой анал не вечен', reply_markup=keyboard4)

    elif message.text.lower() == 'анал мой вечен, твой увы помечен':
        bot.send_message(message.chat.id, 'Мой замаскирован, твой уже разорван')
        bot.send_message(message.chat.id, 'соси лох тупой')

    elif message.text.lower() == 'шлюхи аргумент':
        bot.send_message(message.chat.id, 'Аргумент не вечен, в твоей жопе хуй овечий')

    elif message.text.lower() == 'абоба':
        bot.send_message(message.chat.id, 'Прости, но я не знаю, что ответить, поэтому быкану: Иди нахуй <3')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)
bot.polling()

if __name__ == '__main__':
    bot.infinity_polling()
