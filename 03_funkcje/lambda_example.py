data = [1, 2, 3, 4, 5, 6, 7]


# def wybierz (dane, warunek):
#     out =[]
#     for el in dane:
#         if warunek (el): #el %2 == 0:
#             out.append(el)
#     return out
# def podzielne_przez_2 (x):
#     return x%2 == 0
#
# print (wybierz(a, lambda x: x>3))
#
# print (wybierz(a, lambda x: x%3 == 0))

result = []
def przytnij(data, start, stop):
    out = []
    for el in data:
        if start (el):
            result.append (el)
        if stop (el):
            break

    return out


def test_przytnij():
    przytnij_result = przytnij (
        data = [1, 2, 3, 4, 1, 6, 7, 8]
        start = lambda x: x>3,
        stop = lambda x: x == 6
    )
    assert przytnij(data) == [4, 5, 6]
