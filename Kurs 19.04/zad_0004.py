
#Zaimplementuj funkcje formatującą podane napisy.

# Przykład użycia:

def test_formatuj(*teksty, **znaczniki):
    text = "\n".join(teksty)
    for znaczniki, wartosc in znaczniki.items():
        text = text.replace("$"+znaczniki, str(wartosc))
    return text

def text_formatuj():
    assert formatuj('koszt $cena PLN','koszt $cena brutto', cena = 10 ) == 'koszt 10 PLN\nkwota 10 brutto'
    assert formatuj('koszt $cena PLN','koszt $cena brutto', ) == 'koszt $cena PLN\nkwota 10 brutto'
    assert formatuj('koszt $cena PLN', 'koszt $cena brutto', podatek=15) == 'koszt $cena PLN\nkwota $cena brutto'
    assert formatuj('koszt $cena PLN', 'koszt $cena $podatek', podatek=15) == 'koszt $cena PLN\nkwota podatku 15'
    assert formatuj('koszt $cena PLN', podatek=15) == 'koszt $cena PLN'