# 01 Python? Wat is it?
i = 1

# How to install Python

# How to work with the Python-interpreter

# Numbers and how to calculate with them

# Difference between types and variables

# How to perform operations on text


# 02 Install Python

# Python is 'open source'

# Download from : www.python.org/downloads

# Python installation on Windows
# 2 versions: 32- or 64-bit
# IMPORTANT: SELECT
# 1) Install launcher for all users
# 2) Add Python to PATH

# Check installation on a command prompt (cmd)
# > python --version


# The Python-interpreter has been installed
# The interpreter translate the python programming language statements to machine language which the computer understands


# > Python 3.x.y
# '>>>'
# three times the 'larger than'-sign means the interpreter is ready to receive commands
# To leave the interpreter:
# type exit(), quit() or press Ctrl+D

# To start with Python, use Thonny (standard installed with Python from version 3.7) otherwise use a development tool of your choice (VS Code e.g.)
# ===============================================
# Simple and tail recursive Python program to
# reverse a linked list

# # Node class
# class Node:

#     # Constructor to initialize the node object
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:

#     # Function to initialize head
#     def __init__(self):
#         self.head = None

#     def reverseUtil(self, curr, prev):

#         # If last node mark it head
#         if curr.next is Node:
#             self.head = curr

#         # Update next to prev node
#         curr.next = prev
#         return

#         # Save curr.next node for recursive call
#         next = curr.next

#         # And update next
#         curr.next = prev

#         self.reverseUtil(next, curr)

# ===============================================


# 04 Python as calculator

i += 1
print('[',i,'] > ', 1+1)                        # 2

i += 1
print('[',i,'] > ', 1.5*3)                      # 4.5

# Celsius to Fahrenheit
x=32
i += 1
print('[',i,'] > ', (212-x)*5/9)                # 100.0

print(20*1.8+32)                                # 68.0

# operator '**' means 'exponentiation' (machtsverheffen)
i += 1
print('[',i,'] > ', 3**4)                       # 81

# Python knows two types of numbers 'natural' and 'float' numbers
# If somewhere in a calculation a float is used the final answer will be a float


# 05 Division:
# operator '/' (final answer will always be a float)

# operator '//' (final answer will always be a float), a division with this operator means the decimals will be ignored
i += 1
print('[',i,'] > ', 10/3)                       # 3

# It is possible to call the decimals for a division like this as well
i += 1
print('[',i,'] > ', 10%3)                       # 1

# operators '//' and '%' useable on floats calculations as well


# 06 Types
i += 1
print('[',i,'] > ', type(1+1))                  # <class 'int'>

i += 1
print('[',i,'] > ', type(3.1))                  # <class 'float'>

i += 1
print('[',i,'] > ', type(7.5//2.1))             # <class 'float'>
# answer is 3.0 note a float has been used in the calculation

i += 1
print('[',i,'] > ', type(7//3))                 # <class 'int'>
# answer is 2 note only integers has been used in the calculation


# 07 Variables
_ = 7/3
i += 1
print('[',i,'] > ', _)                          # 2.3333333333333335
i += 1
print('[',i,'] > ', _*5)                        # 11.6666666666666668
# '_' is used as the varable on which the answer previous calculation is stored

teller=10
noemer=3
resultaat=teller//noemer
rest=teller%noemer
i += 1
print('[',i,'] > ', teller)                     # 10
i += 1
print('[',i,'] > ', noemer)                     # 3
i += 1
print('[',i,'] > ', resultaat)                  # 3
i += 1
print('[',i,'] > ', rest)                       # 1
i += 1
print('[',i,'] > ', type(rest))                 # <class 'int'>

# variable 'breuk' has not been instantiate yet, source
# x = type(breuk)
# print(x)                                      # causes a an error with message
# # NameError:name 'breuk' is not defined


# 08 Text

# A string is presented with start and end single (') of double quotes (")
# To use a single or double quotes within a string, these characters need to be to escape: use a backslash
# "This is a \'character\'"

# Operations on text
i += 1
print('[',i,'] > ', 'Py''thon')                 # 'Python'
i += 1
print('[',i,'] > ', 'Py'+'thon')                # 'Python'
i += 1
print('[',i,'] > ', 2*'Py'+2*'thon')            # 'PyPythonthon'
i += 1
print('[',i,'] > ', len('PyPythonthon'))        # 12

# Try
x = 'PyPythonthon'.lower()
i += 1
print('[',i,'] > ', x)
y = 'PyPythonthon'.upper()
i += 1
print('[',i,'] > ', y)
z = 'PyPythonthon'.capitalize()
i += 1
print('[',i,'] > ', z)
v = 'PyPythonthon'.swapcase()
i += 1
print('[',i,'] > ', v)
