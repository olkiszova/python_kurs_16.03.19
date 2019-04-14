import random
class Postac:
    def __init__(self, imie, atak, obrona, energia):
        self.imie = imie
        self._atak = atak
        self._obrona = obrona
        self.energia = energia
        self.ekwipunek = []

    def losowa_postac(self):
        imie = random.choice(["Adam", "Izydor", "Rufus", "Jeremiasz", "Flaneli"])
        atak = round(random.uniform(5,12))
        obrona = random.uniform (5,12)
        energia = random.uniform (20,120)
        return cls(imie, atak, obrona, energia)

    def przedstaw_sie(self):
        print(f"Jestę {self.imie}, mam {self.atak} ataku, {self.obrona} obrony i {self.energia} życia")

    def __str__(self):
        print f"{self.imie}({self.atak:.2f}/{self.obrona})"

    @property
    def atak(self):
        atak = self._atak
        for przedmiot in self.ekwipunek:
            atak += przedmiot.bonus_do_ataku
        return atak

    @property
    def obrona(self):
        return self._obrona
        for przedmiot in self.ekwipunek:
            obrona += przedmiot.bonus_do_obrony
        return obrona

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def uderz(self, postac):
        obrazenia = self.atak - postac.obrona
        obrazenia *= round(random.uniform(0.5, 1), 2)
        if obrazenia > 0:
            postac.energia -= obrazenia
            print(f"{self.imie} zadaje cios za {obrazenia:.2f} punktow") # f- jako fl;oating point, po kropce 2 wartości

    def czy_zyje(self):
        return self.energia > 0

    def walka(self, postac):
        print ('Do walki stają: ')
        self.przedstaw_sie()
        postac.przedstaw_sie()
        while True:
            # self uderza postac
            self.uderz(postac)

            # spr. czy postac zyje
            if not postac.czy_zyje():
                print(f'{self.imie} wygrywa z {postac.imie}')
                break
            # postac uderza self
            postac.uderz(self)
            # spr czy self zyje
            if not self.czy_zyje():
                print(f'{postac.imie} wygrywa z {self.imie}')
                break


class Przedmiot:
    def __init__(self, nazwa, bonus_do_ataku, bonus_do_obrony):
        self.nazwa = nazwa
        self.bonus_do_ataku = bonus_do_ataku
        self.bonus_do_obrony = bonus_do_obrony


class TestPrzedmiot:

    def test_przedmiot_initialization(self):
        przedmiot = Przedmiot('Siekiera', 20, 5)
        assert przedmiot.nazwa == 'Siekiera'
        assert przedmiot.bonus_do_ataku == 20
        assert przedmiot.bonus_do_obrony == 5


class TestPostac:

    def test_postac_initialization(self):
        postac = Postac("Albert", atak=10, obrona=15, energia=100)
        assert postac.imie == "Albert"
        assert postac.atak == 10
        assert postac.energia == 100
        assert postac.ekwipunek == []

    def test_postac_przedstaw_sie(self, capsys):
        postac = Postac("Albert", atak=10, obrona=15, energia=100)
        postac.przedstaw_sie()
        captured = capsys.readouterr()
        assert captured.out == "Jestę Albert, mam 10 ataku, 15 obrony i 100 życia\n"

    def test_postac_daj_przedmiot(self, capsys):
        postac = Postac("Albert", atak=10, obrona=15, energia=100)
        przedmiot = Przedmiot('Siekiera', 20, 5)
        assert len(postac.ekwipunek) == 0
        postac.daj_przedmiot(przedmiot)
        assert len(postac.ekwipunek) == 1
        postac.przedstaw_sie()
        captured = capsys.readouterr()
        assert captured.out == "Jestę Albert, mam 30 ataku, 20 obrony i 100 życia\n"

    def test_czy_zyje(self):
        postac = Postac("Albert", atak=10, obrona=15, energia=100)
        assert postac.czy_zyje()
        postac.energia = 0
        assert postac.czy_zyje() == False

if __name__ == '__main__':
    albert = Postac("Albert", atak=17, obrona=15, energia=100)
    teodor = Postac("Teodor", atak=22, obrona=11, energia=110)
    siekiera = Przedmiot('Siekiera', 20, 5)
    albert.daj_przedmiot(siekiera)
    albert.walka(teodor)

    for _ in range(12):
        Postac.losowa_postac().przedstaw_sie()