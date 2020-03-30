# Korzystając z przypisywania wartości do zmiennych, napisz program
# obliczający pole trapezu o długości podstaw 3 i 9 oraz wysokości 6.5.
# pole_trapezu = 0.5 * (a+b) * h

podstawa_a = 3
podstawa_b = 9
wysokosc = 6.5

print("podstawa_a")  # wyswietlamy string
print(podstawa_a)  # wyswietlamy zawartosc zmiennej podstawa_a

# nazwy zmiennych piszemy:
# - bez polskich znakow
# - BEZ SPACJI!!!
# - posczegolne slowa rozdzielamy _
# poleTrapezu pole_trapezu PoleTrapezu
# Konwencja kodowania, konwencja nazewnicza, czyli zbiór zasad
# jakich sie trzymamy przy pisaniu kodu

pole_trapezu = 0.5 * (podstawa_a + podstawa_b) * wysokosc

print(pole_trapezu)