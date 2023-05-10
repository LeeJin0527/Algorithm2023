import math
def solution(progresses, speeds):
    answer = []
    works = []
    stack = []
    n = len(progresses)
    for index, value in enumerate(progresses):
        works.append(math.ceil((100 - value) / speeds[index]))
    index = 0
    while index < n:
        check = 1
        cnt = 1
        while index + check < n and works[index] >= works[index+check]:
            check += 1
        answer.append(check)
        index += check
    print(answer)
    return answer