from shopping_cart import ShoppingCart
from unittest import TestCase
from unittest.mock import MagicMock, Mock


class ProductTests(TestCase):
    def test_get_total_cart_cost_returns_sum_of_gross_prices_of_all_products(self):
        shopping_cart = ShoppingCart()

        first_product = Mock()
        first_product.get_gross_price = Mock(return_value=100)

        second_product = Mock()
        second_product.get_gross_price = Mock(return_value=200)

        shopping_cart.add_product(first_product)
        shopping_cart.add_product(second_product)

        self.assertEqual(300, shopping_cart.get_total_cart_cost())
