import pandas as pd


def load_dataframe(path):
    """
    This Functions is getting a path to excel file
    and loads it into a pandas Dataframe
    :param path: the path to the excel file
    :return: pandas Dataframe
    """
    df = pd.read_excel(path)
    return df


def fill_na(dataframe):
    """
    This Functions is getting a pandas Dataframe that might contains na fields
    and returns the Dataframe with no na fields
    :param dataframe: the pandas dataframe to fill na values to
    :return: pandas dataframe with no na values
    """
    empty_cols = [col for col in dataframe.columns if dataframe[col].isnull().any()]
    for col in empty_cols:
        dataframe[col].fillna(dataframe[col].mean(), inplace=True)
    return dataframe


def standardization(dataframe):
    """
    This Function is getting a pandas Dataframe and standardizes its values
    only for a float64 datatype columns
    :param dataframe: the dataframe which should me standardizes
    """
    for col in dataframe.columns:
        if("float" in str(dataframe[col].dtype)):
            mean = dataframe[col].mean()
            std = dataframe[col].std()
            stand = lambda x: (x - mean) / std
            dataframe[col] = dataframe[col].apply(stand)
    return dataframe

def group_values_by_year_per_country(dataframe):
    """
    This Function is getting a pandas Dataframe
    and groups all the values of each column by calculating
    the mean of the column for each country by its years
    :param dataframe: the Dataframe to group its values
    :returns new_df: the new Dataframe contains only grouped mean values
    """
    new_df = pd.DataFrame(dataframe)
    new_df = new_df.drop('year', axis=1)
    new_df = new_df.groupby('country', as_index=False).mean()

    return new_df


def pre_process(dataframe):
    """
    This Function is getting a dataframe and start the preprocessing step on it
    :param dataframe: the pandas Dataframe to preprocess
    :return: the preprocessed dataframe
    """
    preprocessed_dataframe = fill_na(dataframe)
    preprocessed_dataframe = standardization(preprocessed_dataframe)
    preprocessed_dataframe = group_values_by_year_per_country(preprocessed_dataframe)

    return preprocessed_dataframe