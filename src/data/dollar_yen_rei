import numpy as np
import pandas as pd
import yfinance as yf
from sklearn import preprocessing

dollar_yen = yf.Ticker('JPY=X')
dollar_yen_data = dollar_yen.history(period = 'max')
print(dollar_yen_data)

dollar_yen_data = dollar_yen_data.drop(['Volume', 'Dividends', 'Stock Splits'], axis = 1)
dollar_yen_data = dollar_yen_data.pct_change()[1:]

for column in dollar_yen_data: 
    mean = np.mean(dollar_yen_data[column])
    std = np.std(dollar_yen_data[column])
    dollar_yen_data[column] = (dollar_yen_data[column] - mean)/std

scalar = preprocessing.MinMaxScaler()
dollar_yen_data[['Open', 'High', 'Low', 'Close']] = scalar.fit_transform(dollar_yen_data[["Open", "High", "Low", "Close"]])
dollar_yen_data.to_csv('data/cleaned/dollar_yen_cleaned.csv')