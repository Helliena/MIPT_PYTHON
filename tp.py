import telebot
from telebot import types

tp_themes = [("Паттерны", "Patterns")]

tp_links = ["https://www.notion.so/8ff1a33000ad427da8214dc87f8723bf"]
  
def get_link_tp(theme):
    if theme == "Patterns":
        return tp_links[0]
 