import telebot
from telebot import types

oop_themes = [("Разложение на множители и приложения", "FindDividers"), ("Бинарный поиск", "BinSearch"), (" Алгоритм быстрого возведения числа в степень", "BinPow"),
              ("Два указателя", "TwoPointers"), ("Сортировка подсчётом", "CountSort"), ("Сорировка Слиянием", )]

oop_links = ["https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2", 
             "https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2",
             "https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2",
             "https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2",
             "https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2",
             "https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2"]
  
def get_link_oop(theme):
    if theme == "FindDividers":
        return oop_links[0]
    elif theme == "BinSearch":
        return oop_links[1]
    elif theme == "BinPow":
        return oop_links[2]
    elif theme == "TwoPointers":
        return oop_links[3]
    elif theme == "CountSort":
        return oop_links[4]
    elif theme == "MergeSort":
        return oop_links[5]
