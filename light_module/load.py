import pandas as pd

# Example structure for the 'load' command
def load(filename):
    data = pd.read_csv(filename)
    data['DATE'] = pd.to_datetime(data['DATE']).dt.date
    data.set_index('DATE', inplace=True)
    return data

def main(filename):
    df = load(filename)
    return df