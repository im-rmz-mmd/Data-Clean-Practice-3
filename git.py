# Import Python Libraries
import pandas as pd
import numpy as np
from colorama import Fore

# Import Dataset
df = pd.read_csv("git.csv")

# Remove Extra Columns
df = df.drop(['Column1', 'Column2', 'Column3', 'Column5', 'Column7', 'Column8', 'Column11',
              'Column12', 'Column13'], axis= 1)

# Change Columns Name
df = df.rename(columns= {'Column4': 'Eduction', 'Column6': 'Marriage', 'Column9': 'Skin',
                         'Column10': 'Gender', 'Column14': 'Country', 'Column15': 'Salary'})

# Remove Duplicates ana Nan Values
df = df.drop_duplicates()
df = df.dropna()

# Change Values Name = Eduction
df['Eduction'] = df['Eduction'].str.split(pat= '-').str[0]
df['Eduction'] = df['Eduction'].replace({' HS': 'High School'})

# Change Values Name = Marriage
df['Marriage'] = df['Marriage'].str.split(pat= '-').str[0]
df['Marriage'] = df['Marriage'].replace({' Never': 'Single'})

# Change Values Name = Skin
df['Skin'] = df['Skin'].str.split(pat= '-').str[0]
df['Skin'] = df['Skin'].replace({' Amer':'Other'})

# Change Name and Remove Nan Values = Country
df['Country'] = df['Country'].str.split(pat= '-').str[0]
df['Country'] = df['Country'].replace({' ?': np.nan, ' United': 'United States', ' El': 'El Salvador',
                                       ' Dominican': 'Dominican Republic', ' Trinadad&Tobago': 'Trinadad and Tobago',
                                       ' Puerto': 'Puerto Rico'})
df = df.dropna()

# Change Values Name = Salary
df['Salary'] = df['Salary'].replace({' <=50K': 'More Than 50K'})
df['Salary'] = df['Salary'].replace({' >50K': 'Less Than 50K'})

# Output and illustration
print(df,
      Fore.GREEN + "\nMost Users have %s Eduction" %(df['Eduction']).value_counts().first_valid_index(),
      Fore.CYAN + "\nMost Users are %s" %(df['Marriage']).value_counts().first_valid_index(),
      Fore.BLUE + "\nMost Users are %s" %(df['Gender']).value_counts().first_valid_index(),
      Fore.RED + "\nMost Users have %s skin" %(df['Skin']).value_counts().first_valid_index(),
      Fore.MAGENTA + "\nMost Users are from %s" %(df['Country']).value_counts().first_valid_index(),
      Fore.YELLOW + "\nMost Users Income is %s" %(df['Salary']).value_counts().first_valid_index())