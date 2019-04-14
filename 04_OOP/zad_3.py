class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self.travel_distance = 0

    def drive(self, distance):
        if self.travel_distance + distance > self.max_range:
            to_travel = self.max_range - self.travel_distance
            self.travel_distance = self.max_range
            return to_travel
        else:
            self.travel_distance += distance
        return distance

    def charge(self,):
        self.travel_distance = 0


def test_car1_initialization():
    car1 = ElectricCar(100)
    assert car1.max_range == 100
    assert car1.travel_distance == 0


def test_charge():
    car1 = ElectricCar(100)
    assert car1.drive(120) == 100
    assert car1.drive(10) == 0
    car1.charge()
    assert car1.drive(120) == 100


def test_drive():
    car1 = ElectricCar(100)
    assert car1.drive(70) == 70
    assert car1.travel_distance == 70
    assert car1.drive(50) == 30
    assert car1.travel_distance == 100
    assert car1.drive(10) == 0
    assert car1.travel_distance == 100
