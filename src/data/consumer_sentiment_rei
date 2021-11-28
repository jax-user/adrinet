import numpy as np
import pandas as pd
from sklearn import preprocessing

df = pd.read_csv('data/raw/Consumer_sentiment.csv', index_col = 0)
df.index = pd.to_datetime(df['DATE'])
df = df['1978-01-01':]
df.index.names = ['Date']
df = df.rename(columns={"UMCSENT": "Total"})

mean = np.mean(df['Total'])
std = np.std(df['Total'])
df['Total'] = (df['Total'] - mean)/std

scalar = preprocessing.MinMaxScaler()
df[['Total']] = scalar.fit_transform(df[['Total']])
df.to_csv('data/cleaned/consumer_sentiment_cleaned.csv')