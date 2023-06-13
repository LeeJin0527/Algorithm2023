from collections import defaultdict
def solution(id_list, report, k):
    result = []
    stopCount = defaultdict(int)
    check = defaultdict(set)
    
    for id in id_list:
        check[id] = list()

    reportCheck = set()
    for rep in report:
        x, y = rep.split()
        if (x, y) in reportCheck:
            continue
        check[x].append(y)
        reportCheck.add((x, y))

    for re in reportCheck:
        x, y = re
        stopCount[y] += 1

    temp = []
    for stop in stopCount:
        if stopCount[stop] >= k:
            temp.append(stop)

    for che in check:
        cnt = 0
        for each in check[che]:
            if each in temp:
                cnt += 1
        result.append(cnt)

    return result