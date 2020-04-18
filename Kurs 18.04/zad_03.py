#Napisz program wyliczający kwotę należną za zakupiony towar na podstawie podanej przez użytkownika
# wagi i nazwy produktu. Do przechowywania informacji o cenie za kilogram danego produktu użyj słownika.
# Wypisz wszystkie dostępne produkty w sklepie.

produkty = {
    "ziemniaki": 2.25,
    "pomidory": 4.15,
    "cebula": 1.99,
    "kalafiory": 3.20
}
magazyn = {
    "ziemniaki": 10,
    "pomidory": 10,
    "cebula": 10,
    "kalafiory": 10
}

print(produkty.items())

for item in produkty.items():
    print(item)
    a, b = item
    print(a, b)

#a,b = "k", "v"
#[("k", "v"), ()]

while True:
    komenda = input("Co chcesz zrobić? [k-kup] [z-zakoncz] [m-magazyn]")

    if komenda == "z":
        break
    elif komenda == "k":
       print("Nasz zielnik oferuje: ")
       for nazwa, cena in produkty.items():
           print(f" - {nazwa} w cenie: {cena} PLN (stan: {magazyn[nazwa]})")

    produkt = input("Co chcesz kupić? ")

    if produkt in produkty:
        ile = input(f"Ile chcesz kupić [{produkt}]? ")
        ile = float(ile)
        if ile < mahazyn[produkt]:
            print(f"Za {ile} kg {produkt} zaplacisz {ile * produkty[produkt]:.2f}" )
            magazyn[produkt] = magazyn[produkt] - ile
        else:
            print("Nie mamy tyle produktu")
    elif komenda == "m":
        pass
    else:
        print("Nierozumiala komenda")


    produkt = input("Co chcesz kupić? ")




