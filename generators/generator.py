#	Yield							|	Return
#	=========================================================================
# 1	Yield is generally used to 		|	Return is generally used for ending
#	convert a regular Python 		|	the execution and “returns”
#	function into a generator. 		|	result to the caller statement.
#	-------------------------------------------------------------------------
# 2	It replace the return of a 		|	It exits a function and handing back
#	function to suspend its 		|	a value to its caller.
#	execution without destroying	|
#	local variables.				|
#	-------------------------------------------------------------------------
# 3	It is used when the generator	|	It is used when a function.
#	returns an intermediate result	|	is ready to send a value.
#	to the caller.
#	-------------------------------------------------------------------------
# 4	Code written after yield 		|	Code written after return statement
# 	statement executes in next 		|	won't be executed.
#	function call.					|
#	-------------------------------------------------------------------------
# 5	It can run multiple times.		|	It only runs single time.
# 6	'yield' functions executes 		|	Every function calls run the
#	from the last state from where 	|	'return' function from the start.
#	the function get paused.		|
#	-------------------------------------------------------------------------

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