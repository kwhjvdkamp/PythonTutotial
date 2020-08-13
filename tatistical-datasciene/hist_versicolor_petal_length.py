# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn import datasets
# from sklearn.datasets import load_iris
iris = datasets.load_iris()

print (iris)

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
_ = plt.hist(iris)

# # Show histogram
plt.show()
