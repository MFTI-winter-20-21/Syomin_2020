import telebot

bot = telebot.TeleBot('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1] )

bot.polling()
