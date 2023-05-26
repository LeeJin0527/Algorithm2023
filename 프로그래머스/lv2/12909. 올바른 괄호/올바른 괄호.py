def solution(array):
    answer = True
    stack = []
    for arr in array:
        if len(stack) == 0 and arr == ')':
            return False
        if arr == '(':
            stack.append('(')
        elif arr == ')':
            stack.pop()
    if len(stack) != 0:
        return False
    return True