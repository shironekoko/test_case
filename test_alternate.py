import unittest
from alternate import alternate

class TestAlternate(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(alternate("beabeefeab"), 5)
        self.assertEqual(alternate("a"), 0)
        self.assertEqual(alternate("abc"), 2)
        self.assertEqual(alternate("abac"), 3)
        self.assertEqual(alternate("ab"), 2)

    def test_edge_cases(self):
        self.assertEqual(alternate(""), 0)
        self.assertEqual(alternate("aa"), 0)
        self.assertEqual(alternate("abababab"), 8)
        self.assertEqual(alternate("aabbcc"), 0) 
        self.assertEqual(alternate("abcabcabc"), 6)

    def test_special_cases(self):
        self.assertEqual(alternate("a"*1000), 0)  
        self.assertEqual(alternate("ab"*500), 1000)  
        self.assertEqual(alternate("a"*500 + "b"*500), 0)  
if __name__ == '__main__':
    unittest.main()
