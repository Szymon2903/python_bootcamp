

# Napisz funkcje sprawdzającą, czy dana liczba jest liczbą pierwszą.Przykład użycia
# >>> czy_jest_pierwsza(10) False
# >>> czy_jest_pierwsza(17) True




liczba = int(input("Podaj liczbe: "))

print(f"czy_jest_pierwsza: {liczba > 10}")
print(f"czy_jest_pierwsza: {liczba <= 17}")
print(f"Miedzy 0 a 100: {liczba >= 0 and liczba <= 10}")