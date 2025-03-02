import unittest
from alterchar import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):

    def test_alternating(self):
        self.assertEqual(alternatingCharacters("ababab"), 0)
        self.assertEqual(alternatingCharacters("abab"), 0)
        self.assertEqual(alternatingCharacters("a"), 0)
        self.assertEqual(alternatingCharacters("b"), 0)

    def test_non_alternating(self):
        self.assertEqual(alternatingCharacters("aaabaaaa"), 5)
        self.assertEqual(alternatingCharacters("bbbb"), 3)
        self.assertEqual(alternatingCharacters("aaaaa"), 4)
        self.assertEqual(alternatingCharacters("aabb"), 2)

    def test_edge_cases(self):
        self.assertEqual(alternatingCharacters(""), 0)
        self.assertEqual(alternatingCharacters("bbbbbb"), 5)
        self.assertEqual(alternatingCharacters("abababab"), 0)

    def test_mixed_cases(self):
        self.assertEqual(alternatingCharacters("aab"), 1)
        self.assertEqual(alternatingCharacters("ababa"), 0)
        self.assertEqual(alternatingCharacters("abbab"), 1)
        self.assertEqual(alternatingCharacters("abcba"), 0)  # Corrected expected result

if __name__ == '__main__':
    unittest.main()