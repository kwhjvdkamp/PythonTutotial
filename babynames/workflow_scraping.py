import os

import requests
import pandas as pd

from pandas.core.frame import DataFrame
from lxml import etree
from bs4 import BeautifulSoup as BS4

# Lifetables
# The lifetables data is available as html files on the SSA website. We will scrape the data,
# parse it and combine all lifetables into a single dataframe and save it as a csv file.

def parse_html_table(table):
    """
    Parse table and filter out rows having child elements ('div') having a class attribute 'pCellBodyR' containing data
    """

    trs = table.find_all('tr')
    print(len(trs))
    my_table = []
    for tr in trs:
        testRow = etree.HTML(str(tr))
        # Catch row containing div containing data only
        dataDivs = testRow.xpath('//*[@class=\'pCellBodyR\']')
        repr(dataDivs)
        if len(dataDivs) == 14:
            my_row = []
            for dataDiv in dataDivs:
                value = dataDiv.text.replace('\n','').replace(',', '')
                if int(float(value)) == float(value):
                    my_row.append(int(float(value)))
                else:
                    my_row.append(float(value))
            my_table.append(my_row)

    return pd.DataFrame(my_table)


def parse_lifetable(lifetable: DataFrame, year):
    """
    Parse extracted lifetable into a pandas dataframe
    """

    lifetable_male = lifetable.iloc[:,:7].assign(sex = 'M')
    df_male = pd.DataFrame(lifetable_male)
    df_male.columns = ['age','qx','lx','dx','Lx','Tx','ex','sex']
    # df_male = df_male.drop('0', axis=1)
    print(f'===={year}====\r\n', df_male.columns, '\r\n============\r\n', df_male, '\r\n============')
    lifetable_female = lifetable.iloc[:,7:].assign(sex = 'F')
    df_female = pd.DataFrame(lifetable_female)
    df_female.columns = ['age','qx','lx','dx','Lx','Tx','ex','sex']
    # df_female = df_female.drop('0', axis=1)
    print(f'===={year}====\r\n', df_female, '\r\n============')

    df = pd.concat([df_male, df_female])
    df = df.dropna()
    reset_indexed_df = df.reset_index(drop=True)
    print(f'===={year}====\r\n', reset_indexed_df, '\r\n==Combined==')
    print(df.columns)
    print('Check concatenation\r\n', df.iloc[118:122])
    # df['year']=year
    df.insert(loc=0, column='year', value=year)
    # column_names = ['year','age','qx','lx','dx','Lx','Tx','ex','sex']
    # df.reindex(columns=column_names)

    print(df.head())
    return df


def scrape_lifetable(year):
    """
    Scrape lifetable into a list of lists
    """

    r = requests.get(f"https://www.ssa.gov/oact/NOTES/as120/LifeTables_Tbl_7_{year}.html")
    doc = BS4(r.content, "lxml")
    table = doc.find_all("table")[1]

    return parse_html_table(table)


def get_lifetable(year):
    """
    Get lifetable for a given year
    """

    lifetable = scrape_lifetable(year)
    print(f'===={year}====\r\n', lifetable, '\r\n============')
    df_lifetable = parse_lifetable(lifetable, year)

    return df_lifetable


def get_lifetables():
    """
    Get lifetables for all years available
    """

    years = range(1900, 2100, 10)
    lifetables = pd.concat([get_lifetable(year) for year in years])
    lifetables.rename(columns={"": "ex"}, inplace=True)

    return lifetables

lifetables = get_lifetables()
cwd = os.getcwd()
path = cwd + '/lifetables.csv'
lifetables.to_csv(path, index=False)



# # ****ORIGINAL SOURCE*********************************************************************************

# import requests
# import re

# from bs4 import BeautifulSoup
# from selectorlib import Extractor

# # Lifetables
# # The lifetables data is available as html files on the SSA website. We will scrape the data,
# # parse it and combine all lifetables into a single dataframe and save it as a csv file.

# def parse_lifetable(lifetable, year):
#     """Parse extracted lifetable into a pandas dataframe"""
#     df = pd.DataFrame(
#         [[float(re.sub('\n|,', '', x)) if x != u"\xa0" else None for x in y] for y in lifetable[4:]],
#         columns = [re.sub('\n|\s', '', x) for i, x in enumerate(lifetable[1])]
#     )
#     df_male = df.iloc[:,:7].assign(sex = 'M')
#     df_female = df.iloc[:,8:].assign(sex = 'F')
#     df = pd.concat([df_male, df_female]).rename(columns={"x": "age"})
#     return df.assign(year = year).dropna()

# def scrape_lifetable(year):
#     """Scrape lifetable into a list of lists"""
#     r = requests.get(f"https://www.ssa.gov/oact/NOTES/as120/LifeTables_Tbl_7_{year}.html")
#     doc = BeautifulSoup(r.content, 'html.parser')
#     tables = doc.find_all("table")
#     table = tables[1]
#     extractor = Extractor(table)
#     extractor.parse()
#     return extractor.return_list()

# def get_lifetable(year):
#     """Get lifetable for a given year"""
#     lifetable = scrape_lifetable(year)
#     df_lifetable = parse_lifetable(lifetable, year)
#     return df_lifetable

# def get_lifetables():
#     """Get lifetables for all years available"""
#     years = range(1900, 2100, 10)
#     lifetables = pd.concat([get_lifetable(year) for year in years])
#     lifetables.rename(columns={"": "ex"}, inplace=True)
#     return lifetables

# lifetables = get_lifetables()
# lifetables.to_csv('lifetables.csv', index=False)

# # ****ORIGINAL SOURCE*********************************************************************************
