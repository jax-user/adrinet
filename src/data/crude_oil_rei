import numpy as np
import pandas as pd
import yfinance as yf
from sklearn import preprocessing

crude_oil = yf.Ticker('CL=F')
crude_oil_data = crude_oil.history(period = 'max')
crude_oil_data = crude_oil_data.drop(['Volume', 'Dividends', 'Stock Splits'], axis = 1)
crude_oil_data = crude_oil_data.pct_change()[1:]

for column in crude_oil_data: 
    mean = np.mean(crude_oil_data[column])
    std = np.std(crude_oil_data[column])
    crude_oil_data[column] = (crude_oil_data[column] - mean)/std

scalar = preprocessing.MinMaxScaler()
crude_oil_data[['Open', 'High', 'Low', 'Close']] = scalar.fit_transform(crude_oil_data[["Open", "High", "Low", "Close"]])
crude_oil_data.to_csv('data/cleaned/crude_oil_cleaned.csv')