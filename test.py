import io
from light_module.__main__ import main
import os
import sys

if __name__ == "__main__":
    # Path to your CSV file
    current_file_path = os.path.abspath(__file__)
    project_directory = os.path.dirname(current_file_path)
    csv_file_path = f"{project_directory}/light_module/data/SP500.csv"
    with open(csv_file_path, 'r') as file:
        # Simulate stdin using io.StringIO
        simulated_stdin = io.StringIO(file.read())

    # Pass the simulated stdin and command line arguments to main
    sys.argv = ['light', 'mom 252']
    sys.stdin = simulated_stdin
    main()