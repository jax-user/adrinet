import numpy as np
import pandas as pd
import yfinance as yf
from sklearn import preprocessing

gold = yf.Ticker('GC=F')
gold_data = gold.history(period = 'max')
gold_data = gold_data.drop(['Volume', 'Dividends', 'Stock Splits'], axis = 1)
gold_data = gold_data.pct_change()[1:]

for column in gold_data: 
    mean = np.mean(gold_data[column])
    std = np.std(gold_data[column])
    gold_data[column] = (gold_data[column] - mean)/std

scalar = preprocessing.MinMaxScaler()
gold_data[['Open', 'High', 'Low', 'Close']] = scalar.fit_transform(gold_data[["Open", "High", "Low", "Close"]])
gold_data.to_csv('data/cleaned/gold_cleaned .csv')