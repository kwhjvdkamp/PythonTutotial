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
from pandas.core.frame import DataFrame
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
    path=pathlib.Path(string)
    return path

# Definition to retrieve Alpha-2 and -3 (Iso 3661) codes from
# country-specific objects like {'Country':{'Iso2':'CC', 'Iso3', 'CCC'}, ...}
# which resides in a local static json-like structure in 'isoCountryCodes.py'
def getIsoCodeForCountry(stateNames:list,iso:str):
    codes=[]
    missingIsoCodesStateNames=[]

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
            if stateName not in missingIsoCodesStateNames:
                missingIsoCodesStateNames.append(stateName)

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

    print('X',missingIsoCodesStateNames)
    return codes


# Definition to iterate over the CountryCodes Json-structure
# {'Country':{'Iso2':'CC', 'Iso3', 'CCC'}, ...}
# to return the iso codes object for a certain country name
def  mapStateNamewithIsoCodesObject(stateName:str):
    for key, value in CountryCodes.items():
        if key==stateName:
            return value


def combineTextColumns(col1:DataFrame, col2:DataFrame):
    col2 = col2.fillna('')
    df = col1.astype(str)+"|"+col2
    dfValues = df.values
    newList=[]
    finalList=[]
    for item in dfValues:
        if item[-1]=='|':
            newList.append(item[:-1])
        else:
            newList.append(item)

    for item in newList:
        item=item.replace('|', ' ')
        finalList.append(item)

    print(finalList[10])
    bla = pd.DataFrame(finalList)
    return bla
    # return dfValues


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

# Calling class
csse=Csse()
# Keys of the dictionary
# print(csse.data.keys())


# print('==Confirmed=======================================')
confirmed='Confirmed'
dfConfirmed: DataFrame=csse.data[confirmed]
# Pivoting 'Confirmed'-dataframe columns to rows
transposedDfConfirmed: DataFrame=pd.melt(dfConfirmed,
                            id_vars=dfConfirmed.columns[:4],
                            value_vars=dfConfirmed.columns[4:],
                            var_name='Updated',
                            value_name=confirmed)
# Extending and Sorting transposed 'Confirmed'-dataframe
# countryRegionConfirmed:list=transposedDfConfirmed['Country/Region'].values
# provinceStateConfirmed:list=transposedDfConfirmed['Province/State'].values
# distinctProvinceStateNamesConfirmed=distinctList(provinceStateConfirmed)
combinedDataFramesConfirmed:DataFrame=combineTextColumns(transposedDfConfirmed['Country/Region'],transposedDfConfirmed['Province/State'])
stateNamesConfirmed=pd.DataFrame(combinedDataFramesConfirmed).values
print('XX', stateNamesConfirmed[10])
dictConfirmed:dict[str, any]={
    'Date':pd.to_datetime(transposedDfConfirmed['Updated'], format=format_str),
    'Country_Region':transposedDfConfirmed['Country/Region'],
    'Province_State':transposedDfConfirmed['Province/State'],
    # 'Country_Region_Province_State':combineTextColumns(transposedDfConfirmed['Country/Region'],transposedDfConfirmed['Province/State']),
    'Latitude':transposedDfConfirmed['Lat'],
    'Longitude':transposedDfConfirmed['Long'],
    'ISO2':getIsoCodeForCountry(stateNamesConfirmed,'Iso2'),
    'ISO3':getIsoCodeForCountry(stateNamesConfirmed,'Iso3'),
    confirmed: transposedDfConfirmed[confirmed]
}
dfConfirmed: DataFrame=pd.DataFrame(dictConfirmed)
dfConfirmed: DataFrame=dfConfirmed.sort_values(by=['Country_Region', 'Date'])
dfConfirmed.sort_values(by=['Date'])
dictConfirmedExtended:dict[str, any]={
    'Date':dfConfirmed['Date'],
    'Country_Region':dfConfirmed['Country_Region'],
    'Province_State':dfConfirmed['Province_State'],
    # 'Country_Region_Province_State':dfConfirmed['Country_Region_Province_State'],
    'Latitude':dfConfirmed['Latitude'],
    'Longitude':dfConfirmed['Longitude'],
    'ISO2':dfConfirmed['ISO2'],
    'ISO3':dfConfirmed['ISO3'],
    confirmed: dfConfirmed[confirmed],
    confirmed+'Change':[num for num in dfConfirmed[confirmed].diff()],
}
dfConfirmedExtended: DataFrame=pd.DataFrame(dictConfirmedExtended)

# print('==Deceased========================================')
deceased='Deceased'
dfDeceased: DataFrame=csse.data[deceased]
# Pivoting 'Deceased'-dataframe columns to rows
transposedDfDeceased: DataFrame=pd.melt(dfDeceased,
                            id_vars=dfDeceased.columns[:4],
                            value_vars=dfDeceased.columns[4:],
                            var_name='Updated',
                            value_name='Deceased')
# Extending and Sorting transposed deceased-dataframe
# countryRegionDeceased:list=transposedDfDeceased['Country/Region'].values
# provinceStateDeceased:list=transposedDfDeceased['Province/State'].values
# distinctProvinceStateNamesDeceased=distinctList(provinceStateDeceased)
combinedDataFramesDeceased:DataFrame=combineTextColumns(transposedDfDeceased['Country/Region'],transposedDfDeceased['Province/State'])
stateNamesDeceased=pd.DataFrame(combinedDataFramesDeceased).values
dictDeceased:dict[str, any]={
    'Date':pd.to_datetime(transposedDfDeceased['Updated'], format=format_str),
    'Country_Region':transposedDfDeceased['Country/Region'],
    'Province_State':transposedDfDeceased['Province/State'],
    # 'Country_Region_Province_State':combineTextColumns(transposedDfDeceased['Country/Region'],transposedDfDeceased['Province/State']),
    'Latitude':transposedDfDeceased['Lat'],
    'Longitude':transposedDfDeceased['Long'],
    'ISO2':getIsoCodeForCountry(stateNamesDeceased,'Iso2'),
    'ISO3':getIsoCodeForCountry(stateNamesDeceased,'Iso3'),
    deceased: transposedDfDeceased[deceased]
}
dfDeceased: DataFrame=pd.DataFrame(dictDeceased)
dfDeceased: DataFrame=dfDeceased.sort_values(by=['Country_Region', 'Date'])
dfDeceased.sort_values(by=['Date'])
dictDeceasedExtended:dict[str, any]={
    'Date':dfDeceased['Date'],
    'Country_Region':dfDeceased['Country_Region'],
    'Province_State':dfDeceased['Province_State'],
    # 'Country_Region_Province_State':dfDeceased['Country_Region_Province_State'],
    'Latitude':dfDeceased['Latitude'],
    'Longitude':dfDeceased['Longitude'],
    'ISO2':dfDeceased['ISO2'],
    'ISO3':dfDeceased['ISO3'],
    deceased: dfDeceased[deceased],
    deceased+'Change':[num for num in dfDeceased[deceased].diff()],
}
dfDeceasedExtended: DataFrame=pd.DataFrame(dictDeceasedExtended)

# print('==Recovered=======================================')
recovered='Recovered'
dfRecovered: DataFrame=csse.data['Recovered']
# Pivoting 'Recovered'-dataframe columns to rows
transposedDfRecovered: DataFrame=pd.melt(dfRecovered,
                            id_vars=dfRecovered.columns[:4],
                            value_vars=dfRecovered.columns[4:],
                            var_name='Updated',
                            value_name=recovered)
# Extending and Sorting transposed 'Recovered'-dataframe
# countryRegionRecovered:list=transposedDfRecovered['Country/Region'].values
# provinceStateRecovered:list=transposedDfRecovered['Province/State'].values
# distinctProvinceStateNamesRecovered=distinctList(provinceStateRecovered)
combinedDataFramesRecovered:DataFrame=combineTextColumns(transposedDfRecovered['Country/Region'],transposedDfRecovered['Province/State'])
stateNamesRecovered=pd.DataFrame(combinedDataFramesRecovered).values
dictRecovered:dict[str, any]={
    'Date':pd.to_datetime(transposedDfRecovered['Updated'], format=format_str),
    'Country_Region':transposedDfRecovered['Country/Region'],
    'Province_State':transposedDfRecovered['Province/State'],
    # 'Country_Region_Province_State':combineTextColumns(transposedDfRecovered['Country/Region'],transposedDfRecovered['Province/State']),
    'Latitude':transposedDfRecovered['Lat'],
    'Longitude':transposedDfRecovered['Long'],
    'ISO2':getIsoCodeForCountry(stateNamesRecovered,'Iso2'),
    'ISO3':getIsoCodeForCountry(stateNamesRecovered,'Iso3'),
    recovered: transposedDfRecovered[recovered]
}
dfRecovered: DataFrame=pd.DataFrame(dictRecovered)
dfRecovered: DataFrame=dfRecovered.sort_values(by=['Country_Region', 'Date'])
dfRecovered.sort_values(by=['Date'])
dictRecoveredExtended:dict[str, any]={
    'Date':dfRecovered['Date'],
    'Country_Region':dfRecovered['Country_Region'],
    'Province_State':dfRecovered['Province_State'],
    # 'Country_Region_Province_State':dfRecovered['Country_Region_Province_State'],
    'Latitude':dfRecovered['Latitude'],
    'Longitude':dfRecovered['Longitude'],
    'ISO2':dfRecovered['ISO2'],
    'ISO3':dfRecovered['ISO3'],
    recovered: dfRecovered[recovered],
    recovered+'Change':[num for num in dfRecovered[recovered].diff()],
}
dfRecoveredExtended: DataFrame=pd.DataFrame(dictRecoveredExtended)

# print('==================================================')
# print('\r\nConfirmed')
# print(dfConfirmedExtended.head())
# print(dfConfirmedExtended.tail())
# print('==================================================')
# print('\r\nDeceased')
# print(dfDeceasedExtended.head())
# print(dfDeceasedExtended.tail())
# print('==================================================')
# print('\r\nRecovered')
# print(dfRecoveredExtended.head())
# print(dfRecoveredExtended.tail())
# print('==================================================')

# ======================================================================================

doWrite=True
if doWrite:

    currentContainer=pathlib.Path(__file__).parent.absolute()
    path=str(currentContainer)

    pathToWriteTo=''
    # current working folder
    if path.__contains__('HomeProjects'):
        # On Laptop write to >>> C:\HomeProjects\COVID-19-Data\bing-data\accumulation\csv-data-bing
        pathToWriteTo=convertToWindowsPath(path.replace('Python\PythonTutorial\download_csv', 'COVID-19-Data\\csse-data\\'))
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
    print('File writing switched OFF')
