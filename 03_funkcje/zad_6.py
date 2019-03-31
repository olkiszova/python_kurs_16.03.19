lista = [1, 2, [3, 4, [5]]]
rezultat = []
def splaszcz(lista):
    for i in lista:
        if isinstance (i, list):
             for e in splaszcz(i):
                rezultat.append(i)
    return rezultat

def test_splaszcz_pusta_lista ():
    assert splaszcz ([]) == []


def test_splaszcz_plaska_lista ():
    assert splaszcz ([1,2,3]) == [1, 2, 3]

def test_splaszcz_zagniezdzona_lista():
    assert splaszcz ([1, 2, [3, 4, [5]]]) == [1, 2, 3, 4, 5]

