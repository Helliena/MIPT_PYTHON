import telebot
from telebot import types


dsa_themes = [("Разложение на множители и приложения", "FindDividers"), ("Бинарный поиск", "BinSearch"), ("Алгоритм быстрого возведения числа в степень", "BinPow"),
                  ("Два указателя", "TwoPointers"), ("Сортировка подсчётом", "CountSort"), ("Сорировка Слиянием", "MergeSort")]

dsa_links = ["https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2", 
             "https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2",
             "https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2",
             "https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2",
             "https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2",
             "https://www.notion.so/Programming-Technologies-Seminar-Course-e3cebd23e48b4125972e2569664166b2"]
  
def get_link_dsa(theme):
    if theme == "FindDividers":
        return dsa_links[0]
    elif theme == "BinSearch":
        return dsa_links[1]
    elif theme == "BinPow":
        return dsa_links[2]
    elif theme == "TwoPointers":
        return dsa_links[3]
    elif theme == "CountSort":
        return dsa_links[4]
    elif theme == "MergeSort":
        return dsa_links[5]
