# Downloading *.csv file from GitHub
# > Bing-COVID19-Data.csv

import os
import pandas as pd
import requests
import io

import time
import progressbar


def convert_dtype(x):
    if not x:
        return ''
    try:
        return str(x)
    except:
        return ''


class Bing:

    def __init__(self):

        # Make sure the url is the raw version of the file on GitHub

        # Note:
        # In case an image needs to be retrieved from GitHub
        # add '?raw=true' at the end of the link to the file

        # BASE_URL = 'REPLACE-ME WITH RAW-VERSION-URL-TO-THE-CSV-FILE'
        BASE_URL_PATH = 'https://github.com/kwhjvdkamp/Bing-COVID-19-Data/blob/master/bing-data/data/'
        FILE = 'Bing-COVID19-Data.csv'
        REQUEST_QUERY = '?raw=true'

        # -----
        # self.URLS = {
        #     'data': f'{BASE_URL}/Bing-COVID19-Data.csv',
        # }

        download = requests.get(f'{BASE_URL_PATH}/{FILE}/{REQUEST_QUERY}').content
        # self.data = pd.read_csv(io.StringIO(download.decode('utf-8')))
        # OUTPUT: Index(['404: Not Found'], dtype='object')

        # self.data = pd.read_csv( delimiter=',', dtype='unicode')
        self.data = pd.read_csv(io.StringIO(download.decode('utf-8')), converters={'ID': convert_dtype, 'Updated': convert_dtype, 'Confirmed': convert_dtype, 'ConfirmedChange': convert_dtype, 'Deaths': convert_dtype, 'DeathsChange': convert_dtype, 'Recovered': convert_dtype, 'RecoveredChange': convert_dtype, 'Latitude': convert_dtype, 'Longitude': convert_dtype, 'ISO2': convert_dtype, 'ISO3': convert_dtype, 'Country_Region': convert_dtype, 'AdminRegion1': convert_dtype, 'AdminRegion2': convert_dtype})

        # -----

        # res = requests.get(f'{BASE_URL_PATH}/{FILE}/{REQUEST_QUERY}', allow_redirects=True)
        # with open(FILE, 'wb') as file:
        #     file.write(res.content)

    # create other useful functions to work with data
    def current_status(self):
        # function to show current status
        pass


# =============================================================

# Returns data as dictionary with DataFrames as Values
bing = Bing()
bing_df = bing.data

print('BING Dataframe\r\n', bing_df.tail())

# TEST
# for i in progressbar.progressbar(range(100), redirect_stdout=True):
#     # Returns data as dictionary with DataFrames as Values
#     bing = Bing()
#     bing_df = bing.data

#     # Keys of the dictionary
#     print(bing.data.keys())

#     # Printing out the first 5 rows of the dataframe
#     # print('BING Dataframe\r\n', bing_df.tail(), i)
#     time.sleep(0.02)