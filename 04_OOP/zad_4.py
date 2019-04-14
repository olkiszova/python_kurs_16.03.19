class Basket:

    def __init__(self):
        self.entries = []

    def add_product(self, product, number):
        for entry in self.entries:
            if entry.product == product:
                entry.number += number
                return
        self.entries.append(BasketEntry(product, number))

    def count_total_price(self):
        total = 0
        for entry in self.entries:
            total += entry.entry_price()
        return total

    # return sum(e.entry_price() for e in self.entries)

    def generate_report(self):
        result = 'Produkty w koszyku:\n'
        for entry in self.entries:
            result += f" {entry.product.name} ({entry.product.id}), cena: {entry.product.price:.2f} x {entry.number}\n"
        result += f"W sumie: {self.count_total_price():.2f}"
        return result


class BasketEntry:
    def __init__(self, product, number):
        self.product = product
        self.number = number

    def entry_price(self):
        return self.product.price * self.number


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


def test_basket_init():
    b = Basket()


def test_product_init():
    p = Product(1, 'Woda', 10.00)
    assert p.name == 'Woda'
    assert p.id == 1
    assert p.price == 10.00


def test_Basket_entry_init():
    p = Product(1, 'Woda', 10.00)
    be = BasketEntry(p, 5)
    assert be.product == p
    assert be.number == 5


def test_add_product_to_basket():
    b = Basket()
    p = Product(1, 'Woda', 10.00)
    b.add_product(p, 5)
    assert b.count_total_price() == 50
    assert b.generate_report() == """Produkty w koszyku:
 Woda (1), cena: 10.00 x 5
W sumie: 50.00"""

def test_add_product_to_basket():
    b = Basket()
    p = Product(1, 'Woda', 10.00)
    b.add_product(p, 4)
    b.add_product(p, 1)
    assert b.count_total_price() == 50
    assert b.generate_report() == """Produkty w koszyku:
 Woda (1), cena: 10.00 x 5
W sumie: 50.00"""
