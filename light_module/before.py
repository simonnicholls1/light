# light/before.py
import pandas as pd

def before_date(df, date):
    return df[df.index < pd.to_datetime(date)]

def main(df, date):
    date = pd.to_datetime(date)
    return before_date(df, date)
