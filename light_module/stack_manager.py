stack = []

def push_to_stack(df):
    stack.append(df)

def get_from_stack():
    return stack[-1] if stack else None

def get_from_stack_pos(pos: int):
    return stack[pos]