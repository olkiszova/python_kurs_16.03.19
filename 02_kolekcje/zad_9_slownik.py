#zdefiniowanie słownika
produkty = {
    'ziemniaki':1.99,
    'bataty': 5.99,
    'pomidory': 6
}
#żeby nie kupić więcej niż jest w magazynie

magazyn = {
    'ziemniaki':40,
    'bataty': 30,
    'pomidory':20
}
#Przechowujemy tu kto ile czego chce kupić, taka jakby kasa na która nabijamy produkty, które chcemy kupić
koszyk = {}
print ("Uruchomiłeś program kasjer.")

while True:
    komenda = input("Przyszedł klient [k] czy chcesz dodać do magazynu [m]? - by zakończyć wpisz 0? " )

    if komenda == 'k':
        print("Witaj w naszym, sklepie, oto nasza oferta: ")
        for pr in produkty:
            print(f" - {pr} w cenie: {produkty[pr]} za kg")

        while True: # pętla while żeby można było kupić więcej niż jeden produkt
            print()
            co_kupi = input("co chcesz kupić [k-koniec]? ")
            if co_kupi == 'k':
                break
            if co_kupi in produkty:
                ile = float(input (f"Ile chcesz [{co_kupi}]?: "))
                if ile > magazyn[co_kupi]:
                    print("Nie mama tyle tego produktu")
                else:
                    cena = ile *produkty [co_kupi]
                    koszyk[co_kupi] = koszyk.get(co_kupi, 0) + round(cena,2)
                    magazyn [co_kupi] -= ile
            else:
                print("Przepraszamy, nie mamy tego w asortymencie")

        for pr in koszyk:
            print (f"Za {pr}: {koszyk[pr]} PLN")
        print ("="*30)
        print(f"Suma: {sum(koszyk.values())}")

    elif komenda == 'm':
        produkt_do_dodania = input ("Co chcesz dodać? ")
        ile_do_dodania = int(input("Ile chcesz tego dodać? "))
        if produkt_do_dodania not in produkty:
            cena_za_kg = float(input("Podaj cenę za kg"))
            produkty[produkt_do_dodania] = cena_za_kg
        magazyn[produkt_do_dodania] = magazyn.get (produkt_do_dodania, 0) + ile_do_dodania

        print(magazyn, produkty)


