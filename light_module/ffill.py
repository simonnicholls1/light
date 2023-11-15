import pandas as pd

# Example structure for the 'load' command
def ffill(df):
    return df.fillna(method='ffill')

def main(df):
    return ffill(df)