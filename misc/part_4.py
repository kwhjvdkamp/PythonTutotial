# 01 Tweak the execution of print
i = 1

numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

# Within the 'while' construct, it is tested if the entered number is 'not in' the given range, if so the question to enter a number is repeated
number = 0
while number -1 not in range(len(numbers)) :
    number = int(input("Enter a whole number from 1 till 9 in: "))
print('[',i,'] > ', number, " is equal ", numbers[number])

i += 1
numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
print('[',i,'] > ', number, numbers[number], sep = ': ', end = '\n1 new line one\n2 new line two\n3 new line three\n\n')

# 02 Placeholders
i += 1
text = 'You hit key {}'.format(input("Hit a random key: "))
print('[',i,'] > ', text)

i += 1
text = 'You hit key {0}, {1}!'.format(input("Hit a random key: "), 'Hurray')
print('[',i,'] > ', text)

i += 1
text = '{min} <= {number} <= {max}'.format(min = 1, max = 10, number = 5)
print('[',i,'] > ', text)

# 03 Iterate thru a list ([1, 'two', '3', 4, 'five'])with 'for'
i += 1
n = 0
names = ['Jan','Kees','Koen','Piet','Koen']
print('[',i,'] > The enumerate object yields pairs containing a count \n        (from start, which defaults to zero)\n        and a value yielded by the iterable argument.\n        \'Enumerate(...)\' is useful for obtaining an indexed list:')
for index, name in enumerate(names) :
    print('[',i,'] > ', '{0} {1}'.format(index, name))

# 04 Iterate thru a dictionary ({1:'one', 2:'two', ...}) with 'for'
