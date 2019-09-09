text= 'StRing ObJeCts haVe mANy inTEResting pROPerTies'  # SPLITTED
# text= 'StRing-ObJeCts-haVe-mANy-inTEResting-pROPerTies'  # NOT SPLITTED
# text= 'StRing|ObJeCts-haVe-mANy|inTEResting-pROPerTies'   # NOT SPLITTED
# text= 'StRing|ObJeCts|haVe|mANy|inTEResting|pROPerTies'  # NOT SPLITTED
word_list = text.split()
print("BEFORE: ", word_list, "Type: ", type(word_list))

# Make every other word uppercased; otherwise - lowercased
for i in range(len(word_list)):
    if i % 2 == 0:
        # print(word_list[i].capitalize())
        word_list[i] = word_list[i].upper()
    else:
        # print(word_list[i].lower())
        word_list[i] = word_list[i].lower()

print("AFTER: ", word_list, "Type: ", type(word_list)) 