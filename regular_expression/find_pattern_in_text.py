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


# text = 'Python has 4 main data structures: list, tuple, set, and dictionary.'
# pattern = r'[,:\.]?\s?'
# splitted_text = re.split(pattern, text)
# print(splitted_text)
# # ['', 'P', 'y', 't', 'h', 'o', 'n', '', 'h', 'a', 's', '', '4', '', 'm', 'a', 'i', 'n', '', 'd', 'a', 't', 'a', '', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 's', '', 'l', 'i', 's', 't', '', 't', 'u', 'p', 'l', 'e', '', 's', 'e', 't', '', 'a', 'n', 'd', '', 'd', 'i', 'c', 't', 'i', 'o', 'n', 'a', 'r', 'y', '', '']
# pattern = r'\w+'
# re_findall_text = re.findall(pattern, text)
# print(re_findall_text)
# ['Python', 'has', '4', 'main', 'data', 'structures', 'list', 'tuple', 'set', 'and', 'dictionary']


# my_string = "the 60-s, the 80s music was much better that the 90s"
# # 'the'  >  extact
# # \s  >  white space
# # +  >  any character, once or more, immediately to the left
# # \s  >  white space
# re_findall = re.findall(r"the\s\d+s", my_string)
# # OUTPUT: ['the 80s', 'the 90s']
# print(re_findall)


# my_string = "the 60-s, the 80s music was much better that the 90s"
# see previous exercise
# # $  >  end of the string
# re_findall = re.findall(r"the\s\d+s$", my_string)
# # OUTPUT: []
# print(re_findall)


# my_string = "The concert was amazing! @ameli!a @joh&&n @mary90"
# # '@'  >  extact
# # \w  >  any word character, followed by + once or more, immediately to the left
# # \W  >  non-word character, followed by * zero or more, immediately to the left
# # \w  >  any word character, followed by + once or more, immediately to the left
# re_findall = re.findall(r"@\w+\W*\w+", my_string)
# # OUTPUT: ['@ameli!a', '@joh&&n', '@mary90']
# # NOTE Is is not looking or machting the numbers, it matches on '@mary'
# print(re_findall)


# my_string = "Just check out this link: www.amazingpics.com. It has amazing photos!"
# # 'www.+com'  >  extact 'www', followed by . match any character except new line to the left, followed by, once or more, immediately to the left, exact 'com'
# re_findall = re.findall(r"www.+com",my_string)
# # OUTPUT: ['www.amazingpics.com']
# # NOTE '.+' means . match any character except new line to the left, followed by once or more > so, including the '.'
# print(re_findall)


# my_string = "I love the music of Mr.Go. However, the sound was too loud."
# re_split = re.split(r".\s", my_string)
# # NOTE split on any character without except new line to the left followed by one white space > so, 'I' is followed by a white space this one-character word is splitted as [] and [I] therefore in the output the first match is a empty one
# print(re_split)


# my_string = "My&name&is#John Smith. I%live$in#London."
# # '[#$%&]'  >  or operator, find one of these characters and if found substitute for a " "
# re_sub = re.sub(r"[#$%&]", " ", my_string)
# # OUTPUT: 'My name is John Smith. I live in London.'
# print(re_sub)


# my_links = "Bad website: www.99.com. Favorite site: www.hola.com"
# # ^ (Accent circonflexe) transforms expression to negative
# re_findall_w = re.findall(r"www[^a-z]+com", my_links)
# re_findall_d = re.findall(r"www[^0-9]+com", my_links)
# print(re_findall_w, re_findall_d)


# text = "Clary has 2 friends who she spends a lot of time with. Susan has 3 brothers while John has 4 sisters."
# re_findall_cg1 = re.findall(r"([A-Za-z]+)\s\w+\s\d+\s\w+", text)
# # # NOTE Although for the first part of the regex '([A-Za-z]+)\s\w+\s', keep in mind it is a part of the total regex '([A-Za-z]+)\s\w+\s(\d+)\s(\w+)',
# print(re_findall_cg1)

# text = "Clary has 2 friends who she spends a lot of time with. Susan has 3 brothers while John has 4 sisters."
# re_findall_cg123 = re.findall(r"([A-Za-z]+)\s\w+\s(\d+)\s(\w+)", text)
# # # NOTE Although for the first part of the regex '([A-Za-z]+)\s\w+\s', keep in mind it is a part of the total regex '([A-Za-z]+)\s\w+\s(\d+)\s(\w+)',
# print(re_findall_cg123)


# sentiment_analysis = [
#     'Just got ur newsletter, those fares really are unbelievable. Write to statravelAU@gmail.com or statravelpo@hotmail.com. They have amazing prices'
#     , 'I should have paid more attention when we covered photoshop in my webpage design class in undergrad. Contact me Hollywoodheat34@msn.net.'
#     , 'hey missed ya at the meeting. Read your email! msdrama098@hotmail.com']
# # (
# # [] or | any character from a to z, A to Z or any number from 0 to 9 within this box
# # + | Greedily matches the any characters within the [] to its left 1 or more times
# # ) | group everything within
# # @ | match on @
# # \S | Matches non-whitespace characters (after an @ never a white space occurs)
# regex_email = r"([A-Za-z0-9]+)@\S+"

# for tweet in sentiment_analysis:
#     # Find all matches of regex in each tweet
#     email_matched = re.findall(regex_email, tweet)

#     # Complete the format method to print the results
#     print("Lists of users found in this tweet: {}".format(email_matched))


# Complete the regular expression to match and capture all the flight information required. Only the first parenthesis were placed for you.
# Find all the matches corresponding to each piece of information about the flight. Assign it to flight_matches.
# Complete the format method with the elements contained in flight_matches. In the first line print the airline,and the flight number. In the second line, the departure and destination. In the third line, the date.
# # Write regex to capture information of the flight
# flight = "Here you have your boarding pass LA4214 AER-CDB 06NOV"
# regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"
# # Find all matches of the flight information
# flight_matches = re.findall(regex, flight)
# # print(flight_matches, type(flight_matches))
# # OUTPUT: [('IB', '3723', 'AMS', 'MAD', '06OCT')]  object list containing one tuple
# # Print the matches
# print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
# print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
# print("Date: {}".format(flight_matches[0][4]))
# # OUTPUT:
# # Airline: LA Flight number: 4214
# # Departure: AER Destination: CDB
# # Date: 06NOV


# Complete the regular expression to capture the words love or like or enjoy. Match and capture the words movie or concert. Match and capture anything appearing until the ..
# Find all matches of the regex in each element of sentiment_analysis. Assign them to positive_matches.
# Complete the .format() method to print out the results contained in positive_matches for each element in sentiment_analysis.
# sentiment_analysis = [
#     'I totally love the concert The Book of Souls World Tour. It kinda amazing!'
#     , 'I enjoy the movie Wreck-It Ralph. I watched with my boyfriend.'
#     , "I still like the movie Wish Upon a Star. Too bad Disney doesn't show it anymore."
# ]
# # Write a regex that matches sentences with the optional words
# regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."
# for tweet in sentiment_analysis:
#     # Find all matches of regex in tweet
#     positive_matches = re.findall(regex_positive, tweet)
#     # Complete format to print out the results
#     print("Positive comments found {}".format(positive_matches))


# Complete the regular expression to capture the words hate or dislike or disapprove. Match but don't capture the words movie or concert. Match and capture anything appearing until the ..
# Find all matches of the regex in each element of sentiment_analysis. Assign them to negative_matches.
# Complete the .format() method to print out the results contained in negative_matches for each element in sentiment_analysis.
# sentiment_analysis = ['That was horrible! I really dislike the movie The cabin and the ant. So boring.'
# , "I disapprove the movie Honest with you. It's full of cliches."
# , 'I dislike very much the concert After twelve Tour. The sound was horrible.'
# ]
# # Write a regex that matches sentences with the optional words
# regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."
# for tweet in sentiment_analysis:
#     # Find all matches of regex in tweet
#     negative_matches = re.findall(regex_negative, tweet)

#     # Complete format to print out the results
#     print("Negative comments found {}".format(negative_matches))


# contract = "Provider will invoice Client for Services performed within 30 days of performance. "\
#     "Client will pay Provider as set forth in each Statement of Work within 30 days of receipt and acceptance of such invoice. "\
#     "It is understood that payments to Provider for services rendered shall be made in full as agreed, "\
#     "without any deductions for taxes of any kind whatsoever, "\
#     "in conformity with Provider’s status as an independent contractor. "\
#     "Signed on 03/25/2001."
# # Write a regex that captures the month, day, and year in which the contract was signed. Scan contract for matches.
# #  Wants: The dates appear as Signed on 05/24/2016 (05 indicating the month, 24 the day). You decide to use capturing groups to extract this information.
# # Write regex and scan contract to capture the dates described
# regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
# dates = re.search(regex_dates, contract)
# print(dates)
# # Assign to each key the corresponding match
# signature = {
#     "day": dates.group(2),
#     "month": dates.group(1),
#     "year": dates.group(3)
# }
# print(signature)


# html_tags = [
#     '<body>Welcome to our course! It would be an awesome experience</body>'
#     , '<article>To be a data scientist, you need to have knowledge in statistics and mathematics</article>'
#     , '<nav>About me Links Contact me!'
# ]
# Complete the regex in order to match closed HTML tags. Find if there is a match in each string of the list html_tags. Assign the result to match_tag.
# If a match is found, print the first group captured and saved in match_tag.
# If no match is found, complete the regex to match only the text inside the HTML tag. Assign it to notmatch_tag.
# Print the first group captured by the regex and save it in notmatch_tag.
# for string in html_tags:
#     # Complete the regex and find if it matches a closed HTML tags
#     match_tag =  re.match(r"<(\w+)>.*?</\1>", string)

#     print(match_tag)

#     if match_tag:
#         # If it matches print the first group capture
#         print("Your tag {} is closed".format(match_tag.group(1)))
#     else:
#         # If it doesn't match capture only the tag
#         notmatch_tag = re.match(r"<(\w+)>", string)
#         # Print the first group capture
#         print("Close your {} tag!".format(notmatch_tag.group(1)))


sentiment_analysis = [
    '@marykatherine_q i know! I heard it this morning and wondered the same thing. Moscooooooow is so behind the times'
    , 'Staying at a friends house...neighborrrrrrrs are so loud-having a party'
    , 'Just woke up an already have read some e-mail'
]
# Complete the regular expression to match an elongated word as described.
# Search the elements in sentiment_analysis list to find out if they contain elongated words. Assign the result to match_elongated.
# Assign the captured group number zero to the variable elongated_word.
# Print the result contained in the variable elongated_word.

# Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1\w*"

for tweet in sentiment_analysis:
    # Find if there is a match in each tweet
    match_elongated = re.search(regex_elongated, tweet)

    if match_elongated:
        # Assign the captured group zero
        elongated_word = match_elongated.group(0)

        # Complete the format method to print the word
        print("Elongated word found: {word}".format(word=elongated_word))
    else:
        print("No elongated word found")