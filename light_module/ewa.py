# light/ewa.py
import pandas as pd
import sys

def equally_weighted_average(df):
    return df.mean(axis=1)

def main(df):
    result = equally_weighted_average(df)
    return result[~result.isna()]
