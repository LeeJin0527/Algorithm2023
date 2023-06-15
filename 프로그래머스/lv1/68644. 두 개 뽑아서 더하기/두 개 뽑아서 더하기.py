from itertools import combinations
def solution(numbers):
    answer = []
    lst = list(combinations(numbers, 2))
    for l in lst:
        answer.append(sum(l))
    answer = list(set(answer))
    answer.sort()
    return answer