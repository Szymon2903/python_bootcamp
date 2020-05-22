
#Zaimplementuj klasę Product przechowującą informacje o cenie, nazwie oraz ID produktu.
#Zaimplementuj metodę wypisującą informacje o produkcie na konsolę.

#Przykład użycia:
# >>> produktc = Product(1, 'Woda' , '10,99)
# >>> produktc.print_info()
# Produkt "Woda" , id: 1. cena: 10.99 PLN

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        text = f"Produkt \"{self.name}\", id: {self.id}, cena: {self.price} PLN"
        print(text)
        return text


class TestProduct:
    def test_init(self):
        produkt = Product(1, "Woda", 10.99)
        assert produkt
        assert produkt.id == 1
        assert produkt.name == "Woda"
        assert produkt.price == 10.99

    def test_print_info(self):
        produkt = Product(1, "Woda", 10.99)
        assert produkt.print_info() == "Produkt \"Woda\", id: 1, cena: 10.99 PLN"
     #produkt.print_info()