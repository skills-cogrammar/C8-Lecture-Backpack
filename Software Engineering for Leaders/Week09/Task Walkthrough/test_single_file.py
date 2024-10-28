'''
Create a program that counts the number of even numbers in a list.
For example, [2, 1, 4, 5, 8] would return 3.
'''

def count_evens(num_list):

    # base case is when the list is empty
    if not num_list:
        return 0

    # Recursive case
    # Check if the first item is even or not
    if num_list[0] % 2 == 0:
        return 1 + count_evens(num_list[1:])
    else:
        return count_evens(num_list[1:])
   
'''
Use recursion to reverse a list. 
For example, [5, 6, 7, 8] will become [8, 7, 6, 5]
             ["a", "b", "c"] will become ["c", "b", "a"]

             
[5, 6, 7, 8]

[8] + reverse_list([5, 6, 7])
[8] + [7] + reverse_list([5, 6])
[8] + [7] + [6] + reverse_list([5])
[8] + [7] + [6] + [5] + reverse_list([])
[8, 7, 6, 5]
'''

def reverse_list(input_list):

    # Base case
    if not input_list:
        return []

    # Recursive case
    return [input_list[-1]] + reverse_list(input_list[:-1])

import unittest

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
        