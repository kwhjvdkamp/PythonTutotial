import psutil, os
# os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
import numpy as np
import pandas as pd
from math import sqrt
from dask import delayed
from graphviz import Digraph


# def memory_footprint():
#     '''Returns memory (in MB) being used by Python process'''
#     mem = psutil.Process(os.getpid()).memory_info().rss
#     return (mem / 1024 ** 2)

# before = memory_footprint()
# # Number of floats that fill 1 MB
# N = (1024 ** 2) // 8
# # Random array filling 50 MB
# x = np.random.randn(50*N)
# after = memory_footprint()

# print('Memory before: {} MB'.format(before))
# print('Memory after: {} MB'.format(after))


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
, 'w = f(z) |>| w = f( z = [ sqrt(',z,') ] + 4 )', ' = ', w\
, ' is equal to f(g(h(x))) = ', f(g(h(x))))

# functions are deferred until the compute method is called (one after each other)
# because dask scheduler manage memory usage
y = delayed(h)(x)
z = delayed(g)(y)
w = delayed(f)(z)
print(w, ', type(w):',type(w),'\r\n')
im = w.visualize()
# print(w.visualize())
# 'wb' flag indicates that the file is opened for writing in binary mode
open('big_data/visualizations/first_dask.png', 'wb').write(im.data)
# Some object is generated, but how to get a picture out of it. I don't know yet!


# Using dask.delayed, we don't need to use generators


# # Define count_flights
# @delayed
# def count_flights(df):
#     return len(df)

# # Define count_delayed
# @delayed
# def count_delayed(df):
#     return (df['DEP_DELAY']>0).sum()

# # Define pct_delayed
# @delayed
# def pct_delayed(n_delayed,n_flights):
#     return 100 * sum(n_delayed) / sum(n_flights)

# # print(filenames)
# # NOTE: these files are NOT on my local system, they, if necessary, can be downloaded from https://www.transtats.bts.gov/
# filenames = [
#     'flightdelays-2016-1.csv'
#     , 'flightdelays-2016-2.csv'
#     , 'flightdelays-2016-3.csv'
#     , 'flightdelays-2016-4.csv'
#     , 'flightdelays-2016-5.csv'
#     , 'flightdelays-2016-6.csv'
#     , 'flightdelays-2016-7.csv'
#     , 'flightdelays-2016-8.csv'
#     , 'flightdelays-2016-9.csv'
#     , 'flightdelays-2016-10.csv'
#     , 'flightdelays-2016-11.csv'
#     , 'flightdelays-2016-12.csv'
# ]
# n_delayed = []
# n_flights = []
# # Loop over the provided filenames list and call read_one: df
# for file in filenames:
#     df = pd.read_csv(file)  # <==> df = read_one(file)
#     # Append to n_delayed and n_flights
#     n_delayed.append(count_delayed(df))
#     n_flights.append(count_flights(df))

# # Call pct_delayed with n_delayed and n_flights: result
# result = pct_delayed(n_delayed,n_flights)

# # Print the output of result.compute()
# print(result.compute())
# # OUTPUT 34.199953360948875
