# Napisz program wyliczający kwotę należną za zakupiony towar na podstawie ceny za kilogram oraz liczby zakupionych kilogramów
# Do przechowywania imformacji o cenie oraz liczbie kilogramów użyj zmiennych. Wypisz wszystkie informacje na konsole

cena = 10.0
waga = 2.5
naleznosc = cena * waga

# Cena za kg: 10.0
# Waga: 2.5
# Należność: 25.0

print("Cena za kg: " + str(cena) + " zl")
print("Cena za kg:", cena, "zl")
print("Waga:", waga, "kg")
print("Naleznosc:", naleznosc, "zl")

# f-string - to takie ustrojstwo, gdzie przy tworzeniu napisu
# dajemy na poczatku f a pozniej wewnatrz tego napisu mozemy sie odwolywac do zmiennych
# https://realpython.com/python-f-strings/

print(f"Cena za kg: {cena} zl")
print(f"Waga: {waga} kg")
print(f"Naleznosc: {naleznosc} zl")