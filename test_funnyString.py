import unittest
from function import funnyString

class TestFunnyString(unittest.TestCase):
    def test_funny_cases(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("bcxz"), "Not Funny")
        self.assertEqual(funnyString("abcd"), "Funny")
        self.assertEqual(funnyString("a"), "Funny")
        self.assertEqual(funnyString("aa"), "Funny")

    def test_edge_cases(self):
        self.assertEqual(funnyString("zxcvbnmlkjhgfdsa"), "Not Funny")
        self.assertEqual(funnyString("zyxw"), "Funny")
        self.assertEqual(funnyString("axby"), "Not Funny")

    def test_additional_cases(self):
        self.assertEqual(funnyString("ab"), "Funny")
        self.assertEqual(funnyString("ba"), "Funny")
        self.assertEqual(funnyString("abc"), "Funny")
        self.assertEqual(funnyString("cba"), "Funny")
        self.assertEqual(funnyString("abcdcba"), "Funny")
        self.assertEqual(funnyString("abccba"), "Funny")

    def test_special_cases(self):
        self.assertEqual(funnyString(""), "Funny")  
        self.assertEqual(funnyString("a"*1000), "Funny")  
        self.assertEqual(funnyString("ab"*500), "Funny")

if __name__ == '__main__':
    unittest.main()