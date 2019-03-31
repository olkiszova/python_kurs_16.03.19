def wiecej_niz(tekst, prog):
    rezultat = set()
    liczniki_liter = {}
    for znak in tekst:
        liczniki_liter[znak] = liczniki_liter.get(znak, 0) + 1
    for znak in liczniki_liter:
        if liczniki_liter[znak] > prog:
            rezultat.add(znak)

    return rezultat

#inny sposób

def wiecej_niz(tekst, prog):
    rezultat = set()
    for znak in tekst:
        if tekst.count(znak) > prog:
            rezultat.add(znak)
    return rezultat


def test_wiecej_niz_dla_pustego_napis():
    assert wiecej_niz("", 1) == set()


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("aaabbcc", 2) == set('a')
