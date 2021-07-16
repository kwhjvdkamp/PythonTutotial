import random

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



def simulate_dice_throws():
    '''
    This function behaves like a normal function, but whenever it needs
    to generate a value, it does so with the 'yield' keyword instead of 'return'.
    '''
    total, out = 0, dict([(i, [0, 0]) for i in range(1, 7)])
    while True:
        # Simulate a single toss to get a new number
        num = random.randint(1, 6)
        total += 1
        # Update the number and the ratio of realizations
        out[num][0] = out[num][0] + 1
        out[num][1] = round(out[num][0]/total, 2)
        yield out

# Create the generator and simulate 1000 tosses
dice_simulator = simulate_dice_throws()
for i in range(1, 1001):
    print(str(i) + ': ' + str(next(dice_simulator)))