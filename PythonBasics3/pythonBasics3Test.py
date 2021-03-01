import unittest

import pythonBasics3

class TestPythonBasicsOne(unittest.TestCase):

#Test case for ends_with_consonant
    def test_ends_with_consonant(self):

        self.assertEqual(pythonBasics3.ends_with_consonant("Once upon a dark, cold night"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("What did Steve just say"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("I once swam with sharks"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("Do I know how old you are you"), False)

        # Please add three more test cases following the order above
        self.assertEqual(pythonBasics3.ends_with_consonant("This ends in a consonant"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("The fridge holds sodas"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("You can pour soda into the cup"), True)

#Test case for ends_with_number
    def test_ends_with_number(self):

        self.assertEqual(pythonBasics3.ends_with_number("What is 3/10"), True)

        self.assertEqual(pythonBasics3.ends_with_number("It was not a cat"), False)

        self.assertEqual(pythonBasics3.ends_with_number("I once swam with sharks"), False)

        self.assertEqual(pythonBasics3.ends_with_number("Blue plus purple equals 5"), True)

        # Please add three more test cases following the order above
        self.assertEqual(pythonBasics3.ends_with_number("This ends in a number 1"), True)

        self.assertEqual(pythonBasics3.ends_with_number("The cups have soda"), False)

        self.assertEqual(pythonBasics3.ends_with_number("The wood was used for a table"), False)

#Test case for binary_multiple_of_6
    def test_binary_multiple_of_6(self):

       

if __name__ == '__main__':

  unittest.main(verbosity=1)

