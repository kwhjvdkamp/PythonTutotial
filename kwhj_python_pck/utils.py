# Import needed functionality
from collections import Counter
import matplotlib.pyplot as plt


# Private function
def plot_counter_most_common(top_items):
    top_items_dict = dict(top_items)
    plt.figure()
    plt.bar(range(len(top_items_dict)), list(top_items_dict.values()), align='center')
    plt.xticks(range(len(top_items_dict)), list(top_items_dict.keys()), rotation='vertical')
    plt.tight_layout()
    plt.show()


def we_need_to_talk(break_up=False):
    """Helper for communicating with significant other"""
    if break_up:
        print("It's not you, it's me...")
    else:
        print('I <3 U!')


def plot_counter(counter, n_most_common=5):

    # Subset the n_most_common items from the input counter
    top_items = counter.most_common(n_most_common)
    # Plot `top_items` ( 'plot_counter_most_common' not implemented)
    plot_counter_most_common(top_items)


def sum_counters(counters):
    # Sum the inputted counters
    return sum(counters, Counter())