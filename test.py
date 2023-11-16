import io
from light_module.__main__ import main
import os
import sys

if __name__ == "__main__":
    # Path to your CSV file
    current_file_path = os.path.abspath(__file__)
    project_directory = os.path.dirname(current_file_path)
    csv_file_path = f"{project_directory}/light_module/data/ALL_FUTURES.csv"
    with open(csv_file_path, 'r') as file:
        # Simulate stdin using io.StringIO
        simulated_stdin = io.StringIO(file.read())

    # Pass the simulated stdin and command line arguments to main
    # unit curve -> uc -> dlog - dlog
    # ur - unit returns
    # sys.argv = ['light', 'after 2000-03-02|ffill|dlog| save dlog.csv | wmom 252 1 | signal |shift 1|-> s | load dlog.csv | unitscale 250 0.01 |mult s| ewa| cumsum 1']
    sys.argv = ['light', 'cgrep SP500 US2|after 2000-03-02|ffill|dlog|save dlog.csv|wmom 252 1|signal|shift 0|-> s|load dlog.csv|unitscale 250 0.01|mult s|cumsum 1|plot']
    sys.stdin = simulated_stdin
    main()