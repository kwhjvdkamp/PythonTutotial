import pandas as pd

from functools import reduce


scores = {['gender': 
['female', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'male', 
'male', 'male', 'female', 'female', 'male', 'male', 'male', 'male', 'male', 'female', 
'female', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'female', 'female', 
'male', 'female', 'female', 'female', 'female', 'female', 'female', 'male', 'male', 'female', 
'male', 'female', 'female', 'female', 'female', 'male', 'male', 'male', 'male', 'male', 
'female', 'female', 'female', 'female', 'female', 'female', 'female', 'male', 'female', 'female', 
'female', 'male', 'male', 'male', 'female', 'female', 'male', 'male', 'female', 'male', 
'female', 'male', 'female', 'female', 'male', 'male', 'female', 'male', 'male', 'female', 
'male', 'male', 'male', 'male', 'male', 'female', 'male', 'female', 'male', 'male', 
'female', 'male', 'female', 'male', 'female', 'male', 'female', 'female', 'female', 'female']
# ,        
# 'race_ethnicity': 
#     ['group E', 'group D', 'group D', 'group B', 'group C', 'group D', 'group D', 'group C', 'group C', 'group B', 'group C', 'group B', 'group C', 'group A', 'group B', 'group C', 'group E', 'group D', 'group C', 'group B', 'group A', 'group C', 'group C', 'group E', 'group E', 'group C', 'group C', 'group C', 'group B', 'group C', 'group B', 'group E', 'group D', 'group C', 'group E', 'group D', 'group D', 'group D', 'group B', 'group C', 'group E', 'group A', 'group D', 'group B', 'group B', 'group B', 'group B', 'group D', 'group E', 'group C', 'group E', 'group C', 'group C', 'group A', 'group D', 'group B', 'group D', 'group B', 'group E', 'group E', 'group D', 'group A', 'group B', 'group B', 'group B', 'group C', 'group C', 'group C', 'group D', 'group B', 'group D', 'group B', 'group A', 'group C', 'group C', 'group D', 'group C', 'group B', 'group C', 'group C', 'group A', 'group D', 'group C', 'group C', 'group C', 'group C', 'group C', 'group C', 'group C', 'group B', 'group B', 'group B', 'group E', 'group D', 'group D', 'group C', 'group A', 'group A', 'group D', 'group D'],
# 'parental level of education': 
#     ["associate\'s degree", 'some college', 'some high school', "bachelor\'s degree", "master\'s degree", "bachelor\'s degree", "associate\'s degree", 'some high school', "associate\'s degree", 'some high school', 'some high school', 'some college', 'some high school', 'some college', 'high school', 'some college', 'high school', "master\'s degree", "bachelor\'s degree", 'some college', "master\'s degree", "associate\'s degree", "associate\'s degree", "master\'s degree", "associate\'s degree", 'some college', "bachelor\'s degree", 'some college', 'some high school', 'high school', 'high school', 'high school', 'high school', "master\'s degree", "bachelor\'s degree", 'high school', 'some college', 'some college', "master\'s degree", "associate\'s degree", "associate\'s degree", "master\'s degree", 'some high school', 'some high school', 'high school', 'high school', 'some college', 'some college', 'high school', 'high school', 'some high school', "master\'s degree", 'some high school', "associate\'s degree", 'some college', "bachelor\'s degree", "associate\'s degree", 'some college', 'some high school', "bachelor\'s degree", "master\'s degree", "associate\'s degree", 'high school', 'some high school', "master\'s degree", 'some college', "associate\'s degree", 'some college', "associate\'s degree", "bachelor\'s degree", 'some high school', "bachelor\'s degree", "bachelor\'s degree", "associate\'s degree", "master\'s degree", 'some college', 'some college', 'some college', "bachelor\'s degree", 'some college', 'high school', 'some college', 'some high school', "master\'s degree", 'some college', 'some college', 'high school', "bachelor\'s degree", 'some college', 'some college', 'some college', 'some high school', 'some high school', "master\'s degree", 'high school', "bachelor\'s degree", "bachelor\'s degree", 'some high school', 'high school', "master\'s degree"],
# 'lunch': 
#     ['free/reduced', 'free/reduced', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'standard', 'standard', 'standard', 'free/reduced', 'standard', 'free/reduced', 'free/reduced', 'free/reduced', 'standard', 'standard', 'free/reduced', 'free/reduced', 'standard', 'free/reduced', 'standard', 'standard'],
# 'test preparation course': 
#     ['none', 'none', 'none', 'none', 'completed', 'completed', 'none', 'none', 'none', 'none', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'none', 'none', 'none', 'completed', 'completed', 'completed', 'none', 'none', 'none', 'completed', 'completed', 'completed', 'completed', 'none', 'completed', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'completed', 'completed', 'none', 'completed', 'completed', 'none', 'completed', 'none', 'none', 'none', 'completed', 'none', 'none', 'completed', 'none', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'none', 'none', 'completed', 'completed', 'completed', 'none', 'none', 'none', 'none', 'none', 'none', 'completed', 'completed', 'none', 'none', 'completed', 'none', 'completed', 'none', 'none', 'completed', 'none', 'none', 'completed', 'completed', 'completed', 'completed', 'none', 'none', 'completed', 'completed', 'completed', 'completed']
}


def rank(series):
    # Calculate the mean of the input series
    mean = np.mean(series)
    # Return the mean and its rank as a list
    if mean > 90:
        return [mean, 'high']
    if mean > 60:
        return [mean, 'medium']
    return [mean, 'low']

# Insert the output of rank() into new columns of scores
cols = ['math score', 'reading score', 'writing score']
scores[['mean', 'rank']] = scores[cols].apply(rank, axis=1,
                                              result_type='expand')
print(scores[['mean', 'rank']].head())