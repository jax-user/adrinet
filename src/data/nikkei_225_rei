import numpy as np
import pandas as pd
import yfinance as yf
from sklearn import preprocessing

nikkei_225 = yf.Ticker('^N225')
nikkei_225_data = nikkei_225.history(period = 'max')
nikkei_225_data = nikkei_225_data.drop(['Volume', 'Dividends', 'Stock Splits'], axis = 1)
nikkei_225_data = nikkei_225_data.pct_change()[1:]

for column in nikkei_225_data: 
    mean = np.mean(nikkei_225_data[column])
    std = np.std(nikkei_225_data[column])
    nikkei_225_data[column] = (nikkei_225_data[column] - mean)/std

scalar = preprocessing.MinMaxScaler()
nikkei_225_data[['Open', 'High', 'Low', 'Close']] = scalar.fit_transform(nikkei_225_data[["Open", "High", "Low", "Close"]])
nikkei_225_data.to_csv('data/cleaned/nikkei_225_cleaned.csv')