class Person:
    moods = ('happy', 'tired', 'lazy')

    def __init__(self, name, money, mood='happy', health_rate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    @property
    def health_rate(self):
        return self.__health_rate

    @health_rate.setter
    def health_rate(self, health_rate):
        if health_rate >= 100:
            self.__health_rate = 100
        elif health_rate < 0:
            self.__health_rate = 0

    def sleep(self, hours):
        if hours > 7:
            self.mood = self.moods[2]
        elif hours < 7:
            self.mood = self.moods[1]
        else:
            self.mood = self.moods[0]

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        self.money -= items*10


# p = Person("mohamed", 1000, 'happy', 75)
# print(p.name, p.money, p.money, p.health_rate)
# p.eat(2)
# p.sleep(5)
# p.buy(10)
# print(p.mood, p.health_rate, p.money)
