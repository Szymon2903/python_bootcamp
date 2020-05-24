


# Zaimplementuj klasę basket umożliwiającą dodawanie prodóktów w określonej liczbie do koszyka. Zaimplementuj
# metodę obliczając całkowitą awrtość koszyka oraz wypisującą informację o zawartości koszyka. Dodanie dwa razy tego samego
#produktu do koszyka powinno stworzyć tylko jedną pozycję.

#Przykład użycia
# >>> basket = Basket()
# >>> product = Product(1, 'Woda' , 10.00)
# >>> basket.add_product(product, 5)
# >>> basket.count_total_prince()
# >>> 50
# >>> basket.generate_report()




class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product, amount):
        self.products.append(BasketEntry(product, amount))

    def count_total_price(self):
        total_price = 0
        for be in self.products:
            total_price += be.price
        return total_price
        # return sum([be.price for be in self.products])

    def generate_report(self):
        report = "Produkty w koszyku:\"
        for be in self.products:
            report += be.report
        report +=f"W sumie: {self.count_total_prince():.2f}"

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class BasketEntry:
    # pokazano tu przykład adnotacji - określenie typów argumentów
    def __init__(self, product: Product, amount: int):
        self.product = product
        self.amount = amount
    @property
    def price(self):
        return self.amount * self.product.price

    @propery
    def report(self):
        return f"- {self.product.name} ({self.product.id})| "

class TestBasket:
    def test_init(self):
        basket = Basket()
        assert basket
        assert basket.products == []

    def test_add_product(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        basket.add_product(product, 5)
        assert len(basket.products) == 1
        assert basket.products[0].product == product
        assert basket.products[0].amount == 5

    def test_count_total_price(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        product2 = Product(2, "Chleb", 2)
        basket.add_product(product, 5)
        basket.add_product(product2, 5)
        assert basket.count_total_price() == 5 * 10.0 + 5 * 2

    def test_generate_report(self):
        expected = '''Produkty w koszyku:
-Woda (1), cena: 10.00 x 5
 W sumie: 50.00'''

class TestProduct:
    def test_init(self):
        product = Product(1, "Woda", 10.00)
        assert product.id == 1
        assert product.name == "Woda"
        assert product.price == 10.00

class TestBasketEntry:
    def test_init(self):
        product = Product(2, "masło", 8)
        be = BasketEntry(product, 5)
        assert be.product == product
        assert be.amount == 5

    def test_price(self):
        product = Product(2, "masło", 8)
        be = BasketEntry(product, 5)
        assert be.price == 5 * 8

    def test_report(self):
        product = Product(2, "masło", 8)
        be = BasketEntry(product, 5)
        assert be.report == '- masło (2), cena: 8.00 x 2\'