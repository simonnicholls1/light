# light/vol_scale.py
from math import sqrt

def calculate_rolling_volatility(df, window_size):
    return df.rolling(window=window_size).std() * sqrt(window_size)

def vol_scale_factor(rolling_vol, target_volatility):
    return target_volatility/rolling_vol

def main(df, window_size, target_vol):
    rolling_vol = calculate_rolling_volatility(df, window_size)
    scaled_vol_factors = vol_scale_factor(rolling_vol, target_vol)
    return df * scaled_vol_factors
