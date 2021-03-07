# Downloading the csv file from CSSE


import os
import pandas as pd
import requests
import io

class Csse:

    def __init__(self):

        # Make sure the url is the raw version of the file on GitHub

        # Note:
        # In case an image needs to be retrieved from GitHub
        # add '?raw=true' at the end of the link to the file

        # URL_PATH = 'REPLACE-ME WITH RAW-VERSION-URL-TO-THE-CSV-FILE'
        URL_PATH = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series'
        CSV_CONFIRMED_GLOBAL = 'time_series_covid19_confirmed_global.csv',
        CSV_DECEASED_GLOBAL = 'time_series_covid19_deaths_global.csv',
        CSV_RECOVERED_RECOVERED = 'time_series_covid19_recovered_global.csv'

        self.URLS = {
            'confirmed': f'{URL_PATH}/{CSV_CONFIRMED_GLOBAL}',
            'deaths': f'{URL_PATH}/{CSV_DECEASED_GLOBAL}',
            'recovered':f'{URL_PATH}/{CSV_RECOVERED_RECOVERED}',
        }

        self.data = {case:pd.read_csv(url) for case, url in self.URLS.items()}

    # create other useful functions to work with data
    def current_status(self):
        # function to show current status
        pass


# =============================================================
# Returns data as dictionary with DataFrames as Values
csse = Csse()

# Keys of the dictionary
print(csse.data.keys())

confirmed_df = csse.data['confirmed']
deaths_df = csse.data['deaths']
recovered_df = csse.data['recovered']

# Save dataframes to csv
# TODO add if exist overwrite
path=r'C:\HomeProjects\Bing-COVID-19-Data\csse-data'

confirmed_df.to_csv(os.path.join(path, r'csse_confirmed.csv'))
# First five rows
print(confirmed_df.head())
# Last five rows
print(confirmed_df.tail())

deaths_df.to_csv(os.path.join(path, r'csse_deaths.csv'))
# First five rows
print(deaths_df.head())
# Last five rows
print(deaths_df.tail())

recovered_df.to_csv(os.path.join(path, r'csse_recovered.csv'))
# First five rows
print(recovered_df.head())
# Last five rows
print(recovered_df.tail())

# with open(os.path.join(path, r'csse_confirmed.csv'), 'w+') as f:
#     f.write(r'csse_confirmed.csv')
