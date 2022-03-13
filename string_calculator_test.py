import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    test_sc = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(0, self.test_sc.Add(""))
    
    def test_empty_white_space(self):
        self.assertEqual(0, self.test_sc.Add("  "))
    
    def test_one_number(self):
        self.assertEqual(1, self.test_sc.Add("1"))

    def test_string_with_multiple_numbers(self):
        self.assertEqual(198, self.test_sc.Add("1,102,5,90"))

    def test_string_with_multiple_numbers_and_spaces(self):
        self.assertEqual(13, self.test_sc.Add(" 1, 2,3, 7"))
        
if __name__ == '__main__':
    unittest.main()