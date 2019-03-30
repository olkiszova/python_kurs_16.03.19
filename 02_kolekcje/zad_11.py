unikalne_liczby = set()

while True:
    dana = input("Podaj liczbę [k aby zakończyć]: ")
    if dana == 'k':
        break
    unikalne_liczby.add(int(dana))


print (f"Unikalne liczby: {len(unikalne_liczby)}")
print (f"Z czego parzystych w przedaile 0-100 jest {len(unikalne_liczby & set(range(0,101,2)))}")