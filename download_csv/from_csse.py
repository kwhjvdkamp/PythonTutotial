# Downloading the csv file from CSSE

import os
import pathlib
import pandas as pd
import requests
import io

from datetime import datetime
from pandas.core import indexing
from typing import Union


def convertToWindowsPath(string: Union[str, pathlib.Path]):
    # This converts a str to a Path (if already a Path, nothing changes)
    path = pathlib.Path(string)
    # print(type(path))
    # print(path)
    return path


class Csse:

    def __init__(self):

        # =============================================================
        # Returns data as dictionary with DataFrames as Values
        # Make sure the url is the raw version of the file on GitHub
        # Note:
        # In case an image needs to be retrieved from GitHub
        # add '?raw=true' at the end of the link to the file

        # Dataframe forked from 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master

        URL_PATH = 'https://raw.github.com/kwhjvdkamp/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'

        # f-strings provide a way to embed expressions inside string literals using a minimal syntax.
        # It should be noted that an f-string is really an expression evaluated at run time, not a constant value.
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


# =========================================================================================


# Original data contains dates formatted like m/d/jj (no preceding zero's and two digit year)
format_str = '%m/%d/%y' # The original date format

csse = Csse()

# Keys of the dictionary
print(csse.data.keys())

# Pivoting columns to rows
confirmedDf = csse.data['Confirmed']
# dateColumnConfirmed = confirmedDf.iloc[:, 4:].columns
# isoDateColumnConfirmed = pd.to_datetime(dateColumnConfirmed).strftime('%Y-%m-%d')
# print('isoDateColumnConfirmed', type(isoDateColumnConfirmed), isoDateColumnConfirmed)
confirmedDfWideToLong = pd.melt(confirmedDf,
                            id_vars=confirmedDf.columns[:4],
                            value_vars = confirmedDf.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Confirmed')
# inplace=True means the original dataframe is changed
# confirmedDfWideToLong.sort_values(by=['Country/Region', 'Updated'], inplace=true)
confirmedDfWideToLong = confirmedDfWideToLong.sort_values(by=['Country/Region', 'Updated'])
dictConfirmed = {
    'Date': pd.to_datetime(confirmedDfWideToLong['Updated'], format=format_str),
    'Province_State': confirmedDfWideToLong['Province/State'],
    'Country_Region': confirmedDfWideToLong['Country/Region'],
    'Latitude': confirmedDfWideToLong['Lat'],
    'Longitude': confirmedDfWideToLong['Long'],
    'Confirmed': confirmedDfWideToLong['Confirmed']
}
dfConfirmed = pd.DataFrame(dictConfirmed)
print(dfConfirmed.keys())
dfConfirmed.sort_values(by=['Date'])
# print('After Melting\r\nDate converted to isoDate as part of new compilated Dataframe\r\n', dfConfirmed)


# print('==================================================')


deceasedDf = csse.data['Deceased']
# dateColumnsDeceased = deceasedDf.iloc[:, 4:].columns
deceasedDfWideToLong = pd.melt(deceasedDf,
                            id_vars=deceasedDf.columns[:4],
                            value_vars = deceasedDf.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Deceased')
deceasedDfWideToLong.sort_values(by=['Country/Region', 'Updated'], inplace=True)
dictDeceased = {
    'Date': pd.to_datetime(deceasedDfWideToLong['Updated'], format=format_str),
    'Province_State': deceasedDfWideToLong['Province/State'],
    'Country_Region': deceasedDfWideToLong['Country/Region'],
    'Latitude': deceasedDfWideToLong['Lat'],
    'Longitude': deceasedDfWideToLong['Long'],
    'Deceased': deceasedDfWideToLong['Deceased']
}
dfDeceased = pd.DataFrame(dictDeceased)
print(dfDeceased.keys())
dfDeceased.sort_values(by=['Date'])
# print('After Melting\r\nDate converted to isoDate as part of new compilated Dataframe\r\n', dfDeceased)


# print('==================================================')


recoveredDf = csse.data['Recovered']
dateColumnsRecovered = recoveredDf.iloc[:, 4:].columns
recoveredDfWideToLong = pd.melt(recoveredDf,
                            id_vars=recoveredDf.columns[:4],
                            value_vars = recoveredDf.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Recovered')
recoveredDfWideToLong.sort_values(by=['Country/Region', 'Updated'], inplace=True)
dictRecovered = {
    'Date': pd.to_datetime(recoveredDfWideToLong['Updated'], format=format_str),
    'Province_State': recoveredDfWideToLong['Province/State'],
    'Country_Region': recoveredDfWideToLong['Country/Region'],
    'Latitude': recoveredDfWideToLong['Lat'],
    'Longitude': recoveredDfWideToLong['Long'],
    'Recovered': recoveredDfWideToLong['Recovered']
}
dfRecovered = pd.DataFrame(dictRecovered)
print(dfRecovered.keys())
dfRecovered.sort_values(by=['Date'])
# print('After Melting\r\nDate converted to isoDate as part of new compilated Dataframe\r\n', dfRecovered)


# print('==================================================')


currentContainer = pathlib.Path(__file__).parent.absolute()
path = str(currentContainer)

pathToWriteTo = ''
# current working folder
if path.__contains__('HomeProjects'):
    # On Laptop write to >>> C:\HomeProjects\COVID-19-Data\bing-data\accumulation\csv-data-bing
    pathToWriteTo = convertToWindowsPath(path.replace('Python\PythonTutorial\download_csv', 'COVID-19-Data\\csse-data\\'))
    print('Laptop:', pathToWriteTo)
elif path.__contains__('GitHubRepositories'):
    # On Desktop write to >>> C:\GithubRepositories\COVID-19-Data\bing-data\accumulation\csv-data-bing
    pathToWriteTo = convertToWindowsPath(path.replace('PythonTutorial\download_csv', 'COVID-19-Data\\csse-data\\'))
    print('Desktop:', pathToWriteTo)
else:
    print('Wrong:', path)

dfConfirmed.to_csv(os.path.join(pathToWriteTo, r'csse_confirmed.csv'))
print('C', dfConfirmed.head())
print('C', dfConfirmed.tail())

dfDeceased.to_csv(os.path.join(pathToWriteTo, r'csse_deceased.csv'))
print('D', dfDeceased.head())
print('D', dfDeceased.tail())

dfRecovered.to_csv(os.path.join(pathToWriteTo, r'csse_recovered.csv'))
print('R', dfRecovered.head())
print('R', dfRecovered.tail())
