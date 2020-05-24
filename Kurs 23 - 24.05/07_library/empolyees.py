
# Napisz program obsługujący bazę danych pracowników.
# W bazie danych przechowuj imię, nazwisko, email, rok urodzeni, pensje.
# --> Skorzystaj z modułu json
# -> Przykład użycia:

# python_employees.py
# Co chcesz zrobić ? [d - dodaj, w - wypisz] d
# Imie: Jan
# Nazwisko: Nowak
# Rok urodzenia: 1980
# Pensja: 5000.0

# python_employees.py
# co chcesz zrobić [d - dodaj, w - wypisz] w
# Pracownicy:
# --> [1] Jan Nowak - rok: 1980, pensja: 5000.0 PLN


import json
try:
    with open("employees.json") as fp:
        lista = json.load(fp)
except FileNotFoundError:
    lista = []
komenda = input("Co chcesz zrobić? [d- dodaj, w-wypisz]: ")

if komenda == "d":
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    rok_urodzenia = int(input("Podaj rok urodzenia: "))
    pensja = input("Podaj pensję: ")
    email = input("Podaj email: ")

    pracownik = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok_urodzenia": rok_urodzenia,
        "pensja": pensja,
        "email": email
    }

    lista.append(pracownik)

    with open("employees.json", "w") as fp:
        json.dump(lista, fp)

elif komenda == "w":
    print("Pracownicy: ")
    for i, emp in enumerate(lista, start=1):
        print(f" - [{i}] {emp['imie']} {emp['nazwisko']} - rok: {emp['rok_urodzenia']}, pensja: {emp['pensja']} PLN")



