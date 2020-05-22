

#Zaimplementuj w klasie CashMachine rzucanie wyjątków w następujących przypadkach:
# >>> brak miejsca na banknoty (ustal limit banknotów w bankomacie)
# >>> zła wartość wypłacanej sumy (musi być podzielna przez 10)
# >>> brak odpowiednich banknotów w bankomacie

# Zaimplementuj prosty interfejs tekstowy do klasy bankomat obsługujący wszystkie wyjątki.
# Obsłuż także wyjątki wynikające z podania złych danych przez użytkownika.

# Przykład użycia:

# Podaj typ operacji: WYPŁATA
# Podaj kwotę do wypłacenia: 150
# BŁĄD: brak wystarczającej liczby banknotów dla kwoty 150!



from bankomat import CashMachine, NotEnoughSpaceForBills, BillException

cash_machine = CashMachine(capacity=8)
cash_machine.put_money([200, 200, 100, 100, 100, 50, 50])


while True:
    operation = input("Podaj typ operacji: [wplata, wypalata, koniec]: ")
    if operation == "koniec":
        break
    elif operation == "wplata":
        bills = input("Podaj liste banknotów rozdzielajac je przecienkiem np:100,100,50,50: ")
        bills = input.split(",")
        bills = [int(bill) for bill in bills]
        try:
            cash_machine.put_money(bills)
        except NotEnoughSpacForBills as e:
            print("Error: ", e)
    elif operation == "wyplata":
        amount =int(input("Podaj kwote do wypłaty: "))
        try:
            bills = cash_machine.withdraw_money(amount)
        except



import pytest

class MyException(Exception):
    pass

def func_with_exception(arg):
    if arg == 1:
        raise MyException()
    else:
        raise ValueError()

def test_is_exception_raised():
    with pytest.raised.raised(MyException):
        func_with_exception(1)