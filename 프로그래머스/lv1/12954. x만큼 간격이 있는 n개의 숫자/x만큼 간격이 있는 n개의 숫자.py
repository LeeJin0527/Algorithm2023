def solution(x, n):
    answer = [x]
    number = x
    for i in range(0, n-1):
        answer.append(answer[-1] + x)
    return answer