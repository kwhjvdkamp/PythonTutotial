print('__file__={0:<35} \r\n__name__={1:<20} \r\n__package__={2:<20}'.format(__file__,__name__,str(__package__)))

from pickle import TRUE
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
from typing import Dict, Match, Union
from awesome_progress_bar import ProgressBar

# Local module(s)
from isoCountryCodes import CountryCodes

# Defining columns
columnUpdated:str='Updated'
columnLatitude:str='Latitude'
columnLongitude:str='Longitude'
columnCountryRegion:str='Country_Region'
columnProvinceState:str='Province_State'
columnCountriesProvinces:str='Country_Region_Province_State'

# Function accepts list of country names and retrieve Alpha-2 and -3 (Iso 3661) codes from
# country-specific objects like {'Country':{'Iso2':'CC', 'Iso3', 'CCC'}, ...}
# which resides in a local static json-like structure in 'isoCountryCodes.py'
# return a list of code according isoLabe; two- or three letter list of codes
def getIsoCodeForCountry(countries:list,isoLabel:str):
    codes=[]
    # missingIsoCodesForCountries=[]

    # Non existing countries: 'Diamond Princess','Grand Princess' and 'Repatriated Travellers'
    # Countries with overseas '(semi) independent' areas are
    # 'Denmark', 'France', 'Netherlands' and 'United Kingdom' (US in not taken into account)
    # These so called '(semi) independent' overseas areas' are
    # listed in the Province/State column some having their own Iso2 & Iso3 codes
    for country in countries:
        pair=mapStateNamewithIsoCodesObject(country)
        # 'None' equivalent to 'null'
        if pair!=None:
            # ...either 'Iso2' or 'Iso3'
            isoCode=pair[isoLabel]
            codes.append(isoCode)
        else:
            # Missing codes
            # if country not in missingIsoCodesForCountries:
            #     missingIsoCodesForCountries.append(country)
            if isoLabel=='Iso2':
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

# Function accepts a country name to iterate over the CountryCodes Json-structure
# to map the Iso-codes for that country
# Function returns and iso code object for that certain country name
# {'Country':{'Iso2':'CC', 'Iso3', 'CCC'}, ...}
def  mapStateNamewithIsoCodesObject(country:str):
    for key,value in CountryCodes.items():
        if key==country:
            return value

# Function accepts two list of dataframe column values from which
# row values of each column should to be concatenated,
# Function returns a list of concatenated row values
def combineColumns(x:list,y:list):
    dfX=pd.DataFrame(x)
    dfY=pd.DataFrame(y)
    dfY=dfY.fillna('')
    dfXY=dfX.astype(str)+"|"+dfY
    dfXYValues=dfXY.values
    listXY=[]
    for dfXYValue in dfXYValues:
        if str(dfXYValue)[2:len(str(dfXYValue))-2][-1] == '|':
            listXY.append(str(dfXYValue)[2:len(str(dfXYValue))-3])
        else:
            listXY.append(str(dfXYValue)[2:len(str(dfXYValue))-2].replace('|',' '))
    # print(f'\r\nDistinct list of values of the concatenated columns \'Country_Region\' and \'Province_Region\'\r\n{distinctList(listXY)}')
    return listXY

# Creating a distinct list
def distinctList(items:list):
    list=[]
    for item in items:
        if item not in list and not pd.isna(item):
            list.append(item)
    return list

# Three achievements
# 1) Calculation the difference between a row value and the previous row value on the same column 'Confirmed'
# 2) Occuring NaN-values, the first value in the part of the column for a set of a country (.groupby(columnCountryRegion)
#    converting to float (0.0) values
# 3) Converting the calculated float values to int (0)
def diffPerDayForCsseDataKey(csseDataKey:str,df:DataFrame):

    countriesProvinces=distinctList(df[columnCountriesProvinces])
    countries=distinctList(df[columnCountryRegion].values)
    # print(f'Countries Regions{len(countries)},{countries}')
    provincesStates=distinctList(df[columnProvinceState].values)
    # print(f'Provinces States {len(stateEntities)},{stateEntities}')
    # countriesProvinces=combineColumns(countries,provincesStates)
    calculatedSeriesForDistinctCountryProvince=[]
    for countryProvince in countriesProvinces:
        for c in df.groupby(columnCountriesProvinces):
            if c[0]==countryProvince:
                # print(c[0]) # The current 'Country'
                # print(c[1]) # The corresponding dataFrame for 'Country'
                # valuesPerCountry = dfCountry.values
                # print(c[1]['Confirmed'])
                delta=[num for num in c[1][csseDataKey].diff().where(c[1][csseDataKey]>0)]
                seriesWithoutNansPerCountryProvince=pd.Series(delta,dtype=object).fillna(0).tolist()
                seriesRoundedWithoutNansPerCountryProvince=[round(num) for num in seriesWithoutNansPerCountryProvince]
                calculatedSeriesForDistinctCountryProvince.extend(seriesRoundedWithoutNansPerCountryProvince)
    # print(f'X{calculatedSeriesForDistinctCountryProvince}')
    return calculatedSeriesForDistinctCountryProvince

# ===========================================================================================

# Function accepts convert a string to a Path-typed structure (if already a Path, nothing changes)
def convertToWindowsPath(string: Union[str,pathlib.Path]):
    path=pathlib.Path(string)
    return path

# Function writes dataframe either to *.csv file or *.json file
def writeObjects(doWrite:bool,fileName:str,df:DataFrame):
    if doWrite:
        currentContainer=pathlib.Path(__file__).parent.absolute()
        path=str(currentContainer)
        pathToWriteTo=''
        device=''
        print('=============================================================================================================================================================')
        # current working folder
        if path.__contains__('HomeProjects'):
            # On Laptop write to >>> C:\HomeProjects\COVID-19-Data\bing-data\accumulation\csv-data-bing
            pathToWriteTo=convertToWindowsPath(path.replace('Python\PythonTutorial\download_csv','COVID-19-Data\\csse-data\\'))
            device='LAPTOP'
        elif path.__contains__('GitHubRepositories'):
            # On Desktop write to >>> C:\GithubRepositories\COVID-19-Data\bing-data\accumulation\csv-data-bing
            pathToWriteTo=convertToWindowsPath(path.replace('PythonTutorial\download_csv','COVID-19-Data\\csse-data\\'))
            device='DESKTOP'
        else:
            print('Wrong:',path)

        # CSV file writing
        df.to_csv(os.path.join(pathToWriteTo,f'{fileName}'+'.csv'))
        print(f'File \'{fileName}.csv\' written to {device}:',pathToWriteTo)

        # JSON file writing
        dateFormatIso='%Y-%m-%d'
        # Till so far the dtype of column df['Updated'] is 'datetime64[ns]'
        # In order to achieve having only the ISO-date-part (YYYY-MM-DD) as dtype 'str'
        # instead of the dtype 'datetime64[ns]' (yyyy-mm-ddThh-mm-ssZ)
        # the entire column 'Updated' needs to be converted to dtype 'str'
        # print(df.Updated.dtype)
        df['Updated'] = df['Updated'].dt.strftime(dateFormatIso)
        # json_records=df.to_json(orient='records',date_format='iso')
        # print(f'Orientation: json_records {json_records}\r\n')
        df.to_json(path_or_buf=os.path.join(pathToWriteTo,f'{fileName}'+'.json'),orient='records',date_format='iso')

        print(f'File \'{fileName}.json\' written to {device}:',pathToWriteTo)

    else:
        print('\r\n=============================================================================================================================================================')
        print('File writing switched OFF')

# ==========================================================================================

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

        # John Hopkins Institute https://github.com/CSSEGISandData

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

        # 1/22/20 is an American date notation equivalent to 22 jan 2020 or 2020-01-22 (ISO data)
        # 6/8/21 should be equivalent to june 8th 2021 of 2021-06-08
        fixedColumns=['Province/State','Country/Region','Lat','Long']
        dateColumns=['2/6/21','3/6/21','4/6/21','5/6/21']
        self.data={case:pd.read_csv(url,header=0,escapechar='\\', usecols=fixedColumns+dateColumns) for case,url in self.URLS.items()}

    # create other useful functions to work with data
    def current_status(self):
        # function to show current status
        pass

# ==========================================================================================

# Dataframe reconstruction and extention with aggregated group 'Worldwide'
class DfReconstructionAndExtentionWithAggregatedGroupWorldwide:

    goal = 'Dataframe construction'
    dateFormatUs='%m/%d/%y' # The original date format
    sortOrder = [columnCountryRegion,columnProvinceState]

    # def __init__(self):
        # print(self.goal)

    def reconstructAndExtend(self,csseDataKey:str,df:DataFrame,country:str):

        total = 10
        bar = ProgressBar(total,bar_length=157)

        # ===== Start Time consuming functions =====

        # Pivoting the 'passed-in'-dataframe (columns to rows)
        transposedDf:DataFrame=pd.melt(df,
                                    id_vars=df.columns[:4],
                                    value_vars=df.columns[4:],
                                    var_name=columnUpdated,
                                    value_name=csseDataKey)
        # Sorting the transposed 'passed-in'-dataframe
        # Converting the US-(m/d/yy)-date-format to the ISO-standard-date-(jjjj-mm-dd)-format
        # thru creating a new dictionary
        dict:Dict[str,any]={
            columnUpdated:pd.to_datetime(transposedDf[columnUpdated],format=self.dateFormatUs),
            csseDataKey: transposedDf[csseDataKey],
            columnLatitude:transposedDf['Lat'],
            columnLongitude:transposedDf['Long'],
            columnCountryRegion:transposedDf['Country/Region'],
            columnProvinceState:transposedDf['Province/State'],
        }
        # Reset the 'passed-in'-dataframe with the transposed dictionary
        df:DataFrame=pd.DataFrame(dict)

        # Create a copy dataframe from the current 'df'-dataframe by grouping on the 'Date'-column
        # meaning all data for all countries can be summed for the same date
        dfWorldwide:DataFrame=df.groupby([columnUpdated]).sum()
        # dfWorldwide.info()
        # print(f'\r\ndfWorldwide Columns {dfWorldwide.columns}')
        # The .sum() calculation on columns 'Latitude' and 'Longitude'
        # in the 'dfWorldwide'-dataframe is meaningless, so delete those columns
        del dfWorldwide[columnLatitude]
        del dfWorldwide[columnLongitude]
        # dfWorldwide.info()
        # The current 'dfWorldwide'-dataframe contains at this stage only the
        # columns 'Date' and the 'summage' of the 'csseDataKey'
        # for all listed countries for that specific date
        dfWorldwide.transpose()
        # Output:
        #       (index)         'csseDataKey' (<='Confirmed', 'Deceased' or 'Recovered')
        #   0   jjjj-mm-dd      0
        #   1   jjjj-mm-dd+1    1
        # Create a new column and copy the existing 'index'-labels into it
        dfWorldwide[columnUpdated]=dfWorldwide.index
        # Reset the index of the current dfWorldwide-dataframe
        dfWorldwide.reset_index(drop=True,inplace=True)
        # The aggregation of 'csseDataKey' for a particular date means 'csseDataKey' for all countries actually 'Worldwide'
        dfWorldwide[columnCountryRegion]='Worldwide'
        dfWorldwide[columnProvinceState]=''
        # Worldwide does not have a 'Latitude' or 'Longitude'
        dfWorldwide[columnLatitude]=None
        dfWorldwide[columnLongitude]=None
        # Reindex existing columns on the dfWorldwide-dataframe in the same order as expected on the original 'passed-in' dataset
        dfWorldwide=dfWorldwide.reindex(columns=[columnUpdated,csseDataKey,columnLatitude,columnLongitude,columnCountryRegion,columnProvinceState])
        # print(f'\r\nColumns {dfWorldwide.columns}\r\ndfWorldwide (rows):{len(dfWorldwide)}')
        # Relying on the fact, the columns of both dataframes do have the same order
        # create a new dataframe on which the created dfWorldwide-dataframe is concatenated with
        # the 'passed-in'-dataframe ignoring the index on both dataframe
        dfWorldwideExtendedWithDf=pd.concat([dfWorldwide,df],ignore_index=True)
        # Reset the 'passed-in'-dataframe with concatenated dataframes and
        # re-order the resetted dataframe (df) first on 'Country/Region', thereafter on 'Province/State'
        df:DataFrame=dfWorldwideExtendedWithDf.sort_values(by=self.sortOrder)
        # At last separately sorting on 'Date' (why separately sorting is needed is not understood)
        df.sort_values(by=[columnUpdated])

        combinedColumnCountryProvince:list=combineColumns(df[columnCountryRegion].values,df[columnProvinceState].values)
        df[columnCountriesProvinces]=combinedColumnCountryProvince
        iso2Codes:list=getIsoCodeForCountry(combinedColumnCountryProvince,'Iso2')
        iso3Codes:list=getIsoCodeForCountry(combinedColumnCountryProvince,'Iso3')

        diffPerDayForDataKey=diffPerDayForCsseDataKey(csseDataKey,df)

        # ===== Stop Time consuming functions =====

        try:
            for x in range(total):
                time.sleep(0.1)
                bar.iter('')
        except:
            bar.stop()
        bar.wait()

        # Test calls checking if each constructed dataframe has the same length of items
        # print(f'1  {len(df[columnUpdated])}')
        # print(f'2  {len(df[csseDataKey])}')
        # print(f'3a {len(combinedColumnCountryProvince)}')
        # print(f'3b {len(diffPerDayForDataKey)}')
        # print(f'4  {len(df[columnLatitude])}')
        # print(f'5  {len(df[columnLongitude])}')
        # print(f'6  {len(iso2Codes)}')
        # print(f'7  {len(iso3Codes)}')
        # print(f'8  {len(df[columnCountryRegion])}')
        # print(f'9  {len(df[columnProvinceState])}')

        # Extending the sorted 'df'-dataframe
        reconstructedDict:dict[str,any]={
            columnUpdated:df[columnUpdated],
            csseDataKey:df[csseDataKey],
            csseDataKey+'Change':diffPerDayForDataKey,
            columnLatitude:df[columnLatitude],
            columnLongitude:df[columnLongitude],
            'ISO2':iso2Codes,
            'ISO3':iso3Codes,
            columnCountryRegion:df[columnCountryRegion],
            columnProvinceState:df[columnProvinceState],
        }

        dfReconstructed=pd.DataFrame(reconstructedDict)

        maskCountry=dfReconstructed['Country_Region']==country

        if country=='Netherlands':
            # TODO For now only 'Netherlands' is filtered,
            # 'Netherlands' is one of the few countries in the retrieved CSSEdataframe
            # having so called 'overseas' areas (like Denmark, France or UK) or is a country so large it has been divided by its provinces
            # ['Province_State']
            # like Australia, Canada, China (US is not in this dataframe enclosed)
            dfReconstructed=dfReconstructed[maskCountry]
            maskIso2=dfReconstructed['ISO2']=='NL'
            dfReconstructed=dfReconstructed[maskIso2]
            maskIso3=dfReconstructed['ISO3']=='NLD'
            dfReconstructed=dfReconstructed[maskIso3]
            dfReconstructed['Province_State']=''
        else:
            print(country)
            dfReconstructed=dfReconstructed[maskCountry]

        return dfReconstructed

    # create other useful functions to work with data
    def current_status(self):
        # function to show current status
        pass

# ==========================================================================================

# Calling class
doWrite=TRUE
print('\r\n\r\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Downloading JHE CSSE Datasets +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
csse=Csse()
# Check keys of the 'data' dictionary
# print(csse.data.keys())
dfReconstructedAndExtended=DfReconstructionAndExtentionWithAggregatedGroupWorldwide()

countries=['Netherlands','Worldwide']
for country in countries:
    confirmed='Confirmed'
    deceased='Deceased'
    recovered='Recovered'
    print(f'\r\n============================================================ Reconstruction of {confirmed} Dataset ============================================================')
    dfConfirmedExtended:DataFrame=dfReconstructedAndExtended.reconstructAndExtend(confirmed,csse.data[confirmed],country)

    print(f'\r\n============================================================ Reconstruction of {deceased} Dataset =============================================================')
    dfDeceasedExtended:DataFrame=dfReconstructedAndExtended.reconstructAndExtend(deceased,csse.data[deceased],country)

    # Merge dataframes having identical (for instance the index or in this case 'Updated' column) columns
    # and drop the duplicate columns after merge
    dfConfirmedExtendedDeceasedExtended=pd.merge(dfConfirmedExtended,dfDeceasedExtended,how='inner',left_on='Updated',right_on='Updated',suffixes=('', '_drop'))
    dfConfirmedExtendedDeceasedExtended.drop([col for col in dfConfirmedExtendedDeceasedExtended.columns if 'drop' in col], axis=1, inplace=True)
    # print(f'Column names order\n{dfConfirmedExtendedDeceasedExtended.keys()}')
    dfConfirmedExtendedDeceasedExtended=dfConfirmedExtendedDeceasedExtended.reindex(columns=['Updated','Confirmed','ConfirmedChange','Deceased','DeceasedChange','Latitude','Longitude','ISO2','ISO3','Country_Region','Province_State'])
    # print(f'Reordered columns\n{dfConfirmedExtendedDeceasedExtended.keys()}')

    print(f'\r\n============================================================ Reconstruction of {recovered} Dataset ============================================================')
    dfRecoveredExtended:DataFrame=dfReconstructedAndExtended.reconstructAndExtend(recovered,csse.data[recovered],country)

    dfConfirmedExtendedDeceasedExtendedRecoveredExtended=pd.merge(dfConfirmedExtendedDeceasedExtended,dfDeceasedExtended,how='inner',left_on='Updated',right_on='Updated',suffixes=('', '_drop'))
    dfConfirmedExtendedDeceasedExtendedRecoveredExtended.drop([col for col in dfConfirmedExtendedDeceasedExtendedRecoveredExtended.columns if 'drop' in col], axis=1, inplace=True)
    # print(f'Column names order\n{dfConfirmedExtendedDeceasedExtendedRecoveredExtended.keys()}')
    dfConfirmedExtendedDeceasedExtendedRecoveredExtended=dfConfirmedExtendedDeceasedExtendedRecoveredExtended.reindex(columns=['Updated','Confirmed','ConfirmedChange','Deceased','DeceasedChange','Recovered','RecoveredChange','Latitude','Longitude','ISO2','ISO3','Country_Region','Province_State'])
    # print(f'Reordered columns\n{dfConfirmedExtendedDeceasedExtendedRecoveredExtended.keys()}')

    print(f'{dfConfirmedExtendedDeceasedExtendedRecoveredExtended.tail(1)}')

    writeObjects(doWrite,'CSSE_'+str(country),dfConfirmedExtendedDeceasedExtendedRecoveredExtended)

# ==========================================================================================
