# 'yield' is used in Python generators 
# A generator function is defined like a normal function, 
# but whenever it needs to generate a value, it does so with 
# the 'yield' keyword rather than return. 
# If the body of a def contains yield, the function automatically 
# becomes a generator function
def shift_string(string, shift):
    len_string = len(string)
    print("Length of ", string, "=" , len(string))
    # Define a for-loop with 'yield' statement
    for idx in range(0, len_string):
        yield string[(idx - shift) % len_string]

# Create a generator
string = 'DataCamp'
# shift = 1                   # 'p'
# shift = 2                   # 'm'
# shift = 3                   # 'a'
# shift = 4                   # 'C'
# shift = 5                   # 'a'
# shift = 6                   # 't'
# shift = 7                   # 'a'
shift = 8                   # 'D'

because_i_contain_yield_i_am_a_generator = shift_string(string, shift)

# Create a new string using the generator and print it out
string_shifted = because_i_contain_yield_i_am_a_generator

print("1 Shifts", shift, "character(s) backwards", next(string_shifted))
print("2 Shifts", shift, "character(s) backwards", next(string_shifted))
print("3 Shifts", shift, "character(s) backwards", next(string_shifted))
print("4 Shifts", shift, "character(s) backwards", next(string_shifted))
print("5 Shifts", shift, "character(s) backwards", next(string_shifted))
print("6 Shifts", shift, "character(s) backwards", next(string_shifted))
print("7 Shifts", shift, "character(s) backwards", next(string_shifted))
print("8 Shifts", shift, "character(s) backwards", next(string_shifted))