# To jest komentarz
print("Ala ma kota")

# TYPY DANYCH

# napisy, ciągi znaków, string
# "Hello world!" - to jest literał typu string
print("Hello world!")
print('Hello world!')
# int - liczba całkowita

print(5)
print(-10)
print("5") # "5" 5
# float - liczba zmiennaprzecinkowa

print(3.14)
print(3) # int
print(3.0) # float
print(0.5)
print(.5) # float, zero na poczatku mozna pominac
print(type(3.14))
print(type(3))
print(type(3.0))
# bool, boolean, typ boolowski
# Algebra Boola
print(True) # achtung! z duzej litery!!!
print(False)
# typ None
# None - wartość oznaczająca brak wartości

print(None)
print("")
print(0)
print(0.0)
import sys
print(ys.float_info)

# OPERATORY

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3) # proces wyliczenia wyrażenia do prostej wartosci ewaluacją
print(10 // 3) # dzielenie calkowitoliczbowe
print(10 % 3) # reszta z dzielenia, modulo
print(10 ** 3) # potega
print("ala " + "ma kota") # laczenie napisow, kankatenacja
print("-" * 30) # zwielokrotnienie napisu

# NAPISY
# mozemy definiowac w " i '

print("Ksiazka \"Pan Tadeusz\"") # eskejpowanie znakow
print('Ksiazka \'Pan Tadeusz\'')
print('Ksiazka "Pan Tadeusz"')
print("Ala ma kota") # napisy mozemy definiowac tylko w ramach jednej linijki, nie mozemy wstawic "entera"
print("Ala\nma\nkota")

# print standardowo wyswietla znak nowej linii na koncu

print(""""
Ala 
ma
kota
asd
asd
asd
asd
""") # jezeli uzywam enterow w napisie, to definiuje napis w """ albo '''

# format specifiers

# https://www.python.org/dev/peps/pep-0498/#format-specifiers

# https://docs.python.org/3.4/library/string.html#formatspec
wartosc = 105.105
print(f"Koszt: >{wartosc:_^10.2f}<")

# OPERATORY POROWNANIA

print()
print(1 > 2) # False
print(2 < 5) # True
print(2 < 2) # False
print(2 <= 2) # True
print(3 >= 2) # True
print(2 == 2) # UWAGA! dwa =, pojednycze = to operator przypisania
print(3 != 2) # True
print()

test_objetosci = 15 * 10 * 10 > 1000
test_objetosci = 1000 < 15 * 10 * 10
print(test_objetosci)

print()

# Instrukcja warunkowa - if

warunek = True

if warunek:

    print("Wartosc w warunek jest prawdziwa")
else:

    print("Wartosc w warunek jest falszywa")

print("Jestem juz za ifem")