# light/before.py
import pandas as pd
import sys

def before_date(df, date):
    return df[df.index < pd.to_datetime(date)]

def main(args):
    date = args[0]
    df = pd.read_csv(sys.stdin, parse_dates=True, index_col=0)
    result = before_date(df, date)
    result.to_csv(sys.stdout, index=False)
