import pandas as pd

wlist = [
            ['Python', 'creativity', 'universe'], 
            ['interview', 'study', 'job', 'university', 'lecture'], 
            ['task', 'objective', 'aim', 'subject', 'programming', 'test', 'research']
        ]

# Create a list of tuples with words and their lengths
word_lengths = [
     (item, len(item)) for items in wlist for item in items
]

print("word_lengths: ", word_lengths)
print("#----------------------------")
# OUTPUT (list of tuples, this is NOT a dictionary): 
# [('Python', 6), ('creativity', 10), ('universe', 8), ('interview', 9), ('study', 5), ('job', 3), ('university', 10), ('lecture', 7), ('task', 4), ('objective', 9), ('aim', 3), ('subject', 7), ('programming', 11), ('test', 4), ('research', 8)]

# Unwrap the word_lengths
words, lengths = zip(*word_lengths)

print("lengths: ", lengths)
print("words: ", words)
print("#----------------------------")
# Create a zip object
col_names = ['word', 'length']
result = zip(col_names, [words, lengths])

print("Zip Object: ", result)
print("#----------------------------")

# Convert the result to a dictionary
dict_result = dict(result)
print("Dictionary of result: ", dict_result)

# Convert the result to a dictionary and build a DataFrame
data_frame = pd.DataFrame(dict_result)
print("Dataframe: ", data_frame)
