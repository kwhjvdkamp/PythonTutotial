# Use on DataCamp to view a function which is preloaded into the environment of the example
# import inspect
# print(inspect.getsource(filter_word_counts)) 

# ==================================

# numbers = [1,2,7,0]
# numbers_cumbed = [ n**3 for n in numbers]
# print(list(zip(numbers, numbers_cumbed)))

# ==================================

# d = {}
# d[3] = 6
# print(d)

# ==================================

# d = {'a':0, 'b':1, 'c':2, 'd':3}
# # insert the appropriate brackets
# v = d['d']
# print(v)

# ==================================

# n1 = [3, 5, 8, 1]
# n2 = [n ** 2 for n in n1]
# pairs = zip(n1, n2)
# for idx, pair in enumerate(pairs):
#     n, m = pair
#     print('{} ^ {} = {}'.format(n, 2, m))

# ==================================

# d = {'a':20, 'b':21, 'c':22, 'd':23}
# d['b'] = 2
# print(d)

# ==================================

# escape_velocity = {
#     'earth': 1,
#     'jupiter': 5.32,
#     'saturn': 3.17
# }
# del(escape_velocity['jupiter'])
# print(escape_velocity)

# ==================================

# x = list(range(3))
# print(x)

# ==================================

# def store_lower(_dict, _string):
#     """Add a mapping between `_string` and a lowercased version of `_string` to `_dict`
  
#     Args:
#       _dict (dict): The dictionary to update.
#       _string (str): The string to add.
#     """
#     orig_string = _string
#     _string = _string.lower()
#     _dict[orig_string] = _string
 
# d = {}
# s = 'Hello'
# bla = store_lower(d, s)
# print(bla)

# ==================================

# x = 50
# def one():
#   x = 10

# def two():
#   global x
#   x = 30

# def three():
#   x = 100
#   print(x)

# for func in [one, two, three]:
#   func()
#   print(x)def return_a_func(arg1, arg2):

# ==================================

# import numpy as np

# # np.correlation
# # np.corrcoef
# # np.corr
# x = np.array([6, 4, 4, 4])
# y = np.array([0, 3, 8, 7])
# print(np.corrcoef(x, y))

# ==================================

# import numpy as np
# x = np.array([14, 21, 24, 24])
# y = np.array([12, 6, 23, 29])
# z = np.array([x, y])
# print(z.shape)

# ==================================

# import collections
# od = [('a',20), ('b',21), ('c',22)]
# d = collections.OrderedDict(od)
# d.popitem()
# print(d.items())

# ==================================

# z = [8,3,3,4,7,6]
# p = z.pop(0)
# print(p)

# ==================================

# l = [0, 3, 0, 3]
# print(sorted(l))

# ==================================

# d = {'a':20, 'b':21, 'c':22, 'd':23}
# for k,v in d.items():
#     print( k,v)
# for k in d.keys() :
#     print(k)
# for v in d.values():
#     print(v)

# ==================================

# d = {'a':10, 'b':11, 'c':12, 'd':13}
# v = d.get('a', 'Beep beep, error!')
# print(v)

# ==================================

# import numpy as np
# x = np.array([14, 21, 24, 24])
# y = np.array([12, 6, 23, 29])
# z = np.array([x, y])
# print(z.shape)

# ==================================

# import numpy as np
# costs = np.column_stack(([2, 1, 2, 1], [4, 6, 5, 5]))
# mean_costs = np.mean(costs[:,1])
# print(mean_costs)

# ==================================

# import numpy as np
# x = np.array([[4, 1, 1], [5, 9, 0]])
# for j in np.nditer(x):
#     print(j)

# ==================================

# ratio_to_earth = { 
#     'mercury': {'gravity': 0.378},
#     'mars': {'gravity': 0.377}
# }
# print(ratio_to_earth)

# ==================================

# import numpy as np
# x = np.random.seed(42)
# print(x)
# # print(np.random.randint(14, 20))

# ==================================

# def add_zeros(string):
#     """Returns a string padded with zeros to ensure consistent length"""
#     updated_string = string + '0'
#     def add_more():
#         """Adds more zeros if necessary"""
#         nonlocal updated_string
#         updated_string = updated_string + '0'
    
#     while len(updated_string) < 6:
#         add_more()
#     return updated_string

# print ((add_zeros('3.4'), add_zeros('2.345')))

# ==================================

# x = [2, -6, 10, -7, 1]
# greater_than_zero = filter(lambda n: (n > 0), x)
# print(list(greater_than_zero))

# ==================================

# def add_numbers(x, y, z):
#     print('x', x)
#     print('y', y)
#     print('z', z)
#     a = x + y + z
#     return a
# 
# add_numbers(2, 3, 4)

# ==================================

# def sorted_elements(x, desc=True, n=2):
#     new_x = sorted(x, reverse=desc)[0:n]
#     return new_x

# a = [5, 5, 12, 12, 14, 7]
# print(sorted_elements(a, desc = False))
# # OUTPUT: [5, 5]

# ==================================

# p = [0, 5, 15, 5, 10, 8]
# print(sorted(p, reverse=False))
# # OUTPUT: [0, 5, 5, 8, 10, 15]

# ==================================

# x = 1
# print(bool(x))
# # OUTPUT: True
# # print(int(x))
# # OUTPUT: 1
# # print(float(x))
# # OUTPUT: 1.0
# # print(log(x))
# # OUTPUT: NameError: name 'log' is not defined

# ==================================

# x = [11, 12, 13, 14]
# y = x
# y[2:4] = [15, 16]
# print(x)
# # OUTPUT: [11, 12, 15, 16]

# ==================================

# Find the mean of the second column of costs
import numpy as np
costs = np.column_stack(([2, 1, 2, 1],  
                         [4, 6, 5, 5]))
#   |c1 c2
# --|------                    
#r1 | 2  4
#r2 | 1  6
#r3 | 2  5
#r4 | 1  5
# print(costs)
# # OUTPUT:
# # [[2 4
# #   1 6
# #   2 5
# #   1 5]]
# mean_costs_a = np.mean(costs[1, :]) #  all elements of row 2 >> (1+6)/2=3.5
# print(mean_costs_a)
# # OUTPUT: 3.5
# mean_costs_b = np.mean(costs[:, 0]) #  all elements of column 1 >> (2+1+2+1)/4=1.5)
# print(mean_costs_b)
# # OUTPUT: 1.5
# mean_costs_c = np.mean(costs[:, 1]) #  all elements of column 2 >> (4+6+5+5)/4=5.0)
# print(mean_costs_c)
# # OUTPUT: 5.0
# mean_costs_d = np.mean(costs[0, :]) #  all elements of row 1 >> (2+4)/2=3.0)
# print(mean_costs_d)
# # OUTPUT: 3.0

# ==================================

# # [0,:] <>  [1,:] <> [:,0] <>  [:,1]
# #   3   <>   3,5  <>  1,5  <>   5.0
# mean_costs = np.mean(costs[:,1])
# print(mean_costs)

# ==================================

# # Remove the correct number from the list x
# x = [9, 2, 8, 4, 5]
# x.remove(9)
# print(x)

# ==================================

# import numpy as np
# x = np.array([14, 21, 24, 24])
# y = np.array([12, 6, 23, 29])
# z = np.array([x, y])
# print(z.size)  # OUTPUT: 8
# print(z.dimensions) # OUTPUT: AttributeError: 'numpy.ndarray' object has no attribute 'dimensions'
# print(z.shape) # OUTPUT: (2,4)

# ==================================

# import numpy as np
# x = np.array([9, 5])
# y = np.array([16, 12])
# # print(np.logical_not(x < 5))   # OUTPUT: [True True]
# # print(np.logical_not(y > 12))   # OUTPUT: [True False]
# print(np.logical_and(x < 6, y > 16))    # OUTPUT: [False False]

# x = 'Mining'
# y = 'Data '
# print(x + y)

# ==================================

# def find_type(**y):
#     return type(y)
# print(find_type(a = 'alpha', b = 'beta'))
# # OUTPUT: <class 'dict'>

# ==================================

# int_list = [-2, 4, 1, 6, -3]
# y = [x for x in int_list if x > 0]
# print(x for x in int_list if x > 0)  #OUTPUT: <generator object <genexpr> at....>
# print(y)    #OUTPUT: [4,1,6]

# ==================================

# x = [7, 'D', 'E', 8, 9, 'F']
# strings = [x for x in x if type(x) == str]
# print(strings)

# ==================================

# x = [2, 4, 1, 5]
# squares = { i: i ** 2 for i in x}
# print(squares)
# {1: 1, 2: 4, 4: 16, 5: 25}

# ==================================

# x = [8, 'M', 'N', 3, 1, 'A']
# integers = [j for j in x if type(j) == int ]
# print(integers)

# ==================================

# x = [1, 2, 3, 4, 5]
# print("First  (", x[0], ") item of list (x=[1, 2, 3, 4, 5], length = ", len(x) )
# print("Second (", x[1], ") item of list (x=[1, 2, 3, 4, 5], length = ", len(x) )
# print("Third  (", x[2], ") item of list (x=[1, 2, 3, 4, 5], length = ", len(x) )
# print("Fourth (", x[3], ") item of list (x=[1, 2, 3, 4, 5], length = ", len(x) )
# print("Fifth  (", x[4], ") item of list (x=[1, 2, 3, 4, 5], length = ", len(x) )
# print("Sixth >>> OUTPUT: list index out of range, length = ", len(x) ) 
# print("x[-1] ", x[-1], " item of list (x=[1, 2, 3, 4, 5], length = ", len(x) )
# print("x[-2] ", x[-2], " item of list (x=[1, 2, 3, 4, 5], length = ", len(x) )
# print("x[-3] ", x[-3], " item of list (x=[1, 2, 3, 4, 5], length = ", len(x) )
# print("x[-4] ", x[-4], " item of list (x=[1, 2, 3, 4, 5], length = ", len(x) )
# print("x[-5] ", x[-5], " item of list (x=[1, 2, 3, 4, 5], length = ", len(x) )
# print("x[-6] >>> OUTPUT: list index out of range, length = ", len(x) ) 

# ==================================

# pip 19.2.2 from c:\xxx\xxx\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)
# class NewClass:
#     num = 0
#     def __init__(self, num):
#         self.num = num
#     def __str__(self):
#         # return str(num) 
#         # is NOT CORRECT because NameError: name 'num' is not defined
#         return str(self.num)

# nc = NewClass(3)
# str(nc)
# print("str(nc): ", str(nc))

# ==================================

# class Answers:
#     def __init__(self, girl_ans, boy_ans):
#         self.girl_ans = girl_ans
#         self.boy_ans = boy_ans
    
#     def breakup(self):
#         if self.girl_ans == "yes" and self.boy_ans == 'yes':
#             return("I love you, yes!!!")
#         else:
#             return("Break up!!!")
    
# print(Answers("no", "yes").breakup())

# ==================================

# import pandas as pd
# p = ["SF", "PG", "PF"]
# q= ["X", "Y", "Z"]
# d = {'player': q, 'position': p}
# df = pd.DataFrame(data = d)
# print(df)

# ==================================

# import pandas as pd
# from numpy import max
# l1 = ['07/06/2019', '07/08/2019', '07/10/2019']
# l1_time = pd.to_datetime(l1)
# print(max(l1_time))

# ==================================

# import numpy as np
# x = np.array([14, 21, 24, 24])
# y = np.array([12, 6, 23, 29])
# z = np.array([x, y])
# print(z.shape)

# ==================================

# import numpy as np
# y = np.array([[4, 5, 6],
#               [11, 12, 13]])
# print(np.transpose(y))
# # OUTPUT
# # # [[ 4 11]
# # #  [ 5 12]
# # #  [ 6 13]]

# ==================================

# import pandas as pd
# planets = { 'planet': ['earth','mars'], 'dist_from_sun': ['1', '1.52'] } 
# planets_df = pd.DataFrame(planets)
# print(planets_df)
# # # OUTPUT
# # #    planet   dist_from_sun
# # # 0   earth               1
# # # 1    mars            1.52

# ==================================

# scarlet_speedster = iter('Barry Allen')
# print(*scarlet_speedster)   
# # # prints the whole string stored in the iter-object at once, 
# # there is the next functioni called a StopIteration-error is returned 
# # when the preceding call on scarlet_speedster is prefixed with an asterix
# print(next(scarlet_speedster))


# ==================================

# import numpy as np
# m = np.array([2, 4, 6])
# n = np.array([2, True, False])
# print(m+n)      # OUTPUT: [4 5 6]
# # print(m**n)     # OUTPUT: [4 4 1]
# # print(m*n)      # OUTPUT: [4 4 0]

# ==================================

# teams = [['barry', 'cisco', 'caitlin'], ['oliver', 'john', 'felicity']]
# print([member[-1] for member in teams])

# ==================================

# s1 = set([90, 4, 92, 91])
# s2 = set([89, 7, 34, 84])
# res = s1.difference(s2)       # OUTPUT: {90, 91, 4, 92} 
# res = s1.intersection(s2)     # OUTPUT: set()
# print(res)

# ==================================

