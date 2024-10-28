import unittest
from recursion_examples import count_evens, reverse_list

class TestRecursionFunctions(unittest.TestCase):

    # Testing count_evens 
    def test_even_and_odd_numbers(self):
        self.assertEqual(count_evens([1, 2, 3, 4, 5]), 2)

    def test_only_odd_numbers(self):
        self.assertEqual(count_evens([1, 3, 5, 7]), 0)
    
    def test_empty_list(self):
        self.assertEqual(count_evens([]), 0)

if __name__ == '__main__':
    unittest.main()
        