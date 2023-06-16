def solution(a, b):
    answer = 0
    for index, value in enumerate(a):
        answer += a[index] * b[index]
    return answer