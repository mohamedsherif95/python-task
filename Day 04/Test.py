# import operator
#
#
# class Spam(object):
#     def __init__(self, description, value):
#         self.description = description
#         self.value = value
#
#
#     @description.setter
#     def description(self, d):
#         if not d:
#             raise Exception("description cannot be empty")
#         self.__description = d
#
#
#     @value.setter
#     def value(self, v):
#         if not (v > 0):
#             raise Exception("value must be greater than zero")
#         self.__value = v
#
#
# class Office:
#     def __init__(self, name, employees=None):
#         if employees is None:
#             employees = [['id', 'name', 'email', 'salary']]
#         self.name = name
#         self.employees = employees
#
#
# office = Office('office1', 1)
#
# print(office.employees)

# import json
#
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))