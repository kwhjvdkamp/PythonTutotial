# def my_zip(*args):
    
#     # Retrieve Iterable lengths and find the minimal length
#     lengths = list(map(len, args))
#     min_length = min(lengths)

#     tuple_list = []
#     for i in range(0, min_length):
#         # Append new items to the 'tuple_list'
#         tuple_list.append(tuple(map(lambda x: x[i], args)))

#     return tuple_list

# result = my_zip([1, 2, 3], ['a', 'b', 'c', 'd'], 'DataCamp')
# print(result)


result_dict = {'DataCamp', tuple(['a', 'b', 'c', 'd'])}
print(result_dict)

