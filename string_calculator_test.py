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
        with self.assertRaises(Exception):
            self.test_sc.Add("1,2, r")
    
    def test_string_with_single_character_as_string(self):
        with self.assertRaises(Exception):
            self.test_sc.Add("r")
    
    def test_string_with_custom_delimeter_colon(self):
        self.assertEqual(23, self.test_sc.Add("//:\n1:22"))
    
    def test_string_with_custom_delimeter_random_characters(self):
        self.assertEqual(23, self.test_sc.Add("//xyz\n1xyz22"))
    
    def test_string_with_negative_numbers(self):
        with self.assertRaises(Exception):
            self.test_sc.Add("-1,2,-3")
    
    def test_string_with_hyphen_as_delimeter(self):
        self.assertEqual(6, self.test_sc.Add("//-\n1-2-3"))
        
    def test_number_greater_than_1000(self):
        self.assertEqual(2, self.test_sc.Add("2, 1002"))
        
if __name__ == '__main__':
    unittest.main()