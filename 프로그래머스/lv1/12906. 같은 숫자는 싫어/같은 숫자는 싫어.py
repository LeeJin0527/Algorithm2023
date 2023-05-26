def solution(array):
    answer = []
    for arr in array:
        if len(answer) == 0:
            answer.append(arr)
        else:
            if answer[-1] != arr:
                answer.append(arr)
    return answer