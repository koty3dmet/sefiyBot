import telebot 
from telebot import types

Token = '7321517765:AAExVV6IG4Xv5uBodM_4TX_DSHhM9UotxsI'
bot = telebot.TeleBot(Token)
bal = 0

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_prof = types.KeyboardButton("Профиль")
    markup.add(btn_prof)
    bot.send_message(message.from_user.id, "Добро пожаловать в sefiyBot \n\n1 Задание: \nиспользуй команду 'профиль'\n --------------------------------", reply_markup=markup)

a = 'lvl1'

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Профиль":
        text_bal = f'твой баланс:\n', bal, 'sF'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_work = types.KeyboardButton("Работы")
        btn_prof = types.KeyboardButton("Профиль")
        markup.add(btn_prof, btn_work)
        str(bal)
        bot.send_message(message.from_user.id, text_bal)
        bot.send_message(message.from_user.id, "Отлично!\n2 Задание:\n\n Посмотри доступные работы(комнада Работы)\n --------------------------------", reply_markup=markup)

    if message.text == 'Работы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_mth = types.KeyboardButton("Счет")
        btn_bck = types.KeyboardButton("Назад")
        markup.add(btn_mth, btn_bck)
        bot.send_message(message.from_user.id, 'Выбери что тебя интересует:\n', reply_markup=markup)

        if message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_work = types.KeyboardButton("Работы")
            btn_prof = types.KeyboardButton("Профиль")
            markup.add(btn_prof, btn_work)
            bot.send_message(message.from_user.id, text_bal)
            bot.send_message(message.from_user.id, "Выбери что тебе нужно:", reply_markup=markup)

bot.polling(none_stop=True,  interval=0)