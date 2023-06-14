from collections import defaultdict
import operator
def solution(N, stages):
    result = []
    answer = [0 for _ in range(N+1)]
    check = [0 for _ in range(N+1)]
    compare = defaultdict(int)
    for index in range(1, N+1):
        cnt = 0
        for stage in stages:
            if stage >= index:
                cnt += 1
        answer[index] = cnt
    for stage in stages:
        if stage <= N:
            check[stage] += 1
    for index in range(1, len(answer)):
        if answer[index] == 0:
            compare[index] = 0
            continue
        compare[index] = (check[index] / answer[index]) * 100
    
    compare = sorted(compare.items(), key=operator.itemgetter(1), reverse = True)
    for comp in compare:
        result.append(comp[0])
    return result