def solution(k, m, score):
    answer = 0
    boxes = len(score) // m
    if boxes == 0:
        return 0
    score.sort(reverse = True)
    index = 0
    while index < len(score):
        check = score[index: index + m]
        if len(check) == m:
            answer += check[-1] * m
        index += m
    return answer