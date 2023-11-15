# light/momentum.py
import pandas as pd
import sys

def calculate_momentum(df, lookback_period, frequency):
    """
    Calculate momentum as the percentage change of prices over a lookback period.

    :param df: Pandas DataFrame with datetime index and price data.
    :param lookback_period: Integer, number of periods over which to calculate momentum.
    :return: Pandas DataFrame with momentum values.
    """
    # Ensure frequency is at least 1
    frequency = max(1, frequency)

    # Calculate pct_change and then take every 'frequency' rows
    momentum = df.pct_change(periods=lookback_period).iloc[::frequency]
    return momentum
    return momentum

def main(df, lookback, frequency):
    lookback = int(lookback)
    frequency = int(frequency)
    if df is None:
        raise ValueError("No data available for momentum calculation.")
    return calculate_momentum(df, lookback, frequency)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
