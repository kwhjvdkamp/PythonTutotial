A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 7, 9, 11, 13, 15}
C = {1, 2, 8, 10, 11, 12, 13, 14, 15, 16, 17}
D = {1, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
E = {9, 10, 11, 12, 13, 14, 15}

#   X ∩ Y  <-> Intersection (∩) between X and Y (all elements which are in both X and Y)
#   X ∪ Y  <-> Union (∪) between X and Y (all elements which are either in X or Y)
#   X − Y  <-> Difference between X and Y (all elements which are in X but not in Y)

# You are given 5 sets of integers A, B, C, D,E. What is the result of the following expression?
# Calculate ( A ∪ ( B ∩ C ) ) − ( D ∩ E )
# In words  ( A union ( B insertection C ) ) difference ( D intersection E )
print( (A.union(B.intersection(C))).difference(D.intersection(E)) ) 