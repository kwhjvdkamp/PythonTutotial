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
            'Confirmed': f'{URL_PATH}/time_series_covid19_confirmed_global.csv',
            'Deceased': f'{URL_PATH}/time_series_covid19_deaths_global.csv',
            'Recovered':f'{URL_PATH}/time_series_covid19_recovered_global.csv',
        }

        self.data = {case:pd.read_csv(url, header=0, escapechar='\\') for case, url in self.URLS.items()}

    # create other useful functions to work with data
    def current_status(self):
        # function to show current status
        pass



# =============================================================
# Returns data as dictionary with DataFrames as Values
csse = Csse()

# print(csse.current_status)

# print(csse.current_status())

# Keys of the dictionary
print(csse.data.keys())

# pivoting columns to rows
confirmedDf = csse.data['Confirmed']
dateColumnsConfirmed = confirmedDf.iloc[:, 4:].columns
confirmedDfWideToLong = pd.melt(confirmedDf,
                            id_vars=confirmedDf.columns[:4],
                            value_vars = confirmedDf.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Confirmed')

deceasedDf = csse.data['Deceased']
dateColumnsDeceased = deceasedDf.iloc[:, 4:].columns
confirmedDfWideToLong = pd.melt(deceasedDf,
                            id_vars=deceasedDf.columns[:4],
                            value_vars = deceasedDf.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Deceased')

recoveredDf = csse.data['Recovered']
dateColumnsRecovered = recoveredDf.iloc[:, 4:].columns
recoveredDfWideToLong = pd.melt(recoveredDf,
                            id_vars=recoveredDf.columns[:4],
                            value_vars = recoveredDf.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Recovered')


# Save dataframes to csv
# TODO add if exist overwrite
pathLt=r'C:\HomeProjects\COVID-19-Data\csse-data'

pathDt=r'C:\GitHubRepositories\COVID-19-Data\csse-data'

# ==================

recoveredDfWideToLong.to_csv(os.path.join(pathLt, r'csse_confirmed.csv'))
# First five rows
print('C', recoveredDfWideToLong.head())
# Last five rows
print('C', recoveredDfWideToLong.tail())

# ==================

confirmedDfWideToLong.to_csv(os.path.join(pathLt, r'csse_deceased.csv'))
# First five rows
print('D', confirmedDfWideToLong.head())
# Last five rows
print('D', confirmedDfWideToLong.tail())

# ==================

recoveredDfWideToLong.to_csv(os.path.join(pathLt, r'csse_recovered.csv'))
# First five rows
print('R', recoveredDfWideToLong.head())
# Last five rows
print('R', recoveredDfWideToLong.tail())

# ==================
