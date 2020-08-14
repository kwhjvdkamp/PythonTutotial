import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm
import pandas as pd
import seaborn as sns

# Import learning dataset from scikit-learn.org
from def_iris import iris

# (E)CDF (Empirical) Cumulative Distribution Function
from def_ecdf import ecdf

iris = iris()
data = iris["data"][:, :4]
print(data)
target = iris["target"]
print(target)
target_names = iris["target_names"]
print(target_names)
df = pd.DataFrame(data, columns = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"])
print(df.head())
print(df.values[0:2, 0:4])

versicolor_petal_length = df.iloc[0:-1,0:1].values

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
