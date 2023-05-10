def solution(array):
    answer = []
    stack = []
    for arr in array:
        if len(stack) == 0:
            stack.append(arr)
        else:
            if stack[-1] != arr:
                stack.append(arr)
    return stack