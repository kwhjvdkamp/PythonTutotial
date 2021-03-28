import pandas as pd

class Corona:


    def __init__(self):

        BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series'

        self.URLS = {'confirmed': f'{BASE_URL}/time_series_covid19_confirmed_global.csv',
                'deaths': f'{BASE_URL}/time_series_covid19_deaths_global.csv',
                'recovered':f'{BASE_URL}/time_series_covid19_recovered_global.csv',
        }


        self.data = {case:pd.read_csv(url) for case, url in self.URLS.items()}

    # create other useful functions to work with data
    def current_status(self):
        # function to show current status
        pass



# returns data as dictionary with DataFrames as Values
corona = Corona()
confirmed_df = corona.data['confirmed']

# If you want to save them to csv
confirmed_df.to_csv('confirmed.csv', index=False)

# show first five rows
print(confirmed_df.head())

# check other DataFrame
print(corona.data.keys())