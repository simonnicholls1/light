# light/vol_scale.py
from math import sqrt

import pandas as pd
import sys

def calculate_rolling_volatility(df, window_size):
    return df.rolling(window=window_size).std() * sqrt(window_size)

def scale_volatility(df, target_volatility):
    return df / df.std() * target_volatility

def main(df, window_size, target_volatility):
    prices = get_from_stack_pos(0)
    rolling_vol = calculate_rolling_volatility(df, window_size)
    scaled_vol = scale_volatility(rolling_vol, target_volatility)
    scaled_vol.to_csv(sys.stdout, index=False)
