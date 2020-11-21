# 01 Tweak the execution of print
i = 1

numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

# Within the 'while' construct, it is tested if the entered number is 'not in' the given range, if so the question to enter a number is repeated
number = 0
while number -1 not in range(len(numbers)) :
    number = int(input("Enter a whole number from 1 till 9 in : "))
print('[',i,'] > ', number, " is equal ", numbers[number])