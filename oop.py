import telebot
from telebot import types

oop_themes = [("Введение", "Introduction"), ("CE, RE, UB", "Behavior"), ("Основные типы", "Types")]

oop_links = ["https://www.notion.so/e0e0fb3a2b2a41cab75d8af5761631c4", 
             "https://www.notion.so/CE-RE-UB-0d59d0beafc845c9968b660879d39c49",
             "https://www.notion.so/d561b2826d3e41cb833336cbb28c8ed5"]
  
def get_link_oop(theme):
    if theme == "Introduction":
        return oop_links[0]
    elif theme == "Behavior":
        return oop_links[1]
    elif theme == "Types":
        return oop_links[2]
