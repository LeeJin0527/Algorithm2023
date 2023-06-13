from itertools import combinations
def solution(number):
    answer = 0
    lst = list(combinations(number, 3))

    for l in lst:
        if sum(l) == 0:
            answer += 1
    return answer