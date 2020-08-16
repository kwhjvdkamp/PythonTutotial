import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.cm

# import seaborn as sns
import pandas as pd

from sklearn import datasets
# from sklearn.decomposition import PCA
# from mpl_toolkits.mplot3d import Axes3D

def iris():
    """Import Iris data sites"""

    # # Set default Seaborn style
    # sns.set()

    iris = datasets.load_iris()
    # print (iris)

    dataframe_keys = iris.keys()
    # print('dataframe_keys:\r\n', dataframe_keys)

    data = iris["data"][:, :4]

    target = iris["target"]
    # print('dataframe_key: \'target\':\r\n', target)

    target_names = iris["target_names"]
    # print('dataframe_key: \'target_names\':\r\n', target_names)

   df = pd.DataFrame(data, \
        columns = [ \
            "sepal length (cm)", \
            "sepal width (cm)", \
            "petal length (cm)", \
            "petal width (cm)" \
        ])
    # print('dataframe: \'df.head()\':\r\n', df.head())
    # print('dataframe: \'statistics\': ', df.describe())

    return iris