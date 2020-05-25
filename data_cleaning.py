import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import pycats
import seaborn as sns
plt.style.use('fivethirtyeight')
pd.set_option('display.max_columns',150)

df = pd.read_csv('fifa_19.csv')

#df.columns

# removing non-numeric data

df = df.drop(['Unnamed: 0','Photo','Flag','Club Logo','Loaned From'], axis = 1)

# removing position specific attributes

df = df.drop(['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
       'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
       'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'], axis = 1)

# checking for null values
#df.isnull().sum().sort_values(ascending = False)

# replace missing values
df['ShortPassing'].fillna(df['ShortPassing'].median(), inplace = True)
df['Volleys'].fillna(df['Volleys'].median(), inplace = True)
df['Dribbling'].fillna(df['Dribbling'].median(), inplace = True)
df['Curve'].fillna(df['Curve'].median(), inplace = True)
df['FKAccuracy'].fillna(df['FKAccuracy'], inplace = True)
df['LongPassing'].fillna(df['LongPassing'].median(), inplace = True)
df['BallControl'].fillna(df['BallControl'].median(), inplace = True)
df['HeadingAccuracy'].fillna(df['HeadingAccuracy'].median(), inplace = True)
df['Finishing'].fillna(df['Finishing'].median(), inplace = True)
df['Crossing'].fillna(df['Crossing'].median(), inplace = True)
df['Contract Valid Until'].fillna(2020, inplace = True)
df['Joined'].fillna('Jul 1, 2018', inplace = True)
df['Jersey Number'].fillna(8, inplace = True)
df['Body Type'].fillna('Normal', inplace = True)
df['Position'].fillna('ST', inplace = True)
df['Club'].fillna('No Club', inplace = True)
df['Work Rate'].fillna('Medium/ Medium', inplace = True)
df['Skill Moves'].fillna(df['Skill Moves'].median(), inplace = True)
df['Weak Foot'].fillna(3, inplace = True)
df['Preferred Foot'].fillna('Right', inplace = True)
df['International Reputation'].fillna(1, inplace = True)

# non-numeric data
df.loc[10:20,['Wage','Value','Release Clause','Weight','Height']]

# cleaning the above columns
def extract_value_from(Value):
    if type(Value) == float:
        return Value
    else:  
        out = Value.replace('€', '')
        if 'M' in out:
            out = float(out.replace('M', ''))*1000000
        elif 'K' in out:
            out = float(out.replace('K', ''))*1000
        elif 'lbs' in Value:
            out = float(Value.replace('lbs',''))
        elif "'" in Value:
            h = Value.split("'",1)
            ft = int(h[0])
            inch = int(h[1])
            out = float(ft * 12 + inch)
        return float(out)

df['Wage'] = df['Wage'].apply(lambda x: extract_value_from(x))
df['Value'] = df['Value'].apply(lambda x: extract_value_from(x))
df['Release Clause'] = df['Release Clause'].apply(lambda x:extract_value_from(x))
df['Weight'] = df['Weight'].apply(lambda x:extract_value_from(x))
df['Height'] = df['Height'].apply(lambda x:extract_value_from(x))

df.to_csv('data_clean.csv', index = False)