# Covering 3 ways to write modular code with Python:
# > packages        e.g. pandas package
# > classes, and    e.g. df class
# > methods         e.g. plot method

# Import the pandas-PACKAGE
import matplotlib.pyplot as plt
import pandas as pd

# gca stands for 'get current axis'
ax = plt.gca()

# Create example data
data = {'x': [1, 2, 3, 4],
        'y': [20.1, 62.5, 34.8, 42.7]}

# Create a dataframe CLASS object
df = pd.DataFrame(data)

print(df)

# https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.plot.html

df.plot(kind='scatter', x='x', y='y', color='red', ax=ax)

plt.show()
