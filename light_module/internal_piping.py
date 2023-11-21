import pandas as pd

import sys
from . import after, before, wmom, cgrep, signal, dlog, \
    unitscale, mult, save, load, ffill, ewa, cumsum, \
    shift, plot, signal_limits

vars = {}
current_df = None


def execute_command(df, command, args):
    if command == 'after':
        result = after.main(df, *args)
    elif command == 'before':
        result = before.main(df, *args)
    elif command == 'wmom':
        result = wmom.main(df, *args)
    elif command == 'cgrep':
        result = cgrep.main(df, args)
    elif command == 'signal':
        result = signal.main(df)
    elif command == 'unitscale':
        window_size = int(args[0])
        target_vol = float(args[1])
        result = unitscale.main(df, window_size, target_vol)
    elif command == 'dlog':
        result = dlog.main(df)
    elif command == 'mult':
        df2 = vars[args[0]]
        result = mult.main(df, df2)
    elif command == 'load':
        filename = args[0]
        result = load.main(filename)
    elif command == 'save':
        filename = args[0]
        result = save.main(df, filename)
    elif command == '->':
        vars[args[0]] = df
        result = df
    elif command == 'ffill':
        result = ffill.main(df)
    elif command == 'ewa':
        result = ewa.main(df)
    elif command == 'cumsum':
        start_number = int(args[0])
        result = cumsum.main(df, start_number)
    elif command == 'shift':
        period = int(args[0])
        result = shift.main(df, period)
    elif command == 'plot':
        result = plot.main(df)
    elif command == 'signallimit':
        buy_level = float(args[0])
        sell_level = float(args[1])
        no_hold_days = float(args[2])
        result = signal_limits.main(df, buy_level, sell_level, no_hold_days)
    else:
        raise ValueError(f"Unknown command: {command}")

    return result


def process_commands(command_string):
    current_df = initial_load()
    commands = command_string.split('|')
    for cmd in commands:
        parts = cmd.strip().split()
        command, args = parts[0], parts[1:]
        result = execute_command(current_df, command, args)
        current_df = result
    current_df.to_csv(sys.stdout, index=True)


def initial_load():
    initial_data = pd.read_csv(sys.stdin)
    initial_data['DATE'] = pd.to_datetime(initial_data['DATE'])
    initial_data = initial_data.groupby(initial_data['DATE'].dt.date).last()
    initial_data['DATE'] = initial_data['DATE'].dt.date
    initial_data.set_index('DATE', inplace=True, drop=True)
    if isinstance(initial_data, pd.Series):
        initial_data = initial_data.to_frame()
    return initial_data
