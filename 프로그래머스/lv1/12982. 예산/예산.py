def solution(d, budget):
    answer = 0
    d.sort()
    for each in d:
        if each <= budget:
            answer += 1
            budget -= each
    return answer