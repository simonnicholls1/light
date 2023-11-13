# light/signal.py
import pandas as pd
import sys

def calculate_signal(df):
    return df.applymap(lambda x: 1 if x > 0 else -1)

def main(df):
    result = calculate_signal(df)
    result.to_csv(sys.stdout, index=True)
