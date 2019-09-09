# nums = [(2 * nums) for nums in range(1, 6)]
# print(nums)

print("-------------------------")

# list comprehension
# an iterable object (e.g. list, tuple, set) : 
#  an operation on an element  |  an iterable object (e.g. list, tuple, set)  |  (optional) conditions
#   [        (2 * num)                         for num in range(1, 6)                    .......    ]

my_range = []
for i in range(1, 11):
    my_range.append(i)
print("range(1,11): ", my_range)
# an iterable object (e.g. list, tuple, set) : 
print("iterable object: ", my_range)
#  an operation on an element  |  an iterable object (e.g. list, tuple, set)  |  (optional) conditions
#   [        (2 * num)                      for num in range(1, 6)                     .......      ]
nums_new = [ (2 * num)                      for num in range(1, 11)                if num % 2 == 0  ]
print(nums_new)

print("-------------------------")

text = 'list COMPREHENSION is A way TO create LISTS'
# Create a list that contains the length of each lowercased word.
# list , is , way , create → [4, 2, 3, 6]
output =   [ len(word)                      for word in text.split()               if word.islower() ]
print("output: ", output)

print("-------------------------")

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
pairs = [(i, j) for i in numbers for j in letters]
print("[(i, j) for i in numbers for j in letters] : ")
print(pairs)
# pairs = []
# for i in numbers:
#   for j in letters:
#       pairs.append((i, j))
# change inner and outer loop
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print("[(i, j) for i in letters for j in numbers] : ")
pairs = [(i, j) for i in letters for j in numbers]
print("tuples: ", pairs)
# pairs = []
# for i in letters:
#   for j in numbers:
#       pairs.append((i, j))

print("-------------------------")

print("Adding square brackets")
print("[[(i, j) for i in numbers] for j in letters] : ")
pairs = [[(i, j) for i in numbers] for j in letters]
print("lists of tuples: ", pairs)
print("[[(i, j) for i in letters] for j in numbers] : ")
pairs = [[(i, j) for i in letters] for j in numbers]
print("lists of tuples: ", pairs)

print("-------------------------")

pairs = []
for j in letters:
    temp = []
    for i in numbers:
        temp.append((j, i))
    pairs.append(temp)
print("lists of tuples: ", pairs)

print("-------------------------")
