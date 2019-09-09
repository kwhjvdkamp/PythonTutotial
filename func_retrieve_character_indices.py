def retrieve_character_indices(string):
    character_indices = dict()
    # Define the 'for' loop
    for index, character in enumerate(string):
        # Update the dictionary if the key already exists
        if character in character_indices:
            print("Dict (character_indices[character]): ", character_indices[character])
            print("Key: ", character, "| Index: ", index)
            character_indices[character].append(index)
            print("Dict (character_indices[character]): ", character_indices[character])
        # Update the dictionary if the key is absent
        else:
            print("Key: ", character)
            print("Index: ", index)
            character_indices[character] = [index]
            
    return character_indices
  
print(retrieve_character_indices('enumerate an Iterable'))