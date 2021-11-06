from product import Product
from unittest import TestCase


class ProductTests(TestCase):
    def test_product_must_not_have_negative_price(self):
        with self.assertRaises(ValueError):
            Product("Negative price", -100, 0.5)

    def test_product_must_not_have_negative_tax(self):
        with self.assertRaises(ValueError):
            Product("Negative tax", 100, -0.5)

    def test_get_price_gets_gross_price(self):
        self.test_product = Product("Box of chocolate", 100, 0.23)
        self.assertEqual(123, self.test_product.get_gross_price())
