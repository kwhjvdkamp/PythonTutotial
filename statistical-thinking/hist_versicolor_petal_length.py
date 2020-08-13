# Import plotting modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import pandas as pd

# ==[1]======================
from sklearn import datasets
from sklearn.decomposition import PCA

# Set default Seaborn style
sns.set()

# import some data to play with
# https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html#sphx-glr-auto-examples-datasets-plot-iris-dataset-py
iris = datasets.load_iris()
# print (iris)
# output: the complete dataframe

# get the key names of the dataframe
dataframe_keys = iris.keys()
print('dataframe_keys:\r\n', dataframe_keys)
# OUTPUT: dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])

# retrieve value of 'data'
data = iris["data"][:, :3]
print('dataframe_key: \'data\':\r\n', data)
# # OUTPUT: all rows according [:,<column(s)>] and the first three columns according [<row(s)>, :3]
# NOTE ['<row(s)>','<column(s)>']

# retrieve what's in 'target'
target = iris["target"]
print('dataframe_key: \'target\':\r\n', target)

target_names = iris["target_names"]
print('dataframe_key: \'target_names\':\r\n', target_names)

# subtract dataframe 'df'
df = pd.DataFrame(data, columns = iris["target_names"])
print('dataframe: \'df.head()\':\r\n', df.head())
print('dataframe: \'statistics\': ', df.describe())

# define scatter-plot: range of xAxis (Setosa) and yAxis (Versicolor)
x_min, x_max = data[:, 0].min() - .5, data[:, 0].max() + .5
print(x_min, x_max)
y_min, y_max = data[:, 1].min() - .5, data[:, 1].max() + .5
print(y_min, y_max)
# z_min, z_max = data[:, 2].min() - .5, data[:, 2].max() + .5
# print(z_min, z_max)

plt.figure(1, figsize = (8, 6))
plt.clf()

# Plot the training points
plt.scatter(data[:, 0], data[:, 1], c = target, edgecolor = 'k')
plt.xlabel('Sepal (Kelkblad) length (cm)')
plt.ylabel('Sepal (Kelkblad) width (cm)')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(())
plt.yticks(())

# Plot histogram of versicolor petal lengths
_ = plt.hist(iris)

# ==[2]======================
# Compute number of data points for versicolor: n_data
data_versicolor = iris["data"][:, 1:2]
n_data = len(data_versicolor)
print('Versicolor: (', n_data,')\r\n', data_versicolor)

# Number of bins is the square root of number of data points: n_bins, and
# convert it to an integer: n_bins
n_bins = int(np.sqrt(n_data))

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the histogram and label axes
_ = plt.hist(data_versicolor, bins=n_bins)
_ = plt.xlabel('Versicolor petal (kelkblad) length (cm)')
_ = plt.ylabel('count')


# ==[3]===============================================================
# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
pca = PCA(n_components = 3).fit_transform(iris["data"])
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
