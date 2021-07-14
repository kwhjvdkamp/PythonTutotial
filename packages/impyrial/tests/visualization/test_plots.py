import pytest
import numpy as np

from packages.impyrial.src.visualization.plots import get_plot_for_best_fit_line

class TestGetPlotForBestFitLine(object):

    """
    The best fit line that the test will draw follows the equation: y = 5x - 2.
    Two points, (1.0, 3.0) and (2.0, 8.0) will fall on the line. The point (3.0, 11.0) won't.
    """
    # Add the pytest marker which generates baselines and compares images
    @pytest.mark.mpl_image_compare # Under the hood baseline generation and comparison
    def test_plot_for_almost_linear_data(self):
        slope = 5.0
        intercept = -2.0
        x_array = np.array([1.0, 2.0, 3.0])
        y_array = np.array([3.0, 8.0, 11.0])
        title = "Test plot for almost linear data"
        # Return the matplotlib figure returned by the function under test
        return get_plot_for_best_fit_line(slope, intercept, x_array, y_array, title)