import unittest
from day1 import *

class TestDay1(unittest.TestCase):
    def test_GIVEN_only_entries_sum_to_total_THEN_return_two_entries(self):
        (v1, v2) = find_summing_pair([1,1], 2)
        self.assertEqual((v1, v2), (1, 1))

    def test_GIVEN_sum_entries_somewhere_in_list_THEN_return_sum_entries(self):
        (v1, v2) = find_summing_pair([5, 3, 1, 6, 1], 2)
        self.assertEqual((v1, v2), (1, 1))

    def test_GIVEN_empty_list_THEN_return_None(self):
        found_values = find_summing_pair([4,4], 1)
        self.assertIsNone(found_values)

if __name__ == '__main__':
    unittest.main()
