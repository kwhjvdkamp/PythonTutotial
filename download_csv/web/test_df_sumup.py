import pandas as pd
import numpy as np

def convertCalculatedSeries(lstFloats:list):
    listWithoutNans = pd.Series(lstFloats, dtype=object).fillna(0).tolist()
    # print(f'{listWithoutNans}')
    roundedListWithoutNans =[round(num) for num in listWithoutNans]
    return roundedListWithoutNans

# List of Tuples
employees_salary = [('Jan', 2000, 2010, 2050, 2134, 2111),
                    ('Piet', 3000, 3022, 3456, 3111, 2109),
                    ('Klaas', np.NaN, 2334, 2077, 2134, 3122),
                    ('Kees', 3012, 3050, 2010, 2122, 1111),
                    ('Koen', 2023, 2232, 3050, 2112, 1099),
                    ('Freek', 2123, 2510, np.NaN, 3134, 2122),
                    ('Mark', 4000, 2000, 2050, 2122, 2111)]

# Create a DataFrame object from list of tuples
df = pd.DataFrame(employees_salary,
                  columns=['Name', 'Jan', 'Feb', 'March', 'April', 'May'])

# Set column name as the index of dataframe
df.set_index('Name', inplace=True)
print(df)

# Get sum of all rows in the Dataframe as a Series
total = df.sum()
print('Total salary paid in each month:')
print(total)

# Get sum of all rows as a new row in Dataframe
total = df.sum()
total.name = 'Total (All)'
# Assign sum of all rows of DataFrame as a new Row
df = df.append(total.transpose())
print(f'Transposed {df}')

# Get sum of 3 DataFrame rows (selected by index labels)
subtotal = df.loc[['Klaas', 'Piet', 'Mark']].sum()
# Option
# Without filling-in the 'name'-property the 'name' column
# is omitted as index-column
# if so the an extra argument 'ignore_index=True' is required
# df = df.append(subtotal.transpose(), ignore_index=True)
# else
subtotal.name = 'subtotal (Klaas, Piet, Mark)'
df = df.append(subtotal.transpose())
print(df)

reconstructedDict:dict[str,any]={
    'Jan':df['Jan'],
    'Feb':df['Feb'],
    'March':df['March'],
    'April':df['April'],
    'May':df['May'],
    'MayChange':convertCalculatedSeries([num for num in df['May'].diff()]),
}

df_new = pd.DataFrame(reconstructedDict)
print(df_new)

print('===\r\n')

data = np.array([['1', '2'], ['3', '4']])

dataFrame = pd.DataFrame(df_new, columns = df_new.keys())
json = dataFrame.to_json()
print(f'Straight {json}\r\n')

json_split = dataFrame.to_json(orient ='split')
print(f'Orientation: json_split {json_split}\r\n')

json_records = dataFrame.to_json(orient ='records')
print(f'Orientation: json_records {json_records}\r\n')

json_index = dataFrame.to_json(orient ='index')
print(f'Orientation: json_index {json_index}\r\n')

json_columns = dataFrame.to_json(orient ='columns')
print(f'Orientation: json_columns {json_columns}\r\n')

json_values = dataFrame.to_json(orient ='values')
print(f'Orientation: json_values {json_values}\r\n')

json_table = dataFrame.to_json(orient ='table')
print(f'Orientation: json_table {json_table}\r\n')