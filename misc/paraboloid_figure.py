# 3D-paraboloid can be described with equation:
# (x2/a2) + (y2/a2) = z
# ******* Set the coefficient a to 1 ******** 
# Then the radius at each cut will be equal to √z (square-root of z).

# Your task is to create a dictionary that stores the mapping 
# from the pair of coordinates (x, y) to the z-coordinate 
# The lists for x and y are given: 
# > range_x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
# and 
# > range_y = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0] 
# respectively.

range_x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
range_y = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0] 

circ_parab = dict()

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
        print("key (x,y): ", key)
        # Create a new key-value pair      
        circ_parab[key] = z


print('circ_parab: ', circ_parab)
print('circ_parab[(1.8, 1.4)]: ', circ_parab[(1.8, 1.4)])