

# Napisz funkcje sprawdzającą, czy dana liczba jest liczbą pierwszą.Przykład użycia
# >>> czy_jest_pierwsza(10) False
# >>> czy_jest_pierwsza(17) True

def czy_jest_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

def test_czy_jest_pierwsza_dla_l_pierwszej():
    assert czy_jest_pierwsza(11) == True

# print(__name__)
# if __name__== "__main__":
#     print("Wykonuje testy")
#     assert czy_jest_pierwsza(6) == False
#     assert czy_jest_pierwsza(10) == False
#     assert czy_jest_pierwsza(11) == True
#     assert czy_jest_pierwsza(17) == True




#print(3, x)