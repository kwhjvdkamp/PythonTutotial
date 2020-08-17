import numpy as np
import pandas as pd

from sklearn import datasets

def iris():
    """
    Import Iris dataset from scikit
    """

    iris = datasets.load_iris()
    # print (iris)

    dataframe_keys = iris.keys()
    # print('dataframe_keys:\r\n', dataframe_keys)

    data = iris["data"][:, :4]
    # print('dataframe_key: \'data\':\r\n', data)

    target = iris["target"]
    # print('dataframe_key: \'target\':\r\n', target)

    target_names = iris["target_names"]
    # print('dataframe_key: \'target_names\':\r\n', target_names)

    sepal_l = "sepal length (cm)"
    sepal_w = "sepal width (cm)"
    petal_l = "petal length (cm)"
    petal_w = "petal width (cm)"
    df = pd \
        .DataFrame(data, columns = [sepal_l, sepal_w, petal_l, petal_w])
    # print('dataframe: \'df.head()\':\r\n', df.head())
    # print('dataframe: \'statistics\': ', df.describe())

    return iris
