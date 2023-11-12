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
    initial_data.set_index('DATETIME', inplace=True)
    stack_manager.push_to_stack(initial_data)
    process_commands(command_string)

if __name__ == "__main__":
    main()