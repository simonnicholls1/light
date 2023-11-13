# light/momentum.py
import pandas as pd
from .stack_manager import push_to_stack, get_from_stack
import sys

def calculate_momentum(df, lookback_period):
    """
    Calculate momentum as the percentage change of prices over a lookback period.

    :param df: Pandas DataFrame with datetime index and price data.
    :param lookback_period: Integer, number of periods over which to calculate momentum.
    :return: Pandas DataFrame with momentum values.
    """
    momentum = df.pct_change(periods=lookback_period)
    return momentum

def main(df, lookback):
    lookback_period = int(lookback)
    # df = get_from_stack()
    if df is None:
        raise ValueError("No data available in the stack for momentum calculation.")
    result = calculate_momentum(df, lookback_period)
    push_to_stack(result)  # Push the result onto the stack
    result.to_csv(sys.stdout, index=True)  # Optional: output the result

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
