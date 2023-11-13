# light/cgrep.py
import pandas as pd
from .stack_manager import push_to_stack, get_from_stack

def filter_columns(df, column_names):
    """
    Filter DataFrame columns based on a list of column names.

    :param df: Pandas DataFrame.
    :param column_names: List of column names to retain.
    :return: Filtered DataFrame.
    """
    filtered_df = df[column_names]
    return filtered_df

def main(args):
    column_names = args  # List of column names
    df = get_from_stack()
    if df is None:
        raise ValueError("No data available in the stack for column filtering.")
    result = filter_columns(df, column_names)
    push_to_stack(result)  # Push the result onto the stack
    result.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
