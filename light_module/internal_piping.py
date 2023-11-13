from .stack_manager import push_to_stack, get_from_stack
from . import after, before, mom, cgrep, signal  # Import other processing modules

def execute_command(command, args):
    df = get_from_stack()
    if command == 'after':
        after.main(df, *args)
    elif command == 'before':
        before.main(df, *args)
    elif command == 'mom':
        mom.main(df, *args)
    elif command == 'cgrep':
        cgrep.main(df, *args)
    elif command =='signal':
        signal.main(df)
    elif command =='scalevol':
        signal.main(df, *args)
    # ... other commands
    else:
        raise ValueError(f"Unknown command: {command}")

def process_commands(command_string):
    commands = command_string.split('|')
    for cmd in commands:
        parts = cmd.strip().split()
        if len(parts) == 2:
            command, args = parts[0], [parts[1]]
        else:
            command, args = parts[0], parts[1:]
        execute_command(command, args)
