import unittest
from day2 import *

class TestGetPWordData(unittest.TestCase):
    def test_GIVEN_single_digit_values_THEN_return_dict(self):
        pword_data = get_pword_data("1-2 a: b")
        self.assertEqual(pword_data, {"char": 'a', "count": [1,2], "pword": 'b'})

    def test_GIVEN_double_digit_values_THEN_return_dict(self):
        pword_data = get_pword_data("10-99 a: abc")
        self.assertEqual(pword_data, {"char": 'a', "count": [10,99], "pword": 'abc'})

class TestIsCompliant(unittest.TestCase):
    def test_GIVEN_exact_pword_THEN_true(self):
        pword = create_pword_data([1,1], char="a", pword="a")
        res = is_compliant(pword)
        self.assertTrue(res)

    def test_GIVEN_exact_count_no_match_THEN_false(self):
        pword = create_pword_data([1,1], char="b", pword="a")
        res = is_compliant(pword)
        self.assertFalse(res)

    def test_GIVEN_exact_count_not_enough_THEN_false(self):
        pword = create_pword_data([2,2], char="a", pword="a")
        res = is_compliant(pword)
        self.assertFalse(res)

    def test_GIVEN_in_count_range_THEN_true(self):
        pword = create_pword_data([1,3], char="a", pword="aa")
        res = is_compliant(pword)
        self.assertTrue(res)
        
    def test_GIVEN_at_max_count_THEN_true(self):
        pword = create_pword_data([1,3], char="a", pword="aaa")
        res = is_compliant(pword)
        self.assertTrue(res)
        
    def test_GIVEN_beyond_max_count_THEN_false(self):
        pword = create_pword_data([1,3], char="a", pword="aaaa")
        res = is_compliant(pword)
        self.assertFalse(res)
        
if __name__ == '__main__':
    unittest.main()
