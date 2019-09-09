import pandas as pd

from functools import reduce

# scores
#     gender race/ethnicity parental level of education         lunch test preparation course  math score  reading score  writing score
# 0   female        group E          associate\'s degree  free/reduced                    none          74             86             82
# 1   female        group D                some college  free/reduced                    none          44             49             53
# 2     male        group D            some high school  free/reduced                    none          54             46             43
# 3   female        group B           bachelor\'s degree      standard                    none          88             95             92
# 4     male        group C             master\'s degree      standard               completed          85             81             81
# 5   female        group D           bachelor\'s degree  free/reduced               completed          81             85             86
# 6     male        group D          associate\'s degree      standard                    none          82             74             69
# 7   female        group C            some high school      standard                    none          65             75             72
# 8     male        group C          associate\'s degree      standard                    none          73             69             69
# 9     male        group B            some high school  free/reduced                    none          54             54             48
# 10    male        group C            some high school      standard                    none          63             67             59
# 11    male        group B                some college  free/reduced                    none          61             65             60
# 12  female        group C            some high school  free/reduced               completed          43             53             47
# 13  female        group A                some college      standard                    none          51             67             66
# 14    male        group B                 high school      standard               completed          49             45             50
# 15    male        group C                some college      standard                    none          82             82             72
# 16    male        group E                 high school  free/reduced                    none          79             70             64
# 17    male        group D             master\'s degree  free/reduced                    none          55             58             52
# 18    male        group C           bachelor\'s degree  free/reduced                    none          41             36             37
# 19  female        group B                some college      standard                    none          55             71             64
# 20  female        group A             master\'s degree  free/reduced               completed          90            100             99
# 21  female        group C          associate\'s degree      standard               completed          93             96             94
# 22    male        group C          associate\'s degree  free/reduced               completed          45             54             53
# 23    male        group E             master\'s degree      standard                    none          79             70             64
# 24  female        group E          associate\'s degree      standard                    none          52             66             60
# 25    male        group C                some college  free/reduced                    none          62             60             54
# 26  female        group C           bachelor\'s degree      standard               completed          69             79             78
# 27    male        group C                some college  free/reduced               completed          66             68             66
# 28  female        group B            some high school  free/reduced               completed          27             53             53
# 29  female        group C                 high school      standard               completed          64             73             71
# 30    male        group B                 high school  free/reduced                    none          46             40             36
# 31  female        group E                 high school      standard               completed          67             81             85
# 32  female        group D                 high school      standard                    none          86             93             94
# 33  female        group C             master\'s degree      standard                    none          55             68             68
# 34  female        group E           bachelor\'s degree      standard               completed          96             84             98
# 35  female        group D                 high school  free/reduced                    none          56             72             68
# 36  female        group D                some college  free/reduced               completed          77             86             90
# 37    male        group D                some college  free/reduced                    none          45             43             40
# 38    male        group B             master\'s degree  free/reduced                    none          64             62             59
# 39  female        group C          associate\'s degree  free/reduced               completed          61             76             78
# 40    male        group E          associate\'s degree  free/reduced               completed          59             51             48
# 41  female        group A             master\'s degree  free/reduced                    none          37             54             53
# 42  female        group D            some high school      standard               completed          90            100            100
# 43  female        group B            some high school      standard               completed          62             72             70
# 44  female        group B                 high school  free/reduced                    none          53             66             54
# 45    male        group B                 high school      standard               completed          75             66             66
# 46    male        group B                some college  free/reduced                    none          46             33             30
# 47    male        group D                some college  free/reduced                    none          59             60             52
# 48    male        group E                 high school      standard                    none          85             76             69
# 49    male        group C                 high school  free/reduced               completed          48             56             57
# 50  female        group E            some high school      standard                    none          71             73             70
# 51  female        group C             master\'s degree      standard                    none          71             83             80
# 52  female        group C            some high school      standard               completed          62             79             80
# 53  female        group A          associate\'s degree      standard                    none          91             97             97
# 54  female        group D                some college  free/reduced                    none          49             65             62
# 55  female        group B           bachelor\'s degree      standard                    none          69             88             83
# 56  female        group D          associate\'s degree      standard               completed          62             74             71
# 57    male        group B                some college      standard                    none          62             62             55
# 58  female        group E            some high school      standard               completed          76             81             87
# 59  female        group E           bachelor\'s degree  free/reduced                    none          57             73             75
# 60  female        group D             master\'s degree      standard                    none          68             78             76
# 61    male        group A          associate\'s degree  free/reduced                    none          46             50             45
# 62    male        group B                 high school      standard               completed          72             64             67
# 63    male        group B            some high school      standard                    none          65             51             53
# 64  female        group B             master\'s degree      standard               completed          83            100            100
# 65  female        group C                some college  free/reduced                    none          43             53             54
# 66    male        group C          associate\'s degree      standard                    none          60             60             53
# 67    male        group C                some college  free/reduced                    none          54             56             52
# 68  female        group D          associate\'s degree  free/reduced                    none          40             53             54
# 69    male        group B           bachelor\'s degree      standard               completed         100             92             94
# 70  female        group D            some high school      standard               completed          69             77             79
# 71    male        group B           bachelor\'s degree      standard               completed          74             72             76
# 72  female        group A           bachelor\'s degree      standard                    none          79             91             90
# 73  female        group C          associate\'s degree      standard                    none          57             70             67
# 74    male        group C             master\'s degree      standard                    none          62             52             51
# 75    male        group D                some college  free/reduced                    none          73             60             64
# 76  female        group C                some college      standard                    none          62             76             66
# 77    male        group B                some college      standard                    none          58             59             51
# 78    male        group C           bachelor\'s degree  free/reduced               completed          72             70             76
# 79  female        group C                some college      standard               completed          68             76             74
# 80    male        group A                 high school      standard                    none          73             66             64
# 81    male        group D                some college      standard                    none          65             71             75
# 82    male        group C            some high school  free/reduced               completed          70             81             75
# 83    male        group C             master\'s degree      standard                    none          66             61             63
# 84    male        group C                some college      standard               completed          66             59             60
# 85  female        group C                some college      standard                    none          64             85             75
# 86    male        group C                 high school      standard                    none          71             67             61
# 87  female        group C           bachelor\'s degree  free/reduced               completed          66             64             76
# 88    male        group C                some college      standard                    none          67             65             62
# 89    male        group B                some college  free/reduced                    none          61             53             47
# 90  female        group B                some college  free/reduced               completed          71             90             94
# 91    male        group B            some high school  free/reduced               completed          58             65             63
# 92  female        group E            some high school      standard               completed          86             85             89
# 93    male        group D             master\'s degree      standard               completed          71             62             73
# 94  female        group D                 high school  free/reduced                    none          48             55             54
# 95    male        group C           bachelor\'s degree  free/reduced                    none          73             85             78
# 96  female        group A           bachelor\'s degree      standard               completed          66             64             69
# 97  female        group A            some high school  free/reduced               completed          74             86             84
# 98  female        group D                 high school      standard               completed          58             56             60
# 99  female        group D             master\'s degree      standard               completed          76             87             99

# [100 rows x 8 columns]

# groups_to_consider = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
# series = [
#         ['female', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'male', 'male', 'male', 'female', 'female', 'male', 'male', 'male', 'male', 'male', 'female', 'female', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'female', 'female', 'male', 'female', 'female', 'female', 'female', 'female', 'female', 'male', 'male', 'female', 'male', 'female', 'female', 'female', 'female', 'male', 'male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'female', 'female', 'male', 'male', 'female', 'male', 'male', 'female', 'male', 'male', 'male', 'male', 'male', 'female', 'male', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'female', 'female', 'female'],
#         ['group E', 'group D', 'group D', 'group B', 'group C', 'group D', 'group D', 'group C', 'group C', 'group B', 'group C', 'group B', 'group C', 'group A', 'group B', 'group C', 'group E', 'group D', 'group C', 'group B', 'group A', 'group C', 'group C', 'group E', 'group E', 'group C', 'group C', 'group C', 'group B', 'group C', 'group B', 'group E', 'group D', 'group C', 'group E', 'group D', 'group D', 'group D', 'group B', 'group C', 'group E', 'group A', 'group D', 'group B', 'group B', 'group B', 'group B', 'group D', 'group E', 'group C', 'group E', 'group C', 'group C', 'group A', 'group D', 'group B', 'group D', 'group B', 'group E', 'group E', 'group D', 'group A', 'group B', 'group B', 'group B', 'group C', 'group C', 'group C', 'group D', 'group B', 'group D', 'group B', 'group A', 'group C', 'group C', 'group D', 'group C', 'group B', 'group C', 'group C', 'group A', 'group D', 'group C', 'group C', 'group C', 'group C', 'group C', 'group C', 'group C', 'group B', 'group B', 'group B', 'group E', 'group D', 'group D', 'group C', 'group A', 'group A', 'group D', 'group D'],
#         ["associate\'s degree", 'some college', 'some high school', "bachelor\'s degree", "master\'s degree", "bachelor\'s degree", "associate\'s degree", 'some high school', "associate\'s degree", 'some high school', 'some high school', 'some college', 'some high school', 'some college', 'high school', 'some college', 'high school', "master\'s degree", "bachelor\'s degree", 'some college', "master\'s degree", "associate\'s degree", "associate\'s degree", "master\'s degree", "associate\'s degree", 'some college', "bachelor\'s degree", 'some college', 'some high school', 'high school', 'high school', 'high school', 'high school', "master\'s degree", "bachelor\'s degree", 'high school', 'some college', 'some college', "master\'s degree", "associate\'s degree", "associate\'s degree", "master\'s degree", 'some high school', 'some high school', 'high school', 'high school', 'some college', 'some college', 'high school', 'high school', 'some high school', "master\'s degree", 'some high school', "associate\'s degree", 'some college', "bachelor\'s degree", "associate\'s degree", 'some college', 'some high school', "bachelor\'s degree", "master\'s degree", "associate\'s degree", 'high school', 'some high school', "master\'s degree", 'some college', "associate\'s degree", 'some college', "associate\'s degree", "bachelor\'s degree", 'some high school', "bachelor\'s degree", "bachelor\'s degree", "associate\'s degree", "master\'s degree", 'some college', 'some college', 'some college', "bachelor\'s degree", 'some college', 'high school', 'some college', 'some high school', "master\'s degree", 'some college', 'some college', 'high school', "bachelor\'s degree", 'some college', 'some college', 'some college', 'some high school', 'some high school', "master\'s degree", 'high school', "bachelor\'s degree", "bachelor\'s degree", 'some high school', 'high school', "master\'s degree"],
#         ['free/reduced', 'free/reduced', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'free/reduced', 'standard', 'standard', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard'],
#         ['none', 'none', 'none', 'none', 'completed', 'completed', 'none', 'none', 'none', 'none', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'none', 'none', 'none', 'completed', 'completed', 'completed', 'none', 'none', 'none', 'completed', 'completed', 'completed', 'completed', 'none', 'completed', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'completed', 'completed', 'none', 'completed', 'completed', 'none', 'completed', 'none', 'none', 'none', 'completed', 'none', 'none', 'completed', 'none', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'none', 'none', 'completed', 'completed', 'completed', 'none', 'none', 'none', 'none', 'none', 'none', 'completed', 'completed', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'completed', 'none', 'none', 'completed', 'completed', 'completed', 'completed', 'none', 'none', 'completed', 'completed', 'completed', 'completed']
# ]
# pars = {'weight': [168, 183, 198], 'height': [77, 79, 135]}

scores = {'gender': ["female", "female", "male", "female", "male", "female", "male", "female", "male", "male", "male", "male", "female", "female", "male", "male", "male", "male", "male", "female", "female", "female", "male", "male", "female", "male", "female", "male", "female", "female", "male", "female", "female", "female", "female", "female", "female", "male", "male", "female", "male", "female", "female", "female", "female", "male", "male", "male", "male", "male", "female", "female", "female", "female", "female", "female", "female", "male", "female", "female", "female", "male", "male", "male", "female", "female", "male", "male", "female", "male", "female", "male", "female", "female", "male", "male", "female", "male", "male", "female", "male", "male", "male", "male", "male", "female", "male", "female", "male", "male", "female", "male", "female", "male", "female", "male", "female", "female", "female", "female"],
        'race/ethnicity': ['group E', 'group D', 'group D', 'group B', 'group C', 'group D', 'group D', 'group C', 'group C', 'group B', 'group C', 'group B', 'group C', 'group A', 'group B', 'group C', 'group E', 'group D', 'group C', 'group B', 'group A', 'group C', 'group C', 'group E', 'group E', 'group C', 'group C', 'group C', 'group B', 'group C', 'group B', 'group E', 'group D', 'group C', 'group E', 'group D', 'group D', 'group D', 'group B', 'group C', 'group E', 'group A', 'group D', 'group B', 'group B', 'group B', 'group B', 'group D', 'group E', 'group C', 'group E', 'group C', 'group C', 'group A', 'group D', 'group B', 'group D', 'group B', 'group E', 'group E', 'group D', 'group A', 'group B', 'group B', 'group B', 'group C', 'group C', 'group C', 'group D', 'group B', 'group D', 'group B', 'group A', 'group C', 'group C', 'group D', 'group C', 'group B', 'group C', 'group C', 'group A', 'group D', 'group C', 'group C', 'group C', 'group C', 'group C', 'group C', 'group C', 'group B', 'group B', 'group B', 'group E', 'group D', 'group D', 'group C', 'group A', 'group A', 'group D', 'group D'],
        'parental level of education': ["associate\'s degree", 'some college', 'some high school', "bachelor\'s degree", "master\'s degree", "bachelor\'s degree", "associate\'s degree", 'some high school', "associate\'s degree", 'some high school', 'some high school', 'some college', 'some high school', 'some college', 'high school', 'some college', 'high school', "master\'s degree", "bachelor\'s degree", 'some college', "master\'s degree", "associate\'s degree", "associate\'s degree", "master\'s degree", "associate\'s degree", 'some college', "bachelor\'s degree", 'some college', 'some high school', 'high school', 'high school', 'high school', 'high school', "master\'s degree", "bachelor\'s degree", 'high school', 'some college', 'some college', "master\'s degree", "associate\'s degree", "associate\'s degree", "master\'s degree", 'some high school', 'some high school', 'high school', 'high school', 'some college', 'some college', 'high school', 'high school', 'some high school', "master\'s degree", 'some high school', "associate\'s degree", 'some college', "bachelor\'s degree", "associate\'s degree", 'some college', 'some high school', "bachelor\'s degree", "master\'s degree", "associate\'s degree", 'high school', 'some high school', "master\'s degree", 'some college', "associate\'s degree", 'some college', "associate\'s degree", "bachelor\'s degree", 'some high school', "bachelor\'s degree", "bachelor\'s degree", "associate\'s degree", "master\'s degree", 'some college', 'some college', 'some college', "bachelor\'s degree", 'some college', 'high school', 'some college', 'some high school', "master\'s degree", 'some college', 'some college', 'high school', "bachelor\'s degree", 'some college', 'some college', 'some college', 'some high school', 'some high school', "master\'s degree", 'high school', "bachelor\'s degree", "bachelor\'s degree", 'some high school', 'high school', "master\'s degree"],
        'lunch': ['free/reduced', 'free/reduced', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'free/reduced', 'standard', 'standard', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard'],
        'test preparation course': ['none', 'none', 'none', 'none', 'completed', 'completed', 'none', 'none', 'none', 'none', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'none', 'none', 'none', 'completed', 'completed', 'completed', 'none', 'none', 'none', 'completed', 'completed', 'completed', 'completed', 'none', 'completed', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'completed', 'completed', 'none', 'completed', 'completed', 'none', 'completed', 'none', 'none', 'none', 'completed', 'none', 'none', 'completed', 'none', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'none', 'none', 'completed', 'completed', 'completed', 'none', 'none', 'none', 'none', 'none', 'none', 'completed', 'completed', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'completed', 'none', 'none', 'completed', 'completed', 'completed', 'completed', 'none', 'none', 'completed', 'completed', 'completed', 'completed']
}
D = pd.DataFrame(scores)
print(D)

# columns of the dataset
groups_to_consider = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
print("groups_to_consider: ", groups_to_consider)

print("scores[groups_to_consider]: " , scores[groups_to_consider[0]])



def prevalence(series):
    vals = list(series)
    # print(vals)
    # Create a tuple list with unique items and their counts
    itms = [(x, vals.count(x)) for x in set(series)]
    print("itms: ", itms)
    # Extract a tuple with the highest counts using reduce()
    res = reduce(lambda x, y: x if x[1] > y[1] else y, itms)
    print("Reduced (present the highest count): ", res)

    # Return the item with the highest counts
    return res[0]


# Apply the prevalence function on the scores DataFrame
# result = scores[groups_to_consider].apply(prevalence)
# print("Result: ", result)


# OUTPUT
# prevalence
# gender                               female
# race/ethnicity                      group C
# parental level of education    some college
# lunch                              standard
# test preparation course                none
# dtype: object

