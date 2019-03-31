
# Silnia
# def silnia(a):
#     if a > 1:
#         return a * silnia(a-1)
#     else:
#         return 1
# print (silnia(3))
#
# def test_silnia():
#     assert silnia(3) == 6
#
# def test_silnia_1():
#     assert silnia(4) == 24
#


lista = [10, 20, 30, 40]

def rekuprint (lista):
    if len(lista) == 1:
        print (lista[0])
        rekuprint (lista [1:])

rekuprint (lista)





#wynik jaki mamy dostać
# 10
# 20
# 30
# 40