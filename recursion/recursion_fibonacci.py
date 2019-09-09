# Calculate the number of function calls
# Let's consider a classic example of recursion – 
# Fibonacci sequence, 
# This sequence, represented by non-negative integers starting 
# from 0 with each element F(n) equals the sum of the preceding two: 
# 0  1  2  3  4  5  6   7   8   9  10  11   12   13   14   15   16    17    18    19    20
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597  2584, 4181  6765
# You are given a function that returns a tuple with the 
# a) n-th element of the sequence, and 
# b) the amount of calls to fib() used:


# How many calls to fib() are needed to calculate the 15th and 20th elements of the sequence?

def fib(n):

  if n < 2:
    return (n, 1)

  fib1 = fib(n-1)
  fib2 = fib(n-2)

  return (fib1[0] + fib2[0], fib1[1] + fib2[1] + 1)


for i in range(1, 21):
    print("Fibonacci element: ", i, fib(i))
