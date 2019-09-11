# import classes
from kwhj_python_pck.kwhj_python import Document

# import package methods
from kwhj_python_pck.kwhj_python.utils import we_need_to_talk
from kwhj_python_pck.kwhj_python.utils import sum_counters
from kwhj_python_pck.kwhj_python.utils import plot_counter

# import external iterables (lists, tuples, dicts)
from repository_lists import word_counts


# utils.py - methods
# -------------------------------------------------------------------
# # Decide to start seeing other people
we_need_to_talk(break_up=False)


# Sum word_counts using sum_counters from text_analyzer
word_count_totals = sum_counters(word_counts)
print("word_count_totals: ", word_count_totals)

plot_counter(word_count_totals, 10)

# ===================================================================


# document.py 
# -------------------------------------------------------------------
doc = Document('test doc')
print(doc.tokens)

# ===================================================================


# social_media.py 
# -------------------------------------------------------------------
# Create a SocialMedia instance with datacamp_tweets
# dc_tweets = kwhj_python_pck.SocialMedia(text=datacamp_tweets)

# ===================================================================

