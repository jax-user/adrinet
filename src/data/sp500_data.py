import yfinance as yf
import pandas as pd
from bond_yield_data import standardize_data, append_name_to_columns
from sklearn import preprocessing
import numpy as np

def get_sp500_pct_change_data():
    sp500 = yf.Ticker("^GSPC")

    data = sp500.history(period = "max").drop(["Dividends", "Stock Splits"], axis = 1).replace(0, np.nan).fillna(method="ffill").pct_change()[1:] # lazy code

    data_standardized = standardize_data(data)

    scalar = preprocessing.MinMaxScaler()

    columns = list(data_standardized.columns.values)

    data_standardized_copy = data_standardized.copy()

    data_standardized_copy[columns] = scalar.fit_transform(data_standardized_copy[columns])

    data_standardized_copy = append_name_to_columns("SP500", data_standardized_copy)

    return data_standardized_copy

# lets us include previous price data
def periods_to_see_back(df, periods):

    initial_variables = list(df.columns.values)

    for variable in initial_variables:
        for i in range(1, periods+1):
            df[f"{variable} t-{i}"] = df[variable].shift(periods = i)
    
    df = df.dropna()

    return df

#def days_to_see_back(dataframe, days):

if __name__ == '__main__':
    data = get_sp500_pct_change_data()

    data = periods_to_see_back(data, 10)
    print(data)
    data.to_csv("data/cleaned/sp500_cleaned_andrew.csv")