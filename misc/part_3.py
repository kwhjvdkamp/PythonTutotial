# 01 Thonny

# 02 Bool
i = 1
names = ['Jan','Kees','Koen','Piet','Koen']
'Koen' in names
print(names)
print('[',i,'] > \'Koen\' in names', 'Koen' in names)                   # True

i += 1
names[2] == 'Koen'
print('[',i,'] > \'Koen\' == names[2] <=>', names[2] == 'Koen')         # True

i += 1
print('[',i,'] > 3.1.is_integer() <=>', 3.1.is_integer())               # False5

i += 1
print('[',i,'] > 3.0.is_integer() <=>', 3.0.is_integer())               # False

# 03/04/05 Testing: if
i += 1
numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
number = int(input("Enter a natural number between 1 and 9\nAny number given outside this range cause this program to stop: "))
if number < 1 :
    print('[',i,'] > number is smaller than 1')
elif number > 9 :
    print('[',i,'] > number is greater than 9')
else :
    print('[',i,'] > numbers:', numbers[number])

i += 1
if number - 1 in range(len(numbers)) :
    print(numbers[number])
else :
    print("Number is not within the range of 1 to 9")

i += 1
print('[',i,'] > Object [\'numbers:\']: ', numbers)

i += 1
keys_view = numbers.keys()
key_iterator = iter(keys_view)
first_key = next(key_iterator)
print('[',i,'] > All keys of object [\'numbers:\']: ', keys_view)
print('[',i,'] > First value of object [\'numbers:\']: ', first_key)

i += 1
values_view = numbers.values()
value_iterator = iter(values_view)
first_value = next(value_iterator)  # first time
first_value = next(value_iterator)  # second time
print('[',i,'] > All values of object [\'numbers:\']: ', values_view)
print('[',i,'] > First value of object [\'numbers:\'\n>1> through iteration of list values_view ( iter(values_view)\n>2> using the first next()-method on the iterator-object (value_iterator) )]: ', first_value)

# 06
i += 1
numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
number = 0
while number -1 not in range(len(numbers)) :
    number = int(input("Enter a whole number from 1 till 9 in : "))
# Within the while construct it is tested the entered number is 'not in' the given range, if so the question to enter a number is repeated
print('[',i,'] > number entered: ', number)


