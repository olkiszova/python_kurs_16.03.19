class Pies:
    liczba_nog = 4
    gatunek = "Canis Canis"


    def __init__(self, imie, rasa, wiek):
        #atrybuty instancji
        self.imie = imie
        self.rasa = rasa
        self.wiek = wiek
        self.usposobienie = 'Przyjacielski'

    #metoda instancji
    def ludzki_wiek(self):
        return self.wiek * 7


 #utworz metode opisz_sie
  def opisz_sie (self):
        print


azor = Pies("Azor", "kundel", 10) #instancja klasy Pies
reksio = Pies("Rex", "owczarek", 4) #instancja klasy Pies

print(azor== reksio) #wynikiem będzie False

azor.imie = "Azor"
azor.rasa = "kundel"
reksio.imie = "Rex"
reksio.rasa = "owczarek"
azor.wiek = 10
reksio.wiek = 4
print(azor.wiek)
# print(reksio.wiek) #będzie bład bo nie ma podanego dla reksia wieku

# wynik jest taki sam dla reksia i azora
print(azor.liczba_nog)
print(reksio.ludzki_wiek())

