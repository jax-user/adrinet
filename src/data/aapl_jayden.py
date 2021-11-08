import yfinance as yf
import pandas as pd

pd.set_option('display.max_columns', 10)

aapl = yf.Ticker("aapl")


# get historical market data
hist = aapl.history(period="max")

print(hist)