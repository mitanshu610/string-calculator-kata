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

    def test_string_with_new_line(self):
        self.assertEqual(198, self.test_sc.Add("1\n102,5,90"))

    def test_string_with_multiple_new_lines(self):
        self.assertEqual(198, self.test_sc.Add("1\n102,5\n90"))

    def test_string_with_characters_and_numbers_to_add(self):
        self.assertEqual(
            "Character different from numbers detected! please insert numbers for the addition",
            self.test_sc.Add("1,2, r")
        )
    
        
if __name__ == '__main__':
    unittest.main()