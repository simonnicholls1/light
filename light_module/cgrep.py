# light/cgrep.py

def filter_columns(df, column_names):
    """
    Filter DataFrame columns based on a list of column names.

    :param df: Pandas DataFrame.
    :param column_names: List of column names to retain.
    :return: Filtered DataFrame.
    """
    filtered_df = df[column_names]
    return filtered_df

def main(df, columns):
    if df is None:
        raise ValueError("No data available")
    return filter_columns(df, columns)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
