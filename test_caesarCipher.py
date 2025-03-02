import unittest
from caesarCipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(caesarCipher("abc", 3), "def")
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")
        self.assertEqual(caesarCipher("hello", 1), "ifmmp")
        self.assertEqual(caesarCipher("hello world!", 1), "ifmmp xpsme!")

    def test_edge_cases(self):
        self.assertEqual(caesarCipher("a", 26), "a")
        self.assertEqual(caesarCipher("a", 0), "a")
        self.assertEqual(caesarCipher("A", 1), "B")
        self.assertEqual(caesarCipher("Z", 1), "A")
        self.assertEqual(caesarCipher("z", 1), "a")
        self.assertEqual(caesarCipher("12345", 5), "12345")

    def test_large_shift(self):
        self.assertEqual(caesarCipher("abc", 30), "efg")

    def test_special_characters(self):
        self.assertEqual(caesarCipher("!@#$", 5), "!@#$")
        self.assertEqual(caesarCipher("hello, world!", 5), "mjqqt, btwqi!")

if __name__ == '__main__':
    unittest.main()
