def shift_string(string, shift):
    len_string = len(string)
    print("Length of ", string, "=" , len(string))
    # Define a for loop with the yield statement
    for idx in range(0, len_string):
        yield string[(idx - shift) % len_string]
       
# Create a generator
string = 'DataCamp'
shift = 5
gen = shift_string(string, shift)

# Create a new string using the generator and print it out
string_shifted = gen
print(string_shifted)