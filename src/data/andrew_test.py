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

infile = open("all_bond_data_cleaned_seperate", "rb")
list = pickle.load(infile)
infile.close()

combined_df = pd.concat(list, axis = 1, join="inner")

print(combined_df.describe())
print(combined_df.isna().sum())

print(combined_df)


