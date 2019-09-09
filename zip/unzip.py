# Define a function searching for the longest word
def get_longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


wlist = [
    ['Python', 'creativity', 'universe'], 
    ['interview', 'study', 'job', 'university', 'lecture'], 
    ['task', 'objective', 'aim', 'subject', 'programming', 'test', 'research']
]

print("List of lists: ", wlist)
print("#----------------------------")
# Create a list of tuples with lengths and longest words
result = [
    (len(item), get_longest_word(item)) for item in wlist
]
print("Tuple: len(item) and get_longest_word(item)) from wlist: ", result)
print("#----------------------------")

# Unzip the result    
lengths, words = zip(*result)
print("lengths: ", lengths)
print("words: ", words)
print("#----------------------------")
for item in zip(wlist, lengths, words):
    print(item)