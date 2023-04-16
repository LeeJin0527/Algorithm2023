import math
def solution(progresses, speeds):
    answer = []
    for index, value in enumerate(progresses):
        progresses[index] = math.ceil((100 - value) / speeds[index])
    start = progresses[0]
    cnt = 0
    for progress in progresses:
        if start >= progress:
            cnt += 1
        else:
            answer.append(cnt)
            start = progress
            cnt = 1
    answer.append(cnt)
    
    return answer