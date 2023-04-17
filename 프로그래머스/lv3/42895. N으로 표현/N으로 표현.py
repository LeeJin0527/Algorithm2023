
def solution(N, number):
    answer = 0
    dic, check = dict(), set()
    for index in range(1, 9):
        preCheck = int(str(N) * index)
        if preCheck == number:
            return index
        dic[index] = [preCheck]
        check.add(preCheck)
    check.add(0)
    for i in range(2, 9):
        for j in range(1, i):
            k = i - j
            for eachJ in dic[j]:
                for eachK in dic[k]:
                    temp = [eachJ + eachK, abs(eachJ - eachK), eachJ // eachK , eachJ * eachK, eachK // eachJ]
                    for tem in temp:
                        if tem not in check:
                            if tem == number:
                                return i
                            check.add(tem)
                            dic[i].append(tem)
    return -1