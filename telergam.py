import telebot
from telebot import types

bot = telebot.TeleBot('1421501275:AAHkZlZ6wW48mM9DGJhHAzePepxAftOPPtI')

@bot.message_handler(commands=['help', 'start'])

def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('1', '2')
    msg = bot.reply_to(message, 'Test text', reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)

def process_step(message):
    chat_id = message.chat.id
    if message.text == '1':
        bot.send_message(message.chat.id, 'Отъебитесь от меня нахуй сука, ну у меня тиииильт блять...')
    else:
        bot.send_message(message.chat.id, 'egegsgsg')
