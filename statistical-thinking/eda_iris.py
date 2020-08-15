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

# Import (E)CDF [(Empirical) Cumulative Distribution Function]
from def_ecdf import ecdf

# ++++++++++++++++++++++++++++++++++++++++++++++++++
# Graphical Exploratory Data Analysis on Iris
# ++++++++++++++++++++++++++++++++++++++++++++++++++

# Set default Seaborn style
sns.set()

figure_number = 0

iris = iris()
data = iris["data"][:, :4]
print(data)
target = iris["target"]
# print(target)
target_names = iris["target_names"]
# print(target_names)
# For use to split the df_iris_data-dataframes
name_setosa = target_names[0]
name_versicolor = target_names[1]
name_virginica = target_names[2]

# For use to split the df_iris_data-dataframes
legend_setosa = target_names[0].capitalize()
legend_versicolor = target_names[1].capitalize()
legend_virginica = target_names[2].capitalize()

df_iris_data = pd.DataFrame(data, columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
# print(df_iris_data.head())
df_target = pd.DataFrame(target, columns = ['target'])
# print(df_target.head())
column_name_target = df_target.columns[0]  # is 'target'

# Number of bins is the square root of number of data points: n_bins, and
# converted it to an integer: n_bins
n_bins = int(np.sqrt(len(target)))


# 1) df_iris_data.iloc[:, 0:1] is the dataframe of the complete first column (incl. column_name)
# 2) df_iris_data.iloc[:, 0:1].values is its list of values
iris_sepal_length = df_iris_data.iloc[:, 0:1].values
iris_sepal_width = df_iris_data.iloc[:, 1:2].values
iris_petal_length = df_iris_data.iloc[:, 2:3].values
iris_petal_width = df_iris_data.iloc[:, 3:4].values


# Merging two dataframes: same length but different dimensions
# Via numpy: apparently not possible
# np_df = np.concatenate((df_iris_data, df_target))
# print(np_df.head())
# Suggested option: via pandas
pd_df = pd.merge(df_iris_data, df_target, right_index=True, left_index=True)
# print(pd_df.head(1))
# print(pd_df.values[0:1, 0:5])
# print(pd_df.values[50:51, 0:5])
# print(pd_df.values[100:101, 0:5])

# OUTPUT
# ============================================================================================
#         sepal        sepal       petal       petal    |
#        length        width      length       width    |  target
#       [:, 0:1]    [:, 1:2]    [:, 2:3]    [:, 3:4]    |       0   [0:50, 4:5]
# --------------------------------------------------------------------------------------------
#           5.1          3.5         1.4         0.2    |       0   [0:50, 4:5]         setosa
# --------------------------------------------------------------------------------------------
#           7.0          3.2         4.7         1.4    |       1   [50:100, 4:5]   versicolor
# --------------------------------------------------------------------------------------------
#           6.3          3.3         6.0         2.5    |       2   [100:150, 4:5]  virginica
# ============================================================================================


# --[Sepals]-------------------------------------------------
setosa_sepal_length = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_setosa))].iloc[:, 2:3].values
setosa_sepal_width = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_setosa))].iloc[:, 3:4].values
# print('Length\r'. setosa_sepal_length, 'Width\r', setosa_sepal_width)
versicolor_sepal_length = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_versicolor))].iloc[:, 2:3].values
versicolor_sepal_width = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_versicolor))].iloc[:, 3:4].values
# print('Length\r'. versicolor_sepal_length, 'Width\r', versicolor_sepal_width)
virginica_sepal_length = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_virginica))].iloc[:, 2:3].values
virginica_sepal_width = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_virginica))].iloc[:, 3:4].values
# print('Length\r'. virginica_sepal_length, 'Width\r', virginica_sepal_width)

# --[Petals]-------------------------------------------------
setosa_petal_length = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_setosa))].iloc[:, 2:3].values
setosa_petal_width = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_setosa))].iloc[:, 3:4].values
# print('Length\r'. setosa_petal_length, 'Width\r', setosa_petal_width)
versicolor_petal_length = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_versicolor))].iloc[:, 2:3].values
versicolor_petal_width = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_versicolor))].iloc[:, 3:4].values
# print('Length\r'. versicolor_petal_length, 'Width\r', versicolor_petal_width)
virginica_petal_length = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_virginica))].iloc[:, 2:3].values
virginica_petal_width = pd_df[(pd_df[column_name_target] == target_names.tolist().index(name_virginica))].iloc[:, 3:4].values
# print('Length\r'. virginica_petal_length, 'Width\r', virginica_petal_width)


# Scatter Iris Sepals lengths
# ==[1]=====================================================================================================
figure_number = figure_number + 1
_ = plt.figure(figure_number, figsize = (8, 6))
_ = plt.clf()

_ = plt.scatter(iris_sepal_length, iris_sepal_width, c = target, edgecolor = 'face', marker='.')
# _ = plt.scatter(iris_petal_length, iris_petal_width, c = target, edgecolor = 'face', marker='.')
_ = plt.xlabel('Sepals (\'falls\') length (cm)')
_ = plt.ylabel('Sepals (\'falls\') width (cm)')

# Determine Axises scales
x_min = df_iris_data.iloc[:, 0:1].values.min() - .5
x_max = df_iris_data.iloc[:, 0:1].values.max() + .5
# print('X-axis:', x_min, x_max)
y_min = df_iris_data.iloc[:, 1:2].values.min() - .5
y_max = df_iris_data.iloc[:, 1:2].values.max() + .5
# print('Y-axis:', y_min, y_max)

# Assign on each Axis the min and max value
_ = plt.title('Distribution of Iris Sepals (\'falls\') length (cm) and width (cm) of three species')
# _ = plt.legend((target_names[0], target_names[1], target_names[2]), loc='upper left')
# _ = plt.legend('Iris', loc='upper right')
_ = plt.xlim(x_min, x_max)
_ = plt.ylim(y_min, y_max)

_ = plt.xticks(np.arange(x_min, x_max, step=1))
_ = plt.yticks(np.arange(y_min, y_max, step=1))


# Scatter Iris petal lengths
# ==[2]=====================================================================================================
figure_number = figure_number + 1
_ = plt.figure(figure_number, figsize = (8, 6))
_ = plt.clf()

_ = plt.scatter(iris_petal_length, iris_petal_width, c = target, edgecolor = 'face', marker='.')
_ = plt.xlabel('petals (\'standards\') length (cm)')
_ = plt.ylabel('petals (\'standards\') width (cm)')

# Determine Axises scales
x_min = df_iris_data.iloc[:, 2:3].values.min() - .5
x_max = df_iris_data.iloc[:, 2:3].values.max() + .5
# print('X-axis:', x_min, x_max)
y_min = df_iris_data.iloc[:, 3:4].values.min() - .5
y_max = df_iris_data.iloc[:, 3:4].values.max() + .5
# print('Y-axis:', y_min, y_max)

# Assign on each Axis the min and max value
_ = plt.title('Distribution of Iris petals length (cm) and width (cm) of three species')
# _ = plt.legend((target_names[0], target_names[1], target_names[2]), loc='upper left')
# _ = plt.legend('Iris', loc='upper right')
_ = plt.xlim(x_min, x_max)
_ = plt.ylim(y_min, y_max)

_ = plt.xticks(np.arange(x_min, x_max, step=1))
_ = plt.yticks(np.arange(y_min, y_max, step=1))

# +++

# Histogram of Iris sepal lengths (all three species)
# ==[3]=====================================================================================================
# Compute number of df_iris_data points for versicolor: n_data

figure_number = figure_number + 1
_ = plt.figure(figure_number, figsize=(8, 6))
_ = plt.clf()

# Plot the histogram and label axes
_ = plt.hist(setosa_sepal_length, bins=round(n_bins/3), color='black')
_ = plt.hist(versicolor_sepal_length, bins=n_bins, color='yellow')
_ = plt.hist(virginica_sepal_length, bins=n_bins, color='red')
_ = plt.title('Distribution of Iris sepals (\'falls\') length (cm)')
_ = plt.xlabel('Iris sepals (\'falls\') length (cm)')
_ = plt.ylabel('count')
bin_number = ' (bins=' + str((n_bins / 3)) + ')'
_ = plt.legend((target_names[0].capitalize() + bin_number , target_names[1].capitalize() + bin_number , target_names[2].capitalize() + bin_number ), loc='upper right')
# use axis={'both', 'x', 'y'} to choose axis
_ = plt.locator_params(axis="y", integer=True, tight=True)



# Histogram of Iris sepal widths (all three species)
# ==[4]=====================================================================================================
# Compute number of df_iris_data points for versicolor: n_data

figure_number = figure_number + 1
_ = plt.figure(figure_number, figsize=(8, 6))
_ = plt.clf()

# Plot the histogram and label axes
_ = plt.hist(setosa_sepal_width, bins=round(n_bins/3), color='black')
_ = plt.hist(versicolor_sepal_width, bins=n_bins, color='yellow')
_ = plt.hist(virginica_sepal_width, bins=n_bins, color='red')
_ = plt.title('Distribution of Iris sepals (\'falls\') width (cm)')
_ = plt.xlabel('Iris sepals (\'falls\') width (cm)')
_ = plt.ylabel('count')
bin_number = ' (bins=' + str((n_bins / 3)) + ')'
_ = plt.legend((target_names[0].capitalize() + bin_number , target_names[1].capitalize() + bin_number , target_names[2].capitalize() + bin_number ), loc='upper right')
# use axis={'both', 'x', 'y'} to choose axis
_ = plt.locator_params(axis="y", integer=True, tight=True)



# Histogram of Iris petal lengths (all three species)
# ==[5]=====================================================================================================
# Compute number of df_iris_data points for versicolor: n_data

figure_number = figure_number + 1
_ = plt.figure(figure_number, figsize=(8, 6))
_ = plt.clf()

# Plot the histogram and label axes
_ = plt.hist(setosa_petal_length, bins=round(n_bins/3), color='black')
_ = plt.hist(versicolor_petal_length, bins=n_bins, color='yellow')
_ = plt.hist(virginica_petal_length, bins=n_bins, color='red')
_ = plt.title('Distribution of Iris petals (\'standards\') length (cm)')
_ = plt.xlabel('Iris petals (\'standards\') length (cm)')
_ = plt.ylabel('count')
bin_number = ' (bins=' + str((n_bins / 3)) + ')'
_ = plt.legend((target_names[0].capitalize() + bin_number , target_names[1].capitalize() + bin_number , target_names[2].capitalize() + bin_number ), loc='upper right')
# use axis={'both', 'x', 'y'} to choose axis
_ = plt.locator_params(axis="y", integer=True, tight=True)



# Histogram of Iris petal widths (all three species)
# ==[6]=====================================================================================================
# Compute number of df_iris_data points for versicolor: n_data

figure_number = figure_number + 1
_ = plt.figure(figure_number, figsize=(8, 6))
_ = plt.clf()

# Plot the histogram and label axes
_ = plt.hist(setosa_petal_width, bins=round(n_bins/3), color='black')
_ = plt.hist(versicolor_petal_width, bins=n_bins, color='yellow')
_ = plt.hist(virginica_petal_width, bins=n_bins, color='red')
_ = plt.title('Distribution of Iris petals (\'standards\') width (cm)')
_ = plt.xlabel('Iris petals (\'standards\') width (cm)')
_ = plt.ylabel('count')
bin_number = ' (bins=' + str((n_bins / 3)) + ')'
_ = plt.legend((target_names[0].capitalize() + bin_number , target_names[1].capitalize() + bin_number , target_names[2].capitalize() + bin_number ), loc='upper right')
# use axis={'both', 'x', 'y'} to choose axis
_ = plt.locator_params(axis="y", integer=True, tight=True)



# (E)CDF) of sepal lengths of the species
# ==[7]=======================================================================================================
figure_number = figure_number + 1
_ = plt.figure(figure_number, figsize=(8, 6))
_ = plt.clf()

# Compute ECDF for versicolor data: x_vers, y_vers
# x_iris, y_iris = ecdf(iris_sepal_length)
# ---------------------------------------------------
x_setosa_sepal_length, y_setosa_sepal_length = ecdf(setosa_sepal_length)
x_versicolor_sepal_length, y_versicolor_sepal_length = ecdf(versicolor_sepal_length)
x_virginica_sepal_length, y_virginica_sepal_length = ecdf(virginica_sepal_length)

# Generate plot
# _ = plt.plot(x_iris, y_iris, marker='.', linestyle='none')
# ---------------------------------------------------
_ = plt.title('(Empirical) Cumulative Distribution\nof Iris sepals (\'falls\') in three species')
_ = plt.plot(x_setosa_sepal_length, y_setosa_sepal_length, marker='.', linestyle='none', color='black')
_ = plt.plot(x_versicolor_sepal_length, y_versicolor_sepal_length, marker='.', linestyle='none', color='yellow')
_ = plt.plot(x_virginica_sepal_length, y_virginica_sepal_length, marker='.', linestyle='none', color='red')

# Label the axes
_ = plt.legend((legend_setosa, legend_versicolor, legend_virginica), loc='upper right')
_ = plt.xlabel('Iris sepals (\'falls\') length (cm)')
_ = plt.ylabel('ECDF')
_ = plt.locator_params(axis="both", integer=False, tight=True)



# (E)CDF) of sepal width of the species
# ==[8]=======================================================================================================
figure_number = figure_number + 1
_ = plt.figure(figure_number, figsize=(8, 6))
_ = plt.clf()

# Compute ECDF for versicolor data: x_vers, y_vers
# x_iris, y_iris = ecdf(iris_sepal_width)
# ---------------------------------------------------
x_setosa_sepal_width, y_setosa_sepal_width = ecdf(setosa_sepal_width)
x_versicolor_sepal_width, y_versicolor_sepal_width = ecdf(versicolor_sepal_width)
x_virginica_sepal_width, y_virginica_sepal_width = ecdf(virginica_sepal_width)

# Generate plot
# _ = plt.plot(x_iris, y_iris, marker='.', linestyle='none')
# ---------------------------------------------------
_ = plt.title('(Empirical) Cumulative Distribution\nof Iris sepals (\'falls\') in three species')
_ = plt.plot(x_setosa_sepal_width, y_setosa_sepal_width, marker='.', linestyle='none', color='black')
_ = plt.plot(x_versicolor_sepal_width, y_versicolor_sepal_width, marker='.', linestyle='none', color='yellow')
_ = plt.plot(x_virginica_sepal_width, y_virginica_sepal_width, marker='.', linestyle='none', color='red')

# Label the axes
_ = plt.legend((legend_setosa, legend_versicolor, legend_virginica), loc='upper right')
_ = plt.xlabel('Iris sepals (\'falls\') width (cm)')
_ = plt.ylabel('ECDF')
_ = plt.locator_params(axis="both", integer=False, tight=True)


# (E)CDF) of petal lengths of the species
# ==[9]=======================================================================================================
figure_number = figure_number + 1
_ = plt.figure(figure_number, figsize=(8, 6))
_ = plt.clf()

# Compute ECDF for versicolor data: x_vers, y_vers
# x_iris, y_iris = ecdf(iris_petal_length)
# ---------------------------------------------------
x_setosa_length, y_setosa_length = ecdf(setosa_petal_length)
x_versicolor_length, y_versicolor_length = ecdf(versicolor_petal_length)
x_virginica_length, y_virginica_length = ecdf(virginica_petal_length)

# Generate plot
# _ = plt.plot(x_iris, y_iris, marker='.', linestyle='none')
# ---------------------------------------------------
_ = plt.title('(Empirical) Cumulative Distribution\nof Iris petals (\'standards\') in three species')
_ = plt.plot(x_setosa_length, y_setosa_length, marker='.', linestyle='none', color='black')
_ = plt.plot(x_versicolor_length, y_versicolor_length, marker='.', linestyle='none', color='yellow')
_ = plt.plot(x_virginica_length, y_virginica_length, marker='.', linestyle='none', color='red')

# Label the axes
_ = plt.legend((legend_setosa, legend_versicolor, legend_virginica), loc='upper right')
_ = plt.xlabel('Iris petals (\'standards\') length (cm)')
_ = plt.ylabel('ECDF')
_ = plt.locator_params(axis="both", integer=False, tight=True)


# (E)CDF) of petal width of the species
# ==[10]=======================================================================================================
figure_number = figure_number + 1
_ = plt.figure(figure_number, figsize=(8, 6))
_ = plt.clf()

# Compute ECDF for versicolor data: x_vers, y_vers
# x_iris, y_iris = ecdf(iris_petal_width)
# ---------------------------------------------------
x_setosa_width, y_setosa_width = ecdf(setosa_petal_width)
x_versicolor_width, y_versicolor_width = ecdf(versicolor_petal_width)
x_virginica_width, y_virginica_width = ecdf(virginica_petal_width)

# Generate plot
# _ = plt.plot(x_iris, y_iris, marker='.', linestyle='none')
# ---------------------------------------------------
_ = plt.title('(Empirical) Cumulative Distribution\nof Iris petals (\'standards\') in three species')
_ = plt.plot(x_setosa_width, y_setosa_width, marker='.', linestyle='none', color='black')
_ = plt.plot(x_versicolor_width, y_versicolor_width, marker='.', linestyle='none', color='yellow')
_ = plt.plot(x_virginica_width, y_virginica_width, marker='.', linestyle='none', color='red')

# Label the axes
_ = plt.legend((legend_setosa, legend_versicolor, legend_virginica), loc='upper right')
_ = plt.xlabel('Iris petals (\'standards\') width (cm)')
_ = plt.ylabel('ECDF')
_ = plt.locator_params(axis="both", integer=False, tight=True)



# Principal Component Analysis (PCA)
# ==[11]===============================================================
# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
pca = PCA(n_components = 4).fit_transform(df_iris_data)
print('Principal Component Analysis:\r\n', pca)
# print(pca[:, 0], pca[:, 0:1])

fig = plt.figure(figure_number + 1, figsize = (8, 6))
ax = Axes3D(fig, elev = -150, azim = 110)

# ax.scatter(pca[:, 0], c = target,
#             cmap=plt.cm.get_cmap('Reds'), edgecolor='k', s=40)
# ax.scatter(pca[:, 0], pca[:, 1], c = target,
#             cmap=plt.cm.get_cmap('Reds'), edgecolor='k', s=40)
# ax.scatter(pca[:, 0], pca[:, 1], pca[:, 2], c = target,
#             cmap=plt.cm.get_cmap('Reds'), edgecolor='k', s=40)
ax.scatter(pca[:, 0], pca[:, 1], pca[:, 2], pca[:, 3], c = target,
            cmap=plt.cm.get_cmap('Reds'), edgecolor='k', s=40)

ax.set_title("Principal Component Analysis on Iris dataset")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])



# ==[PLOT]==========================================================
# Note: the  plots are printed on top of each other !!!
plt.show()
