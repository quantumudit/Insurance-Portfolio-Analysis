# -- Importing Libraries -- #

print('\n')
print('Importing libraries to perform ETL...')

import numpy as np
import pandas as pd
import pyfiglet

import warnings
warnings.filterwarnings('ignore')

print('Initiating ETL Process...')
print('\n')

# -- Starting ETL Process --#

etl_title = "INSURANCE DATA ETL"
ascii_art_title = pyfiglet.figlet_format(etl_title, font='small')
print(ascii_art_title)
print('\n')

# -- Connecting to Dataset -- #

print('Connecting to source dataset')

source_data = pd.read_csv('../01_SOURCE/fl_Insurance_portfolio_raw_data.csv', index_col=None)

print(f'Columns in the source dataset: {list(source_data.columns)}')
print(f'Shape of the source dataset: {source_data.shape}')
print('\n')

# -- Removing Unnecessary Columns -- #

print('Removing unnecessary columns')

keep_columns = ['policyID', 'line', 'construction', 'county', 'point_latitude', 'point_longitude', 'tiv_2020', 'tiv_2021']

insurance_df = source_data[keep_columns]

print(f'Columns in the dataset after removing unnecessary columns: {list(insurance_df.columns)}')
print(f'Shape of the dataset after removing unnecessary columns: {insurance_df.shape}')
print('\n')

# -- Renaming Columns -- #

print('Renaming columns')

new_column_names = ['PolicyID','Line', 'Construction', 'County', 'Latitude', 'Longitude', 'TIV-2020', 'TIV-2021']
insurance_df.columns = new_column_names

print(f'Columns in the dataset after renaming: {list(insurance_df.columns)}')
print(f'Shape of the dataset after renaming: {insurance_df.shape}')
print('\n')

# -- Replacing Unwanted Characters from "County" Column -- #

print(f'Unique items in "County" column:\n{insurance_df["County"].unique()}\n')
print('Replacing unwanted characters from "County" column')

insurance_df['County'] = insurance_df['County'].str.replace(' COUNTY','').str.title()

print(f'Unique items in "County" column after cleaning:\n{insurance_df["County"].unique()}\n')

# -- Checking Uniqueness of "PolicyID" Column -- #

print(f'Is "PolicyID column is unique: {insurance_df["PolicyID"].is_unique}\n')

print(f'Snippet of the transformed dataframe:\n{insurance_df.head()}')
print('\n')

# -- Exporting Data to CSV File --#

print('Exporting the dataframe to CSV file...')

insurance_df.to_csv('../03_DATA/fl_insurance_portfolio_data.csv', encoding='utf-8', index=False)

print('Data exported to CSV...')
print('ETL Process completed !!!')