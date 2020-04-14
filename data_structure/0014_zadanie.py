#Napisz program wyświetlający minimalną oraz maksymalną liczbę z wszystkich liczb wprowadzonych przez użytkownika.
#Daj użytkownikowi możliwość zakończenia wprowadzenia liczb odpowiednią komendą.
#Zadbaj o obsłużenie przypadku gdy użytkownik nie wprowadzi żadnej liczby.

mini_x = None
maxy_x = None

while True:

    number = input("wprowadź liczbę lub x by zakonczyc: ")
    if number == "x":
        break
    number = int(number)
    if mini_x is None or number < mini_x:
        mini_x = number
    if maxy_x is None or number > maxy_x:
        maxy_x = number

print(f"Wartość maksymalna: {maxy_x}")

print(f"Wartość minimalna: {mini_x}")