# Import learning dataset from scikit-learn.org
from def_iris import iris

# (E)CDF (Empirical) Cumulative Distribution Function
from def_ecdf import ecdf

# # Compute ECDF for versicolor data: x_vers, y_vers
# x_vers, y_vers = ecdf(versicolor_petal_length)

# # Generate plot
# _ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')

# # Label the axes
# _ = plt.xlabel('species')
# _ = plt.ylabel('ECDF')

# # Display the plot
# plt.show()
