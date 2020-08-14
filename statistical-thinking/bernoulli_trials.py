# Test this function to perform 'n' Bernoulli trials,
# with function: perform_bernoulli_trials(n, p),
# which returns the number of successes out of n Bernoulli trials,
# each of which has a probability 'p' of success.

# Think of a Bernoulli trial as a flip of a possibly biased coin.
# Specifically, each coin flip has a
# probability 'p' of landing on heads (success)
# probability '1−p' of landing tails (failure)

import array
import numpy as np
import matplotlib.pyplot as plt

def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with
        probability p (success) and return number of successes"""
    # Initialize number of successes: n_success
    # Start with 0 items in the array, it's going to be filled-up
    # One call to the function will do a loop 100 times
    # Note: it's a 'numpy'-array, so this function returns a 'numpy'-array

    n_success = []
    # print('Type of \'n_success\': ', type(n_success))

    # print('Before the has started, list is', n_success)

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one
        random_number = np.random.random()

        # If less than 'p', store a 'True' as 1 into 'n_success'-list
        if random_number < p :
            # print('Loop', i + 1, 'of', n, '| p:',
            #       p, '| Randomly chosen number:',  round(random_number, 5))
            n_success.append(1)

    # print('After the for-loop (\'for i in range(n)\'): ', n_success)

    return n_success

# ============================================================================

# Seed random number generator
np.random.seed(100)

# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000, dtype = np.int)

# print(perform_bernoulli_trials(100, 0.05))

# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = np.int(len(perform_bernoulli_trials(100, 0.05)))

# print('Defaults':', n_defaults)

# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults, density=True, bins=10)
_ = plt.xlabel('Number of \'defaults\' (\'in gebreke zijnde\' ) out of 100 provided loans')
_ = plt.ylabel('Probability')

# Show the plot
plt.show()
