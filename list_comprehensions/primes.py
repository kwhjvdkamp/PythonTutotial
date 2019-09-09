import math

cands = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49]
print("Candidates: ", cands)
print("---------------------------------------")
def is_prime(n):
    # Define the initial check
    if n < 2:
        print(n, "is not a prime!")
        return False
    
    # Define the loop checking if a number is not prime
    # to_int_converted_math_sqrt_of_n = int(math.sqrt(n))
    # print("int(math.sqrt(", n, ")): ", to_int_converted_math_sqrt_of_n)
    to_int_converted_math_sqrt_of_n_plus_1 = int(math.sqrt(n)) + 1
    print("int(math.sqrt(", n, ")) + 1 = ", to_int_converted_math_sqrt_of_n_plus_1)

    for i in range(2, to_int_converted_math_sqrt_of_n_plus_1):
        print(i)
        if n % i == 0:
            return False
    return True
    
# Filter prime numbers into the new list
primes = [num for num in cands if is_prime(num)]

print("primes = " + str(primes))