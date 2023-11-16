# light/cumsum.py
import pandas as pd
import sys

def cumulative_sum(df, start_number):
    df.dropna(inplace=True)
    if isinstance(df, pd.DataFrame):
        df.iloc[0] += start_number
    else:  # it's a Series
        df.iloc[0] += start_number
    # Calculate cumulative sum
    cumsum_df = df.cumsum()
    return cumsum_df


def main(df, start_number):
    return cumulative_sum(df, start_number)
