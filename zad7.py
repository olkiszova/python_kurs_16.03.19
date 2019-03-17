liczba = input("Podaj liczbę: ")
liczba = int(liczba)
wynik = (liczba % 2 == 0 and liczba % 3 == 0 and  liczba > 10) or liczba ==7
print(f"Podzielna przez 2,  3 i większa od 10 lub równa 7",
      wynik
      )

