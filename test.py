import unittest

from dsa import dsa_themes
from oop import oop_themes
from tp import tp_themes
from main import syllabus, get_link

class TestResponse(unittest.TestCase):
    def test_syllabus_dsa(self):
        self.assertEqual(syllabus("DSA") == dsa_themes)
    def test_syllabus_oop(self):
        self.assertEqual(syllabus("OOP") == oop_themes)
    def test_syllabus_tp(self):
        self.assertEqual(syllabus("TP") == tp_themes)
    def test_syllabus_random(self):
        self.assertEqual(syllabus("Python") == [])

    def test_get_link_case1(self):
        self.assertTrue(get_link("BinSearch") == "https://www.notion.so/24d8a01af8b6493aad5a25798145e0bc")
    def test_get_link_case2(self):
        self.assertTrue(get_link("CE, RE, UB") == "https://www.notion.so/CE-RE-UB-0d59d0beafc845c9968b660879d39c49")
    def test_get_link_case3(self):
        self.assertTrue(get_link("BotAPI") == "None")
    def test_get_link_case4(self):
        self.assertTrue(get_link("Patterns") == "https://www.notion.so/8ff1a33000ad427da8214dc87f8723bf")

