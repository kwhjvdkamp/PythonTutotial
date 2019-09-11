from setuptools import setup

setup(name='kwhj',
    version='0.0.1',
    description='First Package.',
    author='K.W.H.J. van der Kamp',
    author_email='info@van-der-kamp.nl',
    packages=['kwhj'],
    install_requires=['collections',
        'numpy==1.15.4',
        'pycodestyle>=2.4.0'])