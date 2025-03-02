import unittest
from primelist import is_prime_list

class TestIsPrimeList(unittest.TestCase):

    def test_all_primes(self):
        self.assertTrue(is_prime_list([2, 3, 5, 7, 11]))
        self.assertTrue(is_prime_list([13, 17, 19, 23, 29]))

    def test_contains_non_prime(self):
        self.assertFalse(is_prime_list([2, 3, 4, 5, 7])) 
        self.assertFalse(is_prime_list([10, 11, 13, 17]))  

    def test_empty_list(self):
        self.assertTrue(is_prime_list([])) 

    def test_contains_one_or_zero(self):
        self.assertFalse(is_prime_list([0, 1, 2, 3])) 
        self.assertFalse(is_prime_list([1])) 
    def test_large_numbers(self):
        self.assertTrue(is_prime_list([101, 103, 107, 109]))
        self.assertFalse(is_prime_list([101, 104, 107, 109]))  

if __name__ == '__main__':
    unittest.main()
