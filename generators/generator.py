# Rewrite func1() as a generator comprehension
def func1(n):
  for i in range(0, n):
    yield i**2

def func2(n):
  for i in range(0, n):
     if i%2 == 0:
       yield 2*i

def func3(n, m):
  for i in func1(n):
    for j in func2(m):
      yield ((i, j), i + j)

print("#-------------------------")

gen_1 = (i**2 for i in range(0, 10))
for item in zip(gen_1, func1(10)):
    print(item)

print("#-------------------------")

# Rewrite func2() as a generator comprehension
gen_2 = (2*i for i in range(0, 20) if i%2 == 0)
for item in zip(gen_2, func2(20)):
    print(item)

print("#-------------------------")

# Rewrite func3() as a generator comprehension
gen_3 = (((i, j), i + j) for i in func1(8) for j in func2(10))
for item in zip(gen_3, func3(8, 10)):
    print(item)