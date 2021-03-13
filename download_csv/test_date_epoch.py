import os
from typing import Union
import pandas as pd
import requests
import io
import pathlib


from datetime import datetime

def convertToWindowsPath(string: Union[str, pathlib.Path]):
    # This converts a str to a Path (if already a Path, nothing changes)
    path = pathlib.Path(string)
    # print(type(path))
    # print(path)
    return path


currentContainer = pathlib.Path(__file__).parent.absolute()
subPathFromHomeProjectsToCurrentContainer = '\Python\PythonTutorial\download_csv'
print('Current container: (', type(currentContainer), ') ', currentContainer)
strCurrentContainer = str(currentContainer)
strCurrentContainer = strCurrentContainer.replace(subPathFromHomeProjectsToCurrentContainer, '')
print('--')
print('Current container: (', type(strCurrentContainer), ') ', strCurrentContainer)
print('--')
windowsPathContainer = convertToWindowsPath(strCurrentContainer)
print('Current container: (', type(windowsPathContainer), ') ' , windowsPathContainer)



formatUSDate ="%m/%d/%Y"
formatUSDateTimeLong ="%m/%d/%YT00:00:00.000Z"

epochDateTimeLong = datetime(1970, 1, 1, 0, 0, 0, 0)
EPOCH_DATETIME_LONG = epochDateTimeLong.strftime(formatUSDateTimeLong)
print(EPOCH_DATETIME_LONG)
print(type(EPOCH_DATETIME_LONG))

inputDateTimeLong = datetime(2021, 2, 21, 0, 0, 0, 0)
INPUT_FROM_DATETIME_LONG = inputDateTimeLong.strftime(formatUSDateTimeLong)
print(INPUT_FROM_DATETIME_LONG)
print(type(INPUT_FROM_DATETIME_LONG))

# ---------------------------------------

epochDate = datetime(1970, 1, 1)
print(epochDate)
strEPOCH_DATE = epochDate.strftime(formatUSDate)
print(type(strEPOCH_DATE))
print(strEPOCH_DATE)

inputDate =datetime(2021, 2, 21)
print(inputDate)
strFROM_DATE = inputDate.strftime(formatUSDate)
print(type(strFROM_DATE))
print(strFROM_DATE)

# --------------------

dtFROM_DATE = datetime.strptime(strFROM_DATE, formatUSDate)
print(type(dtFROM_DATE))
print(dtFROM_DATE)

print(type((datetime.strptime(strFROM_DATE, formatUSDate) - epochDate)))
intDays = (dtFROM_DATE - epochDate).days
print('Delta From epoch (in days)', (dtFROM_DATE - epochDate).days)
print(type((dtFROM_DATE - epochDate).days))
print('Days (', type(intDays), '):', intDays)


# print('From a datetime.strptime-string (\'1234 days\'): cut-off \' days\' and converted to int', type(int (datetime.strptime(FROM_DATE, formatUSDate) - epoch)[:-2]) )
