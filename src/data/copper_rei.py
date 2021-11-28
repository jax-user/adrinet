import numpy as np
import pandas as pd
import yfinance as yf
from sklearn import preprocessing

copper = yf.Ticker('HG=F')
copper_data = copper.history(period = 'max')
copper_data = copper_data.drop(['Volume', 'Dividends', 'Stock Splits'], axis = 1)
copper_data = copper_data.pct_change()[1:]

for column in copper_data: 
    mean = np.mean(copper_data[column])
    std = np.std(copper_data[column])
    copper_data[column] = (copper_data[column] - mean)/std

scalar = preprocessing.MinMaxScaler()
copper_data[['Open', 'High', 'Low', 'Close']] = scalar.fit_transform(copper_data[["Open", "High", "Low", "Close"]])
copper_data.to_csv('data/cleaned/copper_cleaned.csv')