import telebot
from telebot import types

from dsa import dsa_themes, get_link_dsa
from oop import oop_themes, get_link_oop
from tp import tp_themes, get_link_tp

bot = telebot.TeleBot('1852941096:AAFi6b0dWRnm7B4VDsBlg1Bl9cIwQLXKICs');

@bot.message_handler(commands=['start'])
def start_command(message):
    themes = [("Алогритмы и структуры данных", "DSA"), ("Программирование на С++", "OOP"), ("Технологии программирования", "TP"), ("Другое", "Another")]
    keyboard = types.InlineKeyboardMarkup();
    for i in themes:
        keyboard.add(types.InlineKeyboardButton(i[0], callback_data=i[1]))
    bot.send_message(message.from_user.id, "Привет! Для того, чтобы начать изучение программирования выбери интересующий тебя раздел: ", reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)    
def callback_worker(call):
    if call.data in ["DSA", "OOP", "TP", "Another"]:
        tag = call.data
        if tag == "Another":
            bot.send_message(call.from_user.id, "Другие темы ещё находятся в разработке. Приходи позже!")
        else:
            theme = syllabus(tag)
            keyboard = types.InlineKeyboardMarkup();
            for i in theme:
                keyboard.add(types.InlineKeyboardButton(i[0], callback_data=i[1]))
            bot.send_message(call.message.chat.id, text = "Выбери тему: ", reply_markup=keyboard)
    else:
        theme = call.data
        bot.send_message(call.message.chat.id, text = "Ссылка на материалы: " + get_link(theme))
     

def syllabus(tag):
    tags = []
    if tag == "DSA":
        tags = dsa_themes
    elif tag == "OOP":
        tags = oop_themes
    elif tag == "TP":
        tags = tp_themes
    return tags

def get_link(theme):
    if get_link_dsa(theme) != None:
        return get_link_dsa(theme)
    elif get_link_oop(theme) != None:
        return get_link_oop(theme)
    elif get_link_tp(theme) != None:
        return get_link_tp(theme)
    return str(None)


bot.polling(none_stop=True, interval=0)   