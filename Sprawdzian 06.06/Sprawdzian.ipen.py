# Zad 1

# Typy danych takie jak liczby, napisy czy watości logiczne sa podstawowymi elementami używanymi przy budowie  progamów
# Gdy pracujemy z większą ilością takich elementów, potrzebujemy jednak bardziej rozbudowanych struktur, umożliwiających
# nam pamiętanie wielu obiektów jednocześnie i operowanie na nich w sposób zbiorczy
#Python posiada kilka wbudowanych w język struktur danych, są to
# Tuple, listy, słowniki, zbiory
# tuple, list , dict, set

# 2

# Sekwencją są listy krotki i napisy, kolejność jej elementów jest ustalana i  ponumerowana.
# Wyróżniamy trzy typy sekwencji lista krotka i ciąg znaków

# 4

# Instrukacja warunkowa jest jednym z największych i fundamentalnych elementów składniowych prawie każdego języka
# programowania. Dzięki instrukcji warunkowej możemy zdecydować o wykonaniu lub pominięciu wybranego fragmentu
# naszego programu.
# Python posiada specjalny typ danych logicznych, który jest używany w instrukcjach warunkowych i pętlach.
# Wartości logiczne True albo False są najczęściej zwracane, kiedy porównujemy ze sobą dwie wartości.

x = 2
print x == 2 # wypisze True
print x != 2 # wypisze False
print x == 3 # wypisze False
print x < 3  # wypisze True

Operatory logiczne
Operator in
Operator is
Operator not


# 5 zad

# Pentla while swoją składnią przypomina najprostrzą wersje instrukcji warunkowej, w której słowa kluczowe if zastąpiono
# słowem kluczowym while. Różnica pomiędzy pętlą while a instrukcją warunkową polega na wykonaniu bloku pętli wielokrotnie,
# aż do momentu kiedy jej warunek logiczny przestanie być prawdziwy

liczba = 0
while liczba < 10:
    print(liczba)
    liczba = liczba + 1


# 6 zad

pętla for służy do przechowywania iteracji po kolejnych elementach w zadanej kolekcji


# Wypisze liczby 0 1 2 3 4
for x in xrange(5):
    print x,

print

# Wypisze 3 4 5
for x in xrange(3,6):
    print x,


# 8 zad
#Każda funkcja w Pythonie otrzymuje określoną liczbę argumentów, jeśli została zdefiniowana w znany nam z poprzednich
# lekcji sposób: len, print

    def pole_trojkata(podstawa, wysokosc):
        return 1 / 2 * podstawa * wysokość

    wynik = pole_trojkata(10, 5)
    print(f'Pole zadanego trojkata to {wynik}')

    pole_trapezu(pierwsza_podstawa=10, druga_podstawa=5, wysokosc=8)