import copy
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    origin = len(lost)
    answer = 0
    check = []
    for lostPerson in lost:
        if lostPerson in reserve:
            check.append(lostPerson)
    for che in check:
        reserve.remove(che)
        lost.remove(che)
    compareLost = copy.deepcopy(lost)
    for lostPerson in compareLost:
        if lostPerson-1 in reserve:
            if lostPerson-1 not in check:
                check.append(lostPerson-1)
                reserve.remove(lostPerson-1)
                lost.remove(lostPerson)
                
        elif lostPerson+1 in reserve:
            if lostPerson+1 not in check:
                check.append(lostPerson+1)
                reserve.remove(lostPerson+1)
                lost.remove(lostPerson)
    return n - origin + len(check)