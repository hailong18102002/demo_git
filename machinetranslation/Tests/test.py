import unittest
from translator import englishToFrench, frenchToEnglish

class Testfrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

        
class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("hello"), "bonjour")


unittest.main()