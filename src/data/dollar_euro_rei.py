import numpy as np
import pandas as pd
import yfinance as yf
from sklearn import preprocessing

dollar_euro = yf.Ticker('GC=F')
dollar_euro_data = dollar_euro.history(period = 'max')
dollar_euro_data = dollar_euro_data.drop(['Volume', 'Dividends', 'Stock Splits'], axis = 1)
dollar_euro_data = dollar_euro_data.pct_change()[1:]

for column in dollar_euro_data: 
    mean = np.mean(dollar_euro_data[column])
    std = np.std(dollar_euro_data[column])
    dollar_euro_data[column] = (dollar_euro_data[column] - mean)/std

scalar = preprocessing.MinMaxScaler()
dollar_euro_data[['Open', 'High', 'Low', 'Close']] = scalar.fit_transform(dollar_euro_data[["Open", "High", "Low", "Close"]])
dollar_euro_data.to_csv('data/cleaned/dollar_euro_cleaned.csv')