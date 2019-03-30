lista = [9,1,6,8,4,3,2,0]
print (lista)

def selection_sort(lista):
    for m in range(len(lista) - 1, 0, -1):
        maks= 0
        for location in range(1, m + 1):
            if lista[location] > lista[maks]:
                maks = location

        temp = lista[m]
        lista[m] = lista[maks]
        lista[maks] = temp

selection_sort(lista)
print(lista)