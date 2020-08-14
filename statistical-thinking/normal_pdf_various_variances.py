# The Normal PDF
# In this exercise, you will explore the Normal PDF and also learn a way
# to plot a PDF of a known distribution using hacker statistics.
# Specifically, you will plot a Normal PDF for various values of the variance.
import array
import numpy as np
import matplotlib.pyplot as plt

# Draw 100000 samples from a Normal distribution with standars
# of interest: samples_std1, samples_std3, samples_std10
samples_std1 = np.random.normal(20, 1, size=100000)
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 = np.random.normal(20, 10, size=100000)

# In a histogram, the total range of data set (i.e from minimum value to maximum value)
# is divided into 8 to 15 equal parts. These equal parts are known as bins or class intervals.
bins_std1 = np.arange(0, max(samples_std1) + 1.5) - 0.5
bins_std3 = np.arange(0, max(samples_std3) + 1.5) - 0.5
bins_std10 = np.arange(0, max(samples_std10) + 1.5) - 0.5

# Make histograms
plt.hist(samples_std1, density=True, histtype='step', bins=bins_std1)
plt.hist(samples_std3, density=True, histtype='step', bins=bins_std1)
plt.hist(samples_std10, density=True, histtype='step', bins=bins_std1)

_ = plt.title('Normal PDF plot for various values of the variance')
_ = plt.xlabel('X (std)')
_ = plt.ylabel('Y (probability)')

# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()
