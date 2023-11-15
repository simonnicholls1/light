import pandas as pd

# Example structure for the 'load' command
def save(df, filename):
    return df.to_csv(filename)

def main(df, filename):
    save(df, filename)
    return df