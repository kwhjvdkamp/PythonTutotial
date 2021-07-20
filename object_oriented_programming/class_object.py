import numpy as np

# class MyCounter:
#     def set_count(self,n):
#         self.count = n

# mc = MyCounter()
# mc.set_count(5)
# mc.count = mc.count + 1
# print(mc.count)

# # Include a set_name method
# class Employee:

#     def __init__(self, name='', balance=0): # <-- balance parameter added
#         # Preferred way to create attributes
#         self.name = name
#         self.balance = balance # <-- balance attribute added
#         print('The __init__ method was called!\r\nAttributes\r\n'
#             + ' \'name\'-, \r\n \'balance\'\r\ninitially set')

#     # A for Employee created set_name() method
#     def set_name(self, new_name):
#         # A for Employee created attribute name
#         self.name = new_name

#     # A for Employee created set_salary() method
#     def set_salary(self, new_salary):
#         # A for Employee created attribute salary
#         self.salary = new_salary

# # Create an object emp of class Employee
# emp = Employee()

# # Use set_name to set the name of emp to 'Korel Rossi'
# emp.set_name('Korel Rossi')

# # print(emp.salary) # At this stage => AttributeError: 'Employee' object has no attribute 'salary'

# # Set the salary of emp to 50000
# emp.set_salary(50000)

# print(emp.salary)
# # OUTPUT
# # 50000

# print(dir(emp))
# # OUTPUT
# # ['__class__'
# #   , '__delattr__'
# #   , '__dict__'
# #   , '__dir__'
# #   , '__doc__'
# #   , '__eq__'
# #   , '__format__'
# #   , '__ge__'
# #   , '__getattribute__'
# #   , '__gt__'
# #   , '__hash__'
# #   , '__init__'
# #   , '__init_subclass__'
# #   , '__le__'
# #   , '__lt__'
# #   , '__module__'
# #   , '__ne__'
# #   , '__new__'
# #   , '__reduce__'
# #   , '__reduce_ex__'
# #   , '__repr__'
# #   , '__setattr__'
# #   , '__sizeof__'
# #   , '__str__'
# #   , '__subclasshook__'
# #   , '__weakref__'
# #   , 'name'
# #   , 'salary'
# #   , 'set_name'
# #   , 'set_salary'
# # ]



# Write the class Point as outlined in the instructions
# class Point:
#     """ A point on a 2D plane

#    Attributes
#     ----------
#     x : float, default 0.0. The x coordinate of the point
#     y : float, default 0.0. The y coordinate of the point
#     """

#     def __init__(self, x=0.0, y=0.0):
#       self.x = x
#       self.y = y

#     def distance_to_origin(self):
#       """Calculate distance from the point to the origin (0,0)"""
#       return np.sqrt(self.x ** 2 + self.y ** 2)

#     def reflect(self, axis):
#       """Reflect the point with respect to x or y axis."""
#       if axis == "x":
#         self.y = - self.y
#       elif axis == "y":
#         self.x = - self.x
#       else:
#         print("The argument axis only accepts values 'x' and 'y'!")

# 3 Using class Point()
# pt = Point(x=3.0)
# pt.reflect("y")
# print((pt.x, pt.y))
# pt.y = 4.0
# print(pt.distance_to_origin())