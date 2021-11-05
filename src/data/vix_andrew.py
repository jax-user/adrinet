import yfinance as yf

# getting VIX data
vix = yf.Ticker("^vix")
hist = vix.history(period='max').drop(['Volume', 'Dividends', 'Stock Splits'], axis=1)

#Check Missing datapoints
na = hist.isna().sum()
print(f'number of NaN datapoints:\n{na}')

#Visualise data
print(hist)

#Store output as csv in 'data' directory
hist.to_csv("data/cleaned/vix_cleaned_andrew.csv")