# light/after.py
import pandas as pd
import sys

def after_date(df, date):
    return df[df.index > date]

def main(df, date):
    date = pd.to_datetime(date).date()
    return after_date(df, date)
