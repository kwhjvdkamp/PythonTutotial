# //type: ignore
# ========================================================
# Above line tells Pylance to ignore this file
# > At the top of the file to ignore the file
# > At the end of a line to ignore the line
# ========================================================

# Downloading the csv file from CSSE
print('__file__={0:<35} \r\n__name__={1:<20} \r\n__package__={2:<20}'.format(__file__,__name__,str(__package__)))

import numpy as np
import os
import pathlib
import pandas as pd
import requests
import io
import time

from datetime import datetime
from pandas.core import indexing
from pandas.core.frame import DataFrame
from typing import Match, Union
from awesome_progress_bar import ProgressBar


# Local module(s)
from isoCountryCodes import CountryCodes

# Definition to convert a string to a Path-typed structure (if already a Path, nothing changes)
def convertToWindowsPath(string: Union[str, pathlib.Path]):
    path=pathlib.Path(string)
    return path


# Definition to retrieve Alpha-2 and -3 (Iso 3661) codes from
# country-specific objects like {'Country':{'Iso2':'CC', 'Iso3', 'CCC'}, ...}
# which resides in a local static json-like structure in 'isoCountryCodes.py'
def getIsoCodeForCountry(stateNames:list,iso:str):
    codes=[]
    # missingIsoCodesStateNames=[]

    # noneExistingCountryNames = ['Diamond Princess','Grand Princess','Repatriated Travellers']
    # Countries With Overseas Areas = ['Denmark','France','Netherlands','United Kingdom']
    # (US in not taken into account)
    # These 'Overseas areas' listed in Province/State column having their own Iso2 & Iso3 codes

    # print('Overseas areas with own Isocode', provinceStateNames)

    for stateName in stateNames:
        pair= mapStateNamewithIsoCodesObject(stateName)
        # 'None' equivalent to 'null'
        if pair!=None:
            # ...either 'Iso2' or 'Iso3'
            isoCode=pair[iso]
            codes.append(isoCode)
        else:
            # Missing codes
            # if stateName not in missingIsoCodesStateNames:
            #     missingIsoCodesStateNames.append(stateName)

            if iso=='Iso2':
                codes.append('--')
            else:
                codes.append('---')

            # On Python version 3.10 and up it will be possible
            # match iso
            #     case 'Iso2':
            #         codes.append('--')
            #     case 'Iso3':
            #         codes.append('---')

    # print('X',missingIsoCodesStateNames)
    return codes


# Definition to iterate over the CountryCodes Json-structure
# {'Country':{'Iso2':'CC', 'Iso3', 'CCC'}, ...}
# to return the iso codes object for a certain country name
def  mapStateNamewithIsoCodesObject(stateName:str):
    for key, value in CountryCodes.items():
        if key==stateName:
            return value


# Definition to concatenate two dataframe columns containing string values
def combineTextColumns(col1:list,col2:list):
    dfCol1=pd.DataFrame(col1)
    dfCol2=pd.DataFrame(col2)
    dfCol2 = dfCol2.fillna('')
    df = dfCol1.astype(str)+"|"+dfCol2
    dfValues = df.values
    finalList=[]
    for item in dfValues:
        if str(item)[2:len(str(item))-2][-1] == '|':
            finalList.append(str(item)[2:len(str(item))-3])
        else:
            finalList.append(str(item)[2:len(str(item))-2].replace('|', ' '))
    # print(distinctList(finalList))
    return finalList


# Creating a distinct list
def distinctList(items:list):
    list=[]
    for item in items:
        if item not in list and not pd.isna(item):
            list.append(item)
    return list


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

        URL_PATH='https://raw.github.com/kwhjvdkamp/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'

        # 'f-strings' provide a way to embed expressions inside string literals using a minimal syntax.
        # It should be noted that an f-string is really an expression evaluated at run time, not a constant value.
        # In Python source code, an f-string is a literal string, prefixed with 'f',
        # which contains expressions inside braces. The expressions are replaced with their values.
        self.URLS={
            'Confirmed':f'{URL_PATH}/time_series_covid19_confirmed_global.csv',
            'Deceased':f'{URL_PATH}/time_series_covid19_deaths_global.csv',
            'Recovered':f'{URL_PATH}/time_series_covid19_recovered_global.csv',
        }

        self.data={case:pd.read_csv(url, header=0, escapechar='\\') for case, url in self.URLS.items()}

    # create other useful functions to work with data
    def current_status(self):
        # function to show current status
        pass


# =========================================================================================


# private variables
# Original data contains dates formatted like 'm/d/jj' meaning a) no preceding zero's and b) two digit year
# conversion to Iso date 'YYYY-MM-DD' format is mandatory
format_str='%m/%d/%y' # The original date format
sortOrder = ['Country_Region','Province_State','Date']

total = 10
bar = ProgressBar(total, bar_length=39)

# Calling class
print('\r\n\r\n++++ Downloading CSSE JHE Datasets ++++')
csse=Csse()
# Keys of the dictionary
print('\r\n\r\n', csse.data.keys())

confirmed='Confirmed'
print(f'\r\n\r\n= Reconstruction of {confirmed} Dataset =')
dfConfirmed:DataFrame=csse.data[confirmed]
# Pivoting the 'Confirmed'-dataframe columns to rows
transposedDfConfirmed:DataFrame=pd.melt(dfConfirmed,
                            id_vars=dfConfirmed.columns[:4],
                            value_vars=dfConfirmed.columns[4:],
                            var_name='Updated',
                            value_name=confirmed)
# Sorting the transposed 'Confirmed'-dataframe
dictConfirmed:dict[str,any]={
    'Date':pd.to_datetime(transposedDfConfirmed['Updated'], format=format_str),
    'Country_Region':transposedDfConfirmed['Country/Region'],
    'Province_State':transposedDfConfirmed['Province/State'],
    'Latitude':transposedDfConfirmed['Lat'],
    'Longitude':transposedDfConfirmed['Long'],
    confirmed: transposedDfConfirmed[confirmed]
}
dfConfirmed:DataFrame=pd.DataFrame(dictConfirmed)
# Sorting first on 'Country_Region' than 'Province_Region' next 'Date'
dfConfirmed:DataFrame=dfConfirmed.sort_values(by=sortOrder)
# Again sorting on 'Date'
dfConfirmed.sort_values(by=['Date'])
# Start Time consumming functions calls
stateNameConfirmed:list=combineTextColumns(dfConfirmed['Country_Region'].values,dfConfirmed['Province_State'].values)
iso2CodesConfirmed:list=getIsoCodeForCountry(stateNameConfirmed,'Iso2')
iso3CodesConfirmed:list=getIsoCodeForCountry(stateNameConfirmed,'Iso3')
# Stop Time consumming functions calls
# Extending the sorted 'Confirmed'-dataframe
dictConfirmedExtended:dict[str,any]={
    'Date':dfConfirmed['Date'],
    'Country_Region':dfConfirmed['Country_Region'],
    'Province_State':dfConfirmed['Province_State'],
    'Latitude':dfConfirmed['Latitude'],
    'Longitude':dfConfirmed['Longitude'],
    'ISO2':iso2CodesConfirmed,
    'ISO3':iso3CodesConfirmed,
    confirmed:dfConfirmed[confirmed],
    confirmed+'Change':[num for num in dfConfirmed[confirmed].diff().where(dfConfirmed[confirmed]>0)],
}
dfConfirmedExtended:DataFrame=pd.DataFrame(dictConfirmedExtended)
# print('\r\n',dfConfirmedExtended.head(1))
print('\r\n',dfConfirmedExtended.tail(1))

deceased='Deceased'
print('\r\n\r\n= Reconstruction of '+deceased+' Dataset =')
dfDeceased:DataFrame=csse.data[deceased]
# Pivoting the 'Deceased'-dataframe columns to rows
transposedDfDeceased:DataFrame=pd.melt(dfDeceased,
                            id_vars=dfDeceased.columns[:4],
                            value_vars=dfDeceased.columns[4:],
                            var_name='Updated',
                            value_name='Deceased')
# Sorting the transposed 'Deceased'-dataframe
dictDeceased:dict[str,any]={
    'Date':pd.to_datetime(transposedDfDeceased['Updated'], format=format_str),
    'Country_Region':transposedDfDeceased['Country/Region'],
    'Province_State':transposedDfDeceased['Province/State'],
    'Latitude':transposedDfDeceased['Lat'],
    'Longitude':transposedDfDeceased['Long'],
    deceased: transposedDfDeceased[deceased]
}
dfDeceased:DataFrame=pd.DataFrame(dictDeceased)
dfDeceased:DataFrame=dfDeceased.sort_values(by=sortOrder)
dfDeceased.sort_values(by=['Date'])
# Start Time consumming functions calls
stateNameDeceased:list=combineTextColumns(dfDeceased['Country_Region'].values,dfDeceased['Province_State'].values)
iso2CodesDeceased:list=getIsoCodeForCountry(stateNameDeceased,'Iso2')
iso3CodesDeceased:list=getIsoCodeForCountry(stateNameDeceased,'Iso3')
# Stop Time consumming functions calls
# Extending the sorted 'Confirmed'-dataframe
dictDeceasedExtended:dict[str,any]={
    'Date':dfDeceased['Date'],
    'Country_Region':dfDeceased['Country_Region'],
    'Province_State':dfDeceased['Province_State'],
    'Latitude':dfDeceased['Latitude'],
    'Longitude':dfDeceased['Longitude'],
    'ISO2':iso2CodesDeceased,
    'ISO3':iso3CodesDeceased,
    deceased: dfDeceased[deceased],
    deceased+'Change':[num for num in dfDeceased[deceased].diff().where(dfDeceased[deceased]>0)],
}
dfDeceasedExtended:DataFrame=pd.DataFrame(dictDeceasedExtended)
# print('\r\n',dfDeceasedExtended.head(1))
print('\r\n',dfDeceasedExtended.tail(1))

recovered='Recovered'
print('\r\n\r\n= Reconstruction of '+recovered+' Dataset =')
dfRecovered:DataFrame=csse.data['Recovered']
# Pivoting 'Recovered'-dataframe columns to rows
transposedDfRecovered:DataFrame=pd.melt(dfRecovered,
                            id_vars=dfRecovered.columns[:4],
                            value_vars=dfRecovered.columns[4:],
                            var_name='Updated',
                            value_name=recovered)
# Sorting the transposed 'Recovered'-dataframe
dictRecovered:dict[str,any]={
    'Date':pd.to_datetime(transposedDfRecovered['Updated'], format=format_str),
    'Country_Region':transposedDfRecovered['Country/Region'],
    'Province_State':transposedDfRecovered['Province/State'],
    'Latitude':transposedDfRecovered['Lat'],
    'Longitude':transposedDfRecovered['Long'],
    recovered: transposedDfRecovered[recovered]
}
dfRecovered:DataFrame=pd.DataFrame(dictRecovered)
dfRecovered:DataFrame=dfRecovered.sort_values(by=sortOrder)
dfRecovered.sort_values(by=['Date'])
# Start Time consumming functions calls
stateNameRecovered:list=combineTextColumns(dfRecovered['Country_Region'].values,dfRecovered['Province_State'].values)
iso2CodesRecovered:list=getIsoCodeForCountry(stateNameRecovered,'Iso2')
iso3CodesRecovered:list=getIsoCodeForCountry(stateNameRecovered,'Iso3')
# Stop Time consumming functions calls
# Extending the sorted 'Confirmed'-dataframe
dictRecoveredExtended:dict[str,any]={
    'Date':dfRecovered['Date'],
    'Country_Region':dfRecovered['Country_Region'],
    'Province_State':dfRecovered['Province_State'],
    'Latitude':dfRecovered['Latitude'],
    'Longitude':dfRecovered['Longitude'],
    'ISO2':iso2CodesRecovered,
    'ISO3':iso3CodesRecovered,
    recovered: dfRecovered[recovered],
    recovered+'Change':[num for num in dfRecovered[recovered].diff().where(dfRecovered[recovered]>0)],
}
dfRecoveredExtended:DataFrame=pd.DataFrame(dictRecoveredExtended)
# print('\r\n',dfRecoveredExtended.head(1))
print('\r\n',dfRecoveredExtended.tail(1))

doWrite=True
if doWrite:
    currentContainer=pathlib.Path(__file__).parent.absolute()
    path=str(currentContainer)
    pathToWriteTo=''
    # current working folder
    if path.__contains__('HomeProjects'):
        # On Laptop write to >>> C:\HomeProjects\COVID-19-Data\bing-data\accumulation\csv-data-bing
        pathToWriteTo=convertToWindowsPath(path.replace('Python\PythonTutorial\download_csv', 'COVID-19-Data\\csse-data\\'))
        print('\r\n=========== File writing to ===========')
        print('Laptop:', pathToWriteTo)
    elif path.__contains__('GitHubRepositories'):
        # On Desktop write to >>> C:\GithubRepositories\COVID-19-Data\bing-data\accumulation\csv-data-bing
        pathToWriteTo=convertToWindowsPath(path.replace('PythonTutorial\download_csv', 'COVID-19-Data\\csse-data\\'))
        print('Desktop:', pathToWriteTo)
    else:
        print('Wrong:', path)

    dfConfirmedExtended.to_csv(os.path.join(pathToWriteTo, r'csse_confirmed.csv'))
    dfDeceasedExtended.to_csv(os.path.join(pathToWriteTo, r'csse_deceased.csv'))
    dfRecoveredExtended.to_csv(os.path.join(pathToWriteTo, r'csse_recovered.csv'))

else:
    print('\r\n\r\n====== File writing switched OFF ======')

try:
    for x in range(total):
        time.sleep(0.1)
        bar.iter('')

except:
    bar.stop()
bar.wait()
# print('Bar is done')