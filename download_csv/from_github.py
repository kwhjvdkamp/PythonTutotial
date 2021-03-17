## https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values


# Downloading *.csv file from GitHub
# > Bing-COVID19-Data.csv

import io
import os
import pathlib
import pandas as pd
import requests

from typing import Union
from datetime import datetime

# import time
# import progressbar


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

        self.data = pd.read_csv(io.StringIO(download.decode('utf-8')), converters={'ID': convert_dtype, 'Updated': convert_dtype, 'Confirmed': convert_dtype, 'ConfirmedChange': convert_dtype, 'Deaths': convert_dtype, 'DeathsChange': convert_dtype, 'Recovered': convert_dtype, 'RecoveredChange': convert_dtype, 'Latitude': convert_dtype, 'Longitude': convert_dtype, 'ISO2': convert_dtype, 'ISO3': convert_dtype, 'Country_Region': convert_dtype, 'AdminRegion1': convert_dtype, 'AdminRegion2': convert_dtype})

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

bing_df['Updated'] = pd.to_datetime(bing_df['Updated'], format=formatUSDate)

worldwide_df = bing_df.loc[(bing_df['Updated'] > '01/21/2021') & (bing_df['Country_Region'] == 'Worldwide') & (bing_df['AdminRegion1'] == '')]
netherlands_df = bing_df.loc[(bing_df['Updated'] > '01/21/2021') & (bing_df['Country_Region'] == 'Netherlands') & (bing_df['AdminRegion1'] == '')]

# Save dataframes to csv
# TODO add if exist overwrite

currentContainer = pathlib.Path(__file__).parent.absolute()
path = str(currentContainer)
path_dt = convertToWindowsPath(path.replace('PythonTutorial\download_csv', 'COVID-19-Data\csse-data'))
# path_lt = convertToWindowsPath(path.replace('\Python\PythonTutorial\download_csv', ''))
# # COVID-19-Data\csse-data
# print(path_lt)

worldwide_df.to_csv(os.path.join(path_dt, r'WLD-COVID19-Data.csv'))
print('BING Dataframe WLD Count: ', worldwide_df['Country_Region'].count())
netherlands_df.to_csv(os.path.join(path_dt, r'NLD-COVID19-Data.csv'))
print('BING Dataframe NLD Count: ', netherlands_df['Country_Region'].count())






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