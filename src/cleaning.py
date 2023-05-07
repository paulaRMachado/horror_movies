import pandas as pd

def clean_local (df1):
    """
    This drops a few unnecessary columns, creates a new column year_release. Also simplifies the column genre
    args
    :df: dataframe to be cleaned
    return: cleaned dataframe
    """
    # 1. Overall cleaning
    # drop columns from the dataframe
    columns_to_drop = ["Unnamed: 0","runtime", "collection","revenue", "adult","poster_path","original_title", "id", "status", "backdrop_path","overview","tagline"]
    df1.drop(columns = columns_to_drop, inplace=True)

    df1["year_release"] = [i[:4] for i in df1["release_date"]]

    def remove_prefix(x):
        """
        This function removes the genre HORROR from column genre_names. Should be used with the apply method. 
        args
        :x: column item in a dataframe column to be cleaned
        return: cleaned column
        """
        if isinstance(x, str) and x.startswith("Horror, "):
            return x[8:]
        else:
            return x
        

    df1["genre_names"] = df1["genre_names"].apply(remove_prefix)
    df1["genre_names"] = [i.split(",")[0].strip() for i in df1.genre_names]

    # 3. Export and read
    df1.to_csv("data/horror_clean.csv", index=False)
    df1 = pd.read_csv("data/horror_clean.csv")
    return df1

def clean_acquired (df2):
    """
    This function converts columns data from string to ints and floats. Also, sets box office values to match budget values. 
    args
    :df2: a dataframe to be cleaned
    return: cleaned column
    """
    df2["US_box_office"] = df2["US_box_office"].astype(float)*1000000
    df2["runtime"] = df2["runtime"].astype(int)
    df2["imdb_rating"] = df2["imdb_rating"].astype(float)
    return df2

def assemble(df1,df2):
    """
    This function merges 2(two) dataframes under the key title.
    Also creates a profit column with information from both dataframes.
    args
    :df1: a dataframe
    :df2: a dataframe
    return: a merged dataframe
    """
    merged_df = pd.merge(df1, df2, on='title')
    merged_df["profit"] = merged_df["US_box_office"] - merged_df["budget"]
    return merged_df