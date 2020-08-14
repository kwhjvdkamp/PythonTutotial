# Import plotting modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm
import pandas as pd
import seaborn as sns

from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

# Import learning dataset from scikit-learn.org
from def_iris import iris

# Set default Seaborn style
sns.set()

iris = iris()
data = iris["data"][:, :4]
# print(data)
target = iris["target"]
# print(target)
target_names = iris["target_names"]
print(target_names)
df = pd.DataFrame(data, columns = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"])
# print(df)


# define scatter-plot:
# Sepal (kelkblad) length (cm) <==> column 0 => X-Axis
# Sepal (kelkblad) width (cm)  <==> column 1 => Y-Axis

# ==[1]======================
plt.figure(1, figsize = (8, 6))
plt.clf()

# print('============================')
# Learning POINTS:
# 1) df.iloc[:, 0:1] is the dataframe of the complete first column (incl. column_name)
# 2) df.iloc[:, 0:1].values is its list of values
sepal_length = df.iloc[:, 0:1].values
# print(sepal_length[0:3])
sepal_width = df.iloc[:, 1:2].values
# print(sepal_width[0:3])
# print('============================')

# Plot the training points
plt.scatter(sepal_length, sepal_width, c = target, edgecolor = 'k', marker='.')

plt.xlabel('Sepal (Kelkblad) length (cm)')
plt.ylabel('Sepal (Kelkblad) width (cm)')

x_min = df.iloc[:-1, 0:1].values.min() - .5
x_max = df.iloc[:-1, 0:1].values.max() + .5
print('X-axis\r\n', x_min, x_max)
y_min = df.iloc[:-1, 1:2].values.min() - .5
y_max = df.iloc[:-1, 1:2].values.max() + .5
print('Y-axis\r\n', y_min, y_max)

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(sepal_length)
plt.yticks(sepal_width)

# plt.legend((target_names[0], target_names[1], target_names[2]), loc='upper left')
plt.legend((target_names[0].iloc[0]), loc='upper left')
# plt.legend((target_names[1]), loc='upper left')
# plt.legend((target_names[2]), loc='upper left')

# Plot histogram of versicolor petal lengths
# ==[2]======================
# Compute number of df points for versicolor: n_data
data_versicolor = df.iloc[:, 1:2].values
n_flowers = len(data_versicolor)
print('Versicolor: (', n_flowers,')\r\n', data_versicolor)

# Number of bins is the square root of number of data points: n_bins, and
# convert it to an integer: n_bins
n_bins = int(np.sqrt(n_flowers))

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the histogram and label axes
_ = plt.hist(data_versicolor, bins=n_bins)
_ = plt.xlabel('Versicolor petal (kelkblad) length (cm)')
_ = plt.ylabel('count')


# ==[3]===============================================================
# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
pca = PCA(n_components = 3).fit_transform(df)
print('Principal Component Analysis:\r\n', pca)

fig = plt.figure(3, figsize = (8, 6))
ax = Axes3D(fig, elev = -150, azim = 110)

ax.scatter(pca[:, 0], pca[:, 1], pca[:, 2], c = target,
           cmap=plt.cm.get_cmap('Reds'), edgecolor='k', s=40)

ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])


# ==[PLOT]==========================================================
# Note: the  plots are printed on top of each other !!!
plt.show()
