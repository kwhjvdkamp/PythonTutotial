# # **********************************************************************************************************
# # Important (task is often ignored when doing data science)
# # !!! Clean up project by removing any assets that are no longer needed !!!

# # Remove zip file which has downloaded and the directory to which the files were unzipped

# # System utilities
# import os
# from pathlib import Path
# import shutil
# import wget
# from zipfile import ZipFile
# # Remove the zip file downloaded
# os.remove('names.zip')

# # Remove the directory data-us
# shutil.rmtree('data-us')
# # **********************************************************************************************************

# **********************************************************************************************************
# Download Data
# Start by downloading the data and saving it in an easy-to-read format.
# The raw data of babynames is available to download at https://www.ssa.gov/oact/babynames/names.zip
# as a zip file consisting of a set of comma separated text files for each year.
# Let us download the zip file and extract the files into a directory so we can inspect the files.

# Import modules and functions
import numpy as np
import pandas as pd
from wquantiles import quantile

# Plotting libraries
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (14, 6)
plt.style.use('seaborn-darkgrid')
import plotly.express as px

# Import modules and functions
import numpy as np
import pandas as pd
from wquantiles import quantile

from pathlib import Path
import shutil
import wget
from zipfile import ZipFile

# Babynames
# Download the zip file from "https://www.ssa.gov/oact/babynames/names.zip"
wget.download("https://www.ssa.gov/oact/babynames/names.zip")

# Unzip data files to a directory named 'data-us'
zip_names = ZipFile('names.zip')
zip_names.extractall('data-us')
zip_names.close()
# **********************************************************************************************************


# **********************************************************************************************************
# Let us now read the data for each year and combine them into a single data frame.
# Resulting dataframe saved as a gzip compressed csv file for subsequent usage.

# Read data for each year as a dataframe.
babynames = []
for file in Path('data-us').iterdir():
    if file.name.endswith('txt'):
      df = pd.read_csv(file, names=['name', 'sex', 'births'])
      df['year'] = int(file.name[3:7])
      babynames.append(df)

# Combine dataframes into a single dataframe
babynames = pd.concat(babynames)

# Save dataframe as csv.gz file with gzip compression
babynames.to_csv('names.csv.gz', index=False, compression='gzip')
# **********************************************************************************************************


# **********************************************************************************************************
import requests
import re

from bs4 import BeautifulSoup
import Extractor

# Lifetables
# The lifetables data is available as html files on the SSA website. We will scrape the data,
# parse it and combine all lifetables into a single dataframe and save it as a csv file.

def parse_lifetable(lifetable, year):
    """Parse extracted lifetable into a pandas dataframe"""
    df = pd.DataFrame(
        [[float(re.sub('\n|,', '', x)) if x != u"\xa0" else None for x in y] for y in lifetable[4:]],
        columns = [re.sub('\n|\s', '', x) for i, x in enumerate(lifetable[1])]
    )
    df_male = df.iloc[:,:7].assign(sex = 'M')
    df_female = df.iloc[:,8:].assign(sex = 'F')
    df = pd.concat([df_male, df_female]).rename(columns={"x": "age"})
    return df.assign(year = year).dropna()

def scrape_lifetable(year):
    """Scrape lifetable into a list of lists"""
    r = requests.get(f"https://www.ssa.gov/oact/NOTES/as120/LifeTables_Tbl_7_{year}.html")
    doc = BeautifulSoup(r.content, 'html.parser')
    tables = doc.find_all("table")
    table = tables[1]
    extractor = Extractor(table)
    extractor.parse()
    return extractor.return_list()

def get_lifetable(year):
    """Get lifetable for a given year"""
    lifetable = scrape_lifetable(year)
    df_lifetable = parse_lifetable(lifetable, year)
    return df_lifetable

def get_lifetables():
    """Get lifetables for all years available"""
    years = range(1900, 2100, 10)
    lifetables = pd.concat([get_lifetable(year) for year in years])
    lifetables.rename(columns={"": "ex"}, inplace=True)
    return lifetables

lifetables = get_lifetables()
lifetables.to_csv('lifetables.csv', index=False)
