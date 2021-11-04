import re
from Person import Person
from Car import Car

reg = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


class Employee(Person):

    def __init__(self, emp_id, email, salary, car, distance_to_work, name, money):
        super().__init__(name, money)
        self.emp_id = emp_id
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work
        self.car = Car(car)


    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            self.__salary = 1000
        else:
            self.__salary = salary

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not re.search(reg, email):
            raise Exception("Invalid email format")
        self.__email = email

    def work(self, hours):
        if hours > 8:
            self.mood = 'tired'
        elif hours < 8:
            self.mood = 'lazy'
        else:
            self.mood = 'happy'

    def send_mail(self, to, subject, msg, receiver_name):
        email = open(f'email_{subject}', 'w')
        email.write(f'From: {self.email}\nTo: {to}\n\nHi, {receiver_name}\n{msg}')
        email.close()


    def drive(self, velocity):
        self.car.velocity = velocity
        self.car.run(self.distance_to_work, velocity)


    def refuel(self, gas_amount):
        self.car.fuel_rate += gas_amount


# emp1 = Employee(1, 'moh@mail.com', 3000, "Fiat 128", 20, "Mohamed", 5000)
#
# print(f'fuel:{emp1.car.fuel_rate}')
# emp1.drive(75)
# print(f'after arriving fuel:{emp1.car.fuel_rate}')
# emp1.refuel(10)
# print(f'after refuel:{emp1.car.fuel_rate}')




# print(emp1.moods)

# print(emp1.email)

# print(emp1.salary)
# emp1.salary = 5000
# print(emp1.salary)
# emp1.salary = 500
# print(emp1.salary)

# emp1.sleep(3)
# print(emp1.mood)

# emp1.work(8)
# print(emp1.mood)

# emp1.eat(3)
# print(emp1.health_rate)

# emp1.buy(5)
# print(emp1.money)
# emp1.send_mail('emp2@mail.com', 'Task', 'this is a reminder to finish up the task', 'Ahmed')
