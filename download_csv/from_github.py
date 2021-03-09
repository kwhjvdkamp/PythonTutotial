## https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values


# Downloading *.csv file from GitHub
# > Bing-COVID19-Data.csv

import os
import pandas as pd
import requests
import io
from datetime import datetime

import time
import progressbar


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

# dateTimeObj = datetime.now()
dateTimeObj = datetime(2021, 2, 21, 0, 0)
FROM_DATE = dateTimeObj.strftime("%m/%d/%Y)")

p = '%m/%d/%YT%H:%M:%S.%fZ'
myTime = "02/21/2021T00:00:00.000Z"
epoch = datetime(1970, 1, 1)
print((datetime.strptime(myTime, p) - epoch))

worldwide_df = bing_df.loc[((datetime.strptime(bing_df['Updated'], p) - epoch) > (datetime.strptime(FROM_DATE, p) - epoch)) & (bing_df['Country_Region'] == 'Worldwide') & (bing_df['AdminRegion1'] == '')]
netherlands_df = bing_df.loc[((datetime.strptime(bing_df['Updated'], p) - epoch) > (datetime.strptime(FROM_DATE, p) - epoch)) & (bing_df['Country_Region'] == 'Netherlands') & (bing_df['AdminRegion1'] == '')]

# Save dataframes to csv
# TODO add if exist overwrite
path=r'C:\HomeProjects\COVID-19-Data\bing-data\accumulation\csv-data-bing'

worldwide_df.to_csv(os.path.join(path, r'WLD-COVID19-Data.csv'))
print('BING Dataframe WLD Count: ', worldwide_df['Country_Region'].count())
netherlands_df.to_csv(os.path.join(path, r'NLD-COVID19-Data.csv'))
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