# The np.random module and Bernoulli trials
# You can think of a Bernoulli trial as a flip of a possibly biased coin.
# Specifically, each coin flip has a
# probability 'p' of landing on heads(success) and
# probability '1−p' of landing tails(failure).
# In this exercise, you will write a function to perform 'n' Bernoulli trials,
# [ perform_bernoulli_trials(n, p) ],
# which returns the number of successes out of n Bernoulli trials,
# each of which has a probability 'p' of success.
# To perform each Bernoulli trial, use the np.random.random()-function,
# which returns a random number between zero and one.

import numpy as np


def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with
        probability p (success) and return number of successes"""
    # Initialize number of successes: n_success
    # Start with 0 items in the array, it's going to be filled-up
    n_success = np.empty(0)

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()

        # If less than p, it's a success so add one to n_success
        if random_number < p:
            n_success += 1

    return n_success

# ============================================================================

# How many defaults might we expect?
# A bank made 100 mortgage loans (Een bank heeft 100 hypotheekleningen verstrekt).
# It is possible that anywhere between 0 and 100 of these loans
# will be defaulted upon (in gebreke blijven de lening in te lossen).
# You would like to know, the probability of getting a given number of 'defaults',
# given that the probability of a 'default' is p = 0.05.
# To investigate this, you will do a simulation. You will perform 100 Bernoulli trials
# using the perform_bernoulli_trials()-function and record how many 'defaults' we get.
# Here, a function-output 'success' is a 'default'.
# Remember that the word 'success' just means that the Bernoulli trial evaluates to 'True',
# i.e., did the loan recipient 'default').
# Do this for 100 Bernoulli trials.
# Each Bernoulli trial a 1000 times and plot a histogram describing the
# probability 'p' of the number of 'defaults'.

# Seed random number generator
np.random.seed(42)

# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000)

# Compute the number of defaults
for i in range(1000):
    
    n_defaults[i] = perform_bernoulli_trials(100, 0.05)

# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults, normed=True)
_ = plt.xlabel('Number of \'defaults\' out of 100 loans')
_ = plt.ylabel('probability \'p\' ')

# Show the plot
plt.show()
