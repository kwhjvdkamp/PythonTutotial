# Downloading the csv file from CSSE

import os
import pandas as pd
from pandas.core import indexing
import requests
import io

class Csse:

    def __init__(self):

        # Make sure the url is the raw version of the file on GitHub

        # Note:
        # In case an image needs to be retrieved from GitHub
        # add '?raw=true' at the end of the link to the file

        # URL_PATH = 'REPLACE-ME WITH RAW-VERSION-URL-TO-THE-CSV-FILE'

        # https://github.com/kwhjvdkamp/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/
        # time_series_covid19_confirmed_global.csv
        # time_series_covid19_deaths_global.csv
        # time_series_covid19_recovered_global.csv


        # URL_PATH = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series'

        URL_PATH = 'https://raw.github.com/kwhjvdkamp/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'

        # f-strings provide a way to embed expressions inside string literals,
        # using a minimal syntax. It should be noted that an f-string is really an expression
        # evaluated at run time, not a constant value.
        # In Python source code, an f-string is a literal string, prefixed with 'f',
        # which contains expressions inside braces. The expressions are replaced with their values.
        self.URLS = {
            'confirmed': f'{URL_PATH}/time_series_covid19_confirmed_global.csv',
            'deaths': f'{URL_PATH}/time_series_covid19_deaths_global.csv',
            'recovered':f'{URL_PATH}/time_series_covid19_recovered_global.csv',
        }

        self.data = {case:pd.read_csv(url, header=0, escapechar='\\') for case, url in self.URLS.items()}

    # create other useful functions to work with data
    def current_status(self):
        # function to show current status
        pass



# =============================================================
# Returns data as dictionary with DataFrames as Values
csse = Csse()

# print(csse.current_status())

# Keys of the dictionary
print(csse.data.keys())

# pivoting columns to rows and vice versa
confirmed_df = csse.data['confirmed']

date_columns = confirmed_df.iloc[:, 4:].columns
print('X', date_columns)
# confirmed_df = confirmed_df.melt(id_vars=date_columns)
# confirmed_df = confirmed_df.pivot(index = date_columns, columns = 'Country/region', values = confirmed_df.iloc[:, 4:].values)
# print('X', confirmed_df)

# confirmed_df.melt(id_vars=date_columns)



# .pivot(index='1/22/20')
deaths_df = csse.data['deaths']
# .pivot('repeat_id', 'gtex_id', 'norm_exp')
recovered_df = csse.data['recovered']
# .pivot('repeat_id', 'gtex_id', 'norm_exp')


# Save dataframes to csv
# TODO add if exist overwrite
path_lt=r'C:\HomeProjects\COVID-19-Data\csse-data'

path_dt=r'C:\GitHubRepositories\COVID-19-Data\csse-data'

# ==================

confirmed_df.to_csv(os.path.join(path_lt, r'csse_confirmed.csv'))
# First five rows
print(confirmed_df.head())
# Last five rows
print(confirmed_df.tail())

# ==================

deaths_df.to_csv(os.path.join(path_lt, r'csse_deaths.csv'))
# First five rows
print(deaths_df.head())
# Last five rows
print(deaths_df.tail())

# ==================

recovered_df.to_csv(os.path.join(path_lt, r'csse_recovered.csv'))
# First five rows
print(recovered_df.head())
# Last five rows
print(recovered_df.tail())

# ==================

# with open(os.path.join(path, r'csse_confirmed.csv'), 'w+') as f:
#     f.write(r'csse_confirmed.csv')
