

# Napisz program wypisujący na konsolę zawartość wskazanego pliku wraz z numerami linii. Obsłuż sytuację,gdy użytkownik
# nie poda nazwy lub poda błędną nazwę

# --> Przykład użycia:
# python test.txt
# 1. pierwsza linia pliku
# 2. druga linia pliku


import sys

print(sys.argv)
f_name = sys.argv[1]
print("Bede pracować z plikiem: ", f_name)
# 1. utworzenie pliku z zawartoscią:
# with open("test.txt", 'w') ass f:
#    f.write("To jest pierwsza linia\n")
#    f.write("Druga linia\n")
#    f.write("trzecia linia\n")

#odczytaj i ponumeruj linie:

with open ("test.txt") as f:
    text = f.read()
for i, linein enumerate(f, start=1):
    print(f"{i}: {line}")