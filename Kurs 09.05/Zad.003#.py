

# Zaimplementuj klasę ElectricCar odwzorowując zachowanie samochodu elektrycznego. Klasa powinna umozliwić pokonanie
# zadanego dystansu , który nie może przekroczyć maksymalnego zasięgu zdefiniowanego dla samochodu. Samochód powinnien
# mieć także mozliwość naładowania bataerii

# >>> car = ElectricCar(100)
# >>> car.drive(70)
# >>> 70
# >>> car.drive(50)
# >>> (30)
# >>> car.drive(50)
# >>> 0
# >>> car.drive(50)
# >>> 50



class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self.__traveled_distance = 0

    def drive(self, distance):
        if distance + self.__traveled_distance <= self.max_range:
            self.__traveled_distance += distance
            return distance
        else:
            to_travel = self.max_range - self.__traveled_distance
            self.__traveled_distance = self.max_range
            return to_travel


    def possible_distance(self):
         return self.max_range - self.__traveled_distance

    def charge(self):
         self.__trafeled_distance = 0

ec = ElectricCar(100)
print(ec._ElectricCar__traveled_distance)
ec.__traveled_distance = 90
print(ec.__traveled_distance)
print(ec._ElectricCar__traveled_distance)
print(ec.drive(80))
print(ec.possible_distance)


class TestElectricCar:

    def test_init(self):
        car = ElectricCar(100)
        assert car

    def test_drive(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70
        assert car.drive(50) == 30

    def test_drive_over_distance(self):
        car = ElectricCar(50)
        assert car.drive(80) == 50
        assert car.drive(10) == 0

    def test_charge(self):
        car = ElectricCar(50)
        assert car.drive(80) == 50
        assert car.drive(80) == 0
        car.charge()
        assert car.drive(80) == 50