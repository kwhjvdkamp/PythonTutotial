## https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values


# Downloading *.csv file from GitHub
# > Bing-COVID19-Data.csv

import io
import os
import pathlib
import pandas as pd
import requests

import calendar;
import time;
# import progressbar

from typing import Union
import datetime

ts = calendar.timegm(time.gmtime())
timeOfWritingFile = datetime.datetime.fromtimestamp(ts).isoformat()
print(timeOfWritingFile, ' | ', timeOfWritingFile.split("T", 1)[0])


def convert_dtype(x):
    if not x:
        return ''
    try:
        return str(x)
    except:
        return ''


# create other useful functions to work with data
def current_status(self):
    # function to show current status
    pass


def convertToWindowsPath(string: Union[str, pathlib.Path]):
    # This converts a str to a Path (if already a Path, nothing changes)
    path = pathlib.Path(string)
    # print(type(path))
    # print(path)
    return path


class Bing:

    def __init__(self):

        # Make sure the url is the raw version of the file on GitHub
        # BASE_URL = 'REPLACE-ME WITH RAW-VERSION-URL-TO-THE-CSV-FILE'
        BASE_URL_PATH = 'https://github.com/kwhjvdkamp/Bing-COVID-19-Data/blob/master/data/'
        FILE = 'Bing-COVID19-Data.csv'
        REQUEST_QUERY = '?raw=true'

        download = requests.get(f'{BASE_URL_PATH}{FILE}{REQUEST_QUERY}').content

        self.data = pd.read_csv(io.StringIO(download.decode('utf-8')), header=0, escapechar='\\', converters={'ID': convert_dtype, 'Updated': convert_dtype, 'Confirmed': convert_dtype, 'ConfirmedChange': convert_dtype, 'Deaths': convert_dtype, 'DeathsChange': convert_dtype, 'Recovered': convert_dtype, 'RecoveredChange': convert_dtype, 'Latitude': convert_dtype, 'Longitude': convert_dtype, 'ISO2': convert_dtype, 'ISO3': convert_dtype, 'Country_Region': convert_dtype, 'AdminRegion1': convert_dtype, 'AdminRegion2': convert_dtype})

        # =============================================================



# Returns data as dictionary with DataFrames as Values
bing = Bing()
bing_df = bing.data

# Keys of the dictionary
print(bing.data.keys())

# Filter dataframe for
# 1) date today minus 14 days in column 'Updated',
# 2) value 'Worldwide' in column 'Country_Region'
# 3) empty cell in column 'AdminRegion1'

formatUSDate ="%m/%d/%Y"
fromDate = '01/21/2021'

bing_df['Updated'] = pd.to_datetime(bing_df['Updated'], format=formatUSDate)

worldwideDf = bing_df.loc[(bing_df['Updated'] > fromDate) & (bing_df['Country_Region'] == 'Worldwide') & (bing_df['AdminRegion1'] == '')]
netherlandsDf = bing_df.loc[(bing_df['Updated'] > fromDate) & (bing_df['Country_Region'] == 'Netherlands') & (bing_df['AdminRegion1'] == '')]

# Save dataframes to csv
# TODO add if exist overwrite

# dir_path = os.path.dirname(os.path.realpath(__file__))
# print('X1', dir_path)

# dir_path = os.path.join(dir_path, '..', 'somefolder')
# print('X2', dir_path)

# With the resulting string you can do os.chdir(dir_path)

currentContainer = pathlib.Path(__file__).parent.absolute()
path = str(currentContainer)
# print('Y', path)

# path_dt = convertToWindowsPath(path.replace('PythonTutorial\download_csv', 'COVID-19-Data\bing-data\accumulation\csv-data-bing'))

# ======================

pathToWriteTo = ''
# current working folder
if path.__contains__('HomeProjects'):
    # On Laptop write to >>> C:\HomeProjects\COVID-19-Data\bing-data\accumulation\csv-data-bing
    pathToWriteTo = convertToWindowsPath(path.replace('Python\PythonTutorial\download_csv', 'COVID-19-Data\\bing-data\\accumulation\\csv-data-bing'))
    print('Laptop:', pathToWriteTo)
elif path.__contains__('GitHubRepositories'):
    # On Desktop write to >>> C:\GithubRepositories\COVID-19-Data\bing-data\accumulation\csv-data-bing
    pathToWriteTo = convertToWindowsPath(path.replace('PythonTutorial\download_csv', 'COVID-19-Data\\bing-data\\accumulation\\csv-data-bing'))
    print('Desktop:', pathToWriteTo)
else:
    print('Wrong:', path)

isoDate = pd.to_datetime(fromDate)
strIsoDate = str(isoDate.strftime('%Y-%m-%d'))
isoDateShort = strIsoDate.split("T", 1)[0]

print('Time of file writing:', timeOfWritingFile.split("T", 1)[0])

lastUpdatedDayWld = str(worldwideDf['Updated'].iloc[-1])
print('DataFrame from \'first\' day', isoDateShort, 'till \'last\' day \'[Updated]\':', lastUpdatedDayWld.split(" ", 1)[0])
worldwideDf.to_csv(os.path.join(pathToWriteTo, r'WLD-COVID19-Data.csv'))
print('BING Dataframe WLD Count:', worldwideDf['Country_Region'].count())

lastUpdatedDayNld = str(netherlandsDf['Updated'].iloc[-1])
print('DataFrame from \'first\' day', isoDateShort, 'till \'last\' day \'[Updated]\':', lastUpdatedDayNld.split(" ", 1)[0])
netherlandsDf.to_csv(os.path.join(pathToWriteTo, r'NLD-COVID19-Data.csv'))
print('BING Dataframe NLD Count:', netherlandsDf['Country_Region'].count())


# # TEST
# # Combining progressbars with print output
# for i in progressbar.progressbar(range(100), redirect_stdout=True):
#     # Printing out the first 5 rows of the dataframe
#     print('Combining progressbars with print output', i)
#     time.sleep(0.02)

# # Progressbar with unknown length
# bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
# for i in range(20):
#     print('Progressbar with unknown length', i)
#     time.sleep(0.02)
#     bar.update(i)