import investpy as iv
import numpy as np
from sklearn import preprocessing
from tqdm import tqdm
from bond_yield_data import get_data, standardize_data
import pickle
import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)

df = pd.DataFrame({"col1": [i for i in range(20)]})

periods = 5

def periods_to_see_back(df, periods):

    initial_variables = list(df.columns.values)

    for variable in initial_variables:
        for i in range(1, periods+1):
            df[f"{variable} t-{i}"] = df[variable].shift(periods = i)
    
    df = df.dropna()

    return df


dfalt = periods_to_see_back(df, periods)

print(dfalt)
