# == [ BERNOULLI FUNCTION START ] ===============================================
import array
import numpy as np
import matplotlib.pyplot as plt

def perform_bernoulli_trials(n, p):
    """
        Performing 'n' Bernoulli trials
        Determination of the probability p (success)
        returning the number of success finding a 'default'
    """
    n_success = []
    print('Type of \'n_success\': ', type(n_success))

    print('Before the has started, list is', n_success)

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
# == [ BERNOULLI FUNCTION  END  ] ===============================================

# == [ BERNOULLI   TEST   START ] ===============================================
# Initialize number of successes:
# n_success
# Start with 0 items in an array, which is going to be filled-up
# One call to the function will do a loop 100 times

# Note: it's a 'numpy'-array, so this function returns a 'numpy'-array

## Test returns the number of successes out of 'n' Bernoulli trials,
# each of which has a probability 'p' of success

# Probability
# 'p'
# The 'mussel' does NOT open during cooking,
# should be determined as 'not eatable' (defaults) anymore
# '1−p' in contrast,
# should be determined as an 'eatable' one

# Hans is cooking 100 'mussels'
# It is possible that anywhere between 0 and 100 of the 'mussels'
# will be a 'default' one.
# 'Default' means; during cooking the mussel wil NOT open,
# actually meaning the mussel shouldn't be eaten

# Fishmonger has issued a 'probability' of a 'default' less than p = 0.05,
# meaning 5 out of 100 mussels might be 'defaults'

# Bert en Henk both did a simulation of 100 Bernoulli trials
# using the 'perform_bernoulli_trials()-function and
# record how many 'defaults' Hans wil get

# NOTE: The function output 'Success' means a 'default'

# Remember that the word 'Success' just means that the Bernoulli trial
# evaluates to 'True', meaning: Does the mussel be a 'default'?

# Seed random number generator
size_bernoulli_trials=1000
amount_of_mussels_during_cooking=100
fish_monger_probability=0.05
np.random.seed(amount_of_mussels_during_cooking)

# Initialize a list of n_defaults to catch the n_defaults into
n_defaults = np.empty(size_bernoulli_trials, dtype = np.int)

print(perform_bernoulli_trials( \
    amount_of_mussels_during_cooking, \
    fish_monger_probability \
))

# Compute the number of defaults
for i in range(size_bernoulli_trials):
    n_defaults[i] = \
        np.int(len( \
            perform_bernoulli_trials( \
                amount_of_mussels_during_cooking, \
                fish_monger_probability \
            ) \
        ))

# print('Number of \'not eatable mussels\' (defaults):', len(n_defaults))

# Plot the histogram with default number of bins; label your axes
_ = plt.figure(1, figsize=(8, 6))
_ = plt.clf()

n_bins = int(np.sqrt(amount_of_mussels_during_cooking))
bin_number = ' (bins=' + str((n_bins / 3)) + ')'
_ = plt.hist(n_defaults, density=True, bins=round(n_bins), color='red')
_ = plt.title('Bernoulli distribution of\nmussels \'defaults\' during cooking')
_ = plt.legend(('Defaulted mussels'), loc='upper right')
_ = plt.xlabel('Number of \'not eatable mussels\' (defaults) out of ' \
     + str(amount_of_mussels_during_cooking) \
     + ' mussels')
_ = plt.ylabel('Probability (p) on \'defaulted\' mussels')

# Show the plot
plt.show()
# == [ BERNOULLI   TEST    END  ] ===============================================