# Import required functions
from setuptools import find_packages, setup

#Example
# setup(
#       name="univariate_linear_regression",
#       version="0.1.0",
#       description="Univariate linear regression of housing price against housing area",
#       author="Dibya Chakravorty",
#       packages=find_packages("src"),
#       package_dir={"": "src"},
#       author_email="dibyachakravorty@gmail.com",
#       install_requires=["jupyter==1.0.0",
#                         "matplotlib==3.1.1",
#                         "numpy==1.17.3",
#                         "pytest==5.2.2",
#                         "pytest-mpl==0.10",
#                         "pytest-mock==1.11.2",
#                         "scipy==1.3.1",
#                         ],
#       )

setup(
    name="impyrial",
    version="0.1.0",
    description="Learning package - Conversions",
    author="Koen van der Kamp",
    packages=find_packages("src"),
    package_dir={"": "src"},
    author_email="info@van-der-kamp.nl",
    install_requires=[
        "jupyter==1.0.0",
        "matplotlib==3.1.1",
        "numpy==1.17.3",
        "pytest==5.2.2",
        "pytest-mpl==0.10",
        "pytest-mock==1.11.2",
        "scipy==1.3.1",
    ],
    python_requires='>=3.9.5',
)
