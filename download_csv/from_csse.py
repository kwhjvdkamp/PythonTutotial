# //type: ignore
# ========================================================
# Above line tells Pylance to ignore this file
# > At the top of the file to ignore the file
# > At the end of a line to ignore the line
# ========================================================

# Downloading the csv file from CSSE
print('__file__={0:<35} \r\n__name__={1:<20} \r\n__package__={2:<20}'.format(__file__,__name__,str(__package__)))

import os
import pathlib
import pandas as pd
import requests
import io

# Third party modules
from datetime import datetime
from pandas.core import indexing
from typing import Match, Union

# Local module(s)
from isoCountryCodes import CountryCodes

# Converting a string to a Path-typed structure (if already a Path, nothing changes)
def convertToWindowsPath(string: Union[str, pathlib.Path]):
    path = pathlib.Path(string)
    return path

# Definition to retrieve Alpha-2 and -3 (Iso 3661) codes from
# country-specific objects like {'Country': {'Iso2': 'CC', 'Iso3', 'CCC'}, ...}
# which resides in a local static json-like structure in 'isoCountryCodes.py'
def getIsoCodeForCountry(arrayCountryNames, iso):
    codes = []
    # noCodesForCountry = []
    for countryName in arrayCountryNames:
        pair = mapIsoCodesOnCountryName(countryName)
        # 'None' equivalent to 'null'
        if pair != None:
            # ...either 'Iso2' or 'Iso3'
            isoCode = pair[iso]
            codes.append(isoCode)
        else:
            # Missing codes
            # if item not in noCodesForCountry:
            #     noCodesForCountry.append(item)

            if iso == 'Iso2':
                codes.append('--')
            else:
                codes.append('---')

            # On Python version 3.10 and up it will be possible
            # match iso
            #     case 'Iso2':
            #         codes.append('--')
            #     case 'Iso3':
            #         codes.append('---')

    # print(noCodesForCountry)
    return codes


# Definition to iterate over the CountryCodes Json-structure
# {'Country': {'Iso2': 'CC', 'Iso3', 'CCC'}, ...}
# to return the iso codes object for a certain country name
def mapIsoCodesOnCountryName(countryName):
    for key, value in CountryCodes.items():
        if (key == countryName):
            return value


# Reading the data for the Covid-19 repository which itself has been
# forked from the publicly accessible CSSEGISandDATA repository supplied by JHU US
class Csse:

    def __init__(self):

        # =============================================================
        # Returns data as dictionary with DataFrames as Values
        # Make sure the url is the raw version of the file on GitHub
        # Note:
        # In case an image needs to be retrieved from GitHub
        # add '?raw=true' at the end of the link to the file

        # Dataframe forked
        # from 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master
        # into 'https://raw.github.com/kwhjvdkamp/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'

        URL_PATH = 'https://raw.github.com/kwhjvdkamp/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'

        # 'f-strings' provide a way to embed expressions inside string literals using a minimal syntax.
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


# private variables
# Original data contains dates formatted like 'm/d/jj' meaning a) no preceding zero's and b) two digit year
# conversion to Iso date 'YYYY-MM-DD' format is mandatory
format_str = '%m/%d/%y' # The original date format

# Calling class
csse = Csse()
# Keys of the dictionary
# print(csse.data.keys())

# print('==Confirmed=======================================')
dfConfirmed = csse.data['Confirmed']
# Pivoting 'Confirmed'-dataframe columns to rows
transposedDfConfirmed = pd.melt(dfConfirmed,
                            id_vars=dfConfirmed.columns[:4],
                            value_vars = dfConfirmed.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Confirmed')
# Extending and Sorting transposed 'Confirmed'-dataframe
countryNamesConfirmed = transposedDfConfirmed['Country/Region'].values
dictConfirmed = {
    'Date': pd.to_datetime(transposedDfConfirmed['Updated'], format=format_str),
    'Province_State': transposedDfConfirmed['Province/State'],
    'Country_Region': transposedDfConfirmed['Country/Region'],
    'Latitude': transposedDfConfirmed['Lat'],
    'Longitude': transposedDfConfirmed['Long'],
    'ISO2': getIsoCodeForCountry(countryNamesConfirmed, 'Iso2'),
    'ISO3' : getIsoCodeForCountry(countryNamesConfirmed, 'Iso3'),
    'Confirmed': transposedDfConfirmed['Confirmed']
}
dfConfirmed = pd.DataFrame(dictConfirmed)
dfConfirmed.sort_values(by=['Country_Region', 'Date'])
dfConfirmed.sort_values(by=['Date'])

# print('==Deceased========================================')
dfDeceased = csse.data['Deceased']
# Pivoting 'Deceased'-dataframe columns to rows
transposedDfDeceased = pd.melt(dfDeceased,
                            id_vars=dfDeceased.columns[:4],
                            value_vars = dfDeceased.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Deceased')
# Extending and Sorting transposed 'Deceased'-dataframe
countryNamesDeceased = transposedDfDeceased['Country/Region'].values
dictDeceased = {
    'Date': pd.to_datetime(transposedDfDeceased['Updated'], format=format_str),
    'Province_State': transposedDfDeceased['Province/State'],
    'Country_Region': transposedDfDeceased['Country/Region'],
    'Latitude': transposedDfDeceased['Lat'],
    'Longitude': transposedDfDeceased['Long'],
    'ISO2': getIsoCodeForCountry(countryNamesDeceased, 'Iso2'),
    'ISO3' : getIsoCodeForCountry(countryNamesDeceased, 'Iso3'),
    'Deceased': transposedDfDeceased['Deceased']
}
dfDeceased = pd.DataFrame(dictDeceased)
dfDeceased.sort_values(by=['Country_Region', 'Date'])
dfDeceased.sort_values(by=['Date'])

# print('==Recovered=======================================')
dfRecovered = csse.data['Recovered']
# Pivoting 'Recovered'-dataframe columns to rows
transposedDfRecovered = pd.melt(dfRecovered,
                            id_vars=dfRecovered.columns[:4],
                            value_vars = dfRecovered.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Recovered')
# Extending and Sorting transposed 'Recovered'-dataframe
countryNamesRecovered = transposedDfRecovered['Country/Region'].values
dictRecovered = {
    'Date': pd.to_datetime(transposedDfRecovered['Updated'], format=format_str),
    'Province_State': transposedDfRecovered['Province/State'],
    'Country_Region': transposedDfRecovered['Country/Region'],
    'Latitude': transposedDfRecovered['Lat'],
    'Longitude': transposedDfRecovered['Long'],
    'ISO2': getIsoCodeForCountry(countryNamesRecovered, 'Iso2'),
    'ISO3' : getIsoCodeForCountry(countryNamesRecovered, 'Iso3'),
    'Recovered': transposedDfRecovered['Recovered']
}
dfRecovered = pd.DataFrame(dictRecovered)
dfRecovered.sort_values(by=['Country_Region', 'Date'])
dfRecovered.sort_values(by=['Date'])

print('==================================================')
print('\r\nConfirmed')
print(dfConfirmed.head())
print(dfConfirmed.tail())
print('==================================================')
print('\r\nDeceased')
print(dfDeceased.head())
print(dfDeceased.tail())
print('==================================================')
print('\r\nRecovered')
print(dfRecovered.head())
print(dfRecovered.tail())
print('==================================================')

doWrite = False
if doWrite:

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
    dfDeceased.to_csv(os.path.join(pathToWriteTo, r'csse_deceased.csv'))
    dfRecovered.to_csv(os.path.join(pathToWriteTo, r'csse_recovered.csv'))

else:
    print('File writing switched off')
