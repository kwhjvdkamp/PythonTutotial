# Import required functions
from setuptools import find_packages, setup

# Call setup function
setup(
    author="Koen van der Kamp",
    description="Learning package - Conversions",
    name="impyrial",
    packages=find_packages(include=['impyrial', 'impyrial.*']),
    version="0.1.0",
    install_requires=['pandas', 'scipy', 'matplotlib'],
    python_requires='>=3.9.5',
)
