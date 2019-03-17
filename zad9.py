import datetime
rok_urodzenia = int(input("PODAJ ROK URODZENIA"))
aktualny_rok = datetime.datetime.now().year
wynik = aktualny_rok - rok_urodzenia
if wynik >=18:
    print ("Jesteś pełnoletni!")
else:
    print("Nie jesteś pełnoletni!")