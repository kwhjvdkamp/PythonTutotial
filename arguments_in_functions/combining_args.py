# Define the function with an arbitrary number of arguments
def sort_types(*args):
    nums, strings = [], []
    for arg in args:
        # Check if 'arg' is a number, add it to 'nums'-list
        if isinstance(arg, (int, float)):
            nums.append(arg)

        # Check if 'arg' is a string, add it to 'strings'-list
        elif isinstance(arg, str):
            strings.append(arg)

    return (nums, strings)


# Define the arguments passed to the function
def sort_all_types(*args, **kwargs):
    print(" *args   (1st): ", args)
    print("**kwargs (2nd): ", kwargs.items())

    # Find all numbers and strings in the 1st argument
    nums1, strings1 = sort_types(*args)

    # Find all numbers and strings in the 2nd argument
    nums2, strings2 = sort_types(*kwargs.values())

    return (nums1 + nums2, strings1 + strings2)

res = sort_all_types( 1, 2.0, 'dog', 5.1, num1 = 0.0, num2 = 5, str1 = 'cat' )
print(res)