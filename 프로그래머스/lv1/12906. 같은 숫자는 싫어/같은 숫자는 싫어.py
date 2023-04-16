def solution(array):
    stack = []
    for arr in array:
        if len(stack) == 0:
            stack.append(arr)
        if stack[-1] == arr:
            continue
        else:
            stack.append(arr)
    return stack