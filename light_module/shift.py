import pandas as pd

# Example structure for the 'load' command
def shift(df, shift_by):
    return df.shift(shift_by)

def main(df, shift_by):
    return shift(df, shift_by)