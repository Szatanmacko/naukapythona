class Product:
    def __init__(self, name: str, net_price: float, tax_rate: float):
        if net_price < 0:
            raise ValueError("Price must not be negative")

        if tax_rate < 0:
            raise ValueError("Tax rate must not be negative")

        self.name = name
        self.net_price = net_price
        self.tax_rate = tax_rate

    def get_gross_price(self):
        return self.net_price + (self.net_price * self.tax_rate)
