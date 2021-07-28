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
import os
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

cwd = os.getcwd()


# **********************************************************************************************************
# !!! Important !!!
# !!! Clean up project by removing any assets that are no longer needed !!!
# ? in sub directory /babynames/
# ?     sub directory   > data-us
# ?     zip file        > names.zip
# ?     file            > names.csv.gz
# ?     file            > lifetables.csv
# **********************************************************************************************************


pathSubDirDataUs = cwd + '\\babynames\\data-us'
if os.path.exists(pathSubDirDataUs):
     shutil.rmtree(pathSubDirDataUs, ignore_errors=True)

pathFileNamesCsvGz = cwd + '\\babynames\\names.csv.gz'
if os.path.exists(pathFileNamesCsvGz):
  os.remove(pathFileNamesCsvGz)

# Download the zip file from "https://www.ssa.gov/oact/babynames/names.zip"
wget.download("https://www.ssa.gov/oact/babynames/names.zip")

# Unzip data files to a directory named 'data-us'
zipName = 'names.zip'
zip_names = ZipFile(zipName)
zip_names.extractall(cwd + '\\babynames\\' + 'data-us')
zip_names.close()

# Remove zip file after it has been downloaded and the content has been unzipped
pathFileNamesZip = cwd + '\\' + zipName
if os.path.exists(pathFileNamesZip):
    os.remove(pathFileNamesZip)

# Read the data for each year and combine them into a single data frame.
babynames = []
for file in Path(cwd + '\\babynames\\' + 'data-us').iterdir():
    if file.name.endswith('txt'):
      df = pd.read_csv(file, names=['name', 'sex', 'births'])
      df['year'] = int(file.name[3:7])
      babynames.append(df)

# Combine dataframes into a single dataframe
babynames = pd.concat(babynames)

# Save dataframe as csv.gz file with gzip compression
babynames.to_csv(pathFileNamesCsvGz, index=False, compression='gzip')


# **********************************************************************************************************
