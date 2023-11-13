# light/before.py
import pandas as pd
import sys

def before_date(df, date):
    return df[df.index < pd.to_datetime(date)]

def main(df, date):
    date = pd.to_datetime(date)
    result = before_date(df, date)
    result.to_csv(sys.stdout, index=True)
