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
        self.assertEqual(funnyString("axby"), "Funny") 

if __name__ == '__main__':
    unittest.main()