# Import needed functionality
from collections import Counter


def we_need_to_talk(break_up=False):
    """Helper for communicating with significant other"""
    if break_up:
        print("It's not you, it's me...")
    else:
        print('I <3 U!')


def plot_counter(counter, n_most_common=5):

    # Subset the n_most_common items from the input counter
    top_items = counter.most_common(n_most_common)
    # Plot `top_items`
    # NOTE 'plot_counter_most_common' not implemented
    # plot_counter_most_common(top_items)


def sum_counters(counters):
    # Sum the inputted counters
    return sum(counters, Counter())