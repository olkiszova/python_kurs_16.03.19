napis = "Ala ma <kota>, a kot ma Alę"
czy_zliczac = False
licznik = 0


for znak in napis:
    if znak == "<":
        czy_zliczac = True
        continue
    elif znak == ">":
        czy_zliczac = False
    elif czy_zliczac:
        licznik += 1


print(licznik)