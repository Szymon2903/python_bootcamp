
# W sesji interaktywnego środowiska stwórz następujące struktury danych korzystające ze skróconej wersji zapisu:

# > liste zawierającą liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
# > zbiór tupli zawierających 3 elementy - daną liczbę, jej kwadrat i jej sześcian- w przedziale od -10 do 10
# > słownik mapujacy napisy na ich długość powstały ze zbioru napisów

print([x/10 for x in range(11)])

print({(x, x**2, x**3) for x in range(-10, 11)})

napisy = {"xxx", "yyyyy", "xx", "xxxxxxxxxxxcxcxcxcxcx"}
print({napis:len(napis) for napis in napisy})

