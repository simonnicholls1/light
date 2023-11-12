# light/vol_scale.py
import pandas as pd
import sys

def calculate_rolling_volatility(df, window_size):
    return df.rolling(window=window_size).std()

def scale_volatility(df, target_volatility):
    return df / df.std() * target_volatility

def main(args):
    window_size, target_volatility = int(args[0]), float(args[1])
    df = pd.read_csv(sys.stdin)
    rolling_vol = calculate_rolling_volatility(df, window_size)
    scaled_vol = scale_volatility(rolling_vol, target_volatility)
    scaled_vol.to_csv(sys.stdout, index=False)
