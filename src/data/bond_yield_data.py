import investpy as iv
import numpy as np
from sklearn import preprocessing
from tqdm import tqdm
import pickle
import pandas as pd

def standardize_data(df):
    """function that standardizes the data in a dataframe assuming that the varaibles are the columns

    Args:
        df (pandas.DataFrame): a pandas dataframe with the data. a column sould represent a variable

    Returns:
        pandas.DataFrame : modified Dataframe
    """
    for column in df:
        mean = np.mean(df[column])
        std = np.std(df[column])
        df[column] = (df[column] - mean) / std

    return df


def append_name_to_columns(name, dataframe):
    """This function just adds a name to the variable so that users can identify the variable.

    Args:
        name (string): name to be appended
        dataframe (pandas.DataFrame): a pandas dataframe with the data. N x D dataframe with N examples and D dimensions
    """
    renamed_dataframe = dataframe.rename(columns = {old_name: f"{name} {old_name}" for old_name in dataframe})
    return renamed_dataframe


def get_data(bond):
    try:
        # get the seach result class of investpy as a varaible
        search_results = iv.search_quotes(text = bond, products=["bonds"], n_results=1)

        # obtain the historical price data 
        yield_data = search_results.retrieve_historical_data(from_date = "01/01/2000", to_date = "26/11/2021")

        # drop the "Change Pct" column
        yield_data = yield_data.drop(["Change Pct"], axis = 1)

        # transform other columns to percentage change and remove the redundant first row
        yield_data = yield_data.diff()[1:]
        
        # use rename function to specify names so that people can examine dataframe
        renamed_dataframe = append_name_to_columns(bond, yield_data)

        # standardize data with function defined above
        renamed_dataframe = standardize_data(renamed_dataframe)

        # apply sklearn MinMaxScalar
        scalar = preprocessing.MinMaxScaler()

        # ake a copy of the dataframe
        renamed_dataframe_copy = renamed_dataframe.copy()

        # get column headers as list for MinMaxScalar argument
        column_titles = list(renamed_dataframe_copy.columns.values)

        # using MinMaxScalar to scale all data down to values between 0 and 1
        renamed_dataframe_copy[column_titles] = scalar.fit_transform(renamed_dataframe_copy[column_titles])

        return renamed_dataframe_copy
    except:
        return None


if __name__ == '__main__':
    # This first section contained code that was needed to create a pickle object, now the pickle object is just read in to save time

    # # countries and duration of the bond data that we want to collect. These lists will be used to catenate into strings
    # countries = ["us", "uk"]
    # durations = ["1 year", "3 year", "5 year", "10 year", "30 year"]

    # # all possible combinations of above to acquire the search input for investpy for the bond yields of all three countries
    # all_bonds = [f"{country} {duration} bond" for country in countries for duration in durations]

    # all_bond_df = []

    # for bond in tqdm(all_bonds):
    #     bond_df_cleaned = get_data(bond)
    #     all_bond_df.append(bond_df_cleaned)

    infile = open("all_bond_data_cleaned_seperate", "rb")
    list = pickle.load(infile)
    infile.close()

    combined_df = pd.concat(list, axis = 1, join="inner")

    combined_df.to_csv("data/cleaned/us_uk_bond_yield_data.csv")