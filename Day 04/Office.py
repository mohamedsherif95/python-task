from Employee import Employee
import json
import copy


class Office:
    employees_num = 0

    @classmethod
    def change_emps_num(cls, hiring):
        if hiring:
            cls.employees_num += 1
        else:
            cls.employees_num -= 1

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        trip_time = distance / velocity
        arrival_hour = move_hour + trip_time
        return arrival_hour > target_hour

    def __init__(self, name, employees=None):
        if employees is None:
            employees = []
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp_id == emp.get('emp_id'):
                return emp

    def hire(self, *args):
        for i in range(len(args)):
            new_emp = copy.deepcopy(args[i])
            new_emp.__dict__.update({'car': args[i].car.__dict__})
            self.employees.append(new_emp.__dict__)
            self.change_emps_num(True)

    def fire(self, emp_id):
        for emp in self.employees:
            if emp_id == emp.get('emp_id'):
                self.employees.remove(emp)
                self.change_emps_num(False)

    def deduct(self, emp_id, deduction):
        for emp in self.employees:
            if emp_id == emp.get('emp_id'):
                emp.update({'_Employee__salary': emp.get('_Employee__salary') - deduction})

    def reward(self, emp_id, reward):
        for emp in self.employees:
            if emp_id == emp.get('emp_id'):
                emp.update({'_Employee__salary': emp.get('_Employee__salary') + reward})

    def check_lateness(self, emp_id, move_hour):
        for emp in self.employees:
            if emp_id == emp.get('emp_id'):
                distance = emp.get('distance_to_work')
                velocity = emp.get('car')['_Car__velocity']
                if self.calculate_lateness(9, move_hour, distance, velocity):
                    self.deduct(emp_id, 10)
                else:
                    self.reward(emp_id, 10)



emp_car = {'name': 'fiat 128', 'velocity': 70, 'fuel_rate': 100}
emp1 = Employee(1, 'moh@mail.com', 3000, emp_car, 20, "Mohamed", 5000)
emp2 = Employee(2, 'ah@mail.com', 4000, emp_car, 20, "Ahmed", 4245)
emp3 = Employee(3, 'ali@mail.com', 5000, emp_car, 20, "Ali", 7577)
emp4 = Employee(3, 'ali@mail.com', 6000, emp_car, 20, "Ali", 58756)

hr = Office('hr')
it = Office('it')

hr.hire(emp1, emp2)
it.hire(emp4, emp3)

with open("hr office.json", "w") as outfile:
    json.dump(hr.get_all_employees(), outfile, indent=4)

with open("it office.json", "w") as outfile:
    json.dump(it.get_all_employees(), outfile, indent=4)

# hr.check_lateness(1, 11)
# print(hr.get_all_employees())
# print(it.get_all_employees())
# print(hr.employees_num)
# hr.fire(2)
# it.fire(1)
# print(hr.employees_num)
# print(hr.get_employee(1))


# hr.deduct(1, 500)
# print(hr.get_employee(1))
# hr.reward(1, 1000)
# print(hr.get_employee(1))

# emp_attr = emp1.__dict__
# print(dir(emp_attr))

# hr.hire([2,'mohamed','mohamed@mail.com',2000])
# print(hr.get_all_employees())
