# light/signal.py
import pandas as pd
import sys
from stack_manager import push_to_stack
import numpy as np

def calculate_log_returns(df):
    """
    Calculate the logarithmic returns of DataFrame columns.

    :param df: Pandas DataFrame with numeric data.
    :return: DataFrame with logarithmic returns.
    """
    if df is None:
        raise ValueError("No data available in the stack for log return calculation.")
    if not all(df.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise ValueError("All columns in the DataFrame must be numeric to calculate log returns.")

    log_returns = np.log(df / df.shift(1))
    return log_returns

def main(df):
    result = calculate_log_returns(df)
    push_to_stack(result)
    result.to_csv(sys.stdout, index=True)
