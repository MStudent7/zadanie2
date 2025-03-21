import unittest
from app import is_valid_email, calculate_rectangle_area, process_list, convert_date_format, is_palindrome

class TestAppFunctions(unittest.TestCase):
    # Testy dla is_valid_email
    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@domain.com"))

    def test_invalid_email_no_at_symbol(self):
        self.assertFalse(is_valid_email("testdomain.com"))

    def test_invalid_email_domain(self):
        self.assertFalse(is_valid_email("test@domain"))

    # Testy dla calculate_rectangle_area
    def test_positive_dimensions(self):
        self.assertEqual(calculate_rectangle_area(5, 10), 50)

    def test_zero_dimensions(self):
        self.assertEqual(calculate_rectangle_area(0, 10), 0)

    def test_negative_dimensions(self):
        self.assertEqual(calculate_rectangle_area(-5, 10), -50)

    # Testy dla process_list
    def test_typical_case(self):
        self.assertEqual(process_list([3, 15, 7, 20, 1]), [15, 20])

    def test_empty_list(self):
        self.assertEqual(process_list([]), [])

    def test_all_values_below_threshold(self):
        self.assertEqual(process_list([1, 2, 3]), [])

    # Testy dla convert_date_format
    def test_valid_conversion(self):
        self.assertEqual(convert_date_format("21-03-2025", "%d-%m-%Y", "%Y/%m/%d"), "2025/03/21")

    def test_invalid_date_string(self):
        self.assertEqual(convert_date_format("invalid-date", "%d-%m-%Y", "%Y/%m/%d"), "Niepoprawny format daty")

    def test_invalid_format(self):
        self.assertEqual(convert_date_format("21-03-2025", "%m-%d-%Y", "%Y/%m/%d"), "Niepoprawny format daty")

    # Testy dla is_palindrome
    def test_valid_palindrome(self):
        self.assertTrue(is_palindrome("kajak"))

    def test_invalid_palindrome(self):
        self.assertFalse(is_palindrome("samochód"))

    def test_palindrome_with_special_characters(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

if __name__ == "__main__":
    unittest.main()