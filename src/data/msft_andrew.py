import yfinance as yf


msft = yf.Ticker("MSFT")


# get historical market data
hist = msft.history(period="max")


print(msft.balance_sheet)