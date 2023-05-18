def solution(array, divisor):
    answer = []
    for arr in array:
        if arr % divisor == 0:
            answer.append(arr)
    answer.sort()
    if len(answer) == 0:
        return [-1]
    return answer