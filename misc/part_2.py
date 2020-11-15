# 01 Lists
i = 1
names =['Jan','Kees','Koen','Piet','Koen']
print('[',i,'] > ', len(names))                     # 5

# =========================================================
i += 1
empty_list = []
print('[',i,'] > ', len(empty_list))                # 0

# =========================================================
i += 1
# 02 List Elements
print('[',i,'] > ', names[3])                       # 'Piet'
i += 1
print('[',i,'] > ', names[4])                       # 'Koen'
i += 1
print('[',i,'] > ', names[-2])                      # 'Piet'
i += 1
print('[',i,'] > ', names[-3])                      # 'Koen'
i += 1
print('[',i,'] > ', names.count('Koen'))            # 2
i += 1
print('[',i,'] > ', names.count('Jan'))             # 1
i += 1
print('[',i,'] > ', names.count('Tom'))             # 0

# print(names.index('Tom'))
# Traceback (most recent call last);
#   File "<stdin>", line 1, in <module>
# ValueError: 'Tom' is not in list

i += 1
print('[X',i,'] > ', names.index('Koen'))           # 2
# An element which exists more than once in a list, the function 'index' returns only the first position

# It is posible to search from a specific position
i += 1
print('[',i,'] > ', names.index('Koen', 3))         # 4


# 03 Changing a list
i += 1
print('[',i,'] > ', names)                          # ['Jan','Kees','Koen','Piet','Koen']

i += 1
print('[',i,'] > ', names[3])                       # 'Piet'

i += 1
print('[',i,'] > ', names)                          # ['Jan', 'Kees', 'Koen', 'Piet', 'Koen']

names.reverse()
i += 1
print('[',i,'] > ', names)                          # ['Koen', 'Piet', 'Koen', 'Kees', 'Jan']

names.sort()
i += 1
print('[',i,'] > ', names)                          # ['Jan', 'Kees', 'Koen', 'Koen', 'Piet']

names.append('Koos')
i += 1
print('[',i,'] > ', names)                          # ['Jan', 'Kees', 'Koen', 'Koen', 'Piet', 'Koos']

names.insert(0,'Victor')
i += 1
print('[',i,'] > ', names)                          # ['Victor', 'Jan', 'Kees', 'Koen', 'Koen', 'Piet', 'Koos']

names.remove('Koen')
i += 1
print('[',i,'] > ', names)                          # ['Victor', 'Jan', 'Kees', 'Koen', 'Piet', 'Koos']

names.remove('Koen')                                # ['Victor', 'Jan', 'Kees', 'Piet', 'Koos']
i += 1
print('[x',i,'] > ', names)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# ValueError: list.remove(x): x not in list

#  remove an item from the list from a specific spot in the list
names = ['Victor','Jan','Karel','Kees','Piet','Koos']
i += 1
print('[',i,'] > ', names.pop(5))                   # 'Koos'
# removes the sixth item (indexing items on a list start with '0')
# .pop(x)-method remove the desired item and it returns it as answer


# 04 Cutting a list
names = ['Victor','Jan','Karel','Kees','Koen','Koen','Piet','Koos']
i += 1
print('[',i,'] > ', names[1:])                      # ['Jan','Karel','Kees','Koen','Koen','Piet','Koos']
i += 1
print('[',i,'] > ', names[:4])                      # ['Victor', 'Jan', 'Karel', 'Kees']
i += 1
print('[',i,'] > ', names[1:3])                     # ['Jan', 'Karel']


# 05 Dictionaries
names = {'Victor':1,'Jan':2,'Karel':3,'Kees':4,'Koen':5,'Piet':6,'Koos':7}
i += 1
print('[',i,'] > ', names['Koen'])                  # 5
# print(names['Tom'])                               # KeyError: 'Tom'
i += 1
print('[',i,'] > ', len(names))                     # 7
