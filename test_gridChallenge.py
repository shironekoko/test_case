import unittest
from gridChal import gridChallenge

class TestGridChallenge(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES")
        self.assertEqual(gridChallenge(["abc", "lmp", "qrt"]), "YES")
        self.assertEqual(gridChallenge(["mpxz", "abcd", "wlmf"]), "NO")
        self.assertEqual(gridChallenge(["abc", "hjk", "mpq"]), "YES")
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "YES")

    def test_edge_cases(self):
        self.assertEqual(gridChallenge(["a"]), "YES")  
        self.assertEqual(gridChallenge(["z", "y", "x"]), "NO")  
        self.assertEqual(gridChallenge(["a", "b", "c"]), "YES") 
        self.assertEqual(gridChallenge(["cba", "fed", "ihg"]), "YES") 
        self.assertEqual(gridChallenge(["aaa", "aaa", "aaa"]), "YES")  

    def test_large_case(self):
        grid = ["abcd" * 25] * 100  
        self.assertEqual(gridChallenge(grid), "YES")

if __name__ == '__main__':
    unittest.main()
