## 01 Lists
# >>> names =['Jan','Kees','Koen','Piet','Koen']
# >>> len(names)
# 5

# >># >>>empty_list = []
# >>> len(empty_list)
# 0

## 02 List Elements
# >>> names[3]
# 'Koen'

# >>> names[4]
# 'Piet'

# >>> names[-2]
# 'Piet'

# >>> names['-3']
# 'Kees'

# >>> names.count('Koen')
# 2

# >>> names.count('Jan')
# 1

# >>> names.count('Tom')
# 0

# >>> names.index('Tom')
# >>>Traceback (most recent call last);
# >>>  File "<stdin>", line 1, in <module>
# >>>ValueError: 'Tom' is not in list

# >>> names.index('Koen')
# 2
# Voor een element more than once in de lijst voorkomt,
# geeft de function 'index' alleen de eerste position terug

# Possible to search from a certain position
# >>> names.index('Koen', 3)
# 4


## 03 Changing a list
# >>> names
# ['Jan','Kees','Koen','Piet','Koen']

# >>> names[3] = 'Karel'
# ['Jan','Kees','Koen','Karel','Piet','Koen']

# >>> names.reverse()
# >>> names
# [''Koen','Piet','Karel','Koen','Kees','Jan']
