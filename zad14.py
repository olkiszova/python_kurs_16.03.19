
wart_min = None
wart_maks = None
liczba = None
while True:
    komenda = input("Podaj liczbę lub wpisz [k] żeby zakończyć: ")
    if komenda == "k":
        break
    try:
        liczba = int(komenda)
    except:
        print ("Powineneś wpisać liczbę lub [k] by zakończyć")
    if wart_min is None:
        wart_min = liczba
    else:
        if liczba<wart_min:
            wart_min = liczba
    if wart_maks is None:
        wart_maks = liczba
    else:
        if liczba>wart_maks:
            wart_maks = liczba
print (f"Maks: {wart_maks}")
print (f"Min: {wart_min}")