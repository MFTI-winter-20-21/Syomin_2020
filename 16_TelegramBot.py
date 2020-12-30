import telebot

bot = telebot.TeleBot('1421501275:AAHkZlZ6wW48mM9DGJhHAzePepxAftOPPtI')

@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, "Hello World")

bot.polling()
