

# Zaimplementuj funkcje obliczającą silnie dla żądanej wartości.
# Przykład użycia
#>>> silnia(5)
#120

def silnia(n):
    if n < 0:
        return "Erron"
    elif n == 0:
        return 1
    else:
        return n * silnia(n-1)

def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(2) == 2
    assert silnia(3) == 6
    assert silnia(5) == 120
    assert silnia(-5) == "Error"
