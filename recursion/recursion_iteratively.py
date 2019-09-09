# Calculate an average value
# Calculate an average value iteratively:

# def average(nums):
#     result = 0
#     for num in nums:
#         result += num
#     return result/len(nums)

# Could you provide a recursive solution? 
# A formula for updating an average value given a new input might be handy:

# @ = ( xi + ((n−1) * @ ) ) / n

# Here, @ stands for an average value, 
# xi is a new supplied value which is used to update the average, and 
# n corresponds to the recursive call number (excluding the initial call to the function).


# Calculate an average value of the sequence of numbers
def average(nums):
    # Base case
    if len(nums) == 1:  
        return nums[0]
    
    # Recursive call
    n = len(nums)
    return ( nums[0] + (n - 1) * average( nums[1:] ) ) / n  


# Testing the function
print(average([1, 2, 3, 4, 5]))