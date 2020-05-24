
from random import randint

los = randint(1,100)
odp = -1
i = 0
print ("ZAGRAJMY W GRĘ!")

print("Zgadnij liczbe z przediału 1 - 100")

while odp != los:
    i += 1
    odp = int(input("Podaj liczbe: "))
    if odp > los:
        print("Niestety, wylosowana liczba jest mniejsza od Twojej")
    elif odp < los:
        print("Niestety, wylosowana liczba jest większa od Twojej")
print("Brawo ! Odgadłeś za", i, "razem.")

