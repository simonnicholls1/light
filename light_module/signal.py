# light/signal.py
import pandas as pd
import sys
from stack_manager import push_to_stack

def calculate_signal(df):
    return df.applymap(lambda x: 1 if x > 0 else -1)

def main(df):
    result = calculate_signal(df)
    push_to_stack(result)
    result.to_csv(sys.stdout, index=True)
