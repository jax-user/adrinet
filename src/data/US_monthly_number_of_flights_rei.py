import numpy as np
import pandas as pd
from sklearn import preprocessing

df = pd.read_csv('data/raw/US_monthly_number_of_flights.csv', index_col = 'Period', skiprows = [0, 1], skipfooter = 1)
df.index = pd.to_datetime(df.index)
mean = np.mean(df['Total'])
std = np.std(df['Total'])
df['Total'] = (df['Total'] - mean)/std

scaler = preprocessing.MinMaxScaler()
df[['Total']] = scalar.fit_transform(df[['Total']])

df.to_csv('data/cleaned/US_monthly_number_of_flights_cleaned.csv')