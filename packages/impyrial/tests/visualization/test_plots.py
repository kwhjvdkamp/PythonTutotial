import pytest
import numpy as np

from packages.impyrial.src.visualization.plots import get_plot_for_best_fit_line

class TestGetPlotForBestFitLine(object):
    # Add the pytest marker which generates baselines and compares images
    # ____
    def test_plot_for_almost_linear_data(self):
        slope = 5.0
        intercept = -2.0
        x_array = np.array([1.0, 2.0, 3.0])
        y_array = np.array([3.0, 8.0, 11.0])
        title = "Test plot for almost linear data"
        # Return the matplotlib figure returned by the function under test
        # ____ ____(slope, intercept, x_array, y_array, title)