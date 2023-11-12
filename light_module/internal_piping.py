from .stack_manager import push_to_stack, get_from_stack
from . import after, before, mom  # Import other processing modules

def execute_command(command, args):
    df = get_from_stack()
    if command == 'after':
        result = after.process(df, *args)
    elif command == 'before':
        result = before.process(df, *args)
    elif command == 'mom':
        result = mom.main(df, args)
    # ... other commands
    else:
        raise ValueError(f"Unknown command: {command}")
    push_to_stack(result)

def process_commands(command_string):
    commands = command_string.split('|')
    for cmd in commands:
        parts = cmd.strip().split()
        if len(parts) == 2:
            command, args = parts[0], [parts[1]]
        else:
            command, args = parts[0], parts[1:]
        execute_command(command, args)
