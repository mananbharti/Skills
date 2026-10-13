import unittest
from cart import total

class TestDiscount(unittest.TestCase):
    def test_percentage_discount_is_applied_once_to_whole_cart(self):
        cart = [{"name": "book", "price": 20.0, "qty": 1},
                {"name": "pen", "price": 5.0, "qty": 2}]
        self.assertEqual(total(cart, discount=0.10), 27.0)
