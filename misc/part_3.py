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

# 03 Testing: if
i += 1
numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
number = int(input("Enter a natural number between 1 and 9: "))
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
