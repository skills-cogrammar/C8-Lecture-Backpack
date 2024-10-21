""" Keep the FIRST principles in mind while creating the tests.

Fast: Tests execute quickly with minimal setup.
Independent: Each test operates in isolation with its own setup.
Repeatable: Results are consistent across runs with fixed inputs.
Self-Validating: Each test asserts expected outcomes clearly.
Timely: Tests are developed alongside or before the implementation.

"""
import unittest
from c08_sel_w08l01_demo_code_examples import (
    sum_list, 
    get_middle_of_list, 
    get_all_students_average, 
    recursive_word_flip
)

class TestSumList(unittest.TestCase):
    
    def setUp(self):
        # This method is called before each test
        # Initialising test data
        # Arrange
        self.single_value = [7]
        self.two_values = [7, 13]
        self.invalid_values = ["a", 13]
        self.one_value_list = [5]
        self.empty_list = []
        self.four_values = [5, 4, 8, 19]

    def tearDown(self):
        # This method is called after each test
        # Cleaning up any resources or resetting states
        pass  # Nothing to clean up in this example

    # Test the sum_list function
    def test_sum_list_with_one_value(self):
        # Act: Call the function
        result = sum_list(self.single_value)
        # Assert: Check if the result matches the expected output
        self.assertEqual(result, 7)

    def test_sum_list_with_two_values(self):
        # Act: Call the function
        result = sum_list(self.two_values)
        # Assert: Check if the sum is correct
        self.assertEqual(result, 20)

    def test_sum_list_with_invalid_values(self):
        # Act: Call the function
        result = sum_list(self.invalid_values)
        # Assert: Should return None due to invalid input
        self.assertEqual(result, None)  # self.assertIsNone(result)

    # Test the get_middle_of_list function
    def test_get_mid_value_with_one_value(self):
        # Act: Call the function
        result = get_middle_of_list(self.one_value_list)
        # Assert: The middle value should be the only element
        self.assertEqual(result, 5)

    def test_get_mid_value_with_no_values(self):
        # Act: Call the function
        result = get_middle_of_list(self.empty_list)
        # Assert: Should return None for empty list
        self.assertEqual(result, None)

    def test_get_mid_value_with_four_values(self):
        # Act: Call the function
        result = get_middle_of_list(self.four_values)
        # Assert: Should return 8, the middle-right value
        self.assertEqual(result, 8)


class TestStudentGrades(unittest.TestCase):
    
    def setUp(self):
        # Arrange
        self.no_students = []
        self.one_student = [[50, 50, 50]]
        self.multiple_students = [
            [20, 50, 70],
            [80, 60, 50],
            [70, 60, 60],
            [50, 60, 40]
        ]
        
    def tearDown(self):
        pass

    # Test the get_all_students_average function
    def test_grade_average_with_no_students(self):
        # Act: Call the function
        result = get_all_students_average(self.no_students)
        # Assert: Should return 0 for no students
        self.assertEqual(result, 0)

    def test_grade_average_with_one_student(self):
        # Act: Call the function
        result = get_all_students_average(self.one_student)
        # Assert: The average should be 50
        self.assertEqual(result, 50)

    def test_grade_average_with_multiple_students(self):
        # Act: Call the function
        result = get_all_students_average(self.multiple_students)
        # Assert: The average should be 55.83
        self.assertEqual(result, 55.83)

class TestRecursiveFlip(unittest.TestCase):
    
    def setUp(self):
        # Setting up common test data for recursive flips
        # Arrange
        self.single_character = "A"
        self.palindrome = "madam"
        self.regular_word = "hello"

    def tearDown(self):
        # Cleaning up after tests
        pass  # Nothing to clean up in this example

    # Test the recursive_word_flip function
    def test_recursive_flip_single_character(self):
        # Act: Flip the word recursively
        result = recursive_word_flip(self.single_character)
        # Assert: The output should be the same single character
        self.assertEqual(result, "A")

    def test_recursive_flip_palindrome(self):
        # Act: Flip the word recursively
        result = recursive_word_flip(self.palindrome)
        # Assert: The flipped word should still be "madam"
        self.assertEqual(result, "madam")

    def test_recursive_flip_word(self):
        # Act: Flip the word recursively
        result = recursive_word_flip(self.regular_word)
        # Assert: The flipped word should be "olleh"
        self.assertEqual(result, "olleh")

if __name__ == "__main__":
    unittest.main()

# Note that the tests run randomly and not in the order that it is coded.
# You can also run the test from the terminal with:
# python -m unittest test_examples
# python -m unittest -v test_examples
