class Product:
    def __init__(self, id, nazwa, cena):
        #atrybuty instancji
        self.nazwa = nazwa
        self.id = id
        self.cena = cena

    def print_info(self):
        print (self.id, self.nazwa, self.cena)

 #produkt = Product (1, "Woda", 10.99)
# produkt.print_info()

def test_produkt():
     produkt = Product(1, "Woda", 10.99)
     assert produkt.id ==1
     assert produkt.nazwa == "Woda"
     assert produkt.cena == 10.99

def test_product_product_infor (capsys):
    produkt = Product(1, "Woda", 10.99)
    produkt.print_info()
    captured = capsys.readouterr ()
    assert captured.out == "Produkt 'Woda', id: 1, cena: 10.99 "