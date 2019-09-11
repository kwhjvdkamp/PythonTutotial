# ANSWER '(alphabet.index(char) - key) % len(alphabet)' ALSO CORRECT
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(text, key): 
    result = ''
    for char in text.lower():
        idx = (alphabet.index(char) + key) % len(alphabet)
        result = result + alphabet[idx]
    return result
#--------------------------------
def decrypt(text, key): 
    result = ''
    for char in text.lower():
        idx = (alphabet.index(char) - key) % len(alphabet)
        # idx = (alphabet.index(char) - key)
        result = result + alphabet[idx]
    return result
#--------------------------------
encrypted_datacamp = encrypt("datacamp", 10)
#--------------------------------
# Check the encryption function with the shift equals to 10
print("Encrypt \'datacamp\': ", encrypted_datacamp, " | Decrypt: \'", encrypted_datacamp, "\': ", decrypt(encrypted_datacamp, 10) )

# OUTPUT WITH '\ idx = (alphabet.index(char) - key) % len(alphabet)'\ 
# EXACTLY THE SAME AS WITH 
# OUTPUT WITH '\ idx = (alphabet.index(char) - key)'\ 
# Encrypt 'datacamp':  nkdkmkwz  | Decrypt:  ' nkdkmkwz ':  datacamp