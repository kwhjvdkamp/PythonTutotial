from functools import reduce

# Reverse a string using reduce()
string = 'DataCamp'
inv_string = reduce(lambda x, y: y + x, string)
print('Inverted string = ' + inv_string) 

print("#------------------------------")

# Find common items shared among all the lists in lists
lists = [[1, 4, 8, 9], [2, 4, 6, 9, 10, 1], [9, 0, 1, 2, 4]]
common_items = reduce(lambda x, y: set(x).intersection(y), lists)
print('common items = ' + str(common_items))

print("#------------------------------")

# Convert a number sequence into a single number
nums = [5, 6, 0, 1]
num = reduce(lambda x, y: 10*x + y, nums)
print(str(nums) + ' is converted to ' + str(num))