import numpy as np
import pandas as pd
import yfinance as yf
from sklearn import preprocessing

ftse_100 = yf.Ticker('^FTSE')
ftse_100_data = ftse_100.history(period = 'max')
ftse_100_data = ftse_100_data.drop(['Volume', 'Dividends', 'Stock Splits'], axis = 1)
ftse_100_data = ftse_100_data.pct_change()[1:]

for column in ftse_100_data: 
    mean = np.mean(ftse_100_data[column])
    std = np.std(ftse_100_data[column])
    ftse_100_data[column] = (ftse_100_data[column] - mean)/std

scalar = preprocessing.MinMaxScaler()
ftse_100_data[['Open', 'High', 'Low', 'Close']] = scalar.fit_transform(ftse_100_data[["Open", "High", "Low", "Close"]])
ftse_100_data.to_csv('data/cleaned/ftse_100_cleaned.csv')