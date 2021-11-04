class Car:
    def __init__(self, car):
        self.name = car.get('name')
        self.fuel_rate = car.get('fuel_rate')
        self.velocity = car.get('velocity')

    @property
    def fuel_rate(self):
        return self.__fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, fuel_rate):
        if fuel_rate >= 100:
            self.__fuel_rate = 100
        elif fuel_rate < 0:
            self.__fuel_rate = 0
        else:
            self.__fuel_rate = fuel_rate

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        if velocity >= 200:
            self.__velocity = 200
        elif velocity < 0:
            self.__velocity = 0
        else:
            self.__velocity = velocity

    def run(self, distance, velocity):
        self.velocity = velocity
        initial_rate = self.fuel_rate
        self.fuel_rate -= distance
        if self.fuel_rate == 0:
            distance -= initial_rate
        self.stop(distance)

    def stop(self, distance):
        self.velocity = 0
        if self.fuel_rate == 0 and distance != 0:
            print(f"{distance} Km remaining till destination")
        else:
            print("Arrived at destination!")


# emp_car = {'name': 'fiat 128', 'velocity': 100, 'fuel_rate': 100}
# car1 = Car(emp_car)
# print(car1.__dict__)
