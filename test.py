import unittest
from answer import find_optimal_subset


class TestFindOptimalSubset(unittest.TestCase):
    def test_single_item(self):
        items = [["item1", 5, 10]]
        total_items = 1
        capacity = 5
        expected_optimal_items = [["item1", 5, 10]]
        expected_total_value = 10
        optimal_items, total_value = find_optimal_subset(
            items, total_items, capacity)
        self.assertEqual(optimal_items, expected_optimal_items)
        self.assertEqual(total_value, expected_total_value)

    def test_multiple_items(self):
        items = [["item1", 5, 10], ["item2", 3, 8], ["item3", 4, 12]]
        total_items = 3
        capacity = 8
        expected_optimal_items = [["item2", 3, 8], ["item3", 4, 12]]
        expected_total_value = 20
        optimal_items, total_value = find_optimal_subset(
            items, total_items, capacity)
        self.assertEqual(optimal_items, expected_optimal_items)
        self.assertEqual(total_value, expected_total_value)

    def test_low_capacity(self):
        items = [["item1", 5, 10], ["item2", 3, 8], ["item3", 4, 12]]
        total_items = 3
        capacity = 3
        expected_optimal_items = [["item2", 3, 8]]
        expected_total_value = 8
        optimal_items, total_value = find_optimal_subset(
            items, total_items, capacity)
        self.assertEqual(optimal_items, expected_optimal_items)
        self.assertEqual(total_value, expected_total_value)

    def test_zero_capacity(self):
        items = [["item1", 5, 10], ["item2", 3, 8], ["item3", 4, 12]]
        total_items = 3
        capacity = 0
        expected_optimal_items = []
        expected_total_value = 0
        optimal_items, total_value = find_optimal_subset(
            items, total_items, capacity)
        self.assertEqual(optimal_items, expected_optimal_items)
        self.assertEqual(total_value, expected_total_value)

    def test_empty_items(self):
        items = []
        total_items = 0
        capacity = 10
        expected_optimal_items = []
        expected_total_value = 0
        optimal_items, total_value = find_optimal_subset(
            items, total_items, capacity)
        self.assertEqual(optimal_items, expected_optimal_items)
        self.assertEqual(total_value, expected_total_value)
