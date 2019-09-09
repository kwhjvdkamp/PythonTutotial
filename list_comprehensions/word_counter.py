spam = "Dear User, Our Administration Team needs to inform you that you are reaching the storage limit of your Mailbox account. You have to verify your account within the next 24 hours. Otherwise, it will not be possible to use the service. Please, click on the link below to verify your account and continue using our service. Your Administration Team."

# print(spam)

print("----------------------------")

# Convert the text to lower case and create a word list
# words = create_word_list(spam.lower())
spam = spam.replace(',', '')
spam = spam.replace('.', '')
print("----------------------------")
print(spam)
print("----------------------------")

words = [ word.lower() for word in spam.split() ]

# Create a set storing only unique words
word_set = set(words)

# Create a dictionary that counts each word in the list
tuples = [(word, words.count(word)) for word in word_set]
word_counter = dict(tuples)
print(word_counter)

print("----------------------------")

# Printing words that appear more than once
for (key, value) in word_counter.items():
    if value > 1:
        print("{}: {}".format(key, value))

account: 3
to: 4
you: 3
our: 2
team: 2
your: 4
administration: 2
the: 4
verify: 2
service: 2