def solution(s):
    s = list(s.split())
    stack = []
    for value in s:
        if value == 'Z':
            stack.pop()
        else:
            stack.append(int(value))
    return sum(stack)