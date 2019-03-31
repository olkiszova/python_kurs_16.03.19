def czy_jest_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

    return wynik


def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(3) == True
    assert czy_jest_pierwsza(5) == True
    assert czy_jest_pierwsza(17) == True
    assert czy_jest_pierwsza(2) == True


def test_czy_jest_pierwsza_dla_liczby_niepierwszej():
    assert czy_jest_pierwsza(25) == False
