

# Zaimplementuj funkcje obliczającą silnie dla żądanej wartości.
# Przykład użycia
#>>> silnia(5)
#120

x = input('Podaj liczbe: ')

silnia = 1

if x > 0:
    for i in range(1, 1 + x):
        silnia *= i
    print
    'Podana liczba to: %3f' % x
    print
    'Silnia dla podanej liczby wynosi: %10f' % silnia
else:
    print
    'Podana liczba jest mniejsza od zera'