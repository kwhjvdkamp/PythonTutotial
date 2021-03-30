# type: ignore
# ========================================================
# Above line tells Pylance to ignore particular file?
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

# local modules
from isoCountryCodes import CC


from datetime import datetime
from pandas.core import indexing
from typing import Union

print("Count {0}".format(len(CC)))

def convertToWindowsPath(string: Union[str, pathlib.Path]):
    # This converts a str to a Path (if already a Path, nothing changes)
    path = pathlib.Path(string)
    # print(type(path))
    # print(path)
    return path


def columnIterator(column):
    for item in column:
        getIsoCodeKeyForCountryValue(item)
    return item

# function to return key for any value
def getIsoCodeKeyForCountryValue(val):
    for key, value in CC.items():
        if str(val).upper() == value:
            return key
    return "IsoCode for doesn't exist"


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

# print(getIsoCodeKeyForCountryValue("NETHERLANDS"))

# Original data contains dates formatted like m/d/jj (no preceding zero's and two digit year)
format_str = '%m/%d/%y' # The original date format

csse = Csse()

# Keys of the dictionary
print(csse.data.keys())

# Pivoting columns to rows
confirmedDf = csse.data['Confirmed']
confirmedDfWideToLong = pd.melt(confirmedDf,
                            id_vars=confirmedDf.columns[:4],
                            value_vars = confirmedDf.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Confirmed')

print('Dataframe Column \'Country/Region\'', confirmedDf['Country/Region'])

confirmedDfWideToLong['IsoCode'] = confirmedDfWideToLong['Country/Region']
print('Dataframe confirmedDfWideToLong[\'IsoCode\']\r\n', columnIterator([confirmedDfWideToLong['IsoCode']]) )

print('+++++')

dictConfirmed = {
    'Date': pd.to_datetime(confirmedDfWideToLong['Updated'], format=format_str),
    'Province_State': confirmedDfWideToLong['Province/State'],
    'Country_Region': confirmedDfWideToLong['Country/Region'],
    'Latitude': confirmedDfWideToLong['Lat'],
    'Longitude': confirmedDfWideToLong['Long'],
    # 'ISO': getIsoCodeKeyForCountryValue([confirmedDfWideToLong['IsoCode']]),
    'Confirmed': confirmedDfWideToLong['Confirmed']
}
dfConfirmed = pd.DataFrame(dictConfirmed)
dfConfirmed = dfConfirmed.sort_values(by=['Country_Region', 'Date'])
print('AFTER SORTING dfConfirmed', dfConfirmed)
dfConfirmed.sort_values(by=['Date'])
print('After Melting\r\nDate converted to isoDate as part of new compilated Dataframe\r\n', dfConfirmed)

# # print('==================================================')

# deceasedDf = csse.data['Deceased']
# deceasedDfWideToLong = pd.melt(deceasedDf,
#                             id_vars=deceasedDf.columns[:4],
#                             value_vars = deceasedDf.columns[4:],
#                             var_name = 'Updated',
#                             value_name = 'Deceased')
# dictDeceased = {
#     'Date': pd.to_datetime(deceasedDfWideToLong['Updated'], format=format_str),
#     'Province_State': deceasedDfWideToLong['Province/State'],
#     'Country_Region': deceasedDfWideToLong['Country/Region'],
#     'Latitude': deceasedDfWideToLong['Lat'],
#     'Longitude': deceasedDfWideToLong['Long'],
#     'Deceased': deceasedDfWideToLong['Deceased']
# }
# dfDeceased = pd.DataFrame(dictDeceased)
# dfDeceased = dfDeceased.sort_values(by=['Country_Region', 'Date'])
# print('AFTER SORTING dfDeceased', dfDeceased)
# dfDeceased.sort_values(by=['Date'])
# # print('After Melting\r\nDate converted to isoDate as part of new compilated Dataframe\r\n', dfDeceased)

# # print('==================================================')

# recoveredDf = csse.data['Recovered']
# recoveredDfWideToLong = pd.melt(recoveredDf,
#                             id_vars=recoveredDf.columns[:4],
#                             value_vars = recoveredDf.columns[4:],
#                             var_name = 'Updated',
#                             value_name = 'Recovered')
# dictRecovered = {
#     'Date': pd.to_datetime(recoveredDfWideToLong['Updated'], format=format_str),
#     'Province_State': recoveredDfWideToLong['Province/State'],
#     'Country_Region': recoveredDfWideToLong['Country/Region'],
#     'Latitude': recoveredDfWideToLong['Lat'],
#     'Longitude': recoveredDfWideToLong['Long'],
#     'Recovered': recoveredDfWideToLong['Recovered']
# }
# dfRecovered = pd.DataFrame(dictRecovered)
# dfRecovered = dfRecovered.sort_values(by=['Country_Region', 'Date'])
# print('AFTER SORTING dfRecovered', dfRecovered)
# dfRecovered.sort_values(by=['Date'])
# # print('After Melting\r\nDate converted to isoDate as part of new compilated Dataframe\r\n', dfRecovered)

# # print('==================================================')

# print('C', dfConfirmed.head())
# print('C', dfConfirmed.tail())

# print('D', dfDeceased.head())
# print('D', dfDeceased.tail())

# print('R', dfRecovered.head())
# print('R', dfRecovered.tail())

# # print('==================================================')

# doWrite = False
# if doWrite:

#     currentContainer = pathlib.Path(__file__).parent.absolute()
#     path = str(currentContainer)

#     pathToWriteTo = ''
#     # current working folder
#     if path.__contains__('HomeProjects'):
#         # On Laptop write to >>> C:\HomeProjects\COVID-19-Data\bing-data\accumulation\csv-data-bing
#         pathToWriteTo = convertToWindowsPath(path.replace('Python\PythonTutorial\download_csv', 'COVID-19-Data\\csse-data\\'))
#         print('Laptop:', pathToWriteTo)
#     elif path.__contains__('GitHubRepositories'):
#         # On Desktop write to >>> C:\GithubRepositories\COVID-19-Data\bing-data\accumulation\csv-data-bing
#         pathToWriteTo = convertToWindowsPath(path.replace('PythonTutorial\download_csv', 'COVID-19-Data\\csse-data\\'))
#         print('Desktop:', pathToWriteTo)
#     else:
#         print('Wrong:', path)

#     dfConfirmed.to_csv(os.path.join(pathToWriteTo, r'csse_confirmed.csv'))
#     dfDeceased.to_csv(os.path.join(pathToWriteTo, r'csse_deceased.csv'))
#     dfRecovered.to_csv(os.path.join(pathToWriteTo, r'csse_recovered.csv'))

# else:
#     print('\r\n=====================\r\nNo file writing')
