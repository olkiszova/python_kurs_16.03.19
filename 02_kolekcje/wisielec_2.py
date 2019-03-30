imie = input ("Jak się nazywasz? ")

print (f"Cześć {imie}, czas na wisielca!")


word = "zagadka"

guesses = " "

turns = 10

while turns > 0:
    failed = 0
    for i in word:
        if i in guesses:
            print (i)
        else:
            print ("_")
            failed += 1
    if failed == 0:
        print ("Wygrałeś")
        break
    guess = input ("Podaj literę: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print ("Nie ma takiej litery")
        print (f"Pozostało Ci {turns} szans")
        if turns ==0:
            print ("Przegrałeś")


