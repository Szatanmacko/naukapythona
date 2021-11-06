from product import Product


class ShoppingCart:
    def __init__(self):
        self._products = []

    def add_product(self, product: Product):
        self._products.append(product)

    def get_total_cart_cost(self):
        total = 0
        for product in self._products:
            total += product.get_gross_price()
