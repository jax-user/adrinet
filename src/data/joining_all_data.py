import pandas as pd
import os

def get_all_clean_data_paths():
    
    all_cleaned_data_paths = []

    for filename in os.listdir("data/cleaned"):
        if filename.endswith(".csv"):
            path = os.path.join("data/cleaned", filename)
            all_cleaned_data_paths.append(path)

    return all_cleaned_data_paths


def cleaned_data_paths_to_list_of_df(path_list):
    list_of_df = [pd.read_csv(path, index_col=0) for path in path_list]
    return list_of_df



if __name__ == "__main__":
    # get all paths in our clean data dir
    list_of_paths = get_all_clean_data_paths()

    # remove the one that has data frequency of month, we will deal with this later
    list_of_paths.remove("data/cleaned/consumer_sentiment_cleaned.csv")
    list_of_paths.remove("data/cleaned/US_monthly_number_of_flights_cleaned.csv")

    # get list of DataFrames to prepare to merge the dataframes
    list_of_dfs = cleaned_data_paths_to_list_of_df(list_of_paths)

    # join the dataframes together
    combined_dfs_with_day_frequencies = pd.concat(list_of_dfs, axis = 1, join = 'inner')

    combined_dfs_with_day_frequencies.to_csv("data/master.csv")
