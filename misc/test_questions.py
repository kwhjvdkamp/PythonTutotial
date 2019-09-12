import numpy as np
# OUTPUT needs to be [3.  4.  1.  0.  5.2]

# x = np.array([3, 4, True, False, 5.2])
# print(x)

#============================================

# # y = np.array([3, 4, True, False, "5.2"])
# # print(y)

#============================================

# # z = np.array([3, 4, False, True, "5.2"])
# # print(z)

#============================================

# z = np.array([[5, 9, 8], [9, 0, 6]])
# print(z[0:,1:])

#============================================

# print(["A", "B" * 2, "C"])
# # print([2. 4. 6.0 + 2])
# # print([,2,5,7])

#============================================

# p = ['j', 'x', 'n', 'k', 'e', 'x']
# # cut(p[3:5])
# # delete(p[3:5])
# del(p[3:5])
# # rm(p[3:5])
# # replace(p[3:5])
# print(p)

#============================================

# Remove the correct number from the list x
# x = [9, 2, 8, 4, 5]
# # x.delete(9)
# # x.rm(9)
# x.remove(9)
# print(x)

#============================================

# import numpy as np
# store = np.array([0, 9, 0, 1])
# cost  = np.array([82, 82, 73, 73])
# np_cols = np.common_type((store, cost))
# print(np_cols)

# # ========================================================

# superhero_list = ['thor', 'hulk']
# def to_upper(x):
#     for i in x:
#         yield i.upper()

# print(to_upper(superhero_list))
# generator_object = to_upper(superhero_list)
# print(next(generator_object))
# print(next(generator_object))
# print(next(generator_object))
# # OUTPUT:   <generator object to_upper at 0x0000023298AA9B48>
# #   ..      THOR
# #   ..      HULK
# #   ..      Traceback (most recent call last):
# #   ..      File "c:/HomeProjects/PythonTutotial/test_questions.py", line 53, in <module>
# #   ..      print(next(generator_object))
# #   ..      StopIteration

# # ========================================================

# names = ['Thor Odinson', 'Steve Rogers']
# avengers = list(enumerate(names, start = 2))
# print(avengers)

#============================================

# # x = [i for i in range(5)]
# x = (i for i in range(5))
# print(next(x))

#============================================

# def obtain_words(string):
#     # Replace non-alphabetic characters with spaces
#     print(string)
#     return "".join(char if string(char).isalpha() else " " for char in string).split()


# print(obtain_words("Remove words shorter than 3 characters"))

