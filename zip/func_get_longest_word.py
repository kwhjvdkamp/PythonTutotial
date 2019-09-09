wlist = [
            ['Python', 'creativity', 'universe'], 
            ['interview', 'study', 'job', 'university', 'lecture'], 
            ['task', 'objective', 'aim', 'subject', 'programming', 'test', 'research']
        ]

print({}, wlist)

# Define a function searching for the longest word
def get_longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# Create lists with the lengths and longest words
lengths = [len(item) for item in wlist]
words = [get_longest_word(item) for item in wlist]

# Combine the resulting data into one iterable object
zipped_iterables = zip(wlist, lengths, words)
for item in zipped_iterables:
    print(item)