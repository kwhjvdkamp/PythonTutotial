# Covering 3 ways to write modular code with Python: 
# > packages        e.g. pandas package
# > classes, and    e.g. df class
# > methods         e.g. plot method

# Import the pandas PACKAGE
import pandas as pd

# Create some example data
data = {'x': [1, 2, 3, 4], 
        'y': [20.1, 62.5, 34.8, 42.7]}

# Create a dataframe CLASS object
df = pd.DataFrame(data)

# terminal test
# print(df)

# Use the plot METHOD (creates an .exe file at C:/Users/info/AppData/Local/Programs/Python/Python37/python.exe )
# df.plot('x', 'y')