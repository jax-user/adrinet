import numpy as np
import pandas as pd
import yfinance as yf

gold = yf.Ticker('GC=F')
gold_data = gold.history(period = 'max')
gold_data.head()
gold.to_csv()