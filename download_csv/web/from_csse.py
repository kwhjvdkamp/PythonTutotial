# Downloading the csv file from CSSE
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

import os
import pathlib
import pandas as pd
import requests
import io

from ..web.utils import isoCountryCodes

from datetime import datetime
from pandas.core import indexing
from typing import Union

print("Count {0}".format(len(isoCountryCodes.CC)))

# CC = {
#     "AF": "AFGHANISTAN",
#     "AX": "ÅLAND ISLANDS",
#     "AL": "ALBANIA",
#     "DZ": "ALGERIA",
#     "AS": "AMERICAN SAMOA",
#     "AD": "ANDORRA",
#     "AO": "ANGOLA",
#     "AI": "ANGUILLA",
#     "AQ": "ANTARCTICA",
#     "AG": "ANTIGUA AND BARBUDA",
#     "AR": "ARGENTINA",
#     "AM": "ARMENIA",
#     "AW": "ARUBA",
#     "AU": "AUSTRALIA",
#     "AT": "AUSTRIA",
#     "AZ": "AZERBAIJAN",
#     "BS": "BAHAMAS",
#     "BH": "BAHRAIN",
#     "BD": "BANGLADESH",
#     "BB": "BARBADOS",
#     "BY": "BELARUS",
#     "BE": "BELGIUM",
#     "BZ": "BELIZE",
#     "BJ": "BENIN",
#     "BM": "BERMUDA",
#     "BT": "BHUTAN",
#     "BO": "BOLIVIA, PLURINATIONAL STATE OF",
#     "BQ": "BONAIRE, SINT EUSTATIUS AND SABA",
#     "BA": "BOSNIA AND HERZEGOVINA",
#     "BW": "BOTSWANA",
#     "BV": "BOUVET ISLAND",
#     "BR": "BRAZIL",
#     "IO": "BRITISH INDIAN OCEAN TERRITORY",
#     "BN": "BRUNEI DARUSSALAM",
#     "BG": "BULGARIA",
#     "BF": "BURKINA FASO",
#     "BI": "BURUNDI",
#     "KH": "CAMBODIA",
#     "CM": "CAMEROON",
#     "CA": "CANADA",
#     "CV": "CAPE VERDE",
#     "KY": "CAYMAN ISLANDS",
#     "CF": "CENTRAL AFRICAN REPUBLIC",
#     "TD": "CHAD",
#     "CL": "CHILE",
#     "CN": "CHINA",
#     "CX": "CHRISTMAS ISLAND",
#     "CC": "COCOS (KEELING) ISLANDS",
#     "CO": "COLOMBIA",
#     "KM": "COMOROS",
#     "CG": "CONGO",
#     "CD": "CONGO, THE DEMOCRATIC REPUBLIC OF THE",
#     "CK": "COOK ISLANDS",
#     "CR": "COSTA RICA",
#     "CI": "CÔTE D'IVOIRE",
#     "HR": "CROATIA",
#     "CU": "CUBA",
#     "CW": "CURAÇAO",
#     "CY": "CYPRUS",
#     "CZ": "CZECH REPUBLIC",
#     "DK": "DENMARK",
#     "DJ": "DJIBOUTI",
#     "DM": "DOMINICA",
#     "DO": "DOMINICAN REPUBLIC",
#     "EC": "ECUADOR",
#     "EG": "EGYPT",
#     "SV": "EL SALVADOR",
#     "GQ": "EQUATORIAL GUINEA",
#     "ER": "ERITREA",
#     "EE": "ESTONIA",
#     "ET": "ETHIOPIA",
#     "FK": "FALKLAND ISLANDS (MALVINAS)",
#     "FO": "FAROE ISLANDS",
#     "FJ": "FIJI",
#     "FI": "FINLAND",
#     "FR": "FRANCE",
#     "GF": "FRENCH GUIANA",
#     "PF": "FRENCH POLYNESIA",
#     "TF": "FRENCH SOUTHERN TERRITORIES",
#     "GA": "GABON",
#     "GM": "GAMBIA",
#     "GE": "GEORGIA",
#     "DE": "GERMANY",
#     "GH": "GHANA",
#     "GI": "GIBRALTAR",
#     "GR": "GREECE",
#     "GL": "GREENLAND",
#     "GD": "GRENADA",
#     "GP": "GUADELOUPE",
#     "GU": "GUAM",
#     "GT": "GUATEMALA",
#     "GG": "GUERNSEY",
#     "GN": "GUINEA",
#     "GW": "GUINEA-BISSAU",
#     "GY": "GUYANA",
#     "HT": "HAITI",
#     "HM": "HEARD ISLAND AND MCDONALD ISLANDS",
#     "VA": "HOLY SEE (VATICAN CITY STATE)",
#     "HN": "HONDURAS",
#     "HK": "HONG KONG",
#     "HU": "HUNGARY",
#     "IS": "ICELAND",
#     "IN": "INDIA",
#     "ID": "INDONESIA",
#     "IR": "IRAN, ISLAMIC REPUBLIC OF",
#     "IQ": "IRAQ",
#     "IE": "IRELAND",
#     "IM": "ISLE OF MAN",
#     "IL": "ISRAEL",
#     "IT": "ITALY",
#     "JM": "JAMAICA",
#     "JP": "JAPAN",
#     "JE": "JERSEY",
#     "JO": "JORDAN",
#     "KZ": "KAZAKHSTAN",
#     "KE": "KENYA",
#     "KI": "KIRIBATI",
#     "KP": "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",
#     "KR": "KOREA, REPUBLIC OF",
#     "KW": "KUWAIT",
#     "KG": "KYRGYZSTAN",
#     "LA": "LAO PEOPLE'S DEMOCRATIC REPUBLIC",
#     "LV": "LATVIA",
#     "LB": "LEBANON",
#     "LS": "LESOTHO",
#     "LR": "LIBERIA",
#     "LY": "LIBYA",
#     "LI": "LIECHTENSTEIN",
#     "LT": "LITHUANIA",
#     "LU": "LUXEMBOURG",
#     "MO": "MACAO",
#     "MK": "MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF",
#     "MG": "MADAGASCAR",
#     "MW": "MALAWI",
#     "MY": "MALAYSIA",
#     "MV": "MALDIVES",
#     "ML": "MALI",
#     "MT": "MALTA",
#     "MH": "MARSHALL ISLANDS",
#     "MQ": "MARTINIQUE",
#     "MR": "MAURITANIA",
#     "MU": "MAURITIUS",
#     "YT": "MAYOTTE",
#     "MX": "MEXICO",
#     "FM": "MICRONESIA, FEDERATED STATES OF",
#     "MD": "MOLDOVA, REPUBLIC OF",
#     "MC": "MONACO",
#     "MN": "MONGOLIA",
#     "ME": "MONTENEGRO",
#     "MS": "MONTSERRAT",
#     "MA": "MOROCCO",
#     "MZ": "MOZAMBIQUE",
#     "MM": "MYANMAR",
#     "NA": "NAMIBIA",
#     "NR": "NAURU",
#     "NP": "NEPAL",
#     "NL": "NETHERLANDS",
#     "NC": "NEW CALEDONIA",
#     "NZ": "NEW ZEALAND",
#     "NI": "NICARAGUA",
#     "NE": "NIGER",
#     "NG": "NIGERIA",
#     "NU": "NIUE",
#     "NF": "NORFOLK ISLAND",
#     "MP": "NORTHERN MARIANA ISLANDS",
#     "NO": "NORWAY",
#     "OM": "OMAN",
#     "PK": "PAKISTAN",
#     "PW": "PALAU",
#     "PS": "PALESTINE, STATE OF",
#     "PA": "PANAMA",
#     "PG": "PAPUA NEW GUINEA",
#     "PY": "PARAGUAY",
#     "PE": "PERU",
#     "PH": "PHILIPPINES",
#     "PN": "PITCAIRN",
#     "PL": "POLAND",
#     "PT": "PORTUGAL",
#     "PR": "PUERTO RICO",
#     "QA": "QATAR",
#     "RE": "RÉUNION",
#     "RO": "ROMANIA",
#     "RU": "RUSSIAN FEDERATION",
#     "RW": "RWANDA",
#     "BL": "SAINT BARTHÉLEMY",
#     "SH": "SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA",
#     "KN": "SAINT KITTS AND NEVIS",
#     "LC": "SAINT LUCIA",
#     "MF": "SAINT MARTIN (FRENCH PART)",
#     "PM": "SAINT PIERRE AND MIQUELON",
#     "VC": "SAINT VINCENT AND THE GRENADINES",
#     "WS": "SAMOA",
#     "SM": "SAN MARINO",
#     "ST": "SAO TOME AND PRINCIPE",
#     "SA": "SAUDI ARABIA",
#     "SN": "SENEGAL",
#     "RS": "SERBIA",
#     "SC": "SEYCHELLES",
#     "SL": "SIERRA LEONE",
#     "SG": "SINGAPORE",
#     "SX": "SINT MAARTEN (DUTCH PART)",
#     "SK": "SLOVAKIA",
#     "SI": "SLOVENIA",
#     "SB": "SOLOMON ISLANDS",
#     "SO": "SOMALIA",
#     "ZA": "SOUTH AFRICA",
#     "GS": "SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS",
#     "SS": "SOUTH SUDAN",
#     "ES": "SPAIN",
#     "LK": "SRI LANKA",
#     "SD": "SUDAN",
#     "SR": "SURINAME",
#     "SJ": "SVALBARD AND JAN MAYEN",
#     "SZ": "SWAZILAND",
#     "SE": "SWEDEN",
#     "CH": "SWITZERLAND",
#     "SY": "SYRIAN ARAB REPUBLIC",
#     "TW": "TAIWAN, PROVINCE OF CHINA",
#     "TJ": "TAJIKISTAN",
#     "TZ": "TANZANIA, UNITED REPUBLIC OF",
#     "TH": "THAILAND",
#     "TL": "TIMOR-LESTE",
#     "TG": "TOGO",
#     "TK": "TOKELAU",
#     "TO": "TONGA",
#     "TT": "TRINIDAD AND TOBAGO",
#     "TN": "TUNISIA",
#     "TR": "TURKEY",
#     "TM": "TURKMENISTAN",
#     "TC": "TURKS AND CAICOS ISLANDS",
#     "TV": "TUVALU",
#     "UG": "UGANDA",
#     "UA": "UKRAINE",
#     "AE": "UNITED ARAB EMIRATES",
#     "GB": "UNITED KINGDOM",
#     "US": "UNITED STATES",
#     "UM": "UNITED STATES MINOR OUTLYING ISLANDS",
#     "UY": "URUGUAY",
#     "UZ": "UZBEKISTAN",
#     "VU": "VANUATU",
#     "VE": "VENEZUELA, BOLIVARIAN REPUBLIC OF",
#     "VN": "VIET NAM",
#     "VG": "VIRGIN ISLANDS, BRITISH",
#     "VI": "VIRGIN ISLANDS, U.S.",
#     "WF": "WALLIS AND FUTUNA",
#     "EH": "WESTERN SAHARA",
#     "YE": "YEMEN",
#     "ZM": "ZAMBIA",
#     "ZW": "ZIMBABWE"
# }


def convertToWindowsPath(string: Union[str, pathlib.Path]):
    # This converts a str to a Path (if already a Path, nothing changes)
    path = pathlib.Path(string)
    # print(type(path))
    # print(path)
    return path


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

        URL_PATH = 'https://raw.github.com/kwhjvdkamp/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'

        # f-strings provide a way to embed expressions inside string literals using a minimal syntax.
        # It should be noted that an f-string is really an expression evaluated at run time, not a constant value.
        # In Python source code, an f-string is a literal string, prefixed with 'f',
        # which contains expressions inside braces. The expressions are replaced with their values.
        self.URLS = {
            'Confirmed': f'{URL_PATH}/time_series_covid19_confirmed_global.csv',
            'Deceased': f'{URL_PATH}/time_series_covid19_deaths_global.csv',
            'Recovered':f'{URL_PATH}/time_series_covid19_recovered_global.csv',
        }

        self.data = {case:pd.read_csv(url, header=0, escapechar='\\') for case, url in self.URLS.items()}

    # create other useful functions to work with data
    def current_status(self):
        # function to show current status
        pass


# =========================================================================================

print('Count isoCodes', len(CC))

# Original data contains dates formatted like m/d/jj (no preceding zero's and two digit year)
format_str = '%m/%d/%y' # The original date format

csse = Csse()

# Keys of the dictionary
print(csse.data.keys())

# Pivoting columns to rows
confirmedDf = csse.data['Confirmed']
confirmedDfWideToLong = pd.melt(confirmedDf,
                            id_vars=confirmedDf.columns[:4],
                            value_vars = confirmedDf.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Confirmed')
dictConfirmed = {
    'Date': pd.to_datetime(confirmedDfWideToLong['Updated'], format=format_str),
    'Province_State': confirmedDfWideToLong['Province/State'],
    'Country_Region': confirmedDfWideToLong['Country/Region'],
    'Latitude': confirmedDfWideToLong['Lat'],
    'Longitude': confirmedDfWideToLong['Long'],
    # 'ISO': iso_country_codes.CC[confirmedDfWideToLong['Country/Region']],
    'Confirmed': confirmedDfWideToLong['Confirmed']
}
dfConfirmed = pd.DataFrame(dictConfirmed)
dfConfirmed = dfConfirmed.sort_values(by=['Country_Region', 'Date'])
print('AFTER SORTING dfConfirmed', dfConfirmed)
dfConfirmed.sort_values(by=['Date'])
# print('After Melting\r\nDate converted to isoDate as part of new compilated Dataframe\r\n', dfConfirmed)

# print('==================================================')

deceasedDf = csse.data['Deceased']
deceasedDfWideToLong = pd.melt(deceasedDf,
                            id_vars=deceasedDf.columns[:4],
                            value_vars = deceasedDf.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Deceased')
dictDeceased = {
    'Date': pd.to_datetime(deceasedDfWideToLong['Updated'], format=format_str),
    'Province_State': deceasedDfWideToLong['Province/State'],
    'Country_Region': deceasedDfWideToLong['Country/Region'],
    'Latitude': deceasedDfWideToLong['Lat'],
    'Longitude': deceasedDfWideToLong['Long'],
    'Deceased': deceasedDfWideToLong['Deceased']
}
dfDeceased = pd.DataFrame(dictDeceased)
dfDeceased = dfDeceased.sort_values(by=['Country_Region', 'Date'])
print('AFTER SORTING dfDeceased', dfDeceased)
dfDeceased.sort_values(by=['Date'])
# print('After Melting\r\nDate converted to isoDate as part of new compilated Dataframe\r\n', dfDeceased)

# print('==================================================')

recoveredDf = csse.data['Recovered']
recoveredDfWideToLong = pd.melt(recoveredDf,
                            id_vars=recoveredDf.columns[:4],
                            value_vars = recoveredDf.columns[4:],
                            var_name = 'Updated',
                            value_name = 'Recovered')
dictRecovered = {
    'Date': pd.to_datetime(recoveredDfWideToLong['Updated'], format=format_str),
    'Province_State': recoveredDfWideToLong['Province/State'],
    'Country_Region': recoveredDfWideToLong['Country/Region'],
    'Latitude': recoveredDfWideToLong['Lat'],
    'Longitude': recoveredDfWideToLong['Long'],
    'Recovered': recoveredDfWideToLong['Recovered']
}
dfRecovered = pd.DataFrame(dictRecovered)
dfRecovered = dfRecovered.sort_values(by=['Country_Region', 'Date'])
print('AFTER SORTING dfRecovered', dfRecovered)
dfRecovered.sort_values(by=['Date'])
# print('After Melting\r\nDate converted to isoDate as part of new compilated Dataframe\r\n', dfRecovered)

# print('==================================================')

print('C', dfConfirmed.head())
print('C', dfConfirmed.tail())

print('D', dfDeceased.head())
print('D', dfDeceased.tail())

print('R', dfRecovered.head())
print('R', dfRecovered.tail())

# print('==================================================')

doWrite = False
if doWrite:

    currentContainer = pathlib.Path(__file__).parent.absolute()
    path = str(currentContainer)

    pathToWriteTo = ''
    # current working folder
    if path.__contains__('HomeProjects'):
        # On Laptop write to >>> C:\HomeProjects\COVID-19-Data\bing-data\accumulation\csv-data-bing
        pathToWriteTo = convertToWindowsPath(path.replace('Python\PythonTutorial\download_csv', 'COVID-19-Data\\csse-data\\'))
        print('Laptop:', pathToWriteTo)
    elif path.__contains__('GitHubRepositories'):
        # On Desktop write to >>> C:\GithubRepositories\COVID-19-Data\bing-data\accumulation\csv-data-bing
        pathToWriteTo = convertToWindowsPath(path.replace('PythonTutorial\download_csv', 'COVID-19-Data\\csse-data\\'))
        print('Desktop:', pathToWriteTo)
    else:
        print('Wrong:', path)

    dfConfirmed.to_csv(os.path.join(pathToWriteTo, r'csse_confirmed.csv'))
    dfDeceased.to_csv(os.path.join(pathToWriteTo, r'csse_deceased.csv'))
    dfRecovered.to_csv(os.path.join(pathToWriteTo, r'csse_recovered.csv'))

else:
    print('\r\n=====================\r\nNo file writing')
