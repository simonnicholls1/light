# light/ewa.py
import pandas as pd
import sys

def equally_weighted_average(df):
    return df.mean(axis=1)

def main(args):
    df = pd.read_csv(sys.stdin)
    result = equally_weighted_average(df)
    result.to_csv(sys.stdout, index=False)
