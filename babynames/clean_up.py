# **********************************************************************************************************
# !!! Important !!!
# !!! Clean up project by removing any assets that are no longer needed !!!
# ? in sub directory /babynames/
# ?     sub directory   > data-us
# ?     zip file        > names.zip
# ?     file            > names.csv.gz
# ?     file            > lifetables.csv
# **********************************************************************************************************



import os
from pathlib import Path
import shutil

# Root directory
cwd=os.getcwd()
pathSubDirBabyNames=cwd+'\\babynames'
if os.path.exists(pathSubDirBabyNames):

    # Remove the zip file downloaded (actually after extraction already deleted)
    namesZip = 'names.zip'
    if os.path.exists(pathSubDirBabyNames+'\\'+namesZip):
        # Remove downloaded zip cabinet
        os.remove(pathSubDirBabyNames+'\\'+namesZip)
    else:
        print(f'Zip cabinet         \'{namesZip}\'        removed!')

    compressedArchive='names.csv.gz'
    if os.path.exists(pathSubDirBabyNames+'\\'+compressedArchive):
        # Remove the compressed archive (gz) downloaded
        os.remove(pathSubDirBabyNames+'\\'+compressedArchive)
    else:
        print(f'Compressed archive  \'{compressedArchive}\'     removed!')

    # Remove compiled csv
    fileCsv='lifetables.csv'
    if os.path.exists(pathSubDirBabyNames+'\\'+fileCsv):
        os.remove(pathSubDirBabyNames+'\\'+fileCsv)
    else:
        print(f'Csv file            \'{fileCsv}\'   removed!')

    # Remove the sub directory data-us
    dirDataUs='data-us'
    if os.path.exists(pathSubDirBabyNames+'\\'+dirDataUs):
        shutil.rmtree(pathSubDirBabyNames+'\\'+dirDataUs)
    else:
        print(f'Sub directory       \'{dirDataUs}\'          removed!')

else:
    print('?')
