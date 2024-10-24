"""========= Python testing in Visual Studio Code

Unit - A piece of code to be tested
Unit tests  - Pieces of code to exercise the 'code to be tested' and includes
              a full range of different inputs, including boundary and edge cases.
            - Only concerned with the arguments and return values.
Report - The combined results of all the tests.

The practice of test-driven development is to write the tests first and 
then write the code that needs to pass the tests.

--- 1.  Create a folder for your working space / project.
        /Workspace

--- 2.  Create a folder in the workspace and place the file 
        with the code to be tested in it.
        /modulestotest/sum_list_module.py

--- 3.  Open the python file in step 2 to make sure the workspace is active.

--- 4.  Make sure the Python extention is installed.
        https://marketplace.visualstudio.com/items?itemName=ms-python.python

--- 5.  Open the glass test beaker icon on the left and choose 
        Configure Python Tests

        - If you don't see the Configure Python Tests option under the beaker icon,
            use the menu /View/Command Palette/Python: Configure Tests
        - If unittest and pytest frameworks are enabled, only pytest will run.

        - Select the workspace <My_Workspace>
        - Select the test framework <unittest>
        - Select directory containing the tests code <testsformodules>
        - Select the file name pattern to identify the test files
          in the previous step directory, ie. <test_*.py> or <*_test.py>  

--- 6.  Time to create tests
        Create a filename in the testsformodules folder with name pattern
        ie. for test_*.py naming pattern - test_unittest.py

        ============ STEPS for writing unit tests using the unittest framework
        a. Import the unittest module.
        b. Import file with code to be tested
        c. Create a test class that inherits from unittest.TestCase.
        d. Write test methods within the test class, where 
           each method represents a specific test case.
        e. Use various assertion methods provided by the unittest.TestCase class 
           to check the expected outcomes of your code.
        f. Optionally, set up and tear down code that needs to run before 
           and after each test using setUp() and tearDown() methods.
        g. run unittest.main()

--- 7.  Test Discovery
        The discovered tests will show under the beaker icon.

        If discovery failed, you can see the errors in the terminal under the 
        OUTPUT TAB with Python selected in the dropdown list.

        For multi-level folders, a blank __init__.py file might need to be 
        placed in the folder in order for the files to be part of the discovery.

        If you really get stuck, there are times when Visual Code have issues
        with auto-updates and a simple restart of VS might solve the issue just
        to force a reset.
"""

import unittest
from testsformodules import sum_list_module       # Package / Folder name is case sensitive

class TestExamples(unittest.TestCase):
    """
    Now to create the first test for our unit. 
    We can perform a very basic test to see if our function 
    will give us the intended result for a list with a single value.
    """
    def test_list_add_with_one_number(self):
        #Arrange:
        num_list = [5]
        #Act:
        result = sum_list_module.sum_list(num_list)
        #Assert:
        self.assertEqual(result, 5)

    """
    We can now run the test and have a look at the result. 
    For the first test we can see that our test has run without any failure.
    """
    """
    Lets create some more tests to see if our behaviour is in fact what 
    we intend it to be. 
    """
    def test_list_add_with_two_number(self):
        #Arrange:
        num_list = [5, 10]
        #Act:
        result = sum_list_module.sum_list(num_list)
        #Assert:
        self.assertEqual(result, 15)
    """
    From our first test we saw that our behaviour returned the single value 
    when a list with one value is provided but 
    what happens with two values in our list?
    Ans: Our second test has failed indicating there is an error in our code.
    
    At closer inspection we can see that we have a logical error 
    that is preventing our test from passing. => Change =+ to +=

    Remember when we correct this error all our previous test should still pass.
    """
if __name__ == '__main__':
    unittest.main()
    