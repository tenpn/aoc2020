import unittest
from day1 import *

class TestFindSummingPair(unittest.TestCase):
    def test_GIVEN_only_entries_sum_to_total_THEN_return_two_entries(self):
        res = find_summing_pair([1,1], 2)
        self.assertEqual(res, (1, 1))

    def test_GIVEN_sum_entries_somewhere_in_list_THEN_return_sum_entries(self):
        res = find_summing_pair([5, 3, 1, 6, 1], 2)
        self.assertEqual(res, (1, 1))

    def test_GIVEN_empty_list_THEN_return_None(self):
        found_values = find_summing_pair([], 1)
        self.assertIsNone(found_values)

class TestFindSummingTriple(unittest.TestCase):
    
    def test_GIVEN_empty_list_THEN_return_None(self):
        found_values = find_summing_triple([], 1)
        self.assertIsNone(found_values)

    def test_GIVEN_only_entries_sum_to_total_THEN_return_three_entries(self):
        res = find_summing_triple([2,3,4], 9)
        self.assertEqual(res, (2, 3, 4))

    def test_GIVEN_sum_entries_somewhere_in_list_THEN_return_sum_entries(self):
        res = find_summing_triple([5, 3, 1, 6, 1], 5)
        self.assertEqual(res, (3, 1, 1))

if __name__ == '__main__':
    unittest.main()
