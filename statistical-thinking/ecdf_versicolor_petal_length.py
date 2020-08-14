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
# print(iris)
data = iris['data'][:, :4]
# print(data)
target = iris['target']
# print(target)
target_names = iris['target_names']
# print(target_names)

name_setosa = target_names[0]
name_versicolor = target_names[1]
name_virginica = target_names[2]

df_data = pd.DataFrame(data, columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
column_name_setosa = df_data.columns[0]
df_target = pd.DataFrame(target, columns = ['target'])
column_name_target = df_target.columns[0]

# print(df_data.head())
# print(df_target.head())

# df = pd.concat([df_data, df_target])
df = pd.merge(df_data, df_target, right_index=True, left_index=True)
# print(df.head())

# print(df.values[0:2, 0:5])

# iris_petal_length = df_data.iloc[0:-1,0:1].values
# ---------------------------------------------------
setosa_petal_length = df[(df[column_name_target] == target_names.tolist().index(name_setosa))].iloc[0:-1, 0:1].values
# print(setosa_petal_length)
versicolor_petal_length = df[(df[column_name_target] == target_names.tolist().index(name_versicolor))].iloc[0:-1, 0:1].values
# print(versicolor_petal_length)
virginica_petal_length = df[(df[column_name_target] == target_names.tolist().index(name_virginica))].iloc[0:-1, 0:1].values
# print(virginica_petal_length)

# Compute ECDF for versicolor data: x_vers, y_vers
# x_iris, y_iris = ecdf(iris_petal_length)
# ---------------------------------------------------
x_setosa, y_setosa = ecdf(setosa_petal_length)
x_versicolor, y_versicolor = ecdf(versicolor_petal_length)
x_virginica, y_virginica = ecdf(virginica_petal_length)

# Generate plot
# _ = plt.plot(x_iris, y_iris, marker='.', linestyle='none')
# ---------------------------------------------------
_ = plt.title('(Empirical) Cumulative Distribution\nPetal Length (cm) of three species Irises')
_ = plt.plot(x_setosa, y_setosa, marker='.', linestyle='none', color='black')
_ = plt.plot(x_versicolor, y_versicolor, marker='.', linestyle='none', color='yellow')
_ = plt.plot(x_virginica, y_virginica, marker='.', linestyle='none', color='orange')

# Label the axes
_ = plt.legend((name_setosa, name_versicolor, name_virginica), loc='upper right')
_ = plt.xlabel(column_name_setosa)
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
