import unittest
from Task2 import calculate_total_cost

class TestCalculateTotalCost(unittest.TestCase):
    def test_typical_case(self):
        item_costs = {'apple': 0.5, 'banana': 0.3, 'orange': 0.8}
        items_bought = ['apple', 'banana', 'apple', 'orange']
        tax_rate = 0.07
        self.assertEqual(calculate_total_cost(item_costs, items_bought, tax_rate), 2.25)

    def test_empty_items_bought(self):
        item_costs = {'apple': 0.5, 'banana': 0.3, 'orange': 0.8}
        items_bought = []
        tax_rate = 0.07
        self.assertEqual(calculate_total_cost(item_costs, items_bought, tax_rate), 0.00)

    def test_items_not_in_cost_dict(self):
        item_costs = {'apple': 0.5, 'banana': 0.3, 'orange': 0.8}
        items_bought = ['grape', 'melon']
        tax_rate = 0.07
        self.assertEqual(calculate_total_cost(item_costs, items_bought, tax_rate), 0.00)

    def test_zero_tax_rate(self):
        item_costs = {'apple': 0.5, 'banana': 0.3, 'orange': 0.8}
        items_bought = ['apple', 'banana', 'orange']
        tax_rate = 0.00
        self.assertEqual(calculate_total_cost(item_costs, items_bought, tax_rate), 1.60)

    def test_high_tax_rate(self):
        item_costs = {'apple': 0.5, 'banana': 0.3, 'orange': 0.8}
        items_bought = ['apple', 'banana', 'orange']
        tax_rate = 1.00
        self.assertEqual(calculate_total_cost(item_costs, items_bought, tax_rate), 3.20)

    def test_duplicate_items(self):
        item_costs = {'apple': 0.5, 'banana': 0.3, 'orange': 0.8}
        items_bought = ['apple', 'apple', 'apple']
        tax_rate = 0.07
        self.assertEqual(calculate_total_cost(item_costs, items_bought, tax_rate), 1.60)

    def test_no_items_in_cost_dict(self):
        item_costs = {}
        items_bought = ['apple', 'banana', 'orange']
        tax_rate = 0.07
        self.assertEqual(calculate_total_cost(item_costs, items_bought, tax_rate), 0.00)

if __name__ == '__main__':
    unittest.main()