def solution(s):
    answer = 0
    same = 0
    diff = 0
    start = -1
    for index, value in enumerate(s):
        if start == -1:
            start = value
        if value == start:
            same += 1
        else:
            diff += 1
        if same == diff:
            answer += 1
            start = -1
            same = 0
            diff = 0
    if same != diff:
        answer += 1
    return answer