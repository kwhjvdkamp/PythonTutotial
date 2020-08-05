pets = {
    'Harry': 'Hedwig the owl', 
    'Hermione': 'Crookshanks the cat', 
    'Ron': 'Scabbers the rat'
}

for key, value in pets.items():
    print("key: ", key, "| value: ", value)

print("----------")

iter_pets = iter(pets)
print(next(iter_pets))
print(next(iter_pets))
print(next(iter_pets))

print("----------")

# print(list(iter_pets))        # prints an empty list ([])
# print(next(list(iter_pets)))    # prints TypeError: 'list' object is not an iterator

print("----------")

print("Count items: ", len(pets.items()))

for i in range(len(pets.items())):
    print("Next ", i+1, " >> ", list(next(iter_pets)))

# print("Twice next(iter_pets): ", list(iter_pets))

# print(next(iter_pets))

# print(next(iter_pets))
# <dict_keyiterator object at 0x000002414F3B3228>
# Harry
# Hermione
# Ron
# Traceback (most recent call last):
#   File "c:/HomeProjects/PythonTutotial/iteration_dict.py", line 9, in <module>
#     print(next(iter_pets))
# StopIteration
