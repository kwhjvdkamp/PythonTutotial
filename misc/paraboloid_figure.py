# Import the pandas-PACKAGE
import matplotlib.pyplot as plt
import pandas as pd

# gca stands for 'get current axis'
ax = plt.gca()

# 3D-paraboloid can be described with equation:
# (x2/a2) + (y2/a2) = z

# If the coefficient 'a' is set to 1 
# then the radius at each cut will be equal to √z (square-root of z).

# Your task is to create a dictionary that stores the mapping
# from the pair of coordinates (x, y) to the z-coordinate

# The list for 'x' and the list for 'y' are given:
range_x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
range_y = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

circ_paraboloid = dict()

for x in range_x:
    for y in range_y:
        # Calculate the value for z
        # Equation: (x**2/a**2) + (y**2/a**2) = z
        # Coefficient (a) = 1
        # => ( x**2 / (1**2) ) + ( y**2 / (1**2) ) = z
        p = x**2 / (1**2)
        q = y**2 / (1**2)
        z = ( p ) + ( q )
        # Create a new key for the dictionary
        key = (x,y)
        # print("key (x,y): ", key)
        # Create a new key-value pair
        circ_paraboloid[key] = z

# print (circ_paraboloid.items())
# print('circ_paraboloid: ', circ_paraboloid)
# # Prints something like
# ====================================
# [
#   ((0.0, 0.0), 0.0), 
#   ((0.0, 0.2), 0.04000000000000001), 
#   ....
# ]
# ====================================

# print('circ_paraboloid[(1.8, 1.4)]: ', circ_paraboloid[(1.8, 1.4)])

my_paraboloid = dict()
my_keys = []
my_keys_index = []
my_values = []

for key, value in circ_paraboloid.items():
    my_keys.append(key)
    my_values.append(value)

# my_paraboloid[key.index()] = value
print(len(my_keys))
print(len(my_values))

for key in my_keys:
    my_keys_index.append(my_keys.index(key) + 1 )

# print(my_keys_index)

# my_paraboloid = zip(my_keys_index, my_values)
my_paraboloid= {}

# print(my_paraboloid)

# Create a dataframe CLASS object
df = pd.DataFrame(my_paraboloid)

print(df)

df.plot(kind='scatter', x=0, y=1, color='red', ax=ax)

plt.show()