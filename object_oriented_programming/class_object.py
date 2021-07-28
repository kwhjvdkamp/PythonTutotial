import numpy as np
# import datetime from datetime
from datetime import datetime


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

#     # Class attributes are GLOBAL variables (constants), no self
#     # CAP_ITAL = '<string>'or INT/FLOAT
#     # To be used as: ClassName.CAP_ITAL

#     def __init__(self, x=0.0, y=0.0):
#       # Instance attributes (binding to 'self'; the current instance)
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


# class Player:
#     MAX_POSITION = 10

#     def __init__(self):
#         self.position = 0

#     # Add a move() method with steps parameter
#     def move(self, steps):
#         if self.position + steps < Player.MAX_POSITION:
#             self.position = self.position + steps
#         else:
#             self.position = Player.MAX_POSITION


#     # This method provides a rudimentary visualization in the console
#     def draw(self):
#         drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
#         print(drawing)

# p = Player(); p.draw()
# p.move(4); p.draw() # moves 'pipe' 4 steps (if)
# p.move(5); p.draw() # moves 'pipe' 5 steps (if)
# p.move(3); p.draw() # moves 'pipe' 10 steps (else)


# class BetterDate:
#     def __init__(self, year, month, day):
#       self.year, self.month, self.day = year, month, day

#     @classmethod
#     def from_str(cls, datestr):
#       year, month, day = map(int, datestr.split("-"))
#       return cls(year, month, day)

#     # Define a class method from_datetime accepting a datetime object
#     @classmethod
#     def from_datetime(cls, datedatetime):
#       return cls(datedatetime.year, datedatetime.month, datedatetime.day)


# # You should be able to run the code below with no errors:
# today = datetime.today()
# now = datetime.now().isoformat()
# print(now.split("T")[0]) # current date and time

# bdStr = BetterDate.from_str(now.split("T")[0])
# print(bdStr.year)
# print(bdStr.month)
# print(bdStr.day)
# bdDatetime = BetterDate.from_datetime(today)
# print(bdDatetime.year)
# print(bdDatetime.month)
# print(bdDatetime.day)


# class Counter:
#     def __init__(self, count=0):
#        self.count = count

#     def add_counts(self, n):
#         print('self', self.count)
#         print('n', n)
#         self.count += n
#         print('self', self.count)

# class Indexer(Counter):
#    pass

# ind = Indexer()
# indAddedCounts = ind.add_counts(5)
# print(indAddedCounts)


class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)


mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)