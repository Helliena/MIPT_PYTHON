import telebot
from telebot import types


dsa_themes = [("Разложение на множители и приложения", "FindDividers"), ("Бинарный поиск", "BinSearch"), ("Алгоритм быстрого возведения числа в степень", "BinPow"),
                  ("Два указателя", "TwoPointers"), ("Сортировка подсчётом", "CountSort"), ("Сорировка Слиянием", "MergeSort")]

dsa_links = ["https://www.notion.so/12570eb7adbc44249f21ea4309a1327b", 
             "https://www.notion.so/24d8a01af8b6493aad5a25798145e0bc",
             "https://www.notion.so/e96201bfc3e341798122bfcb4fe088ef",
             "https://www.notion.so/32e8f653822a4d589dbbd0fcfccc40fb",
             "https://www.notion.so/46d3e2e410b44b998ecd69d4c42b2107",
             "https://www.notion.so/1aca050c2e0044f1bf4b269ecbd2b2de"]
  
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
