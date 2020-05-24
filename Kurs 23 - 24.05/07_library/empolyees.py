
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

text = '{}'
dane = json.loads(text)

int(input("d - dodaj: "))
int(input("w - wypisz: "))

print(dane)
print(type(dane))

x = {i: i*3 for i in range(10)}

print(x, type(x))
print(json.dumps(x))


los = randint(1,100)
odp = -1
i = 0
print ("ZAGRAJMY W GRĘ!")



