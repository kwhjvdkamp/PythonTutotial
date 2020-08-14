import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import pandas as pd

 # import some data to play with
# https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html#sphx-glr-auto-examples-datasets-plot-iris-dataset-py
from sklearn import datasets
from sklearn.decomposition import PCA

def iris():
    """Import Iris data sites"""

    # Set default Seaborn style
    sns.set()

    iris = datasets.load_iris()
    # print (iris)
    # output: the complete dataframe

    # get the key names of the dataframe
    dataframe_keys = iris.keys()
    # print('dataframe_keys:\r\n', dataframe_keys)
    # OUTPUT: dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])

    # retrieve 'data': petal (kelkblad) length of three species iris flower
    data = iris["data"][:, :4]
    # print('dataframe_key: \'data\':\r\n', data)
    # # OUTPUT: all rows according [:,<column(s)>] and the first three columns according [<row(s)>, :3]
    # NOTE ['<row(s)>','<column(s)>']

    # retrieve 'target': list 0, 1, 2 same length as data rows
    target = iris["target"]
    # print('dataframe_key: \'target\':\r\n', target)

    # retrieve 'target_names': species names (actually column names)
    target_names = iris["target_names"]
    # print('dataframe_key: \'target_names\':\r\n', target_names)

    # subtract dataframe 'df'
    # columns = iris[["sepal length (cm)"], ["sepal width in cm"], ["petal length in cm"], ["petal width in cm"]]
    df = pd.DataFrame(data, columns = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"])
    # print('dataframe: \'df.head()\':\r\n', df.head())
    # print('dataframe: \'statistics\': ', df.describe())

    return iris