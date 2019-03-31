def dodaj (*args):
    print (args)
    return sum(args)
dodaj (1,2,3,4,5,6,7,7)
def test_dodaj():
    assert dodaj (1,2) == 3
    assert dodaj (1, 2, 3, 4, 5) == 15
    assert dodaj (1,2, 3, 4, 5, 7, 1, 2, 3) == 15 + 7+ 6



def foo (a, *args, stawka =2, kwargs):
    print (a, stawka)
    print (args)
    print (kwargs)
    for k in kwargs:
        print 


foo (1, 2, 3, b=2, c=3)