import random

# 'yield' is used in Python generators 
# A generator function is defined like a normal function, 
# but whenever it needs to generate a value, it does so with 
# the 'yield' keyword rather than return. 
# If the body of a def contains yield, the function automatically 
# becomes a generator function
def simulate_dice_throws():
    total, out = 0, dict([(i, [0, 0]) for i in range(1, 7)])
    while True:
        # Simulate a single toss to get a new number
        num = random.randint(1, 6)
        total += 1
        # Update the number and the ratio of realizations
        out[num][0] = out[num][0] + 1
        out[num][1] = round(out[num][0]/total, 2)
        # Yield the updated dictionary
        # 'return' sends a specified value back to its caller, 
        # whereas 'yield' can produce a sequence of values. 
        # Use 'yield' when it is needed to iterate over a sequence 
        # but it is not needed to store the entire sequence in memory
        yield out

# Create the generator and simulate 1000 tosses
dice_simulator = simulate_dice_throws()
for i in range(1, 1001):
    print(str(i) + ': ' + str(next(dice_simulator)))