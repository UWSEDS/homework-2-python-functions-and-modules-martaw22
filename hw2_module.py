import pandas as pd

#Function to create a dataframe from a URL

def read_df_from_url(url):
    df = pd.read_csv(url)
    return df


#function to test the properties of a dataframe

def test_create_dataframe(dataframe, list_colnames):
    if list(dataframe.columns) == list_colnames and len(set(list(dataframe.dtypes))) == 1 and dataframe.shape[0] >= 10:
        return True
