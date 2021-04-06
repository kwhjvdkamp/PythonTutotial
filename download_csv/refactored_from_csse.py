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

# =========================================================================================

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
        pair=mapStateNamewithIsoCodesObject(stateName)
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
    dfCol2=dfCol2.fillna('')
    df=dfCol1.astype(str)+"|"+dfCol2
    dfValues=df.values
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

# =========================================================================================

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

#
class DataframeReconstruction:
    goal = 'Dataframe construction'
    format_str='%m/%d/%y' # The original date format
    sortOrder = ['Country_Region','Province_State']

    # def __init__(self):
        # print(self.goal)

    def reconstruct (self, set:str, df:DataFrame):
        print(f'\r\n\r\n= Reconstruction of {set} Dataset =')
        # Pivoting the 'passed-in'-dataframe (columns to rows)
        transposedDf:DataFrame=pd.melt(df,
                                    id_vars=df.columns[:4],
                                    value_vars=df.columns[4:],
                                    var_name='Updated',
                                    value_name=set)
        # Sorting the transposed 'passed-in'-dataframe
        # Converting the US-(m/d/yy)-date-format to the ISO-standard-date-(jjjj-mm-dd)-format
        # thru creating a new dictionary
        dict:dict[str,any]={
            'Date':pd.to_datetime(transposedDf['Updated'], format=self.format_str),
            'Country_Region':transposedDf['Country/Region'],
            'Province_State':transposedDf['Province/State'],
            'Latitude':transposedDf['Lat'],
            'Longitude':transposedDf['Long'],
            set: transposedDf[set]
        }
        # Reset the 'passed-in'-dataframe with the just created dictionary
        df:DataFrame=pd.DataFrame(dict)

        # Create a new dataframe from the current 'df'-dataframe by grouping on the
        # 'Date'-column which causes that in the new dfWorldwide-dataframe the entity (in this case 'Date')
        # on which is aggregated is set as the index of on new created dfWorldwide-dataframe
        dfWorldwide:DataFrame= df.groupby(['Date']).sum()
        # dfWorldwide.info()
        # print(f'\r\ndfWorldwide Columns {dfWorldwide.columns}')
        # For each row where the sum is shown for a particular 'Date'-set of rows aggregation on
        # the entities 'Latitude' and 'Longitude' is meaningless and therefore needs to be deleted
        # on the dfWorldwide-dataframe
        del dfWorldwide['Latitude']
        del dfWorldwide['Longitude']
        # dfWorldwide.info()
        # The current dfWorldwide-dataframe contains at this stage only the 'Date' and the 'sum' of 'set'
        # for all listed countries for that specific date meaning that 'set' is the total of all 'set' of all countries
        # Call transpose()-method
        dfWorldwide.transpose()
        # Output:
        #       (index)         'set' is 'Confirmed', 'Deceased' or 'Recovered'
        #   0   jjjj-mm-dd      0
        #   1   jjjj-mm-dd+1    1
        # Create a new column and copy the existing 'index'-labels into it
        dfWorldwide['Date']= dfWorldwide.index
        # Reset the index of the current dfWorldwide-dataframe
        dfWorldwide.reset_index(drop=True, inplace=True)
        # The aggregation of 'set' for a particular date means 'set' for all countries actually 'Worldwide'
        dfWorldwide['Country_Region']='Worldwide'
        dfWorldwide['Province_State']=None
        # Worldwide does not have a 'Latitude' or 'Longitude'
        dfWorldwide['Latitude']=None
        dfWorldwide['Longitude']=None
        # Reindex existing columns on the dfWorldwide-dataframe in the same order as expected on the original 'passed-in' dataset
        dfWorldwide=dfWorldwide.reindex(columns=['Date','Country_Region','Province_State','Latitude','Longitude',set])
        # print(f'\r\nColumns {dfWorldwide.columns}\r\ndfWorldwide (rows):{len(dfWorldwide)}')
        # Concatenate the created dfWorldwide-dataframe with the 'passed-in'-dataframe
        # (relying on the fact, columns of both dataframe have the same order on the moment of concatenation)
        # ignoring the index on both dataframe
        dfWorldwideExtendedWithDf = pd.concat([dfWorldwide, df], ignore_index=True)
        # Reset the 'passed-in'-dataframe with concatenated dataframes and
        # re-order the resetted dataframe (df) first on 'Country/Region', thereafter on 'Province/State'
        df:DataFrame=dfWorldwideExtendedWithDf.sort_values(by=self.sortOrder)
        # At last separately sorting on 'Date' (why separately sorting is needed is not understood)
        df.sort_values(by=['Date'])

        total = 10
        bar = ProgressBar(total,bar_length=39)

        # Start Time consuming functions
        stateNames:list=combineTextColumns(df['Country_Region'].values,df['Province_State'].values)
        iso2Codes:list=getIsoCodeForCountry(stateNames,'Iso2')
        iso3Codes:list=getIsoCodeForCountry(stateNames,'Iso3')
        # Stop Time consuming functions

        try:
            for x in range(total):
                time.sleep(0.1)
                bar.iter('')
        except:
            bar.stop()
        bar.wait()

        # Extending the sorted 'passed in'-dataframe
        reconstructedDict:dict[str,any]={
            'Date':df['Date'],
            'Country_Region':df['Country_Region'],
            'Province_State':df['Province_State'],
            'Latitude':df['Latitude'],
            'Longitude':df['Longitude'],
            'ISO2':iso2Codes,
            'ISO3':iso3Codes,
            set:df[set],
            set+'Change':[num for num in df[set].diff().where(df[set]>0)],
        }

        return pd.DataFrame(reconstructedDict)

    # create other useful functions to work with data
    def current_status(self):
        # function to show current status
        pass

# =========================================================================================

# Calling class
print('\r\n\r\n++++ Downloading CSSE JHE Datasets ++++')
csse=Csse()
# Keys of the dictionary
print('\r\n\r\n', csse.data.keys())

dfReconstruction = DataframeReconstruction()

confirmed='Confirmed'
dfConfirmedExtended:DataFrame=dfReconstruction.reconstruct(confirmed, csse.data[confirmed])
# print('\r\n',dfConfirmedExtended.head(1))
print('\r\n',dfConfirmedExtended.tail(1))

deceased='Deceased'
dfDeceasedExtended:DataFrame=dfReconstruction.reconstruct(deceased, csse.data[deceased])
# print('\r\n',dfDeceasedExtended.head(1))
print('\r\n',dfDeceasedExtended.tail(1))

recovered='Recovered'
dfRecoveredExtended:DataFrame=dfReconstruction.reconstruct(recovered, csse.data[recovered])
# print('\r\n',dfRecoveredExtended.head(1))
print('\r\n',dfRecoveredExtended.tail(1))

# =========================================================================================

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


# print('Bar is done')