def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for index, value in enumerate(numbers):
        while stack and numbers[stack[-1]] < value:
            x = stack.pop()
            answer[x] = value
        stack.append(index)
    
    return answer