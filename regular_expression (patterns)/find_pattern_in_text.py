import re

# Special characters
# -------------------------------------------------
# Simple characters and numbers are mapped onto themselves:
# >-> a → a
# >-> A → A
# >-> 1 → 1
# Dot (.) maps to anything:
# >-> . → any character
#     . → 'a' , '1' , '"', ' ', ...
# >-> \. → .

# The following meta-characters presented in the pattern as a '\' followed by a letter:
# >-> \w → any alphanumeric character or underscore
#     \w → '1' , 'a' , '_' , ...
# >-> \d → any digit
#     \d → '1' , '2' , '3' , ...
# >-> \s → any whitespace character
#     \s → ' ' , '\t' , ...

# Square brackets
# -------------------------------------------------
# Several meta-characters can be enclosed in square brackets:
# [aAbB] → a , A , b , B
# [a-z] → a , b , c , ...
# [A-Z] → A , B , C , ...
# [0-9] → 0 , 1 , 2 , ...
# [A-Za-z] → A , B , C , ..., a , b , c , ...

# Repetitions
# -------------------------------------------------
# >-> * → no character or it repeats an undefined number of times
#     a* → '', 'a', 'aa', 'aaa', ...
# >-> + → the character is present at least once
#     a+ → 'a', 'aa', 'aaa', ...
# >-> ? → the character exists or not
#     a? → '', 'a'
# >-> {n, m} → the character is present from n to m times
#     a{2,4} → 'aa', 'aaa', 'aaaa'

# text = 'Let\'s consider the following temperatures using the Celsius scale: +23 C, 0 C, -20.0 C, -2.2 C, -5.65 C, 0.0001 C. '\
#      'To convert them to the Fahrenheit scale you have multiply the number by 9/5 and add 32 to the result. '\
#      'Therefore, the corresponding temperatures in the Fahrenheit scale will be: +73.4 F, 32 F, -4.0 F, +28.04 F, 21.83 F, +32.00018 F.'

# pattern = re.compile(r'[+-]?\d+\.?\d* [CF]')

# print(re.findall(pattern, text))

# # Create an object storing the matches using 'finditer()'
# matches_storage = re.finditer(pattern, text)

# # Loop over matches_storage and print out item properties
# for match in matches_storage:
#     print('matching sequence = ' + match.group())
#     print('start index = ' + str(match.start()))
#     print('end index = ' + str(match.end()))

# date = 'blabla bla October 26, 1988, blab blab Oct 26, 1988'
# # date_pattern = re.compile(r'\w+\s[1-3]?\d,\s\d+')
# # date_pattern = re.compile(r'[A-Z][a-z]+\s\d{1,2},\s\d+')
# date_pattern = re.compile(r'[A-Z][a-z]+\s[1-3]?\d,\s\d+')
# # date_pattern = re.compile(r'[A-Z][a-z]+\s[1-3]?\d,\s\d*')
# print(re.findall(date_pattern, date))


text = 'Python has 4 main data structures: list, tuple, set, and dictionary.'
pattern = r'[,:\.]?\s?'
splitted_text1 = re.split(pattern, text)
print(splitted_text1)
# ['', 'P', 'y', 't', 'h', 'o', 'n', '', 'h', 'a', 's', '', '4', '', 'm', 'a', 'i', 'n', '', 'd', 'a', 't', 'a', '', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 's', '', 'l', 'i', 's', 't', '', 't', 'u', 'p', 'l', 'e', '', 's', 'e', 't', '', 'a', 'n', 'd', '', 'd', 'i', 'c', 't', 'i', 'o', 'n', 'a', 'r', 'y', '', '']
pattern = r'\w+'
splitted_text2 = re.findall(pattern, text)
print(splitted_text2)
# ['Python', 'has', '4', 'main', 'data', 'structures', 'list', 'tuple', 'set', 'and', 'dictionary']



