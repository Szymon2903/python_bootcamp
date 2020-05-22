
# Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika. Sprawdź jak dużo z tych liczb
# jest liczbami parzystymi w zakresie 0-100- w tym celu skorzystaj z operatora iloczynu

zbior = set()

while True:
    polecenie = input("Wpisz liczbe lub k by zakonczyc: ")
    if polecenie == "k":
        break
    zbior.add(int(polecenie))

Liczby_parzyste = set(range(0, 101, 2))

print(f"Unikalnych liczb: {len(zbior)}")
print(f"Parzystych z zakresu 1-101: {len(zbior & liczby_parzyste)}")





