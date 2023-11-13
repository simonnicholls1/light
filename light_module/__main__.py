# light/__main__.py
import sys
from light_module.internal_piping import process_commands
import pandas as pd
import light_module.stack_manager as stack_manager

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m light 'command1 | command2 | ...'")
        sys.exit(1)

    command_string = sys.argv[1]
    initial_data = pd.read_csv(sys.stdin)
    initial_data['DATETIME'] = pd.to_datetime(initial_data['DATETIME'])
    initial_data = initial_data.groupby(initial_data['DATETIME'].dt.date).last()
    initial_data['DATE'] = initial_data['DATETIME'].dt.date
    initial_data.drop(["DATETIME"], axis=1, inplace=True)
    initial_data.set_index('DATE', inplace=True)
    stack_manager.push_to_stack(initial_data)
    process_commands(command_string)

if __name__ == "__main__":
    main()

