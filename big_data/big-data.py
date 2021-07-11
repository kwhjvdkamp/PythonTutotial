import psutil, os
import numpy as np
import pandas as pd
from math import sqrt
from dask import delayed


def memory_footprint():
    '''Returns memory (in MB) being used by Python process'''
    mem = psutil.Process(os.getpid()).memory_info().rss
    return (mem / 1024 ** 2)

before = memory_footprint()
# Number of floats that fill 1 MB
N = (1024 ** 2) // 8
# Random array filling 50 MB
x = np.random.randn(50*N)
after = memory_footprint()

print('Memory before: {} MB'.format(before))
print('Memory after: {} MB'.format(after))



# def filter_is_long_trip(data):
#     "Returns DataFrame filtering trips longer than 20 mins"
#     is_long_trip = (data.trip_time_in_secs > 1200)
#     return data.loc[is_long_trip]

# filename = 'NYC_taxi_2013_01.csv'
# List Comprehension
# chunks = [filter_is_long_trip(chunk) for chunk in pd.read_csv(filename, chunksize=1000)]
# Generators
# chunks = (filter_is_long_trip(chunk) for chunk in pd.read_csv(filename, chunksize=1000))



# NOTE in a list comprehesion, if the enclosing brackets are replaced with parenthesis,
# than the result is a generator expression,
# generator expression resemble list comprehension but the they use lazy evaluation
# > meaning handle one at the time



def f(z):
    return sqrt(z + 4)

def g(y):
    return y - 3

def h(x):
    return x ** 2

x = 4
y = h(x)
z = g(y)
w = f(z)
print('x = 4 >>\r\n  \
y = h(x) |>| y = h( x = [',x,'] ** 2 )','=', y,' >>\r\n '\
, 'z = g(y) |>| z = g( y = [',y,'] - 3 )','=', z, ' >>\r\n '\
, 'w = f(z) |>| w = f( z = [ sqrt(',z,') ] + 4 )', ' = ', w, ' is equal to f(g(h(x))) = ', f(g(h(x))) \
, ' mapping an input function ')