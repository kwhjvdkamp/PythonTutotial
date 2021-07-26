# **********************************************************************************************************
# Important (task is often ignored when doing data science)
# !!! Clean up project by removing any assets that are no longer needed !!!

# Remove zip file which has downloaded and the directory to which the files were unzipped

# System utilities
import os
from pathlib import Path
import shutil
import wget
from zipfile import ZipFile
# Remove the zip file downloaded
os.remove('names.zip')
os.remove('names.csv.gz')

# Remove the directory data-us
shutil.rmtree('data-us')
# **********************************************************************************************************
