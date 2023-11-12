# light/cumsum.py
import pandas as pd
import sys

def cumulative_sum(df):
    return df.cumsum()

def main(args):
    df = pd.read_csv(sys.stdin)
    result = cumulative_sum(df)
    result.to_csv(sys.stdout, index=False)
